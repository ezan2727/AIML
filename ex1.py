#write sa function to check a number is odd or even
def check_odd_even(number):
    if(number%2==0):
        print('{number} is even')
    else:
        print('{number} is odd')

given_number=int(input('enter number'))
check_odd_even(given_number)