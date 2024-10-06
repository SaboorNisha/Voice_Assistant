import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and return text, with timeout and phrase time limit
def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise

        # Add timeout and phrase_time_limit
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak_text("Timeout: No speech detected. Please try again.")
            return ""
        
    try:
        # Convert speech to text
        speech_text = recognizer.recognize_google(audio)
        print(f"You said: {speech_text}")
        return speech_text.lower()
    except sr.UnknownValueError:
        speak_text("Sorry, I didn't catch that. Can you repeat?")
        return ""
    except sr.RequestError:
        speak_text("Sorry, I'm unable to connect to the speech recognition service.")
        return ""

# Function to respond based on voice command
def respond_to_command(command):
    if "hello" in command:
        speak_text("Hello! How can I assist you today?")
    elif "how are you" in command:
        speak_text("I'm doing well, thank you for asking!")
    elif "bye" in command or "goodbye" in command:
        speak_text("Goodbye! Have a great day!")
        return False  # Exit the loop if the user says goodbye
    else:
        speak_text("I'm sorry, I don't understand that command.")
    return True

# Main loop for the voice assistant
def voice_assistant():
    speak_text("Hello! I am your voice assistant. How can I help you?")
    active = True
    while active:
        command = recognize_speech()  # Get the user's voice command
        if command:
            active = respond_to_command(command)  # Respond to the command

# Run the voice assistant
if __name__ == "__main__":
    voice_assistant()
