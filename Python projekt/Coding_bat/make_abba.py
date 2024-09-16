ns = input("Input 2 words: ")
words = ns.split()
if len(words) > 1:
    words[1] = words[1]
modified_ns = words[0] + words[1]
reversed_ns = words[1] + words[0]
print(modified_ns.replace(",", "").replace(" ", "") + reversed_ns.replace(",", "").replace(" ",""))