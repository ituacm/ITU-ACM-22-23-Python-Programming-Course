map_from = "abcd"
map_to = "1234"
code = "adc"
key_code = {}
new_code = ""
for i in range(len(map_from)):
    key_code[map_from[i]] = map_to[i]

for j in code:
    new_code = new_code + key_code[j]
