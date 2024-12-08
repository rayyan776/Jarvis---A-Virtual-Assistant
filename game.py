import pyttsx3
import speech_recognition as sr
import random

# Initialize Text-to-Speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    """Speak the provided text using the TTS engine."""
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Capture voice input from the microphone and return it as text."""
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 300
            # Wait up to 5 seconds for input and limit the phrase time to 10 seconds
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please repeat.")
            return "None"
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
            return "None"
        return query.lower()
    except Exception as e:
        print(f"Error accessing the microphone: {e}")
        return "None"

def game_play():
    """Play the Rock, Paper, Scissors game."""
    speak("Let's play Rock, Paper, Scissors!")
    print("Let's play!")
    round_count = 0
    me_score = 0
    jarvis_score = 0

    while round_count < 5:
        options = ("rock", "paper", "scissors")
        jarvis_choice = random.choice(options)

        print("\nYour turn! Speak 'rock', 'paper', or 'scissors':")
        query = takeCommand()

        if query in ["rock", "paper", "scissors", "scissor"]:
            # Game logic
            if query == "rock":
                if jarvis_choice == "rock":
                    speak("Rock! It's a tie.")
                elif jarvis_choice == "paper":
                    speak("Paper! I win this round.")
                    jarvis_score += 1
                else:
                    speak("Scissors! You win this round.")
                    me_score += 1

            elif query == "paper":
                if jarvis_choice == "rock":
                    speak("Rock! You win this round.")
                    me_score += 1
                elif jarvis_choice == "paper":
                    speak("Paper! It's a tie.")
                else:
                    speak("Scissors! I win this round.")
                    jarvis_score += 1

            elif query in ["scissors", "scissor"]:
                if jarvis_choice == "rock":
                    speak("Rock! I win this round.")
                    jarvis_score += 1
                elif jarvis_choice == "paper":
                    speak("Paper! You win this round.")
                    me_score += 1
                else:
                    speak("Scissors! It's a tie.")

            # Print the round result
            print(f"JARVIS chose: {jarvis_choice.capitalize()}")
            print(f"Score: ME - {me_score} | JARVIS - {jarvis_score}")

        else:
            speak("Invalid input. Please say 'rock', 'paper', or 'scissors'.")
            print("Invalid input. Please try again.")
            continue

        round_count += 1

    # Final score announcement
    print("\nGame Over!")
    speak("Game over!")
    print(f"Final Score: ME - {me_score} | JARVIS - {jarvis_score}")
    if me_score > jarvis_score:
        speak("Congratulations! You won the game.")
    elif me_score < jarvis_score:
        speak("I won the game! Better luck next time.")
    else:
        speak("It's a tie! Well played.")

# Main execution
if __name__ == "__main__":
    game_play()
