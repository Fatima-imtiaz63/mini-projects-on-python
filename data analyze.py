def analyze_text():
    text = input("Enter a sentence: ")
    lenght = len(text)
    print("length of the text:", lenght)
    print(text.upper())
    print(text.lower())
    first_char = text[0]
    last_char = [-1]
    print(first_char)
    print(last_char)
    analyze_text()

# story creation
def make_story():
    name = input("Enter your name: ")
    place = input("Enter a place: ")
    thing = input ("Enter your thing: ")
    feeling = input("Enter your feeling: ")
    print() 
    print("Story")
    print(name + " went to " + place + "and saw a" + thing + " .")
    print("it made" + name + " feel" + feeling + ".")
    make_story()

#word formatter
def word_format():
    word = input("Enter a word: ")
    print("word in title case:", word.capitalize())
    print("word reversed:" , word[-1])
    word_format()
