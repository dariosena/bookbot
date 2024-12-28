
def count_characters(content):
    characters_count = {}

    for original_character in content:
        character = original_character.lower()

        if not character.isalpha():
            continue

        if character in characters_count:
            characters_count[character] += 1
        else:
            characters_count[character] = 1

    return characters_count


def count_all_words(content):
    count = 0
    for word in content.split():
        count += 1

    return count


def main():
    book = 'books/frankenstein.txt'

    with open(book) as f:
        contents = f.read()
        words_count = count_all_words(contents)

        print(f'--- Begin report of {book} ---')
        print(f'{words_count} words found in the document')
        print()
        
        characters_count = count_characters(contents)

        def sort_on(characters):
            return characters['count']


        characters = []

        for character, count in characters_count.items():
            characters.append({ 'character': character, 'count': count })
        
        characters.sort(reverse=True, key=sort_on)

        for character_dict in characters:
            character = character_dict['character']
            character_count = character_dict['count']

            print(f"The '{character}' was found {character_count} times")

        print('--- End report ---')


if __name__ == '__main__':
    main()

