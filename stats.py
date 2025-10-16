def get_word_count(text):
  words = text.split()
  return len(words)

def get_char_count(text):
  chars = {}
  words = text.split()
  for word in words:
    for i in range(0, len(word)):
      char = word[i].lower()
      if char not in chars:
        chars[char] = 0
      chars[char] += 1
  return chars