import calendar
from datetime import datetime

class Reminder:
  def __init__(self, date, text):
    self.date = date
    self.text = text

class CalendarApp:
  def __init__(self):
    self.reminders = []
    self.current_date = datetime.now()

  def display_calendar(self):
    """Displays the calendar for the current month."""
    year = self.current_date.year
    month = self.current_date.month
    print(calendar.month(year, month))

  def add_reminder(self):
    """Gets user input and adds a reminder for a specific date."""
    while True:
      try:
        date_str = input("Enter reminder date (YYYY-MM-DD format): ")
        reminder_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        reminder_text = input("Enter reminder text: ")
        self.reminders.append(Reminder(reminder_date, reminder_text))
        break
      except ValueError:
        print("Invalid date format. Please try again.")

  def view_reminders(self):
    """Displays all upcoming reminders."""
    upcoming_reminders = [r for r in self.reminders if r.date >= self.current_date.date()]
    if upcoming_reminders:
      print("Upcoming Reminders:")
      for reminder in upcoming_reminders:
        print(f"- {reminder.date.strftime('%Y-%m-%d')}: {reminder.text}")
    else:
      print("You don't have any upcoming reminders.")

  def run(self):
    """Main loop for user interaction."""
    while True:
      print("\nCalendar and Reminder App")
      print("1. Display Calendar")
      print("2. Add Reminder")
      print("3. View Reminders")
      print("4. Exit")

      choice = input("Enter your choice: ")

      if choice == '1':
        self.display_calendar()
      elif choice == '2':
        self.add_reminder()
      elif choice == '3':
        self.view_reminders()
      elif choice == '4':
        break
      else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
  app = CalendarApp()
  app.run()