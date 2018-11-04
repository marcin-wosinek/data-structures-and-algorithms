import random

days = range(356)

for n in range(5, 101, 5):
  print('Testing the birthday paradox for', n)

  birthdays = []
  count = 0

  for x in range(n):
    day = random.choice(days)
    if (day in birthdays):
      count += 1
    else:
      birthdays.append(day)

  print('There were', count, 'colisitions')
