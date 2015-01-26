# Problem:
#
#     Each new term in the Fibonacci sequence is generated by adding the
#     previous two terms. By starting with 1 and 2, the first 10 terms
#     will be:
#
#         1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#     By considering the terms in the Fibonacci sequence whose values do
#     not exceed four million, find the sum of the even-valued terms.
#
def fibTo1M():
    L = [1,2]
    while L[-1] < 4*10**6:
        l = len(L)
        L.append(L[l-2] + L[l-1])
    return(L[0:-1])

def solve():
    T=0
    fs = fibTo1M()

    for i in fs:
        if i % 2 == 0:
            T = T + i
    return T

if __name__ == '__main__':
    print(solve())