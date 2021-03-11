# O(n) time and space
def remove_comments(code):
    # lines = code.split('\n')
    block_comment_started = False
    clean_code = []
    for row in code:
        string = ''
        for i in range(0, len(row)):
            if not block_comment_started and i < len(row) - 1 \
                    and row[i: i + 2] == '//':
                break

            if i < len(row) - 1 and row[i: i + 2] == '/*':
                block_comment_started = True

            if row[i - 2:i] == '*/':
                block_comment_started = False

            if not block_comment_started:
                string += row[i]

        if row[-2:] == '*/':
            block_comment_started = False

        if string == '':
            continue
        clean_code.append(string + '\n')
    return ''.join(clean_code)


def main():
    source = ["/* Example code for feature */",
              "int main() {",
              "  /*",
              "  This is a",
              "  block comment",
              "  */",
              "  int value = 10;  // This is an inline comment",
              "  int sum = value + /* this is // also a block */ value;",
              "  return 0;",
              "}"]
    print(remove_comments(source))


main()
