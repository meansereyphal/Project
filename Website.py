print("Welcome to Pig Latin translator")
pyg = "ay"
word = input('Enter your word')

if len(word) > 0 and word.isalpha():
  
  new_word = word.lower()
  first = word[0]
  pyg_word = new_word + first + pyg
  pyg_word = pyg_word[1:len(pyg_word)]
  print (pyg_word)
else:
  print('empty')
