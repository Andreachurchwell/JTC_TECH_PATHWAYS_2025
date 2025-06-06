# import tkinter as tk
# import random
# import pygame

# pygame.mixer.init()

# sound_map = {
#     'The Wonder Years': 'sounds/wonderYears.mp3',
#     'Dukes of Hazzard': 'sounds/dukesOfH.mp3',
#     'Cheers': 'sounds/cheers.mp3',
#     'The Golden Girls': 'sounds/ggs.mp3',
#     'The Cosby Show': 'sounds/cosby.mp3',
#     'Samford and Son': 'sounds/samford.mp3',
#     'The Jeffersons': 'sounds/theJs.mp3',
#     'Doogie Howser MD': 'sounds/doogie.mp3',
#     'Full House': 'sounds/fullHouse.mp3',
#     'Saved By The Bell': 'sounds/sbtb.mp3',
#     'Married With Children': 'sounds/mwc.mp3',
#     'Fresh Prince Of Belair': 'sounds/freshP.mp3',
#     'Frasier': 'sounds/frasier.mp3',
#     'Home Improvement': 'sounds/homeImp.mp3',
#     'Threes Company': 'sounds/threesC.mp3',
#     'Different Strokes': 'sounds/diffSt.mp3',
#     'Night Court': 'sounds/nightCourt.mp3',
#     'The Office': 'sounds/theOffice.mp3',
#     'Two and a Half Men': 'sounds/twoAndaH.mp3',
#     'Night Rider': 'sounds/nightRider.mp3'

# }

# last_show = None
# score = 0
# clip_duration_ms = 35000  

# def play_clip(show):
#     try:
#         pygame.mixer.music.stop()
#         pygame.mixer.music.load(sound_map[show])
#         pygame.mixer.music.set_volume(1.0)
#         pygame.mixer.music.play()
#         # Schedule stop clip after 15 seconds
#         root.after(clip_duration_ms, stop_clip)
#         print(f"Playing: {show}")
#     except Exception as e:
#         print(f"Error playing {show}: {e}")

# def stop_clip():
#     pygame.mixer.music.stop()

# def play_random_clip():
#     global last_show
#     shows = list(sound_map.keys())
#     if last_show and len(shows) > 1:
#         shows = [s for s in shows if s != last_show]
#     show = random.choice(shows)
#     last_show = show
#     current_label.config(text='NAME THAT SHOW!')
#     play_clip(show)
#     guess_entry.delete(0, tk.END)
#     guess_entry.focus()

# def check_guess(event=None):
#     global score
#     guess = guess_entry.get().strip().lower()
#     if not last_show:
#         current_label.config(text="Click 'Play' to start!")
#         return

#     correct_answer = last_show.lower()

#     if guess == correct_answer:
#         score += 1
#         feedback = f"Correct! It was {last_show}."
#     else:
#         feedback = f"Wrong! It was {last_show}."

#     score_label.config(text=f"Score: {score}")
#     current_label.config(text=feedback)

#     stop_clip()
#     # Automatically play next clip after short delay so user sees feedback
#     root.after(2000, play_random_clip)

# # GUI setup
# root = tk.Tk()
# root.title("📺 Guess That Sitcom!")
# root.configure(bg="#1e1e2f")  # Retro dark purple background

# title_font = ("Comic Sans MS", 20, "bold")
# text_font = ("Courier New", 14)

# current_label = tk.Label(root, text="Click 'Play Jingle' to start!", 
#                          font=title_font, fg="#ffcc00", bg="#1e1e2f")
# current_label.pack(pady=20)

# play_btn = tk.Button(root, text="▶️ Play Jingle", command=play_random_clip,
#                      font=text_font, bg="#00bcd4", fg="white", activebackground="#008c9e")
# play_btn.pack(pady=10)

# guess_entry = tk.Entry(root, font=text_font, bg="#333355", fg="white", insertbackground="white")
# guess_entry.pack(pady=10)
# guess_entry.bind('<Return>', check_guess)

# submit_btn = tk.Button(root, text="✅ Submit Guess", command=check_guess,
#                        font=text_font, bg="#00bcd4", fg="white", activebackground="#008c9e")
# submit_btn.pack(pady=10)

# score_label = tk.Label(root, text=f"Score: {score}", 
#                        font=("Comic Sans MS", 14), fg="#ffcc00", bg="#1e1e2f")
# score_label.pack(pady=10)

# root.mainloop()



# import tkinter as tk
# import random
# import pygame

# pygame.mixer.init()

# sound_map = {
#     'The Wonder Years': 'sounds/wonderYears.mp3',
#     'Dukes of Hazzard': 'sounds/dukesOfH.mp3',
#     'Cheers': 'sounds/cheers.mp3',
#     'The Golden Girls': 'sounds/ggs.mp3',
#     'The Cosby Show': 'sounds/cosby.mp3',
#     'Samford and Son': 'sounds/samford.mp3',
#     'The Jeffersons': 'sounds/theJs.mp3',
#     'Doogie Howser MD': 'sounds/doogie.mp3',
#     'Full House': 'sounds/fullHouse.mp3',
#     'Saved By The Bell': 'sounds/sbtb.mp3',
#     'Married With Children': 'sounds/mwc.mp3',
#     'Fresh Prince Of Belair': 'sounds/freshP.mp3',
#     'Frasier': 'sounds/frasier.mp3',
#     'Home Improvement': 'sounds/homeImp.mp3',
#     'Threes Company': 'sounds/threesC.mp3',
#     'Different Strokes': 'sounds/diffSt.mp3',
#     'Night Court': 'sounds/nightCourt.mp3',
#     'The Office': 'sounds/theOffice.mp3',
#     'Two and a Half Men': 'sounds/twoAndaH.mp3',
#     'Knight Rider': 'sounds/knightRider.mp3'
# }

# last_show = None
# score = 0
# clip_duration_ms = 35000
# playlist = []  # To track shuffled songs

# def play_clip(show):
#     try:
#         pygame.mixer.music.stop()
#         pygame.mixer.music.load(sound_map[show])
#         pygame.mixer.music.set_volume(1.0)
#         pygame.mixer.music.play()
#         # root.after(clip_duration_ms, stop_clip)
#         print(f"Playing: {show}")
#     except Exception as e:
#         print(f"Error playing {show}: {e}")

# def stop_clip():
#     pygame.mixer.music.stop()

# def play_random_clip():
#     global last_show, playlist

#     if not playlist:
#         playlist = list(sound_map.keys())
#         random.shuffle(playlist)

#     show = playlist.pop()
#     last_show = show
#     current_label.config(text='NAME THAT SHOW!')
#     play_clip(show)
#     guess_entry.delete(0, tk.END)
#     guess_entry.focus()

# def check_guess(event=None):
#     global score
#     guess = guess_entry.get().strip().lower()

#     if not last_show:
#         current_label.config(text="Click 'Play' to start!")
#         return

#     correct_answer = last_show.lower()

#     if guess == correct_answer:
#         score += 1
#         feedback = f"✅ Correct! It was {last_show}."
#     else:
#         feedback = f"❌ Wrong! It was {last_show}."

#     score_label.config(text=f"Score: {score}")
#     current_label.config(text=feedback)

#     stop_clip()
#     root.after(2000, play_random_clip)

# # GUI setup
# root = tk.Tk()
# root.title("📺 Guess That Sitcom!")
# root.configure(bg="#1e1e2f")

# title_font = ("Comic Sans MS", 20, "bold")
# text_font = ("Courier New", 14)

# current_label = tk.Label(root, text="Click 'Play Jingle' to start!", 
#                          font=title_font, fg="#ffcc00", bg="#1e1e2f")
# current_label.pack(pady=20)

# play_btn = tk.Button(root, text="▶️ Play Jingle", command=play_random_clip,
#                      font=text_font, bg="#00bcd4", fg="white", activebackground="#008c9e")
# play_btn.pack(pady=10)

# guess_entry = tk.Entry(root, font=text_font, bg="#333355", fg="white", insertbackground="white")
# guess_entry.pack(pady=10)
# guess_entry.bind('<Return>', check_guess)

# submit_btn = tk.Button(root, text="✅ Submit Guess", command=check_guess,
#                        font=text_font, bg="#00bcd4", fg="white", activebackground="#008c9e")
# submit_btn.pack(pady=10)

# score_label = tk.Label(root, text=f"Score: {score}", 
#                        font=("Comic Sans MS", 14), fg="#ffcc00", bg="#1e1e2f")
# score_label.pack(pady=10)



# is_playing = False

# def reset_score():
#     global score, playlist
#     score = 0
#     score_label.config(text=f"Score: {score}")
#     playlist = list(sound_map.keys())
#     random.shuffle(playlist)
#     current_label.config(text="Game reset! Click Play to start.")

# def toggle_play():
#     global is_playing
#     if is_playing:
#         stop_clip()
#         play_btn.config(text="▶️ Play Jingle")
#         is_playing = False
#     else:
#         play_random_clip()
#         play_btn.config(text="⏹ Stop")
#         is_playing = True

# reset_btn = tk.Button(root, text="🔄 Reset Score", command=reset_score,
#                       font=text_font, bg="#ff5722", fg="white")
# reset_btn.pack(pady=5)



# root.mainloop()


import tkinter as tk
import random
import pygame

pygame.mixer.init()

sound_map = {
    'The Wonder Years': 'sounds/wonderYears.mp3',
    'Dukes of Hazzard': 'sounds/dukesOfH.mp3',
    'Cheers': 'sounds/cheers.mp3',
    'The Golden Girls': 'sounds/ggs.mp3',
    'The Cosby Show': 'sounds/cosby.mp3',
    'Samford and Son': 'sounds/samford.mp3',
    'The Jeffersons': 'sounds/theJs.mp3',
    'Doogie Howser MD': 'sounds/doogie.mp3',
    'Full House': 'sounds/fullHouse.mp3',
    'Saved By The Bell': 'sounds/sbtb.mp3',
    'Married With Children': 'sounds/mwc.mp3',
    'Fresh Prince Of Belair': 'sounds/freshP.mp3',
    'Frasier': 'sounds/frasier.mp3',
    'Home Improvement': 'sounds/homeImp.mp3',
    'Threes Company': 'sounds/threesC.mp3',
    'Different Strokes': 'sounds/diffSt.mp3',
    'Night Court': 'sounds/nightCourt.mp3',
    'The Office': 'sounds/theOffice.mp3',
    'Two and a Half Men': 'sounds/twoAndaH.mp3',
    'Knight Rider': 'sounds/knightRider.mp3'
}

last_show = None
score = 0
high_score = 0
clip_time_sec = 20
timer_id = None
playlist = []

def play_clip(show):
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(sound_map[show])
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        print(f"Playing: {show}")
    except Exception as e:
        print(f"Error playing {show}: {e}")

def stop_clip():
    pygame.mixer.music.stop()

def start_timer(seconds):
    def countdown(t):
        global timer_id
        if t >= 0:
            timer_label.config(text=f"Time Left: {t}s")
            timer_id = root.after(1000, countdown, t-1)
        else:
            reveal_answer_and_next()
    countdown(seconds)

def reveal_answer_and_next():
    global score, high_score, timer_id
    stop_clip()
    if timer_id is not None:
        root.after_cancel(timer_id)

    feedback = f"⏰ Time's up! It was {last_show}."
    current_label.config(text=feedback)
    update_high_score()
    root.after(3000, play_random_clip)

def update_high_score():
    global score, high_score
    if score > high_score:
        high_score = score
        high_score_label.config(text=f"High Score: {high_score}")


def get_cute_msg(final_score):
    if final_score <= 3:
        return "Don't worry, every sitcom fan starts somewhere! 😅"
    elif final_score <= 7:
        return "Nice! You know your classics! 👍"
    else:
        return "TV Trivia Master! 👑 You're unstoppable!"

def play_random_clip():
    global last_show, playlist, timer_id
    if not playlist:
        # Game over - show final score and cute message
        cute_msg = get_cute_msg(score)
        current_label.config(text=f"🎉 Game Over! Final Score: {score}\n{cute_msg}\nPress 'Reset Game' to play again.")

        stop_clip()
        timer_label.config(text="Time Left: --")
        update_high_score()
        return

    show = playlist.pop()
    last_show = show
    current_label.config(text='NAME THAT SHOW!')
    play_clip(show)
    guess_entry.delete(0, tk.END)
    guess_entry.focus()
    start_timer(clip_time_sec)

# def check_guess(event=None):
#     global score, timer_id
#     guess = guess_entry.get().strip().lower()

#     if not last_show:
#         current_label.config(text="Click 'Play Jingle' to start!")
#         return

#     if timer_id is not None:
#         root.after_cancel(timer_id)

#     correct_answer = last_show.lower()

#     if guess == correct_answer:
#         score += 1
#         feedback = f"✅ Correct! It was {last_show}."
#     else:
#         feedback = f"❌ Wrong! It was {last_show}."

#     score_label.config(text=f"Score: {score}")

#     # Only show basic feedback during the game, no cute message here
#     current_label.config(text=feedback)
#     stop_clip()
#     root.after(3000, play_random_clip)

def check_guess(event=None):
    global score, timer_id
    guess = guess_entry.get().strip().lower()

    if not last_show:
        current_label.config(text="Click 'Play Jingle' to start!")
        return

    if timer_id is not None:
        root.after_cancel(timer_id)

    correct_answer = last_show.lower()

    if guess == correct_answer:
        score += 1
        feedback = f"✅ Correct! It was {last_show}."
        update_high_score()  # <-- update high score here!
    else:
        feedback = f"❌ Wrong! It was {last_show}."

    score_label.config(text=f"Score: {score}")
    current_label.config(text=feedback)

    stop_clip()
    root.after(3000, play_random_clip)


def reset_game():
    global score, playlist, last_show, timer_id
    if timer_id is not None:
        root.after_cancel(timer_id)
    score = 0
    score_label.config(text=f"Score: {score}")
    current_label.config(text="Game reset! Click 'Play Jingle' to start.")
    timer_label.config(text="Time Left: --")
    playlist = list(sound_map.keys())
    random.shuffle(playlist)
    last_show = None
    stop_clip()
    guess_entry.delete(0, tk.END)

# GUI setup remains the same as before...

root = tk.Tk()
root.title("📺 Guess That Sitcom!")
root.configure(bg="#1e1e2f")

title_font = ("Comic Sans MS", 20, "bold")
text_font = ("Courier New", 14)

current_label = tk.Label(root, text="Click 'Play Jingle' to start!", 
                         font=title_font, fg="#ffcc00", bg="#1e1e2f", justify="center")
current_label.pack(pady=20)

timer_label = tk.Label(root, text="Time Left: --", font=text_font, fg="#ffcc00", bg="#1e1e2f")
timer_label.pack(pady=5)

high_score_label = tk.Label(root, text=f"High Score: {high_score}", font=text_font, fg="#ffcc00", bg="#1e1e2f")
high_score_label.pack(pady=5)

play_btn = tk.Button(root, text="▶️ Play Jingle", command=play_random_clip,
                     font=text_font, bg="#00bcd4", fg="white", activebackground="#008c9e")
play_btn.pack(pady=10)

guess_entry = tk.Entry(root, font=text_font, bg="#333355", fg="white", insertbackground="white")
guess_entry.pack(pady=10)
guess_entry.bind('<Return>', check_guess)

submit_btn = tk.Button(root, text="✅ Submit Guess", command=check_guess,
                       font=text_font, bg="#00bcd4", fg="white", activebackground="#008c9e")
submit_btn.pack(pady=10)

score_label = tk.Label(root, text=f"Score: {score}", 
                       font=("Comic Sans MS", 14), fg="#ffcc00", bg="#1e1e2f")
score_label.pack(pady=10)

reset_btn = tk.Button(root, text="🔄 Reset Game", command=reset_game,
                      font=text_font, bg="#ff5722", fg="white")
reset_btn.pack(pady=10)

playlist = list(sound_map.keys())
random.shuffle(playlist)

root.mainloop()

