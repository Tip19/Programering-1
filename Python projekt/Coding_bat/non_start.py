ns = input("Input 2 words: ")
words = ns.split()
if len(words) > 1:
    words[1] = words[1][1:]
modified_ns = words[0] + words[1]
print(modified_ns.replace[1:](",", "").replace(" ", ""))
