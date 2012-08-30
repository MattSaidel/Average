#This module computes the average of a set of numbers

a = raw_input("Enter any number of values, separated by spaces: ")
numbers = map(int, a.split())
length = len(numbers)
total = sum(numbers)
average = total / float(length)
print "The mean of the set is %f" % average



