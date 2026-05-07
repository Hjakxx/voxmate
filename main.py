# from core.audio import record_until_silence, temp_wav_path
# from core.stt import transcribe
# from core.nlp import classify
# from core.dispatcher import execute
# from core.tts import speak

# def run_once():
#     """Runs one full command cycle from hotkey trigger."""
#     print("\n[VoxMate] Listening...")

#     wav_path = temp_wav_path("voxmate_cmd.wav")
#     record_until_silence(wav_path)

#     print("[STT] Transcribing...")
#     text = transcribe(wav_path)
#     print("[You said]:", text)

#     intent_data = classify(text)
#     intent = intent_data["intent"]
#     params = intent_data["params"]
#     print("[Intent]:", intent)

#     success, message = execute(intent, params)
#     print("[Action]:", message)

#    # If message is too long (like file search outputs), shorten for TTS
#     tts_msg = message
#     if len(tts_msg) > 150:
#         tts_msg = "Command executed successfully."

#     speak(tts_msg)

#     print("[VoxMate] Ready.\n")


# def main_loop():
#     """Normal old loop if you run python main.py manually."""
#     print("\n====== VoxMate CLI Assistant ======")
#     print("Press ENTER to speak. Silence stops recording.\n")

#     while True:
#         input(">> Press ENTER to start recording...")
#         run_once()python -c "import pyttsx3; e=pyttsx3.init(); e.say('audio test'); e.runAndWait()"



# if __name__ == "__main__":
#     main_loop()
from core.audio import record_until_silence, temp_wav_path
from core.stt import transcribe
from core.nlp import classify
from core.dispatcher import execute
from core.feedback import success_message, error_message


def run_once():
    wav_path = temp_wav_path("voxmate_cmd.wav")
    record_until_silence(wav_path)

    text = transcribe(wav_path)
    print("[You said]:", text)

    intent_data = classify(text)
    intent = intent_data["intent"]
    params = intent_data["params"]

    success, message = execute(intent, params)
    print("[Action]:", message)

    if success:
        success_message(message)
    else:
        error_message(message)


def main_loop():
    """Normal old loop if you run python main.py manually."""
    print("\n====== VoxMate CLI Assistant ======")
    print("Press ENTER to speak. Silence stops recording.\n")

    while True:
        input(">> Press ENTER to start recording...")
        run_once()


if __name__ == "__main__":
    main_loop()
