import tkinter as tk
import random

# Sample data
nba_players = {
    # Modern players
    "LeBron James": "Lakers",
    "Stephen Curry": "Warriors",
    "Kevin Durant": "Suns",
    "Giannis Antetokounmpo": "Bucks",
    "Jayson Tatum": "Celtics",
    "Luka Doncic": "Lakers",
    "Joel Embiid": "76ers",
    "Nikola Jokic": "Nuggets",
    "Jimmy Butler": "GSW",
    "Ja Morant": "Grizzlies",
    "Damian Lillard": "Bucks",
    "Anthony Davis": "Mavericks",
    "Zion Williamson": "Pelicans",
    "Kawhi Leonard": "Clippers",
    "Paul George": "Clippers",
    "James Harden": "Clippers",
    "Devin Booker": "Suns",
    "Trae Young": "Hawks",
    "Karl-Anthony Towns": "Knicks",
    "Shai Gilgeous-Alexander": "Thunder",

    # Legends
    "Michael Jordan": "Bulls",
    "Kobe Bryant": "Lakers",
    "Shaquille O'Neal": "Lakers",
    "Tim Duncan": "Spurs",
    "Allen Iverson": "76ers",
    "Magic Johnson": "Lakers",
    "Larry Bird": "Celtics",
    "Hakeem Olajuwon": "Rockets",
    "Charles Barkley": "Suns",
    "Scottie Pippen": "Bulls",
    "Dirk Nowitzki": "Mavericks",
    "Kevin Garnett": "Celtics",
    "Dwyane Wade": "Heat",
    "Steve Nash": "Suns",
    "Gary Payton": "SuperSonics",
    "Vince Carter": "Raptors",
    "Ray Allen": "Celtics"
}


# Acceptable team name variants
team_variants = {
    "Lakers": ["lakers", "la", "los angeles lakers"],
    "Warriors": ["warriors", "gsw", "golden state", "golden state warriors"],
    "Suns": ["suns", "phoenix"],
    "Bucks": ["bucks", "milwaukee"],
    "Celtics": ["celtics", "boston"],
    "Mavericks": ["mavericks", "mavs", "dallas"],
    "76ers": ["76ers", "sixers", "philadelphia"],
    "Nuggets": ["nuggets", "denver"],
    "Heat": ["heat", "miami"],
    "Grizzlies": ["grizzlies", "memphis"],
    "Pelicans": ["pelicans", "new orleans"],
    "Clippers": ["clippers", "la clippers", "los angeles clippers"],
    "Hawks": ["hawks", "atlanta"],
    "Timberwolves": ["timberwolves", "wolves", "minnesota"],
    "Thunder": ["thunder", "okc", "oklahoma city"],
    "Spurs": ["spurs", "san antonio"],
    "Rockets": ["rockets", "houston"],
    "Bulls": ["bulls", "chicago"],
    "SuperSonics": ["supersonics", "sonics", "seattle"],
    "Raptors": ["raptors", "toronto"]
}


teams = list(set(nba_players.values()))  # Unique teams

window = tk.Tk()
window.title("🏀 NBA Team Guessing Game")
window.geometry("600x450")
window.configure(bg="#0f172a")  # Midnight Blue

# --- Fonts and Colors ---
HEADER_FONT = ("Helvetica", 24, "bold")
TEXT_FONT = ("Helvetica", 14)
BUTTON_FONT = ("Helvetica", 13, "bold")
LABEL_COLOR = "#f1f5f9"
BUTTON_BG = "#3b82f6"
BUTTON_FG = "#ffffff"
ENTRY_BG = "#3b311e"
ENTRY_FG = "#e2e8f0"

# Game state
score = 0
current_player = random.choice(list(nba_players.keys()))
guess_count = 0
MAX_GUESSES = 10


# Functions

# Add this set for legends
legend_players = {
  "Michael Jordan": "Bulls",
    "Kobe Bryant": "Lakers",
    "Shaquille O'Neal": "Lakers",
    "Tim Duncan": "Spurs",
    "Allen Iverson": "76ers",
    "Magic Johnson": "Lakers",
    "Larry Bird": "Celtics",
    "Hakeem Olajuwon": "Rockets",
    "Charles Barkley": "Suns",
    "Scottie Pippen": "Bulls",
    "Dirk Nowitzki": "Mavericks",
    "Kevin Garnett": "Celtics",
    "Dwyane Wade": "Heat",
    "Steve Nash": "Suns",
    "Gary Payton": "SuperSonics",
    "Vince Carter": "Raptors",
    "Ray Allen": "Celtics"
}

def next_player():
    global current_player
    current_player = random.choice(list(nba_players.keys()))
    
    # Change question depending on legend or modern player
    if current_player in legend_players:
        player_label.config(text=f"Who did {current_player} play for?")
    else:
        player_label.config(text=f"Which team does {current_player} play for?")
    
    result_label.config(text="")
    answer_entry.delete(0, tk.END)



def check_answer():
    global score, current_player, guess_count
    user_input = answer_entry.get().strip().lower()
    correct_team = nba_players[current_player]
    accepted_inputs = team_variants.get(correct_team, [])

    guess_count += 1

    if user_input in accepted_inputs:
        result_label.config(text="✅ Correct!")
        score += 1
    else:
        result_label.config(text=f"❌ Wrong! It was {correct_team}")

    score_label.config(text=f"Score: {score}/{guess_count}")
    answer_entry.delete(0, tk.END)

    if guess_count >= MAX_GUESSES:
        player_label.config(text="🎉 Game Over!")
        result_label.config(text=f"Final Score: {score}/{MAX_GUESSES}")
        answer_entry.config(state="disabled")
        submit_button.config(state="disabled")
        next_button.config(state="disabled")
    else:
        next_player()


# --- Layout ---
frame = tk.Frame(window, bg=window["bg"])
frame.pack(pady=30)

player_label = tk.Label(frame, text=f"Which team does {current_player} play for?",
                        font=HEADER_FONT, bg=window["bg"], fg=LABEL_COLOR, wraplength=500, justify="center")
player_label.pack(pady=20)

answer_entry = tk.Entry(frame, font=TEXT_FONT, bg=ENTRY_BG, fg=ENTRY_FG,
                        insertbackground=ENTRY_FG, justify='center', bd=2, relief="flat")
answer_entry.pack(pady=10, ipadx=10, ipady=6)

submit_button = tk.Button(frame, text="Submit", font=BUTTON_FONT,
                          bg=BUTTON_BG, fg=BUTTON_FG, relief="flat",
                          command=check_answer)
submit_button.pack(pady=5, ipadx=12, ipady=4)

next_button = tk.Button(frame, text="Next Player", font=BUTTON_FONT,
                        bg="#6366f1", fg=BUTTON_FG, relief="flat",
                        command=next_player)
next_button.pack(pady=5, ipadx=10, ipady=4)

result_label = tk.Label(frame, text="", font=TEXT_FONT, bg=window["bg"], fg=LABEL_COLOR)
result_label.pack(pady=15)

score_label = tk.Label(frame, text="Score: 0/0", font=TEXT_FONT, bg=window["bg"], fg="#fbbf24")
score_label.pack()

window.mainloop()
