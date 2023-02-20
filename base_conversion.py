"""           Copyright (C) 2023 Knugi

This work is free.  You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To But It's Not My Fault Public
License, Version 1, as published by Ben McGinnes:

    DO WHAT THE FUCK YOU WANT TO BUT IT'S NOT MY FAULT PUBLIC LICENSE
                    Version 1, October 2013

 Copyright (C) 2013 Ben McGinnes <ben@adversary.org>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

   DO WHAT THE FUCK YOU WANT TO BUT IT'S NOT MY FAULT PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

  1. Do not hold the author(s), creator(s), developer(s) or
     distributor(s) liable for anything that happens or goes wrong
     with your use of the work.
"""

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
