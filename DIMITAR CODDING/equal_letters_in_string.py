string_a = "python"

string_b = "honbe"

same = []

a_len = len(string_a)
b_len = len(string_b)

for a in string_a:
    for b in string_b:

        if a == b:
            same.append(b)

print (same)
