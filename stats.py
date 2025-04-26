def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    text = text.lower()
    character_count = {}
    for character in text:
        if character in character_count:
           character_count[character] += 1
        else: 
            character_count[character] = 1

    return character_count

def sorted_characters(character_count):
    character_list = []
    for key, value in character_count.items():
        character_list.append({"char": key, "count": value})

    character_list.sort(key=lambda item: item["count"], reverse=True)
    return character_list
        