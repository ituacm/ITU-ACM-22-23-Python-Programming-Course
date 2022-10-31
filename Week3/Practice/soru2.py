liste = [3,9,5,3,3,5]
new_list = list(set(liste))
final_list = []
for i in new_list:
    count = 0
    for j in liste:
        if i == j:
            count += 1
    if count % 2 == 1:
        final_list.append(i)

final_list.sort()
print(final_list[-1])