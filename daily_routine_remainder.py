import schedule
import time

def morning_walk_reminder():
    print("Reminder: It's time for your morning walk. Enjoy the fresh air!")

def medication_reminder():
    print("Reminder: Please take your prescribed medication.")

# Schedule reminders
schedule.every().day.at("07:00").do(morning_walk_reminder)
schedule.every().day.at("09:00").do(medication_reminder)
schedule.every().day.at("21:00").do(medication_reminder)

while True:
    schedule.run_pending()
    time.sleep(1)
