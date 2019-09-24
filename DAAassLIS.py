'''The stock price of 30 days of month is stored in a list.
Write program to find out how the  stock  price  has  increased  with  respect  to  last  increases.
[Longest  increasing subsequence]'''

def longest_increasing_subsequence(X):
    """Returns the Longest Increasing Subsequence in the Given List/Array"""
    N = len(X)
    P = [0] * N
    M = [0] * (N+1) 
    L = 0
    for i in range(N):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (X[M[mid]] < X[i]):
               lo = mid+1
           else:
               hi = mid-1
 
       newL = lo
       P[i] = M[newL-1]                                               
       M[newL] = i
       #print(newL)
       #print(M[L])
       
       if (newL > L):
           L = newL
    S = []
    k = M[L]
    for i in range(L-1, -1, -1):
        S.append(X[k])
        k = P[k]
        print(S)
        print(k+1)
       

    print('\nLength of obtained LIS for 30 days stock prices is :: %d'%(len(S)))
    return S[::-1]
 
if __name__ == '__main__':
    for d in [[1200.4,1100,1010.5,1400.6,1111,1234,1456.56,1543,1056.7,1300,1100,1200,1234,1235,1345,1349,1379,1389.89,1390,1238,1308,1307,1401,1450,1146,1420,1290,1100,1169.9,1467.7 ]]:
        print('\nL.I.S. of %s is ::\n\n%s' % (d, longest_increasing_subsequence(d)))
#1200.4,1100,1010.5,1400.6,1111,1234,1456.56,1543,1056.7,1300,1100,1200,1234,1235,1345,1349,1379,1389.89,1390,1238,1308,1307,1401,1450,1146,1420,1290,1100,1169.9,1467.7            
        

























        