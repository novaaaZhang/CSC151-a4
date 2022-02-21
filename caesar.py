# Shift a letter by the designated amount, regardless of case
def shiftLetter(char,shift):
    pass

    # Get the ASCII number for the character
    ascii = ord(char)
    
    # If the ASCII code is an uppercase letter,
    # Shift and unshift by 65 so A=0 and Z=25
    if (ascii >= 65) and (ascii <= 90):
        shifted = (ascii - 65 + shift) % 26 + 65

    # If the ASCII code is a lowercase letter,
    # Shift an unshift by 97 so a=0 and z=25
    elif (ascii >= 97) and (ascii <= 122):
        shifted = (ascii - 97 + shift) % 26 + 97
    
    # If the ASCII code isn't a letter,
    # Don't shift it at all
    else:
        shifted = ascii

    # Return the shifted ASCII code as a character
    return chr(shifted)

import random

#generate a pad for cipher
def generatePad(size):
  pass
  with open ("One_time_pad.txt","w") as file:
    for i in range(size):      
      file.write(chr(random.randrange(65,65+26)))
  
  with open ("One_time_pad.txt") as file:
    pad = file.read()
  
  return pad

#decipher a code
def decipher(message,pad):
  pass
  decipher = ""
  count = 0
  dec_asc=0

  for i in range (len(message)):
    if message[i].isalpha()== True:
      asc = ord(message[i])      
      asc_pad = ord(pad[count])-65      
      de_asc = asc - asc_pad
      if 64 < asc < 91:
        if de_asc < 65:
          de_asc = de_asc + 26
      else: 
        if de_asc < 97:
          de_asc = de_asc + 26        
      decipher += chr(de_asc)
      count += 1
    else:
      decipher += message[i]

  return decipher

#encipher a code
def encipher(message,pad):
  pass
  encipher = ""
  count = 0
  en_asc=0

  for i in range (len(message)):
    if message[i].isalpha()== True:
      asc = ord(message[i])      
      asc_pad = ord(pad[count])-65
      en_asc = asc + asc_pad
      if 64 < asc < 91:
        if en_asc > 90:
          en_asc = en_asc - 26
      else: 
        if en_asc > 122:
          en_asc = en_asc - 26
      encipher += chr(en_asc)
      count += 1
    else:
      encipher += message[i]

  return encipher

# Shift all characters in a message by the designated amount, regardless of case
def shiftMessage(message,shift):
    return "".join([shiftLetter(c,shift) for c in message])
