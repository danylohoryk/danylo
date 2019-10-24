from Lab1 import static
f = open('SZ_78', 'r')
text = f.read()
alf =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',', ';', '-', "'", '\n']
decode=['F', ',', 'G', 'O', 'I', ';', 'M', 'L', 'N', 'K', 'H', 'R', 'J', 'S', 'B', 'W', 'Y', ' ', 'Z', 'Q', '-', 'A', 'X', "'", 'P', 'C', 'D', 'E', 'V', 'U', 'T', ".", '\n']
dtext = ""
for i in text:
        dtext += decode[alf.index(i)]
static(text)
print(dtext)
