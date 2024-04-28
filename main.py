def main():
    book_path = "books/frankenstein.txt"
    text=get_book_text(book_path)
    number_of_words=get_word_count(text)
    number_of_characters=get_number_of_each_character(text)
    print(text)
    print(number_of_words)
    print(number_of_characters)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words=text.split()
    return len(words)

def get_number_of_each_character(text):
        num_characters={}
        lower_text=text.lower()
        for characters in lower_text:
            if characters not in num_characters.keys():
                  num_characters[characters]=1
            else:
                num_characters[characters]+=1
        return num_characters
main()
