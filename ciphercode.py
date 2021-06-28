ERRORTEXT = "#error#"
OFFSET = 3
OVERFLOWOFFSET = 23

# This function only takes in lowercase letters and spaces
# It will return an error text when a character in the
# input string is not a lowercase letter or a space. 
def getCipherText(inputStr):

    # The variables hold the inputted letter and the encrypted character
    intValue = 0
    convInt = 0

    # This variable builds the encrypted message
    cipherText = ""

    # The message gets encrypted by changing each letter one by one.
    for element in inputStr:
        if element >= "a" and element <= "z":
            if element >= "x" and element <= "z":
                intValue = ord(element)
                convInt = intValue - OVERFLOWOFFSET
                cipherText = cipherText + chr(convInt)
            else:
                intValue = ord(element)
                convInt = intValue + OFFSET
                cipherText = cipherText + chr(convInt)
        elif element == " ":
            cipherText = cipherText + " "
        else:
            # Detected a character that is not a lowercase letter or a space.
            cipherText = ERRORTEXT
            break
        
    return(cipherText)


#Converts the encrypted text back to the inputted message.
def getPlainText(cipherText):
    intValue = 0
    convInt = 0
    plainText = ""
    for element in cipherText:
        if element == " ":
            plainText = plainText + " "
        elif element >= "a" and element <= "c":
            intValue = ord(element)
            convInt = intValue + OVERFLOWOFFSET
            plainText = plainText + chr(convInt)
        else:
            intValue = ord(element)
            convInt = intValue - OFFSET
            plainText = plainText + chr(convInt)
    return(plainText)


# The input
inputStr = input("What do you want to encrypt? Only use lowercase letters.\n")
cipherText = getCipherText(inputStr)

# Printing results
if cipherText == ERRORTEXT:
    print("Please only enter lowercase letters")
else:
    print("The encrypted message is:",cipherText)
    plainText = getPlainText(cipherText)
    print("The decrypted message is:",plainText)

#Done by Suhrith Kaushik on 6/23/2021
