def code(input):
    input = input('Geef je naam en bestemming: ')
    data = list(input)
    output = str(''.join(str(ord(c) + 3) for c in data))
    print(output)
    return output

code(input)
