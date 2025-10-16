def get_word_count(text):
  words = text.split()
  return len(words)

def get_char_count(text):
  char_list = []
  words = text.split()
  for word in words:
    for i in range(0, len(word)):
      char = word[i].lower()
      
      found = False
      
      for j in range(0, len(char_list)):
        if char_list[j]['char'] == char:
          char_list[j]['num'] += 1
          found = True
          break
      
      if not(found):
        char_list.append({'char': char, 'num': 1})

  return char_list

def sort_on(items):
  return items["num"]