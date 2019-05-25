# -*- coding: utf-8 -*-
# 1 Write Python code that prints Hello World!. 
print "Hello world"

# 2 Write Python code to print out the number of items in a list, B.
B = [ 'a', 1 , 2.3, 'c', 7 ]
print len(B)

# 3 Write Python code to construct a list, L, with the following components in order: a string:
#’Hello’, a real number: 0.345, two integer numbers: 111333 and 44.
L = ['Hello',0.345,111333,44]

# 4 Given some list, A:
#(a) Write Python code to make L2 a list containing only the first to the 3rd element of A.
L2 =['A','A','A',1,2,3]
#(b) Write Python code to make L3 a list containing only the last 3 elements of A.
L3 =[1,2,3,'A','A','A']

# 5 A list, L, contains the following components in order: 'hello',23.45, 45, 'Brown', and
#[756.45, 34.5]. Write Python code to:

#(a) Modify L by adding 111 to the integer number component of the list (that is, the 45).
L=['hello',23.45, 45, 'Brown', [756.45, 34.5]]
for x in range(len(L)):
    if isinstance(L[x],int):
        L[x]+=111
        
#(b) Modify L by inserting the elements 'new' and 21.5 between the 'Hello' and the 23.45
#of L.
L[1:1] = ['new',21.5]
print L

#(c) Modify L by inserting the list ['old', 33] before the element 'Brown'. Note, this is not
#inserting two elements but inserting one element which is a list
L[3:3] = ['old',33]
print L

# 6 List the ways a string such as ’Hello’ can be represented.
AA = 'Hello'
print AA

# 7 Write Python code to:

#(a) Make a new string S with the concatenation of the two strings ’Tony’ and ’Vignaux’.
Str = 'Tony' + 'Vignaux'

#(b) Do the same as in part (a) but including a space between the two words of the string.
Str = 'Tony' +' '+ 'Vignaux'

#(c) Print out the first letter and the last letter of the new string.
print Str[0] + Str[-1]

# 8 L is a a string which may have unwanted spaces at both ends. Write Python code to return
# a string, M, without those spaces.

L = ' banana '
L = L.strip()

# 9 Write Python code to print out a string, S, without the automatic newline after it.

Str = '123'
print Str,
