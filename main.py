def main():
    book_path = "books/frankenstein.txt"
    text=get_book_text(book_path)
    number_of_words=get_word_count(text)
    number_of_characters=get_number_of_each_character(text)
    report(number_of_words,number_of_characters,book_path)
   
    
    
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

def report(number_words,number_char,book_path):
        
        print("--Begin report of "+ book_path+ " --")
        print(str(number_words)+" words found in the document")
        letters=[]
        
        for value in number_char:
            if (value.isalpha()):
                letters.append({"name":value, "num":number_char[value]})
        def sort_on(letters):
             return letters['num']
        letters.sort(reverse=True, key=sort_on)
        for letter in letters:
             print("The "+str(letter['name'])+" character was found "+str(letter['num'])+" times")
        print('--End report--')
main()
