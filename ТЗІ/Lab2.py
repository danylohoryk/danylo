from Lab1 import static
f = open('CC_08', 'r')
text = f.read()
alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z', ' ', '.', ',', ';', '-', "'"]
key = 22
decode = {}
dtext = ""
for i in alf:
    k = alf.index(i) - key
    decode[i] = k
for i in text:
    try:
        if i != '\n':
            dtext += alf[decode.get(i)]
        else:
            dtext += i
    except TypeError:
        continue
print(dtext)

static(dtext)
