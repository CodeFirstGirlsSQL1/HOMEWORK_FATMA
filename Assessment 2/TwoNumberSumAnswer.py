"""

9.	TWO NUMBER SUM:

●	Write a function that takes in a non-empty array of
distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum,
the function should return them in an array, in any order.
If no to numbers sum up to the target sum, the function should
return an empty array.

●	Note that the target sum has to be obtained by summing
two different integers in the array. You cannot add a single
integer to itself in order to obtain the target sum.

●	You can assume that there will be at most one pair of numbers
summing up to the target sum.

"""

def two_number_sum(arr, sum):
    num1 = 0
    ans = []
    for i in range(0, len(arr)):
        num1 = arr[i]
        for j in range(i+1, len(arr)):
            if num1 + arr[j] == sum:
                ans.append(num1)
                ans.append(arr[j])
                return ans
    return ans

list_of_numbers = [3, 5, -4 ,8, 11, 1, -1, 6]
target_sum = 10

print(two_number_sum(list_of_numbers, target_sum)) # will print [11, -1]
