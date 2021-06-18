from collections import namedtuple, deque

Word = namedtuple('Word', ('word', 'size'))


def fullJustify(words, maxWidth: int):
    def fomat_line(words, size, last=False):
        if last:
            t = ' '.join([s.word for s in words])

            words = [Word(t, len(t))]
        if len(words) == 1:
            return words[0].word.ljust(maxWidth, ' ')

        total_chars = sum([w.size for w in words])
        space_chars = maxWidth - total_chars
        breaks = [0] * (len(words) - 1)
        i = 0

        while space_chars > 0:
            breaks[i] += 1
            space_chars -= 1
            i += 1
            if i == len(breaks):
                i = 0
        breaks.reverse()

        line = ''
        for i, word in enumerate(words):
            line += word.word
            if breaks:
                line += (' ' * breaks.pop())
        return line.rjust(maxWidth, ' ')

    que = deque()
    for w in words:
        que.append(Word(w, len(w)))

    lines = []
    while que:
        total_size = maxWidth
        temp = []
        while que and total_size <= maxWidth:
            if que[0].size <= total_size:
                temp.append(que.popleft())
                total_size -= (temp[-1].size + 1)
            else:
                break
        line = fomat_line(temp, maxWidth, len(que) == 0)
        lines.append(line)

    return lines


input = [
    ["This", "is", "an", "example", "of", "text", "justification."],
    16,
    ["What", "must", "be", "acknowledgment", "shall", "be"],
    16,
    ["Science", "is", "what", "we", "understand", "we", "understand", "we", "understand", "we", "understand", "we",
     "understand", "we", "understand", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
     "Art", "is", "everything", "else", "we", "do"],
    20,
]

while input:
    a, b = input.pop(0), input.pop(0)
    print(fullJustify(a, b))
