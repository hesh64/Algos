cheater = "quiqutit"
student = "quit"


def match(cheater, student):
    letters = {}
    j = 0

    for end in range(len(cheater)):
        char = cheater[end]
        if j < len(student) and student[j] == char:
            letters[char] = end
            j += 1

        if char in letters:
            print(char, end, letters[char])
            letters[char] = max(end, letters[char])
            print('outcome', letters[char])

    minidx, maxidx = min(letters.values()), max(letters.values())
    return cheater[minidx: maxidx + 1]


def find_window(cheater, student):
    i, j = 0, 0
    mini = len(cheater) + 1
    window = ''
    while i < len(cheater):
        if cheater[i] == student[j]:
            j += 1
            if j == len(student):
                end = i + 1
                j -= 1
                while j >= 0:
                    if cheater[i] == student[j]:
                        j -= 1
                    i -= 1
                j += 1
                i += 1
                if (end - i) < mini:
                    mini = end - i
                    window = cheater[i: end]
        i += 1
    return window


print(match(cheater, student))
print(find_window(cheater, student))
