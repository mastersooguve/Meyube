def count_words(text_input):
    words = text_input.split()           # splits the input at white spaces, 
                                         # also remove excess white spaces
    return len(words)                    # returns count of words

if __name__ == "__main__":
    text  = input("Enter Text here: ")   # getting user inputs
    out = count_words(text)
    print(f"{out} words found")          # printing the output