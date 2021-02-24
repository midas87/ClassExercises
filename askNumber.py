
count = []


while True:
    numb = input('Enter a number: ')
    if numb.isnumeric():
        addNumb = count.append(numb)
    if numb == 'done':
        print('it got here')
        break
    try:
        if numb is numb.isalpha():
            print('exception')
    except:
        print('Invalid input, Please Enter a numbers/Digit')
    for n in count:
        print(n)
    print('length of n is:',len(count))


    #print(toTal)