"""           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO."""

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
