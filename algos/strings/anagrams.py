def find_anagrams(string):
    words = string.split(' ')
    anagrams = {}
    for word in words:
        chars = sorted(word)
        key = tuple(chars)

        if key not in anagrams:
            anagrams[key] = set()
        anagrams[key].add(word)

    return [an for an in anagrams.values() if len(an) > 1]


def main():
    string = '''below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat while cried during the night caused by pain in its bowel'''

    for group in find_anagrams(string):
        print(group)


main()
