"""
core/audio.py
Simple, reliable audio recording utilities for VoxMate (Windows).
Uses RMS-based silence detection.
"""

import sounddevice as sd
import soundfile as sf
import numpy as np
import tempfile
from pathlib import Path
import time
from typing import Optional, Tuple

DEFAULT_SR = 16000
DEFAULT_CHANNELS = 1
DEFAULT_SUBTYPE = "PCM_16"


def temp_wav_path(name: str = "voxmate_cmd.wav") -> str:
    return str(Path(tempfile.gettempdir()) / name)


def _rms(frame: np.ndarray) -> float:
    if frame.size == 0:
        return 0.0
    return float(np.sqrt(np.mean(np.square(frame.astype("float32")))))


def record_until_silence(
    out_path: str,
    samplerate: int = DEFAULT_SR,
    channels: int = DEFAULT_CHANNELS,
    chunk_duration: float = 0.4,
    silence_threshold: float = 0.015,
    silence_duration: float = 1.0,
    max_record_seconds: float = 10.0,
) -> str:

    sd.default.samplerate = samplerate
    sd.default.channels = channels

    frames = []
    silence_chunks_needed = max(1, int(silence_duration / chunk_duration))
    silence_counter = 0
    total_chunks = 0
    max_chunks = int(max_record_seconds / chunk_duration)

    print("[audio] Recording (speak your command)... silence will stop recording.")

    try:
        with sd.InputStream(dtype="float32") as stream:
            while True:
                chunk, _ = stream.read(int(chunk_duration * samplerate))
                frames.append(chunk.copy())
                total_chunks += 1

                rms_val = _rms(chunk)

                if rms_val < silence_threshold:
                    silence_counter += 1
                else:
                    silence_counter = 0

                if silence_counter >= silence_chunks_needed:
                    print("[audio] Silence detected — stopping.")
                    break

                if total_chunks >= max_chunks:
                    print("[audio] Max record time reached — stopping.")
                    break

    except Exception as e:
        raise RuntimeError(f"Recording failed: {e}")

    audio = np.vstack(frames)
    sf.write(out_path, audio, samplerate, subtype=DEFAULT_SUBTYPE)
    print(f"[audio] Saved {out_path} ({len(audio) / samplerate:.2f}s)")
    return out_path
