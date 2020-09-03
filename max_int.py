# Given a positive integer from the user until the input becomes a negative integral
# First you need to ask the user for a positive integer
# To be able to put all numbers together to a list you need to make an emtpy list
# Next, make a while loop that asks user for a number while the input is not negative
# Every positive integer that the user chooses needs to be added to the list
# to find the maximum number in the list we can use the "max" command that will find the larges number




num_int = int(input("Input a number: "))    # Do not change this line

listi = []

while num_int >= 0:
    listi.append(num_int)     
    num_int = int(input("Input a number: "))
max_int=max(listi)
print("The maximum is", max_int)

