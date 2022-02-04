# Limited version of main.py

print("choose a number between 1 and 10")

questionLoop = True
calculateLoop = True
numLoopGuess = 0


def OddEvenCheck(num):
    if (num % 2) == 0:
        # print(str(num) + ": Even")
        return False
    else:
        # print(str(num) + ": Odd")
        return True

while questionLoop:
    uInput = int(input())
    if uInput > 10:
        print("Number was above 10")
    elif uInput < 1:
        print("Number was below 1")
    else:
        questionLoop = False

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
