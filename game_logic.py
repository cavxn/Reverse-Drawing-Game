import time

def start_guess_timer(seconds=5):
    print(f"\n⏳ You have {seconds} seconds to guess!")
    time.sleep(seconds)
    print("⌛ Time's up! What did you guess?")
def check_guess(user_guess, correct_answer):
    return user_guess.strip().lower() == correct_answer.lower()
