import winsound  # For Windows systems (replace with playsound for broader compatibility)
import time
from datetime import datetime

def play_alarm(tone="alarm.wav"):
  """Plays the alarm sound."""
  try:
    winsound.PlaySound(tone, winsound.SND_FILENAME)
  except FileNotFoundError:
    print("Alarm tone file not found. Using default beep.")
    winsound.Beep(1000, 500)  # Default beep sound

def snooze(duration=5):
  """Waits for a specified duration before repeating the alarm."""
  print(f"Snoozing for {duration} minutes...")
  time.sleep(duration * 60)

def get_alarm_time():
  """Gets user input for desired alarm time."""
  while True:
    try:
      alarm_time_str = input("Enter desired alarm time (HH:MM format): ")
      alarm_time = datetime.strptime(alarm_time_str, "%H:%M").time()
      return alarm_time
    except ValueError:
      print("Invalid time format. Please try again.")

def get_alarm_tone():
  """Gets user input for the alarm tone filename (optional)."""
  tone = input("Enter alarm tone filename (optional, leave blank for default): ")
  return tone if tone else "alarm.wav"  # Use default tone if no input

def main():
  """Main function to run the alarm clock."""
  print("Welcome to your customizable alarm clock!")

  while True:
    alarm_time = get_alarm_time()
    alarm_tone = get_alarm_tone()

    while True:
      now = datetime.now().time()
      if now >= alarm_time:
        play_alarm(alarm_tone)
        snooze_choice = input("Snooze (s) or Stop (q)? ").lower()
        if snooze_choice == 's':
          snooze()
        else:
          break

if __name__ == "__main__":
  main()