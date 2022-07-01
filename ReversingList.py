# Take the size of the list from the user
size = int(input("Enter size of list\n"))
print("Enter the numbers of the list one by one\n")

# Initialize a blank list
mylist = []

# Take the input from the user one by one
for i in range(size):
    mylist.append(int(input("Enter list element\n")))

# mylist = [7,3,2, 34, 1,0]
print(f"Your list is {mylist}\n")

# 1st METHOD(Build-in module)
reverse1 = mylist[:]
reverse1.reverse()
print(f"My First reversed list of {mylist} is {reverse1}")

# 2nd METHOD(String Slicing)
reverse2 = mylist[::-1]
print(f"My Second reversed list of {mylist} is {reverse2}")


# 3rd METHOD(Swapping list item)
reverse3 = mylist[:]
for i in range(len(reverse3) // 2): #---->(Here we will go till n/2 length as list is reverse when iteraction is reach till n/2, any further we will get same list in straight order)
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]


print(f"My Third reversed list of {mylist} is {reverse3}")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")
