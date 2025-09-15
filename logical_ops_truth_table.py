value = [True, False]
print("A\t B\tA and B\tA or B\tnot A\tnot B")
for a in value:
    for b in value:
        print(f"{a}\t{b}\t{a and b}\t{a or b}\t{not a}\t{not b}")