def equal(memory, value):
  return value
 
def sum(memory, value):
  return memory + value
 
def multiply(memory, value):
  return memory * value

def divide(memory, value):
  return memory / value

def rest(memory, value):
  return memory - value

options = {
  '': equal,
  '=': equal,
  '+': sum,
  '*': multiply,
  '/': divide,
  '-': rest
}

play = True

memory = 0
operation = None

while play:

  value = input()

  if (value.isdecimal()):
    if operation is None:
      memory = float(value)
    else:
      memory = operation(memory, float(value))
  else:
    operation = options[value]

  print(memory)

