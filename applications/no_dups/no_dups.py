def no_dups(s):
    # Your code here
    start_split = s.split(' ')
    current_split = []
    for word in start_split:
        if word not in current_split:
            current_split.append(word)

    output = ""
    for i in range(len(current_split)):
        if i == 0:
            output += current_split[i]
        else:
            output += f' {current_split[i]}'
    return output


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))