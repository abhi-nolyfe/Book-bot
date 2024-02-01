def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = words_count(text)
    letters_dict = letters_count(text)
    report = generate_report(book_path, num_words, letters_dict)
    print(text)
    print(num_words)
    print(letters_dict)
    print(report)

def generate_report(path, num_words, letters_dict):
  sorted_letters = sorted(letters_dict.items(), key=lambda x: x[1], reverse = True)
  result = ""
  for tuple in sorted_letters:
      if tuple[0].isalpha():
          result += (f"The '{tuple[0]}' character was found {tuple[1]} times\n")
  return (f"--- Begin report of {path} ---\n"
          f"{num_words} words found in the document\n\n"
          f"{result}"
          "--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def words_count(text):
    return len(text.split())

def letters_count(text):
    result = {}
    for letter in text.lower():
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result


main()