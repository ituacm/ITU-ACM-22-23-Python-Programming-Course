s = input("Kelime gir:")
new_s = ""
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        new_s = new_s + letter
print(new_s)