# main function opens text file
# reads content into string
# uses word count function to count number of words
# uses character count function to count characters
# prints results to output in report form by creating a list of dictionaries
# and using ".isalpha()" and "lambda" functions to sort method alpha characters in reverse order of frequency

def main():
    with open("/home/zjamirian/workspace/github.com/ZarehAm/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print("-- Begin report of books/frankenstein.txt --")
    print(f"{word_count(file_contents)} words found in document\n")

    character_dict = character_count(file_contents)
    character_list = [{"letter": letter, "freq": freq} for letter, freq in character_dict.items() if letter.isalpha()]
    character_list.sort(key=lambda dict: dict["freq"], reverse=True)

    for character in character_list:
        print(f"The '{character["letter"]}' character was found {character["freq"]} times")
    print("-- End report --")

# word count function
# initializes words string and splits file_contents
# returns length of words string

def word_count(file_contents):
    words = file_contents.split()        
    return len(words)

# individual character count function (not case sensitive)
# function initializes a character dictionary
# initializes a characters string that makes all characters lower case
# loops for each character in the characters string whereby
# if the character key in the character dictionary is present, its value is increased by one
# else it sets the character as the key with a value of 1

def character_count(file_contents):
    character_dict = {}
    characters = file_contents.lower()
    for character in characters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict


main()
