print ("This is the Collatz Conjecture, or the HailStone Sequence")
print ("For numbers that are even, the rule is to divide that number by two.")
print ("For numbers that are odd, the rule is to multiply that number by three and add one.")
print ("Your objective, find a number for which the final number is not 1.")
origNum = abs(int(input("Enter a number: ")))
tempNum = origNum
stepCnt = 0
up = True
maxNum = 0

while tempNum != 1:
    if up:
        print ("Number Increasing \t")
    else:
        print ("Number Decreasing", '\t')
    if tempNum % 2 == 0:
        print (tempNum, "/ 2 =")
        tempNum /= 2
        print (tempNum)
        stepCnt += 1
        up = False
    else:
        print ("3 *", tempNum, "+ 1 =")
        tempNum = tempNum * 3 + 1
        print (tempNum)
        if maxNum < tempNum:
            maxNum = tempNum
        stepCnt += 1
        up = True

width = 40
origStr =  str(origNum)
orgLen = width - len(origStr)
resStr = "Results"
orgStr = "Original String:"
print ('\n', resStr.center(width, '='), '\n')
print ('{:<30}{}\n'.format("Original Number:",origNum))
print ('{:<30}{}\n'.format("Final Number:", tempNum))
print ('{:<30}{}\n'.format("Maximum Number:", maxNum))
print ('{:<30}{}\n'.format("Number of Steps to Complete:", stepCnt))
print ("="*width, '\n')
