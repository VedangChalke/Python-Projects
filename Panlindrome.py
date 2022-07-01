
def is_panlindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n = n + 1
    while not is_panlindrome(n):
        n +=1
    return n

if __name__== "__main__":
    n = int(input("Enter the number of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number:\n"))
        numbers.append(number)
        if str(number) == str(number)[::-1]:
            print("INPUT NUMBER IS A PALINDROME")
        else:
            print("INPUT NUMBER IS NOT A PALINDROME")

        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")

