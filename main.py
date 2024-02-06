# individual character count function (not case sensitive)
# function initializes a character dictionary
# initializes a characters string that makes all characters lower case
# loops for each character in the characters string whereby
    #if the character key in the character dictionary is present
        #its value is increase by one
    #else it sets the character as the key with a value of 1

def character_count(file_contents):
    character_dict = {}
    characters = file_contents.lower()
    for character in characters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

# word count function
# initializes words string and splits file_contents
# returns length of words string

def word_count(file_contents):
    words = file_contents.split()        
    return len(words)       

# main function opens text file
# reads content into string
# uses word count function to count number of words
# uses character count function to count characters
# prints results to output

def main():
    with open("/home/zjamirian/workspace/github.com/ZarehAm/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print(word_count(file_contents))
    print(character_count(file_contents)) 

main()
