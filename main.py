from stats import get_word_count, get_char_count, sort_on

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()

  return file_contents

def main():
  frankenstein_text = get_book_text("books/frankenstein.txt")
  num_words = get_word_count(frankenstein_text)
  character_counts = get_char_count(frankenstein_text)
  character_counts.sort(key=sort_on, reverse=True)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt")
  print ("----------- Word Count ----------")
  print(f"Found {num_words} total words.")
  print("-------- Character Count --------")
  for counts in character_counts:
    print(f"{counts['char']}: {counts['num']}")

main()