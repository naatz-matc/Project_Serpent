#!/usr/bin/env python3

#result of expression True and True
print (bool(True and True))

#result of expression False and True
print (bool(False and True))

#result of expression 1 == 1 and 2 == 1
print (bool(1 == 1 and 2 == 1))

#result of expression 0
print (bool(0))

#result of expression ""
print (bool(""))

#result of expression 0.0
print (bool(0.0))

#result of expression not 0
print (bool(not 0))

#result of expression "test" == "test"
print (bool("test" == "test"))

#reslut of expression 1 == 1 or 2 != 1
print (bool(1 == 1 or 2 != 1))

#result of expression True and 1 == 1
print (bool(True and 1 == 1))

#result of expression False and 0 != 0
print (bool(False and 0 != 0))

#result of expression True or 1 == 1
print (bool(True or 1 == 1))

#result of expression "test" == "testing"
print (bool("test" == "testing"))

#result of expression 1 != 0 and 2 == 1
print (bool(1 != 0 and 2 ==1))

#result of expression "test" != "testing"
print (bool("test" != "testing"))

#result of expression "test" == 1
print (bool("test" == 1))

#result of expression 1 == 1 and not ("testing" == 1 or 1 == 0)
print (bool(1 == 1 and not ("testing" == 1 or 1 == 0)))

#result of expression "chunky" == "bacon" and not (3 == 4 or 3 ==3)
print (bool("chunky" == "bacon" and not (3 == 4 or 3 == 3)))

#result of expression 3 == 3 and not ("testing" == "testing" or "Python == "Fun")
print (bool(3 == 3 and not ("testing" == "testing" or "Python" == "Fun")))

