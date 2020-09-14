def check(s1, s2):
    # the sorted strings are checked
    if sorted(s1) == sorted(s2):
        return True
    return False


words = []
with open('../files/anagrams.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        words.append(line.replace('\n', ''))
size = len(words)
for i in range(size):
    if '' == words[i]:
        continue
    for j in range(i + 1, size):
        if '' == words[j]:
            continue
        if check(words[i], words[j]):
            print(words[j], end=' ')
            words[j] = ''
    print(words[i])
