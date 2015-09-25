# Check if the number is a prime number

Int = 5
IsPrime = True


if Int != 0:
    for x in range(2, Int / 2):
        if Int%x == 0:
            IsPrime = False
            break
                            
    if IsPrime:
        print "Its a prime number"
    else:
        print "Its not a prime number"

else:
    print "0 is an invalid number! Please try again with a different number."
