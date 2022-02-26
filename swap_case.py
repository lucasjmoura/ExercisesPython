def swap_case(s):
    for index,char in enumerate(s):
        if char.isupper():
            s = s[:index] + s[index:].replace(char, char.lower())
        else:
            s =s[:index] + s[index:].replace(char, char.upper())
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
