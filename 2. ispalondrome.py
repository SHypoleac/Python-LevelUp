def ispalindrome(theword):
    theword=theword.lower()
    theword=theword.replace(" ","")
    thewordbackward=theword[::-1]
    return thewordbackward==theword
while True:
    typed=input("enter a word : ")
    if typed=="exit":
        print("Bye! :*")
        exit()
    print(ispalindrome(typed))


