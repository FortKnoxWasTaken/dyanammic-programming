# without memoization
def gridtraveller(m, n):
    if m==0 or n==0:
        return 0
    elif m==1 and n==1:
        return 1
    return gridtraveller(m-1,n)+gridtraveller(m,n-1)


# with memoization
def gridtraveller_on_drugs(m,n, memo={}):
    if (m, n) in memo:
        return memo[(m,n)]
    
    if m==0 or n==0:
        return 0
    elif m==1 and n==1:
        return 1

    memo[(m, n)]= gridtraveller_on_drugs(m-1, n, memo)+gridtraveller_on_drugs(m, n-1, memo)
    return memo[(m, n)]

print(gridtraveller_on_drugs(18,18))
