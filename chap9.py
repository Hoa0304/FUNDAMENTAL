def long_words(filename):
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > 20:
                    print(word)

filename = 'words.txt'

long_words(filename)

def has_no_e(word):
    return 'e' not in word

def no_e_words(filename):
    total_words = 0
    no_e_count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                total_words += 1
                if has_no_e(word):
                    no_e_count += 1
                    print(word)
    percentage = (no_e_count / total_words) * 100
    print(f"Percentage of words without 'e': {percentage}%")

no_e_words(filename)

def avoids(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True

def count_avoids(filename, forbidden_letters):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if avoids(word, forbidden_letters):
                    count += 1
    print(f"Number of words that don’t contain any of the forbidden letters: {count}")

forbidden_letters = input("Enter forbidden letters: ")
count_avoids(filename, forbidden_letters)

def uses_only(word, allowed_letters):
    for letter in word:
        if letter not in allowed_letters:
            return False
    return True

allowed_letters = "acefhlo"
sentence = "Hoe alfalfa"
if uses_only(sentence, allowed_letters):
    print("The sentence uses only allowed letters.")
else:
    print("The sentence contains other letters.")

def uses_all(word, required_letters):
    return all(letter in word for letter in required_letters)

def count_uses_all(filename, required_letters):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if uses_all(word, required_letters):
                    count += 1
    print(f"Number of words that use all '{required_letters}': {count}")

required_letters = "aeiou"
count_uses_all(filename, required_letters)

def is_abecedarian(word):
    return list(word) == sorted(word)

def count_abecedarian_words(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if is_abecedarian(word):
                    count += 1
    print(f"Number of abecedarian words: {count}")

count_abecedarian_words(filename)
