a = ""
word = "xss"


while True:
    a = input("Type a sentance\n")
    if a == "quit":
        break
    if word in a:
        print("there is xss\n")
    else:
        print("there is no xss\n")