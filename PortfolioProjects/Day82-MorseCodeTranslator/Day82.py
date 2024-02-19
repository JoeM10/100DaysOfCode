def whichWayToTranslate():
  fromOrTo = str(input("\nWould you like to translate 'TO' or 'FROM' Morse Code? : ")).upper()
  while True:
    if fromOrTo == "TO" or fromOrTo == "FROM":
      return fromOrTo
    else:
      fromOrTo = str(input("Please type 'TO' or 'FROM' : ")).upper()

def toMorseCode():
  userInput = str(input("\nWhat would you like to translate to Morse Code?\n")).upper().split(" ")
  
  sentance = []
  for word in userInput:
    characters = []
    for character in word:
      if character in morseCodeDictionary.keys():
        characters.append(morseCodeDictionary[character])
      else:
        characters.append("ERROR")
    charString = " ".join(characters)
    sentance.append(charString)
  sentanceString = "   ".join(sentance)
  print(sentanceString)

def fromMorseCode():
  userInput = str(input("\nWhat would you like to translate from Morse Code?\nSeperate letters with 1 space and words with 2.\n")).upper().split(" ")
  print(userInput)
  word = []
  for code in userInput:
    if code in morseCodeDictionary.values():
      word.append(list(morseCodeDictionary.keys())[list(morseCodeDictionary.values()).index(code)])
    else:
      word.append("ERROR")
  sentanceString = "".join(word)
  print(sentanceString)

def toFrom(fromOrTo):
  if fromOrTo == "TO":
    toMorseCode()

  else:
    fromMorseCode()


morseCodeDictionary = {
  "A" : "._",
  "B" : "_...",
  "C" : "_._.",
  "D" : "_..",
  "E" : ".",
  "F" : ".._.",
  "G" : "__.",
  "H" : "....",
  "I" : "..",
  "J" : ".___",
  "K" : "_._",
  "L" : "._..",
  "M" : "__",
  "N" : "_.",
  "O" : "___",
  "P" : ".__.",
  "Q" : "__._",
  "R" : "._.",
  "S" : "...",
  "T" : "_",
  "U" : ".._",
  "V" : "..._",
  "W" : ".__",
  "X" : "_.._",
  "Y" : "_.__",
  "Z" : "__..",

  "0" : "_____",
  "1" : ".____",
  "2" : "..___",
  "3" : "...__",
  "4" : "...._",
  "5" : ".....",
  "6" : "_....",
  "7" : "__...",
  "8" : "___..",
  "9" : "____.",

  "." : "._._._",
  "," : "__..__",
  "?" : "..__..",
  "'" : ".____.",
  "!" : "_._.__",
  "/" : "_.._.",
  "(" : "_.__.",
  ")" : "_.__._",
  "&" : "._...",
  ":" : "___...",
  ";" : "_._._.",
  "=" : "_..._",
  "+" : "._._.",
  "-" : "_...._",
  "_" : "..__._",
  '"' : "._.._.",
  "$" : "..._.._",
  "@" : ".__._.",
  " " : ""
}

restart = True
while restart:
  toFrom(whichWayToTranslate())

  asking = True
  while asking:
    askToRestart = str(input("\nWould you like to translate again? 'Y' or 'N' : ")).upper()
    if askToRestart == "Y":
      asking = False

    elif askToRestart == "N":
      print("\nGoodbye")
      asking = False
      restart = False

    else:
      print("\nPlease type 'Y' or 'N'\n")