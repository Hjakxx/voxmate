# Voxmate

Voxmate is a voice-driven automation/assistant project built in Python. It includes core speech and NLP logic, user-defined skills, and local runtime tooling for running on Windows.

## Repository Structure

- `main.py`
  - The primary application entry point.
  - Starts the Voxmate runtime and loads core modules.

- `hotkey_listener.py`
  - Handles global hotkey detection and triggers the assistant.

- `core/`
  - Contains the main backend components used by the assistant.
  - `audio.py` - Audio playback and recording utilities.
  - `dispatcher.py` - Routes commands and tasks to the correct handlers.
  - `feedback.py` - Manages user feedback and responses.
  - `nlp.py` - Natural language processing and intent parsing logic.
  - `stt.py` - Speech-to-text integration.
  - `tts.py` - Text-to-speech integration.

- `skills/`
  - Contains independent skill modules that extend Voxmate functionality.
  - Examples include browser control, file search, screenshot capture, volume control, and system info.

- `assets/`
  - Stores static resources used by the application.

- `config/`
  - Configuration files and settings for the project.

- `logs/`
  - Output logs generated during runtime.

- `python_embedded/`
  - Embedded Python runtime files.
  - This directory is ignored by Git and should not be committed.

- `voxmate-env/`
  - Local virtual environment directory.
  - This directory is ignored by Git and should not be committed.

## Notes

- `.gitignore` currently excludes `voxmate-venv/` and `python_embedded/`.
- Keep project-specific configuration and logs out of version control.
- Use `main.py` as the launch point when running the assistant locally.
