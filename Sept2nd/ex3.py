numsList = [1, 4, 17, 25, 3, 100]
maxNumsList = []

numsList.sort(reverse=True)
print("Original array sorted in descendent order:")
print(numsList)
for i in range(3):
    maxNumsList.append(numsList[i])

print("3 maximum numbers:")
print(maxNumsList)