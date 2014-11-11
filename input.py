#!/usr/bin/python
x = int(raw_input("Please enter an integer: "))
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
     print 'Zero'
elif x == 1:
     print 'Single'
else:
     print 'More'
#FOR LOOP
words = ['cat', 'window', 'defenestrate']
for w in words:
   print w, len(w)

# SEQUENCE
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]

#table
for n in range(2, 10):
  for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
else:
        # loop fell through without finding a factor
        print n, 'is a prime number'

for letter in 'Python': 
   if letter == 'h':
     # pass
     print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"
