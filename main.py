from stats import get_word_count, get_char_count, sort_on
import sys

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()

  return file_contents

def main():
  print(sys.argv)
  if len(sys.argv) != 2:
    print("Usage: python3 main.py path_to_file")
    sys.exit(1)
  path_to_file = sys.argv[1]
  book_text = get_book_text(path_to_file)
  num_words = get_word_count(book_text)
  character_counts = get_char_count(book_text)
  character_counts.sort(key=sort_on, reverse=True)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path_to_file}")
  print ("----------- Word Count ----------")
  print(f"Found {num_words} total words.")
  print("-------- Character Count --------")
  for counts in character_counts:
    print(f"{counts['char']}: {counts['num']}")

main()