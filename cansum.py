# without memoization
def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum<0:
        return False

    for i in numbers:
        if canSum(targetSum-i, numbers):
            return True

    return False

#with memoization
def canSum_on_drugs(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum<0:
        return False
    if targetSum == 0:
        return True

    for i in numbers:
        remainder = targetSum-i
        if canSum_on_drugs(remainder, numbers, memo) == True:
            memo[targetSum] = True 
            return True

    memo[targetSum] = False
    return False


# print(canSum_on_drugs(7, [2, 3]))
# print(canSum_on_drugs(7, [5, 3, 4, 7]))
print(canSum_on_drugs(7, [2, 4]))
# print(canSum_on_drugs(8, [2, 3, 5]))
# print(canSum_on_drugs(300, [7, 14]))