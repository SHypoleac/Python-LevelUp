def alphasort(thelistofwords):
    return sorted(thelistofwords,key=str.capitalize)

while True:
    thelistofwords=input("Enter the words : ").split(" ")
    if any(thelistofwords)=="exit":
        print("bye :*")
        exit()
    print(alphasort(thelistofwords))
