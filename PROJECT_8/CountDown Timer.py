import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print("👉\t", timer, end="\r")  # overwrite line
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")

try:
    total_time = int(input("\n⏳ Enter time in seconds: "))
    print("      Starting countdown...")
    countdown_timer(total_time)
except ValueError:
    print("❌ Invalid input! Please enter an integer.")