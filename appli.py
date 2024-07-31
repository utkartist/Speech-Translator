from deep_translator import GoogleTranslator
from playsound import playsound 
import speech_recognition as sr 
from googletrans import Translator 
from gtts import gTTS 
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Language tuple with language name and code
languages = {
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 
    'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 
    'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 
    'cebuano': 'ceb', 'chichewa': 'ny', 'chinese': 'zh-cn', 'corsican': 'co', 
    'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 
    'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 
    'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 
    'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 
    'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 
    'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 
    'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 
    'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 
    'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 
    'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 
    'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 
    'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 
    'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 
    'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 
    'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 
    'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 
    'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 
    'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 
    'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 
    'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 
    'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 
    'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 
    'yoruba': 'yo', 'zulu': 'zu'
}

# Function to capture voice input
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could not understand audio, please say that again...")
        return "None"
    return query

# Function to get the destination language from the user
def destination_language(prompt):
    print(prompt)
    to_lang = take_command().lower()
    while to_lang == "None" or to_lang not in languages:
        print("Language not available or not recognized, please input a different language:")
        to_lang = take_command().lower()
    return languages[to_lang]

# Function to translate and store the translation
def translate_and_store(text, lang_code, filename):
    translator = Translator()
    text_to_translate = translator.translate(text, dest=lang_code)
    translated_text = text_to_translate.text
    
    # Convert the translated text to speech
    speak = gTTS(text=translated_text, lang=lang_code, slow=False)
    speak.save(filename)
    
    # Play the translated voice
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Print the translated text
    print(translated_text)
    
    return translated_text

# Main process
if __name__ == "__main__":
    # Get the user's voice input
    query = take_command()
    while query == "None":
        query = take_command()
    
    # Get the primary language
    primary_lang = destination_language("Enter the primary language in which you want to convert (e.g., Hindi, English, etc.):")
    
    # Get the secondary language
    secondary_lang = destination_language("Enter the secondary language in which you want to convert (e.g., Hindi, English, etc.):")
    
    # Translate and store the translations
    primary_translation = translate_and_store(query, primary_lang, "primary_translation.mp3")
    secondary_translation = translate_and_store(query, secondary_lang, "secondary_translation.mp3")
    
    # Print both translations
    print(f"Primary Translation: {primary_translation}")
    print(f"Secondary Translation: {secondary_translation}")
    
    # Stop playback and remove the files
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove("primary_translation.mp3")
    os.remove("secondary_translation.mp3")
