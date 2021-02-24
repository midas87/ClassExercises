largestNumber = 0

numbers = [9,41,12,3,74,15]

for i in numbers:
    if i > largestNumber:
        largestNumber = i
    print(largestNumber, i)
print('The largest number: ', largestNumber)


smallestNumbers = None

for s in numbers:
    if smallestNumbers is None:
        smallestNumbers = s
    elif s < smallestNumbers:
        smallestNumbers = s
    print(smallestNumbers, s)

print('smallest number is: ',smallestNumbers)
