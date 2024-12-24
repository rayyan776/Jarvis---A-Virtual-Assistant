# JARVIS: Your Virtual AI Assistant

JARVIS is an intelligent virtual assistant that brings convenience to your fingertips. Designed to perform a wide array of tasks, JARVIS responds to voice commands, making it a hands-free, efficient companion for your daily needs.

## Features

### 1. Basic Interaction
- **Greet You**: Say "Hello."
- **Respond to Mood Inquiries**: Ask "How are you?" or respond with "I am fine."
- **Thank You Response**: Say "Thank you."
- **Status Commands**:
  - "Wake up" (activate JARVIS)
  - "Go to sleep" (temporary deactivation)
  - "Finally sleep" (complete shutdown)

### 2. System Management
- **Open Applications**: "Open [app name]."
- **Shutdown the System**: "Shutdown the system" (confirmation required).
- **Password Protection**:
  - Change password: "Change password."
  - Startup requires a password.

### 3. Entertainment & Media
- **Play Songs on YouTube**: "Play a song."
- **Video Control**:
  - "Pause," "Play," "Mute."
  - "Volume up," "Volume down."

### 4. Camera & Photography
- **Take a Photo**: "Click my photo."
- **Take a Screenshot**: "Take a screenshot."

### 5. Search & Information
- **Google Search**: "Google [search term]."
- **YouTube Search**: "YouTube [search term]."
- **Wikipedia Search**: "Wikipedia [search term]."

### 6. Weather & Temperature
- **Weather Updates**: "What's the weather?"
- **Temperature Check**: "What's the temperature in [location]?"

### 7. Timekeeping
- **Current Time**: "What is the time?"

### 8. Memory Functions
- **Store Information**: "Remember that [text]."
- **Recall Information**: "What do you remember?"

### 9. Task Management
- **Schedule Tasks**: "Schedule my day."
- **View Schedule**: "Show my schedule." (Includes notifications.)

### 10. Mathematics & Calculations
- **Perform Calculations**: "Calculate [math problem]."

### 11. Games
- **Play Games**: "Play a game."

### 12. Internet Speed Check
- **Check Speed**: "Internet speed."

### 13. Shutdown & Exit
- **Shutdown JARVIS**: "Shutdown the system" (confirmation required).
- **Exit Completely**: "Finally sleep."


## How It Works

### Career Guidance Integration
1. **Trigger the Quiz**:
   - Use the command "Start career quiz."
2. **Voice-Prompted Questions**:
   - Uses `pyttsx3` for text-to-speech and `speech_recognition` for input.
3. **Evaluate Answers**:
   - Analyzes responses and calculates scores to suggest the top three career paths.

## Tech Stack
- **Python**: Core programming language.
- **Libraries**:
  - `pyttsx3` for text-to-speech.
  - `speech_recognition` for voice input.
  - `Wikipedia` API for search.
  - `OpenCV` for photography.
  - `pywhatkit` for YouTube integration.

## Getting Started

### Prerequisites
- Python 3.x
- Required Libraries:
  ```bash
  pip install pyttsx3 speechrecognition wikipedia pywhatkit opencv-python
  ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/JARVIS.git
   ```
2. Navigate to the project directory:
   ```bash
   cd JARVIS
   ```
3. Run the main script:
   ```bash
   python jarvis.py
   ```

### Usage
- Activate JARVIS by saying "Wake up."
- Interact using the commands listed above.

## Contributing
Feel free to fork the repository and make contributions. For major changes, please open an issue to discuss your ideas.

## License
This project is licensed under the MIT License.

---
### Have Fun Interacting with JARVIS!

