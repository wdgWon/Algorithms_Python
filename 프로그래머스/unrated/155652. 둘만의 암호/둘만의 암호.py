def solution(s, skip, index):
    alphabet = [chr(x) for x in range(97,123)]
    result = ''

    for al in skip:
        alphabet.remove(al)

    for al in s:
        i = (alphabet.index(al) + index) % len(alphabet)
        result += alphabet[i]

    return result