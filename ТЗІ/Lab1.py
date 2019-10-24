import matplotlib.pyplot as plt
from itertools import islice

f = open('VT00', 'r')
text = f.read()


def static(text):
    alf = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
           'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, '_': 0, ',': 0,
           "'": 0, '.': 0, ';': 0, '-': 0}
    two = {}
    three = {}
    for i in text.upper():
        if i in alf:
            k = alf.get(i)
            k += 1
            alf[i] = k
        if i == ' ':
            k = alf.get('_')
            k += 1
            alf['_'] = k
    print(alf)
    for i in range(len(text)):
        t = text[i:i + 2].upper()
        c = 0
        for k in range(len(text)):
            if t == text[k:k + 2].upper():
                c += 1
        if ' ' in t:
           t = t.replace(' ', '_')
        two[t] = c
    print(two)
    for i in range(len(text)):
        t = text[i:i + 3].upper()
        c = 0
        for k in range(len(text)):
            if t == text[k:k + 3].upper():
                c += 1
        if ' ' in t:
           t = t.replace(' ', '_')
        three[t] = c
    print(three)
    alfs = dict(sorted(alf.items(), key=lambda x: x[1], reverse=True))
    twos = dict(sorted(two.items(), key=lambda x: x[1], reverse=True))
    threes = dict(sorted(three.items(), key=lambda x: x[1], reverse=True))
    twos = dict(islice(twos.items(), 15))
    threes = dict(islice(threes.items(), 15))
    plt.bar(alf.keys(), alf.values(), color=["red"])
    plt.show()
    plt.bar(alfs.keys(), alfs.values(), color=["red"])
    plt.show()
    plt.bar(twos.keys(), twos.values(), color=["red"])
    plt.show()
    plt.bar(threes.keys(), threes.values(), color=["red"])
    plt.show()

# static(text)
