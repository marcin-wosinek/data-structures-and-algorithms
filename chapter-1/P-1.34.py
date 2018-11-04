import random

sentence = "I will never spam my friends again"
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

array = [list(sentence) for i in range(100)]

for x in range(8):
  typo = random.choice(array)
  letter = random.randint(0, len(typo) - 1)
  typo[letter] = random.choice(alphabets)
else:
  arrayStrings = map(''.join, array)
  print('\n'.join(arrayStrings))
