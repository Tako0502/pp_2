from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Date Five Days Ago:", new_date)
 #-------------------------Tasks---------------------------
today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
 #-------------------------Tasks---------------------------

current_datetime = datetime.now()

current_datetime = current_datetime.replace(microsecond=0)

print("Datetime without Microseconds:", current_datetime)
 #-------------------------Tasks---------------------------


date1 = datetime(2024, 2, 10, 12, 30, 45)
date2 = datetime(2024, 2, 5, 8, 15, 30)

difference = (date1 - date2).total_seconds()

print("Difference in seconds:", difference)