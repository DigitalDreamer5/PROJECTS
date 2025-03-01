import speech_recognition as sr
import datetime
import pyttsx3  # Optional

def get_username():

    return "e/kashi55"

def get_current_datetime():

    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def listen():

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Helps filter noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None  # Return None if it doesn't recognize
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

def speak(text):

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():

    username = get_username()

    while True:
        command = listen()
        if command is None:
            continue  # Skip iteration if voice input was not understood

        print(f"You said: {command}")  # Display what the user said

        if "hello" in command or "hi" in command:
            response = f"Hello {username}! The current date and time is {get_current_datetime()}."
        elif "tell me the time" in command:
            response = f"The current time is {get_current_datetime()}."
        elif "exit" in command or "quit" in command:
            print("Goodbye!")
            speak("Goodbye!")
            break
        else:
            response = "I didn't understand. Try saying hello or tell me the time."

        print(response)  # Display the response
        speak(response)  # Speak the response

if __name__ == "__main__":
    main()
