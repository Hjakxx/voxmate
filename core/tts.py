import pyttsx3
import threading

_engine = None
_engine_lock = threading.Lock()

def _init_engine():
    engine = pyttsx3.init(driverName="sapi5")
    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)
    return engine

def speak(text: str):
    global _engine

    if not text:
        return

    with _engine_lock:
        if _engine is None:
            _engine = _init_engine()

        try:
            _engine.say(text)
            _engine.runAndWait()
        except Exception as e:
            print("[TTS ERROR]:", e)
