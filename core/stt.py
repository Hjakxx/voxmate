"""
core/stt.py
Offline Speech-to-Text for VoxMate with:
 - Whisper small.en model (better accuracy for English commands)
 - Noise reduction (noisereduce)
 - Command-style biasing via initial_prompt
"""

import whisper
import soundfile as sf
import noisereduce as nr
from pathlib import Path

# Set your FFmpeg path (same as before)
FFMPEG_PATH = r"C:\ffmpeg-8.0.1-essentials_build\bin\ffmpeg.exe"

_model = None


def load_model(name="small.en"):
    """Load Whisper model once and reuse."""
    global _model
    if _model is None:
        print("[STT] Loading Whisper model:", name)
        _model = whisper.load_model(name)
        print("[STT] Model loaded.")
    return _model


def reduce_noise(wav_path):
    """Apply noise reduction and save clean version."""
    data, sr = sf.read(wav_path)

    # Noise reduction (very effective for classroom noise)
    reduced = nr.reduce_noise(y=data, sr=sr)

    clean_path = wav_path.replace(".wav", "_clean.wav")
    sf.write(clean_path, reduced, sr)

    return clean_path


def transcribe(wav_path, model_name="small.en"):
    """Full STT pipeline: denoise → whisper → text."""

    # 1. Noise reduction
    clean_path = reduce_noise(wav_path)

    # 2. Load Whisper
    model = load_model(model_name)

    # 3. Bias transcription for short English commands
    prompt = (
        "The user is giving short English voice commands like: "
        "open chrome, close chrome, take screenshot, increase volume, decrease volume, "
        "system info, create folder, search file, brightness up, brightness down."
    )

    # 4. Transcribe
    result = model.transcribe(
        clean_path,
        fp16=False,
        initial_prompt=prompt
    )

    text = result["text"].strip()
    return text
