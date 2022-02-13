#without memoization
def fib(n):
    if n<=2: return 1
    return fib(n-1)+fib(n-2)


#with memoization
def fib_on_drugs(n, memo={}):
    if n in memo: return memo[n]
    if n<=2: return 1

    memo[n] = fib_on_drugs(n-1, memo) + fib_on_drugs(n-2, memo)
    return memo[n]

print(fib_on_drugs(50))