
# Import the sqlite3 module for working with the SQLite database
import sqlite3

# Import tkinter for creating the GUI
import tkinter as tk

# Import messagebox for showing pop-up alerts
from tkinter import messagebox

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('rock_albums.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the main application class
class MusicQuizApp:
    def __init__(self, master):
        self.master = master  # Reference to the main window
        self.score = 0  # Tracks the number of correct answers
        self.total_questions = 5  # Total number of quiz questions
        self.current_question = 0  # Counter for the current question

        # --- Window setup ---
        self.master.title("🎵 Music Quiz")  # Set the window title
        self.master.configure(bg="#1e1e2f")  # Set background color
        self.master.geometry("600x350")  # Set window size

        # --- Fonts and color themes ---
        self.header_font = ("Segoe UI", 20, "bold")
        self.text_font = ("Segoe UI", 14)
        self.btn_font = ("Segoe UI", 14, "bold")

        self.bg_color = "#1e1e2f"  # Background color
        self.fg_color = "#e0e0e0"  # Default text color
        self.accent_color = "#61afef"  # Accent color for highlights
        self.success_color = "#98c379"  # Color for correct answers
        self.error_color = "#e06c75"  # Color for wrong answers
        self.entry_bg = "#2c2f44"  # Background color for input box
        self.entry_fg = "#ffffff"  # Text color for input box

        # --- Main container frame for layout ---
        self.container = tk.Frame(master, bg=self.bg_color)
        self.container.pack(expand=True, fill="both", padx=40, pady=30)

        # --- Label to display the quiz question ---
        self.question_label = tk.Label(
            self.container, text="", font=self.header_font, 
            bg=self.bg_color, fg=self.accent_color, 
            wraplength=550, justify="center"
        )
        self.question_label.pack(pady=(0, 30))

        # --- Text entry for the user to type their answer ---
        self.answer_entry = tk.Entry(
            self.container, font=self.text_font, bg=self.entry_bg, fg=self.entry_fg,
            insertbackground=self.entry_fg, relief="flat", justify="center"
        )
        self.answer_entry.pack(ipadx=10, ipady=8, pady=(0, 20))

        # --- Button to submit the answer ---
        self.submit_button = tk.Button(
            self.container, text="Submit", font=self.btn_font,
            bg=self.accent_color, fg=self.bg_color,
            activebackground="#528cd9", activeforeground=self.bg_color,
            relief="flat", command=self.check_answer  # Link to check_answer method
        )
        self.submit_button.pack(ipadx=10, ipady=8, pady=(0, 20))

        # --- Label to show feedback (correct/wrong) ---
        self.result_label = tk.Label(
            self.container, text="", font=self.text_font,
            bg=self.bg_color, fg=self.fg_color
        )
        self.result_label.pack()

        # Start the first question
        self.next_question()

    # Fetch a random album and its artist from the database
    def get_random_album_artist(self):
        cursor.execute("SELECT album, artist FROM albums ORDER BY RANDOM() LIMIT 1")
        return cursor.fetchone()

    # Load the next question or show the final score if quiz is over
    def next_question(self):
        if self.current_question < self.total_questions:
            self.album, self.artist = self.get_random_album_artist()  # Get new Q&A
            self.question_label.config(text=f"Who is the artist of the album\n'{self.album}'?")
            self.answer_entry.delete(0, tk.END)  # Clear input box
            self.result_label.config(text="")  # Clear result label
            self.current_question += 1
            self.answer_entry.focus()  # Focus cursor on input
        else:
            # Show final score and close app
            messagebox.showinfo("Quiz Over", f"You scored {self.score} out of {self.total_questions}!")
            self.master.quit()

    # Check user's answer and give feedback
    def check_answer(self):
        user_answer = self.answer_entry.get().strip()  # Get and trim user input
        if user_answer.lower() == self.artist.lower():  # Compare ignoring case
            self.score += 1
            self.result_label.config(text="✅ Correct!", fg=self.success_color)
        else:
            self.result_label.config(
                text=f"❌ Wrong! The correct answer is {self.artist}.",
                fg=self.error_color
            )
        self.submit_button.config(state="disabled")  # Prevent multiple submissions
        self.master.after(1500, self._enable_next)  # Wait 1.5 sec, then move on

    # Re-enable submit button and go to next question
    def _enable_next(self):
        self.submit_button.config(state="normal")
        self.next_question()

# --- Run the application ---
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = MusicQuizApp(root)  # Create an instance of the quiz app
    root.mainloop()  # Start the Tkinter event loop
    conn.close()  # Close the database connection when the app is done