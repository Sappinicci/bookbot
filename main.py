import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]
print(f"The file path you provided is: {book_path}")

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

	words = text.split()
	return len(words)

from stats import get_num_words
from stats import count_characters
from stats import sort_character_count

def main():
	print("========== BOOKBOT ==========")
	print("Analyzing book found at books/frankenstein.txt...")
	print("---------- Word Count ----------")
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	print(f"Found {num_words} total words")
	print("---------- Character Count ----------")
	dict_results = count_characters(text)
	#print(dict_results)
	character_counts = count_characters(text)
	sorted_chars = sort_character_count(character_counts)

	for item in sorted_chars:
		print (f"{item['char']}: {item['num']}")



main()

