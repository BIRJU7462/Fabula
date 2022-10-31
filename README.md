# Fabula

## Overview
Fabula is a story telling AI assistant. It takes a story request from the user in form of speech, searches the database for the story and, if the story is found, it is recited to the user. 

The stories are stored locally on the system and the path needs to be specified before the script is executed. The biggest advantage this provides is that more and more stories can be added effortlessly. 

Now, Fabula is able is to perform the speech-to-text conversion with no delay what so ever! The majority of the running time, after the user had requested a story, is used up to search for the same in the database. The library employed, Pyttsx3, uses Google API to perform the conversion, and Pyaudio to input command from the microphone.

## Libraries Used
- SpeechRecognition
- pyttsx3
- pyaudio

## How to Install and Run the Project
Install the library mentioned above on your local system.

Story names will be displayed on the screen which are stored in the database.
Then, user need to give input of story name which he want to listen in form of speech.


`path(in function 'read') is static, i.e, user need to give path where their stories are saved.
        example- If stories are in 'D' drive in folder named 'stories'. Then,
                    path="D:\\\\stories\\"+val+".txt"
                        Use \\ for \`

## Significance
- Beneficial for visually impaired people.
- Cost effective. You just need Python.
- More stories can be added.

## Future Implications
- Authors and writers can publish their stories online.
- People can publish their own stories.
- Can be extended to different languages.



