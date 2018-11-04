import random

value = input()

words = value.split()

wordCounts = {}

for word in words:
  if (word in wordCounts):
    wordCounts[word] += 1
  else:
    wordCounts[word] = 1

print(wordCounts)
