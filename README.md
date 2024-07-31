# speech-translator-using-llms
This script is a voice translation program that captures spoken input, translates it into specified languages, and then converts the translated text into speech. Here's a step-by-step breakdown of the code's functionality:

## Initialization and Imports:
The script imports necessary libraries such as GoogleTranslator, playsound, speech_recognition, googletrans, gtts, os, and pygame.

## Language Dictionary:
A dictionary named languages is created, mapping language names to their corresponding ISO codes. This dictionary is used to identify and convert language names to their respective codes.

## Pygame Mixer Initialization: 
The pygame mixer is initialized for playing the audio.

## Voice Command Function (take_command):

This function captures voice input using the microphone.
It uses the speech_recognition library to listen to the user's voice and convert it to text.
If the voice input is recognized, it returns the recognized text. If not, it prompts the user to repeat.
Destination Language Function (destination_language):

This function prompts the user to specify the language they want to translate their speech into.
It uses the take_command function to capture the language input.
It validates the captured language against the languages dictionary to ensure it's a recognized language.
If the input language is not recognized, it keeps prompting the user until a valid language is provided.
Main Process:

The script captures the user's voice input using the take_command function.
It ensures valid voice input is captured by repeating the take_command function until a valid input is obtained.
It captures the primary and secondary languages using the destination_language function.
It translates the captured text to the specified languages using the googletrans library's Translator class.
The translated text is converted to speech using the gTTS (Google Text-to-Speech) library.
The generated speech is saved as MP3 files named primary_translation.mp3 and secondary_translation.mp3.
The pygame mixer is used to play the MP3 files.
After playing the audio, the MP3 files are removed from the system.
Finally, the translated text is printed to the console.


## Features:
### Dual Translations: 
The script now translates the input into both a primary and a secondary language.
### Translation Storage: 
Both translations are stored as separate MP3 files and played back sequentially.
User Prompts for Languages: Separate prompts for the primary and secondary languages are provided to the user.
Print Both Translations: Both translations are printed to the console.

## Applications:
### Language Learning: 
This tool can assist in learning new languages by providing audio translations.

### Travel Assistance: 
It can be used by travelers to communicate in different languages.

### Accessibility:
The tool can help people with speech or language impairments to communicate more effectively.

### Multilingual Customer Support:
Businesses can use it to provide customer support in multiple languages.

### Educational Tools: 
It can be integrated into educational platforms to support multilingual education.

Overall, the script seamlessly integrates voice recognition, translation, text-to-speech conversion, and audio playback to provide a complete voice translation experience.
