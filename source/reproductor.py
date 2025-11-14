import time
import vlc
from yt_dlp import YoutubeDL
import ctypes
from enum import Enum

import sys, os

# Excepciones de la API
class ReproduccionError(Exception):
    """Base de errores de Reproduccion."""

class EntradaInvalidaError(ReproduccionError):
    """Parámetros de entrada inválidos (IDs, rutas...)."""

class ResolverStreamError(ReproduccionError):
    """No se pudo resolver la URL de streaming de YouTube."""

class PlayError(ReproduccionError):
    """Fallo al iniciar/controlar la reproducción (VLC)."""

class EstadoReproductor(Enum):
    """Enumerado que define el estado actual del reproductor"""
    SIN_REPRODUCCION = 1
    REPRODUCIENDO = 2
    PAUSADO = 3

class Reproductor:
    """Clase que nos permite crear una instancia del reproductor, capaz de reproducir canciones de YouTube"""

    def __init__(self):
        # Instancia global de VLC con flags "silenciosos"
        # "--quiet" reduce verbosidad; el callback de logs (abajo) la elimina por completo.
        self._instance = vlc.Instance("--quiet")
        self._player = self._instance.media_player_new()

        # Interceptar y anular logs internos de libVLC
        log_callback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int,
                                        ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)

        def __log_sink(data, level, ctx, fmt, args):
            # No hacemos nada: se descartan todos los logs de VLC.
            return

        self.__log_cb = log_callback(__log_sink)  # guardarlo en self para que no lo recoja el GC
        try:
            # Enlazar el callback a la instancia
            vlc.libvlc_log_set(self._instance, self.__log_cb, None)
        except Exception:
            # Si el build no soporta libvlc_log_set, se puede usar esta alternativa:
            # import os, sys
            # devnull = os.open(os.devnull, os.O_WRONLY)
            # os.dup2(devnull, 2)  # redirige stderr globalmente
            pass

    # ---------- Utilidades internas ----------
    def _esperar_para_reproducir(self, tiempo_seg: float = 10.0) -> None:
        """Espera a que VLC entre en Playing o lanza PlaybackError."""
        start = time.time()
        while time.time() - start < tiempo_seg:
            if not self._player:
                raise PlayError("No hay reproductor inicializado.")
            state = self._player.get_state()
            if state == vlc.State.Playing:
                return
            if state in (vlc.State.Error, vlc.State.Ended, vlc.State.Stopped):
                raise PlayError(f"VLC en estado {state}.")
            time.sleep(0.05)
        raise PlayError("Timeout esperando a que comience la reproducción.")

    def _detener_si_activo(self) -> None:
        """Detiene sin error si hay reproducción previa (evita superposiciones)."""
        if self._player is not None:
            try:
                self._player.stop()
            except Exception:
                pass

    # ---------- Reproducción (especificación pública) ----------

    def obtener_estado_reproductor(self) -> "EstadoReproductor":
        """Devuelve el estado actual del reproductor usando los estados personalizados definidos."""
        if not self._player:
            raise PlayError("No hay reproductor inicializado.")

        estado_vlc = self._player.get_state()

        # Mapeo de estados de VLC -> estados personalizados
        if estado_vlc in (vlc.State.Playing, vlc.State.Opening, vlc.State.Buffering):
            return EstadoReproductor.REPRODUCIENDO
        elif estado_vlc == vlc.State.Paused:
            return EstadoReproductor.PAUSADO
        elif estado_vlc in (vlc.State.NothingSpecial, vlc.State.Stopped, vlc.State.Ended, vlc.State.Error):
            return EstadoReproductor.SIN_REPRODUCCION
        else:
            # Por precaución, cualquier otro valor se considera sin reproducción activa
            return EstadoReproductor.SIN_REPRODUCCION

    def reproducir_desde_youtube(self, video_id: str, espera_hasta_reproducir: bool = True, timeout_sec: float = 10.0) -> bool:
        """
        Reproduce en streaming desde YouTube (corta cualquier reproducción previa).
        Devuelve True si comenzó correctamente.
        Lanza InvalidInputError, StreamResolveError o PlaybackError en caso de fallo.
        """
        if not video_id or not isinstance(video_id, str):
            raise EntradaInvalidaError("video_id inválido.")

        url = f"https://www.youtube.com/watch?v={video_id}"
        ydl_opts = {
            "quiet": True,
            "skip_download": True,
            "format": "bestaudio/best",
        }

        try:
            # -------- Bloque para suprimir todos los warnings de la librería yt-dlp --------
            devnull = os.open(os.devnull, os.O_WRONLY)
            old_stderr = os.dup(2)  # Guardar stderr original
            os.dup2(devnull, 2)  # Redirigir stderr a /dev/null

            try:
                from yt_dlp import YoutubeDL
                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
            finally:
                # Restaurar stderr original
                os.dup2(old_stderr, 2)
                os.close(devnull)
                os.close(old_stderr)
        except Exception as e:
            raise ResolverStreamError(f"No se pudo resolver el stream: {e}")

        stream_url = info.get("url") if isinstance(info, dict) else None
        if not stream_url:
            raise ResolverStreamError("No se pudo obtener la URL del stream.")

        # Cortar reproducción previa
        self._detener_si_activo()

        try:
            media = self._instance.media_new(stream_url)
            self._player.set_media(media)
            rc = self._player.play()
            if rc != 0:
                raise PlayError(f"No se pudo iniciar la reproducción (rc={rc}).")
            time.sleep(0.2)
            if espera_hasta_reproducir:
                self._esperar_para_reproducir(tiempo_seg=timeout_sec)
            return True
        except ReproduccionError:
            self._detener_si_activo()
            raise
        except Exception as e:
            self._detener_si_activo()
            raise PlayError(f"Error de reproducción: {e}")

    # ---------- Controles ----------
    def pausar(self) -> bool:
        """Pausa (toggle interno de VLC). Devuelve True o lanza PlaybackError si no hay reproductor."""
        if not self._player:
            raise PlayError("No hay reproductor activo para pausar.")
        try:
            self._player.pause()
            return True
        except Exception as e:
            raise PlayError(f"Error al pausar: {e}")

    def reanudar(self) -> bool:
        """Reanuda forzando 'play' de VLC. Devuelve True o lanza PlaybackError."""
        if not self._player:
            raise PlayError("No hay reproductor activo para reanudar.")
        try:
            rc = self._player.play()
            if rc != 0:
                raise PlayError(f"No se pudo reanudar (rc={rc}).")
            return True
        except Exception as e:
            raise PlayError(f"Error al reanudar: {e}")