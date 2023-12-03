from random import choice

userInput = input("\x1b[34mWelcome to TrollText! Enter the Text:\n")

characters = ["!","@","#","$","%","^","&","*","(",")","-","=","1","2","3","4","5","6","7","8","9","0","[","]",";","'",".","/"]
characters_to_replace = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()!@#$%^&*{}:<>,123456789'
colors = ["\x1b[31m", "\x1b[32m", "\x1b[33m", "\x1b[34m", "\x1b[35m", "\x1b[36m"]

trolltext = userInput

for character in characters_to_replace:
  trolltext = trolltext.replace(character, f"{choice(colors)} {choice(characters)}")

print(f"\x1b[33m{trolltext}\x1b[0m")
