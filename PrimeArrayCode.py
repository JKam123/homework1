import time
start = time.time()
Array = []
Count = 0

def IsPrime( Int ):
    if Int != 0 and Int != 1:
        for x in range(len(Array)):
            if Int%Array[x] == 0:
                return False
                break
        return True
                                
    else:
        return False



while len(Array) < 100:
    Count = Count + 1
    if IsPrime( Count ):
        Array.append( Count )
        #print Count

print Array
end = time.time()
print "The array has " + str(len( Array )) + " elements"
print "Time needed " + str(end-start)
    

