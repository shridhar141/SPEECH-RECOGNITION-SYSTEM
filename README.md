## SPEECH-RECOGNITION-SYSTEM

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: SHRIDHAR B MAREPPAGOL

*INTERN ID*: CT04DM1492

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

## TASK DESCRIPTION

Speech-to-Text Transcription App (GUI-Based)

This Speech-to-Text Transcription App is a desktop application developed in Python that allows users to convert spoken words into written text in real time. It features a clean and interactive GUI built with the tkinter library and utilizes the speech_recognition module to capture and transcribe audio through the user's microphone. Once the user clicks the “Start Recording” button, the app listens to the audio, processes it using Google’s Speech Recognition API, and displays the transcribed text within the interface. This makes it especially useful for dictation, note-taking, or accessibility support for users who prefer speaking over typing.

The application includes several user-friendly features such as dark/light mode toggle, automatic saving of transcriptions with timestamps, and error logging for debugging. The interface also supports clearing text, and it handles exceptions like API errors, unrecognized speech, and timeouts gracefully. With responsive design enabled by Python threading, the app remains smooth and non-blocking during audio capture and transcription. Overall, it provides an efficient and accessible solution for turning speech into text, suitable for both casual users and professional environments.

How it work:The Speech-to-Text Transcription App works by combining graphical user interface elements with real-time speech recognition. When the user clicks on the “Start Recording” button, the application uses Python’s speech_recognition library to access the microphone and begin listening. Before recording, it calibrates for ambient noise to improve accuracy. The app listens to the user's voice for up to 10 seconds, captures the audio input, and then sends it to Google’s Speech Recognition API for transcription. The recognized text is then displayed in the app’s text area. This entire process runs on a separate thread to ensure the user interface stays responsive during audio capture and processing.

The tool also includes logic to automatically save each transcription into a timestamped .txt file if the auto-save option is enabled. Additional features like dark mode, clear text, and error handling enhance usability. For instance, if speech isn’t detected within the timeout period, or if the API fails, the app provides appropriate feedback messages and logs the errors in a file for troubleshooting. Through this seamless combination of speech processing, file handling, and GUI interaction, the app offers a practical, real-world solution for converting voice into text efficiently.

Key features:
  1.Real-Time Speech Recognition: Converts spoken words into written text using Google’s Speech Recognition API

  2. Ambient Noise Calibration: Automatically adjusts for background noise to improve transcription accuracy.

  3. Live Transcription Display: Shows transcribed text instantly within the GUI as soon as the speech is processed.

  4. Auto-Save Functionality: Saves each transcription as a .txt file with a unique timestamp when enabled.

  5. Dark/Light Mode Toggle: Switch between light and dark themes for better visual comfort.

  6. Clear Text Option: Quickly clears the transcription area for a new recording session.

  7. Error Handling & Logging: Captures and logs common issues like microphone errors, timeouts, and API failures.

  8. Multithreading for Responsiveness: Uses threading to keep the interface smooth and non-blocking during recording.

Applications: This tool has wide-ranging applications across industries and professions:

   1.Voice Note-Taking: Ideal for students and professionals who want to quickly record lecture notes, meeting summaries, or brainstorming ideas without typing.

   2. Journalism & Interviews: Helps reporters and content creators transcribe interviews or spoken content for article drafting and documentation.

   3.Healthcare Transcription: Useful for doctors and medical staff to record and transcribe patient notes, diagnoses, or voice memos hands-free.
   
   4.Accessibility Support: Assists individuals with physical disabilities or limited typing ability by offering an easier method to input text using voice.

   5.  Language Learning: Language learners can practice pronunciation and get instant text feedback, helping improve speaking and listening skills.

   6.Voice-Controlled Systems: Can be used as a module in larger voice-controlled applications, chatbots, or personal assistants.

   7. Business Productivity: Enhances workflow by allowing busy professionals to dictate memos, reports, and emails on the go.

The Speech-to-Text Transcription App is a Python-based desktop application that transforms spoken words into text using Google’s Speech Recognition API. Designed with a user-friendly tkinter GUI, it allows users to record audio, view live transcriptions, and optionally auto-save the results with timestamps. The app also features dark/light mode switching, error handling, and multithreaded processing to ensure a responsive and smooth user experience.













