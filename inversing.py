list_=[8, 6, 2, 5, 9]

for index in range(round(len(list_)/2)):
    temp=list_[index]
    list_[index] = list_[len(list_) - 1 - index]
    list_[len(list_) - 1 - index]=temp

print(list_)
