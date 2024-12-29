# JARVIS

JARVIS (Just Another Really Very Intelligent System) is a Python-based voice assistant that can perform various tasks like fetching information from Wikipedia, opening websites, playing media files, and more. The program is designed to interact with the user using speech recognition and text-to-speech capabilities.

---

## Features

- **Voice Interaction**: Uses speech recognition and text-to-speech for seamless communication.
- **Personalized Greetings**: Wishes the user based on the time of day.
- **Wikipedia Search**: Fetches summaries of topics from Wikipedia.
- **Web Browsing**: Opens popular websites like YouTube, Google, Stack Overflow, and Learn CBSE.
- **Media Playback**: Plays movies or music from specified directories.
- **Time Announcement**: Tells the current time.
- **Customizable Exit Commands**: Multiple ways to exit or pause the assistant.
- **Introduction**: Provides a brief introduction about JARVIS.

---

## Requirements

To run this project, ensure you have the following installed:

- Python 3.8 or higher
- Required Python Libraries:
  - `pyttsx3`
  - `speech_recognition`
  - `wikipedia`
  - `pyaudio` (for speech recognition)
  - `pywin32` (for SAPI5 integration)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/JARVIS.git
   cd JARVIS
   ```

2. Install the required Python libraries:
   ```bash
   pip install pyttsx3 speechrecognition wikipedia pywin32
   ```

3. Ensure you have the correct directories for movies and music specified in the code:
   - Movies: `D:\MOVIE`
   - Music: `D:\music`

   Update these paths in the code if necessary.

4. Ensure `pyaudio` is installed. If you encounter issues, install it using:
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

---

## Usage

1. Run the script:
   ```bash
   python JARVIS.py
   ```

2. Interact with JARVIS using voice commands. Examples:
   - "Introduce yourself"
   - "What is the time?"
   - "Search for Albert Einstein on Wikipedia"
   - "Open YouTube"
   - "Play music"
   - "Quit"

---

## Project Structure

- **`JARVIS.py`**: The main application script containing all functionalities.

---

## Known Issues

- Ensure a stable microphone connection for accurate speech recognition.
- The program may throw errors if the specified directories for movies or music are incorrect or empty.

---

## Future Enhancements

- Add support for more complex queries and tasks.
- Improve the error handling mechanism for better reliability.
- Integrate additional APIs for enhanced functionality.

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


---

## Acknowledgments

- The Python community for providing open-source libraries.
- The creators of `pyttsx3`, `speech_recognition`, and `wikipedia` for their tools.

.
