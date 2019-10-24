from Lab1 import static
alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z', ' ', '.', ',', ';', '-', "'"]
table = []
key = 'VOLODYMYR PANKIV'
f = open('Lab3.txt', 'r')
text = f.read()
key_str = ''
dtext = ''
for i in range(0, len(alf)):
    k = alf[:i]
    c = alf[i:]
    table.append(c + k)
print(*table, sep="\n")

count = len(text) // len(key)
for i in range(0, count):
    key_str += key
key_str += key[:len(text) % len(key)]

for i in range(0, len(text)):
    if text[i] != '\n':
        dtext += table[alf.index(text[i])][alf.index(key_str[i])]
    else:
        dtext += '\n'
print(dtext, "\n")
print(text)
static(dtext)
