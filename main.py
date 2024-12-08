# def getLetterMap(words,letter_map):
#     for word in words:
#        lower_case_word = word.lower()
#        if lower_case_word.isalpha():    
#           for letter in lower_case_word:
#              if letter in letter_map:
#                 letter_map[letter] = letter_map[letter] +1
#              else:
#                 letter_map[letter] = 1
#     print(letter_map)
#     return letter_map

def getLetterMap(words,letter_map):
    for word in words:
       lower_case_word = word.lower()
       for letter in lower_case_word:
        if letter.isalpha():
          if letter in letter_map:
            letter_map[letter] = letter_map[letter] +1
          else:
            letter_map[letter] = 1
    print(letter_map)
    return letter_map


def sort_on(dict):
   return dict["value"]

def sortLetterMap(letter_map):
   letter_map_array = []
   for item in letter_map.keys():
      obj = {"char":item,"value":letter_map[item]}
      letter_map_array.append(obj)
   letter_map_array.sort(reverse=True,key=sort_on)
   return letter_map_array
      

def printReport(letter_map_array,wordCount):
    print("--- Begin report of books/frankenstein.txt ---")
    print('{} words found in the document'.format(wordCount))
    print("\n")
    for item in letter_map_array:
       print('The {} character was found {} times'.format(item["char"],item["value"]))
    print("--- End report ---")


with open("books/frankenstein.txt") as f:
    letter_map = {}
    file_contents = f.read()
    words = file_contents.split()
    letter_map = getLetterMap(words,letter_map)    
    letter_map_array = sortLetterMap(letter_map)
    printReport(letter_map_array,len(words))


