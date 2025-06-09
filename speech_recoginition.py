import sys
import threading
import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

class SpeechToTextApp:
    def __init__(self, root):  # ✅ Double underscores!
        self.root = root
        root.title("🎙 Speech to Text Transcriber")
        root.geometry("650x450")

        self.is_recording = False
        self.auto_save = tk.BooleanVar(value=True)
        self.dark_mode = False

        self.recognizer = sr.Recognizer()

        self.status_label = tk.Label(root, text="Press 'Start Recording' to begin 🎤", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.text_box = scrolledtext.ScrolledText(root, width=70, height=12, font=("Arial", 14))
        self.text_box.pack(padx=10, pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.record_button = tk.Button(btn_frame, text="▶ Start Recording", command=self.start_recording, font=("Arial", 12))
        self.record_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(btn_frame, text="⏹ Stop", command=self.stop_recording, font=("Arial", 12), state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.clear_button = tk.Button(btn_frame, text="🧹 Clear", command=self.clear_text, font=("Arial", 12))
        self.clear_button.grid(row=0, column=2, padx=5)

        self.theme_button = tk.Button(btn_frame, text="🌙 Dark Mode", command=self.toggle_theme, font=("Arial", 12))
        self.theme_button.grid(row=0, column=3, padx=5)

        self.save_checkbox = tk.Checkbutton(root, text="Auto Save Transcription", variable=self.auto_save, font=("Arial", 11))
        self.save_checkbox.pack()

    def start_recording(self):
        self.is_recording = True
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="🎙 Calibrating microphone...", fg="blue")
        self.text_box.delete('1.0', tk.END)
        threading.Thread(target=self.listen_and_transcribe).start()

    def stop_recording(self):
        self.is_recording = False
        self.status_label.config(text="🛑 Stopped recording early.", fg="orange")
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def listen_and_transcribe(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=2)
                self.status_label.config(text="🎙 Speak now... (you have 10 seconds)", fg="blue")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                if not self.is_recording:
                    return
                self.status_label.config(text="🔊 Audio captured, transcribing...", fg="green")
                text = self.recognizer.recognize_google(audio)
                self.text_box.insert(tk.END, text + "\n")
                self.status_label.config(text="✅ Transcription complete!", fg="darkgreen")

                if self.auto_save.get():
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    filename = f"transcription_{timestamp}.txt"
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(text)
        except sr.WaitTimeoutError:
            self.status_label.config(text="⌛ Timeout: You didn’t start speaking in time.", fg="red")
        except sr.UnknownValueError:
            self.status_label.config(text="😕 Could not understand the audio.", fg="red")
        except sr.RequestError as e:
            self.status_label.config(text=f"❌ API error: {e}", fg="red")
            self.log_error(e)
        except Exception as e:
            self.status_label.config(text=f"⚠ Error: {e}", fg="red")
            self.log_error(e)
        finally:
            self.record_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.is_recording = False

    def clear_text(self):
        self.text_box.delete('1.0', tk.END)
        self.status_label.config(text="🧹 Text cleared.", fg="gray")

    def toggle_theme(self):
        if self.dark_mode:
            self.root.config(bg="SystemButtonFace")
            self.status_label.config(bg="SystemButtonFace", fg="black")
            self.text_box.config(bg="white", fg="black", insertbackground="black")
            self.theme_button.config(text="🌙 Dark Mode")
        else:
            self.root.config(bg="#2e2e2e")
            self.status_label.config(bg="#2e2e2e", fg="white")
            self.text_box.config(bg="#1e1e1e", fg="white", insertbackground="white")
            self.theme_button.config(text="☀ Light Mode")
        self.dark_mode = not self.dark_mode

    def log_error(self, error):
        with open("error_log.txt", "a", encoding="utf-8") as log:
            log.write(f"[{datetime.now()}] {error}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()
