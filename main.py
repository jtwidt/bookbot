from stats import get_word_count

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()

  return file_contents

def main():
  frankenstein_text = get_book_text("books/frankenstein.txt")
  num_words = get_word_count(frankenstein_text)
  print(f"Found {num_words} total words.")

main()