print("choose a random number (keep in mind that very high numbers can freeze your computer for hours or days and "
      "NEGATIVE numbers can entirely break your computer if you are not careful)")  # Lies, python has safety

questionLoop = True
calculateLoop = True
numLoopGuess = 0


def OddEvenCheck(num):  # Checks if a number is odd or even
    if (num % 2) == 0:
        # print(str(num) + ": Even")
        return False
    else:
        # print(str(num) + ": Odd")
        return True


uInput = int(input())

while calculateLoop:
    if uInput == 4:
        numLoopGuess += 1
    oec_result = OddEvenCheck(uInput)
    if oec_result:
        print("Multiply by 3 =")
        uInput = uInput * 3
        print(uInput)
        print("Sum by 1 =")
        uInput += 1
        print(uInput)
    else:
        print("Divide by 2")
        uInput = uInput / 2
        uInput = int(uInput)
        print(uInput)

    if numLoopGuess > 1:
        calculateLoop = False

print("Calculation Loop Reached")
