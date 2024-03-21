from diceware import Diceware

dw = Diceware()

def create_password(words_nr):
    password = dw.generate(words_nr)
    print("Generated passowrd:", password)

x=input("Enter a number : ")
while x!="exit":
    create_password(x)
    x=input("Enter a number of words: ")
print("Baja bongo! PA! :*")