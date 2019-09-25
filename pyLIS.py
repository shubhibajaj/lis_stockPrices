# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:54:31 2019

@author: HP
"""

def longest_increasing_subsequence(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len)
                  + [d[i]])
    
    return max(l, key=len)
 
if __name__ == '__main__':
    for d in [[1200.4,1100,1010.5,1400.6,1111,1234,1456.56,1543,1056.7,1300,1100,1200,1234,1235,1345,1349,1379,1389.89,1390,1238,1308,1307,1401,1450,1146,1420,1290,1100,1169.9,1467.7 ]]:
        print('a L.I.S. of %s is \n%s' % (d, longest_increasing_subsequence(d)))