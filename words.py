import re

def spin_words(sentence):

    revers_sentence = []
    delimiter = " "

    words = sentence.split()

    for word in words:
        letters = re.findall(r'[a-zA-Z]', word)

        if len(letters) >= 5:
            reversed_word = word[::-1]
            revers_sentence.append(reversed_word)
        else:
            revers_sentence.append(word)

    result = delimiter.join(revers_sentence)
    return result


print(spin_words("Hey fellow warriors"))