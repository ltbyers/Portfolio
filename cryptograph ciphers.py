alphabet = "abcdefghijklmnopqrstuvwxyz"

def ceasar_decode_message(message,offset):
  new_message = ""
  message = message.lower()
  for i in range(len(message)):
    if message[i] in alphabet:
      x = alphabet.find(message[i])+offset
      if x < len(alphabet):
        new_message += alphabet[x]
      else:
        y = x - 26
        new_message += alphabet[y]
    else:
      new_message += message[i]
  return new_message


def ceasar_code_message(message,offset):
  message = message.lower()
  new_message = ""
  for i in range(len(message)):
    if message[i] in alphabet:
      x = alphabet.find(message[i])-offset
      if x >= 0:
        new_message += alphabet[x]
      else:
        y = x + 26
        new_message += alphabet[y]
    else:
      new_message += message[i]
  return new_message

def vigenere_decode_message(message,word):
  y = 0
  message = message.lower()
  new_message = ""
  for x in range(len(message)):
    if message[x] in alphabet:
      if y >= len(word):
        y = 0
      z = alphabet.find(message[x])
      a = alphabet.find(word[y])
      if z - a < 0:
        new_char = alphabet[(z - a) + 26]
      else:
        new_char = alphabet[z - a]
      new_message += new_char
      y += 1
    else:
      new_message += message[x]
  return new_message

def vigenere_code_message(message,word):
  y = 0
  message = message.lower()
  new_message = ""
  for x in range(len(message)):
    if message[x] in alphabet:
      if y >= len(word):
        y = 0
      z = alphabet.find(message[x])
      a = alphabet.find(word[y])
      if z + a > 25:
        new_char = alphabet[(z + a) - 26]
      else:
        new_char = alphabet[z + a]
      new_message += new_char
      y += 1
    else:
      new_message += message[x]
  return new_message