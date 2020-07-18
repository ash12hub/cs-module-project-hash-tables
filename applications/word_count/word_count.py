def word_count(s):
    # Your code here
    split_characters = ['"', ':', ';', ',', '.', '-',
    '+', '=', '/', '\\', '\r', '\t', '\n', '|', '[', ']', '{', '}', '(',
    ')', '*', '^', '&', ' ']
    words = {}
    word_start = 0

    for i in range(len(s)):
        if s[i] in split_characters:
            word = s[word_start:i].lower()
            word_start = i + 1
            if len(word) > 0 and word not in split_characters:
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1
        elif i == len(s) - 1:
            word = s[word_start:].lower()
            if len(word) > 0 and word not in split_characters:
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))