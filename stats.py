def count_words(text):    
    return len(text.split())

def count_characters(text):
    words = text.lower().split()
    characters_dictionary = {}
    for word in words:
        for char in word:
            if char not in characters_dictionary:
                characters_dictionary[char] = 1
            else:
                characters_dictionary[char] += 1
    
    return characters_dictionary

def sort_dictionary(dictionary):
    list_of_dictionaries = []   
    for entry in dictionary:
        if entry.isalpha():       
            character = {
                "name": entry,
                "count": dictionary[entry]
            }
            list_of_dictionaries.append(character)

    def sort_on(items):
        return items["count"]
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    
    return list_of_dictionaries

