try:
    apples = int(input("ENTER THE NUMBER OF APPLES\n"))
    mn = int(input("ENTER LOWER BOUND\n"))
    mx = int(input("ENTER UPPER BOUND\n"))

except ValueError:
    print("Enter Interger Value Only!!")
    exit()

if mx > mn:
    for i in range(mn, mx+1):
         if apples%i ==0:
            print(f"{i} is divisor of {apples}\n")
         else:
             print(f"{i} is not a divisor of {apples}\n")

elif mx == mn:
    print("Ranges are same!!")

else:
    print("Lower Bound Value should not exceeded Upper Bound Value!!")





