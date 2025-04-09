from datetime import datetime


"""Dates"""

now = datetime.now()
print("Current date and time:", now)
print("Current date:", now.date())
print("Current time:", now.time())
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current second:", now.second)

birth_date = datetime(1985, 6, 17, 9, 30, 0)
print("Birth date:", birth_date)
print("Birth date year:", birth_date.year)
print("Birth date month:", birth_date.month)


difference = (now - birth_date).days
print("Days since birth:", difference)
print(type(difference))

years = difference // 365
print("Years since birth:", years)

"""Exercise"""

# Day, month, year
print(birth_date.strftime("%d/%m/%Y"))
print(birth_date.strftime("%d/%m/%y"))

# Hour, minute, second
print(birth_date.strftime("%H:%M:%S"))
print(birth_date.strftime("%H:%M"))

# Day of the year
print(birth_date.strftime("%j"))
print(birth_date.strftime("%w"))

# Day of the week
print(birth_date.strftime("%A"))
print(birth_date.strftime("%a"))

# Name of the month
print(birth_date.strftime("%B"))
print(birth_date.strftime("%b"))

# Local default representation
print(birth_date.strftime("%c"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))

# AM/PM
print(birth_date.strftime("%I:%M %p"))
print(birth_date.strftime("%p"))


print(f"My birthday is on {birth_date.strftime('%A')}, {birth_date.strftime('%d')} of {birth_date.strftime('%B')} of {birth_date.strftime('%Y')} at {birth_date.strftime('%H:%M:%S')}")
print(f"My birthday is on {birth_date.strftime('%A')}, {birth_date.strftime('%d')} of {birth_date.strftime('%B')} of {birth_date.strftime('%Y')} at {birth_date.strftime('%I:%M %p')}")
