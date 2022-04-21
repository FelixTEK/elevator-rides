#FELIXTEK 2022
argument = ""
n=0
x=0
finalweight = 0
elevrides = 0

def calc():
    global finalweight
    global x
    global elevrides
    n=0
    x=0
    finalweight = 0
    elevrides = 1
    w = []
    n = int(input("Insert number of people."))
    if n > 20:
        print("Can't exceed 20.")
        main()
    x = int(input("Insert max. weight."))
    if n > 1000000000:
        print("Can't exceed 1 billion.")
        main()

    for i in range(n):
        w.append(int(input("Insert weight of each individual.")))
        finalweight = finalweight + int(w.pop())

    return finalweight, elevrides
    

def fnweightloop():
    global finalweight
    global elevrides
    global x
    elevrides = elevrides + 1
    finalweight = finalweight - x
    if finalweight > x:
        fnweightloop()
    return finalweight

def runagain():
  global argument
  argument = input("Run again? (Y/N)\n> ").capitalize()
  if argument == "Y":
    main()
  elif argument == "N":
    print("Bye.")
  else:
    print("Invalid response.")
    runagain()

def main():
    calc()
    if finalweight > x:
        fnweightloop()
    print("The number of least elevator rides is %d." %elevrides)
    runagain()

if __name__ == "__main__":
    while True:
        main()
        if argument == "N":
            break
    

