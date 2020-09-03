# Given an lenght of the sequence from the user
# The sequence constis of the last 3 previous numbers added togeather to genereate
# The next number in the sequence
# First number = 1
# 2nd number = 2
# 3rd number = 3
# 4th number = 3 + 2 + 1 
# 5th number = 6 + 3 + 2 = 11
# for all n >= 3 the algorithm calculated the sum of the last 3 numbers in the sequence

n = int(input("Enter the length of the sequence: ")) 

listi= []
number = 0
for i in range(1,n+1):
    if i <= 3:
        listi.append(i)
        print(i)
    elif i > 3:
        number = listi[-1] + listi[-2] + listi[-3]
        listi.append(number)
        print(number)


        # If i >= 3 then calculate the sum for last 3 numbers
    # If i <= 3 then print i and do nothing
