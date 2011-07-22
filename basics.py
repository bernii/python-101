'''
Created on 11-06-2011

@author: berni
'''
# 5 standard python modules
import urlparse
print urlparse.urljoin("http://www.wp.pl", ".")
import string, re, StringIO, datetime, random

# 5 not standard
# BeautifulSoup, selenium, mysql, crypto, django, gd, scapy

# simple one
d = {1:2, 4:54, 3:22}
for k in d:
    print k
    
# immutables (string, tuple)
def im(a):
    a += 'e'
    return a
a = "abcd"
print im(a)
print a

# f(123456789) -> 123,456,789 mathematical way
def ff(number):
    out = []
    rest = number % 1000
    number = number / 1000
    out.append(str(rest))
    while number > 1000:
        rest = number % 1000
        number = number / 1000
        out.append(str(rest))
    out.append(str(number))
    out.reverse()
    return ",".join(out)
print ff(123456789)

# f(123456789) -> 123,456,789 string way
def ff2(number):
    strn = str(number)
    out = []
    i = len(strn)
    while i>3:
        out.append(strn[i-3:i])
        i -= 3
    out.append(strn[0:i])
    out.reverse()
    return out
print "String ", ",".join(ff2(123456789))

# Create a list by getting rid of elements matching criteria
a= [1,2,4,2,5,6,7,2,3,4,5,2,4,2,3,6]
print [x for x in a if x != 2]

# Get letter and number of repetitions of 
# letter with max repetitions in a string
a = "dskjhewuiyerjfdjkghewirfjkfsdkjgfuyweruygsdfhdfsgfsdjhgweaytewuy"
d = {}
[d.__setitem__(x,1+d.get(x,0)) for x in list(a)] 
print "MAX TOUPLE", max([(d[x],x) for x in d])

# What * and ** mean in function declaration
def f(a, *b, **c): print a,b,c
f(1,2,3) # 1 (2, 3) {}
f(1,2,3,c=4) # 1 (2, 3) {'c': 4}

# Delete list elements matching criteria in-place
# do it form back so index is not broken
a = [2,4,2,5,6,7,2,4,5,3]
for i in range(len(a)-1, -1, -1):
    if a[i] == 2:
        del a[i]
print a # [4, 5, 6, 7, 4, 5, 3]