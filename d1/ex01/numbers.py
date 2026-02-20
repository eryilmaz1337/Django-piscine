def numbers():
    with open('numbers.txt', 'r') as dosya:
        text = dosya.read()
    i = 0
    str = ""
    while i < len(text):
        while i < len(text) and text[i] != ',':
            str += text[i]
            i += 1
        print(str)
        str = ""
        i += 1

if __name__ == '__main__':
    numbers()