class main:
    def __init__(self):
        pass
        
    def AnyDec(self, userInput, system):
        i = 0
        sum = 0
        reversedInput = userInput[::-1]
        print(reversedInput)
        for x in reversedInput:
            temp = system**i * int(x)
            sum = sum + temp
            i = i + 1
        return sum

    def DecAny(self, userInput, system):
        sum = ""
        number = userInput
        quotient = int(number)
        divisor = system
        while True:
            remainder = quotient % divisor
            quotient = quotient // divisor
            sum = str(remainder) + sum
            if(quotient == 0):
                break
        return sum
    
if __name__ == "__main__":
    p1 = main()
    user = input().split(" ")
    print(p1.AnyDec(user[0], int(user[1])))
    #print(p1.DecAny(user[0], int(user[1])))
