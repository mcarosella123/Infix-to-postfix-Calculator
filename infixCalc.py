# Mark Carosella
# Data Structures
# Individual Project 05
# 10/31/2016

from scanner import *
from tokens import *
from arraystack import *
from model import *

class IFToPFConverter(object):
    """Converts an infix expression into a postfix expression."""
    def __init__(self,eachToken):
        self._eachToken = eachToken

    def convert(self):

        # Initialize variables 
        legalOps = ["*","/","+","-","(",")"]
        numInts = 0
        numOps = 0
        tokensProcessed = 0
        opStack = ArrayStack()
        postfixExp = []
        finalExp = []
        # Create expression list (infix order)
        while self._eachToken.hasNext():
            postfixExp.append(str(self._eachToken.next()))
        # Recording quantity of integers and operators (for later use)
        for eachItem in postfixExp:
            if eachItem not in legalOps:
                numInts += 1
            else:
                numOps += 1
        for eachItem in postfixExp:
            tokensProcessed += 1    # Keep track of where we are
            tempToken = Token(eachItem)
            precedence = tempToken.getPrecedence()
            # If operand
            if precedence == 1:
                finalExp.append(str(tempToken))
                numInts -= 1
                if numInts == 0:
                    # If last int in exp and no parenthesis, pop entire stack
                    if "(" not in postfixExp:
                        lastOps = opStack.pop()
                        finalExp.append(str(lastOps))
                        if len(opStack) == 0:
                            break
            # If multiplication or division
            elif precedence == 2:
                # If first operator
                if len(opStack) == 0:
                    opStack.push(eachItem)
                # If ops of equal precedence on stack
                elif "*" in opStack or "/" in opStack:
                    while opStack.peek() == "*" or opStack.peek() == "/":
                        poppedOp = opStack.pop() # pop them
                        finalExp.append(str(poppedOp))
                        if len(opStack) == 0 or eachItem == "(":
                            break
                    opStack.push(eachItem)
                else:
                    opStack.push(eachItem)
            # If addition or subtraction
            elif precedence == 3:
                # If first operator
                if len(opStack) == 0:
                    opStack.push(eachItem)
                # If equal or higher precedence
                elif "*" in opStack or "/" in opStack or "+" in opStack \
                     or "-":
                    # Pop equal or higher precedence
                    while opStack.peek() == "+" or opStack.peek() == "-" \
                          or opStack.peek() == "*" or opStack.peek() == "/":
                        poppedOp = opStack.pop()
                        finalExp.append(str(poppedOp))
                        if len(opStack) == 0 or eachItem == "(":
                            break
                    opStack.push(eachItem)
                else:
                    opStack.push(eachItem)
            # If parenthesis
            elif precedence == "par":
                if eachItem == "(":
                    opStack.push(eachItem)
                else:
                    # If right parenthesis, pop until you see a left
                    while opStack.peek() != "(":
                        poppedOp = opStack.pop()
                        finalExp.append(str(poppedOp))
                    opStack.pop()    # Pop the left

            # While expression is done
            while tokensProcessed == len(postfixExp):
                # Keep popping until empty stack
                if len(opStack) == 0:
                    break
                else:
                    lastOps = opStack.pop()
                    finalExp.append(str(lastOps))
                
        return finalExp

def main():
    again = True
    while again == True:
        postfixStr = ""
        userExp = input("Enter an infix expression: ")
        if userExp == "":
            again = False
            continue
        scannedExp = Scanner(userExp)
        toPostfix = IFToPFConverter(scannedExp)
        toPostfix = toPostfix.convert()
        for eachToken in toPostfix:
            postfixStr += eachToken + " "
        print("Postfix: ",postfixStr)
        print(userExp," = ",PFEvaluatorModel().evaluate(postfixStr))
        
main()

