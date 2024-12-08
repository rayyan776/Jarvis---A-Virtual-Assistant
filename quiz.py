import pyttsx3
import speech_recognition as sr

# Initialize the voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that. Please repeat.")
            return listen()  # Retry listening
        except sr.RequestError:
            speak("Could not request results; check your network connection.")
            return ""

# Quiz Data
questions = [
    "What aspect of healthcare interests you the most?",
    "Which skill do you value the most for professional success?",
    "What type of work environment do you thrive in?",
    "How do you prefer to solve problems?",
    "Which activity do you find most fulfilling?",
    "What do you believe is essential for environmental sustainability?",
    "Which role do you see yourself taking in a team?",
    "How do you prefer to express your creativity?",
    "What type of content do you enjoy consuming the most?",
    "What is your preferred method of communication?",
    "How do you view your impact on society?",
    "What type of innovation excites you the most?",
    "How do you manage your personal or professional finances?",
    "What do you think is the most important quality in a leader?",
    "Which subject did you enjoy most in school?",
    "What drives you to achieve your goals?",
    "How do you prefer to spend your leisure time?",
    "Which type of project excites you the most?",
    "What do you prioritize when creating a product or service?",
    "How do you view teamwork in achieving success?",
    "Which area of environmental science intrigues you the most?",
    "How do you handle feedback or criticism?",
    "What type of challenges do you enjoy solving?",
    "What aspect of human behavior are you most curious about?",
    "How do you view the issue of climate change?",
    "What is your preferred way to learn new skills?",
    "What makes a story compelling for you?",
    "What do you believe is the most important element of marketing?",
    "What qualities do you admire most in a teacher?",
    "What does success mean to you?"
]

answers = [
    ["Patient care", "Research", "Healthcare technology", "Policy-making"],
    ["Critical thinking", "Creativity", "Communication", "Leadership"],
    ["Office", "Laboratory", "Outdoor", "Creative studio"],
    ["Analytical", "Intuitive", "Collaborative", "Creative"],
    ["Reading medical journals", "Designing or creating", "Playing or listening to music", "Writing articles or blogs"],
    ["Renewable energy solutions", "Conservation practices", "Public education and awareness", "Technological innovation"],
    ["Leader", "Contributor", "Innovator", "Supporter"],
    ["Designing products or systems", "Animating or illustrating", "Performing music", "Writing stories or reports"],
    ["Medical advancements", "Scientific breakthroughs", "Creative arts and design", "Public relations or marketing trends"],
    ["Face-to-face", "Social media", "Writing", "Presentations"],
    ["Providing healthcare or solutions", "Innovating in engineering or design", "Teaching or guiding others", "Contributing to public discourse through media"],
    ["Medical technology", "Engineering breakthroughs", "Creative and artistic developments", "Business or financial innovations"],
    ["Strategic planning", "Budgeting and saving", "Investments", "Entrepreneurship or business ventures"],
    ["Vision", "Empathy", "Integrity", "Resilience"],
    ["Biology or Chemistry", "Physics or Math", "Art or Music", "Literature or Journalism"],
    ["Ambition", "Passion for creating", "Curiosity about the world", "Dedication to teaching or helping others"],
    ["Exploring nature or the outdoors", "Designing or building projects", "Practicing or playing music", "Writing or communicating with others"],
    ["Research or hands-on experiments", "Creative or artistic work", "Strategic business planning", "Teaching or mentoring others"],
    ["Functionality and efficiency", "Aesthetic appeal", "User-friendliness", "Innovation and uniqueness"],
    ["Collaboration is key", "Independence is important", "Leadership drives the team", "Innovation comes from team effort"],
    ["Climate change solutions", "Renewable energy", "Conservation efforts", "Environmental technology"],
    ["Constructively, using it for growth", "Creatively, incorporating it into future work", "Positively, staying motivated", "Encouraging others through support"],
    ["Practical, real-world issues", "Theoretical, concept-driven problems", "Creative, artistic challenges", "Analytical, data-driven tasks"],
    ["Psychological and emotional", "Cultural and societal", "Environmental influence", "Historical development"],
    ["Through scientific research and action", "By advocating for public awareness", "Creating technology for solutions", "Educating others on the importance"],
    ["Visual learning through diagrams or videos", "Auditory learning through listening", "Hands-on experience", "Learning through social interaction or teamwork"],
    ["Real-life relevance", "Intriguing characters", "Unexpected plot twists", "Cultural or societal significance"],
    ["Understanding the audience", "Creativity in campaigns", "Thorough research", "Engaging presentation"],
    ["Knowledge and expertise", "Patience and understanding", "Creativity in teaching methods", "Real-world experience"],
    ["Personal fulfillment through helping others", "Financial stability or entrepreneurship", "Gaining recognition in your field", "Creating an impact through your work"]
]

# Weights for each career domain
weights = [
    [4, 3, 1, 2],  # Medicine, Engineering, Environmental Science, Designing
    [1, 4, 3, 2],  # Medicine, Engineering, Environmental Science, Designing
    [2, 4, 3, 1],  # Environmental Science, Engineering, Designing
    [3, 4, 1, 2],  # Engineering, Environmental Science, Designing
    [4, 3, 1, 2],  # Designing, Engineering, Music, Journalism
    [3, 2, 1, 4],  # Environmental Science, Designing, Marketing, Entrepreneurship
    [4, 3, 2, 1],  # Entrepreneurship, Designing, Engineering, Medicine
    [3, 4, 1, 2],  # Animation, Designing, Medicine, Journalism
    [2, 4, 3, 1],  # Marketing, Journalism, Music
    [3, 4, 1, 2],  # Public Relations, Marketing, Journalism
    [1, 4, 2, 3],  # Medicine, Public Relations, Journalism
    [3, 4, 2, 1],  # Engineering, Medicine, Finance
    [3, 4, 2, 1],  # Finance, Entrepreneurship
    [4, 3, 2, 1],  # Leadership, Marketing, Medicine
    [1, 4, 2, 3],  # Medicine, Teaching, Environmental Science
    [4, 3, 2, 1],  # Creativity, Designing
    [3, 4, 2, 1],  # Engineering, Teaching
    [4, 3, 2, 1],  # Entrepreneurship, Music, Journalism
    [2, 3, 4, 1],  # Engineering, Designing, Marketing
    [3, 4, 1, 2],  # Teamwork, Leadership, Marketing
    [2, 4, 1, 3],  # Environmental Science, Agriculture
    [4, 3, 2, 1],  # Feedback management
    [2, 4, 1, 3],  # Problem-solving
    [1, 4, 2, 3],  # Psychology, Medicine
    [4, 3, 1, 2],  # Environmental Science, Agriculture
    [3, 4, 1, 2],  # Skill learning
    [2, 4, 1, 3],  # Journalism, Music
    [4, 2, 3, 1],  # Marketing
    [2, 4, 3, 1],  # Teaching
    [1, 4, 3, 2]   # Success measure
]

# Assuming career_domains is a list of career domain names
career_domains = ['Medicine', 'Engineering', 'Environmental Science', 'Designing', 'Animation', 
                  'Music', 'Journalism', 'Public Relations', 'Marketing', 'Entrepreneurship', 
                  'Finance', 'Teaching', 'Agriculture', 'Sports']

def evaluate_answers(selected_answers):
    scores = [0] * len(career_domains)  # Assuming career_domains is a list

    for i, answer in enumerate(selected_answers):
        if answer is not None:  # If the answer is valid
            for j in range(len(career_domains)):
                scores[j] += weights[i][answer]

    # Get the index of the top career domain based on scores
    top_index = scores.index(max(scores))
    return career_domains[top_index]  # Return a single top career domain


def conduct_quiz():
    # Introduction
    speak("Welcome to the career guidance quiz. Please answer the questions to the best of your ability.")

    # Ask if the user wants to start the quiz (Typed Input)
    print("Would you like to start the quiz? Please type yes or no.")
    speak("Would you like to start the quiz? Please type yes or no.")
    start_command = input("Your response: ").strip().lower()  # User types 'yes' or 'no'

    if start_command == "yes":
        selected_answers = []

        # Start the quiz
        for i in range(len(questions)):
            print(f"Question {i + 1}:")  # Print the question number
            print(questions[i])
            speak(questions[i])

            # Display and speak the answer options
            for j, answer in enumerate(answers[i]):
                print(f"{chr(65 + j)}. {answer}")  # Display options as A, B, C, D
                speak(answer)

            # For the first question, ask for a choice explicitly
            if i == 0:
                print("Please type the letter corresponding to your choice (A, B, C, or D).")
                speak("Please type the letter corresponding to your choice, for example, A, B, C, or D.")

            # Prompt the user to answer (Typed Input for a, b, c, or d)
            answer_command = input("Your choice: ").strip().lower()

            # Convert answer to index and store it
            if answer_command in ['a', 'b', 'c', 'd']:
                selected_answers.append(ord(answer_command) - ord('a'))  # Convert a, b, c, d to 0, 1, 2, 3
            else:
                print("Invalid answer. Please choose from A, B, C, or D.")
                speak("Invalid answer. Please answer with A, B, C, or D.")
                selected_answers.append(None)  # Append None for invalid answers

        # After answering all questions, evaluate the results
        top_career = evaluate_answers(selected_answers)
        print(f"Based on your answers, the top career path for you is: {top_career}.")
        speak(f"Based on your answers, the top career path for you is: {top_career}.")
    
    else:
        # If user types "no"
        print("Okay, I won't start the quiz. I'm here if you need anything else.")
        speak("Okay, I won't start the quiz. I'm here if you need anything else.")
