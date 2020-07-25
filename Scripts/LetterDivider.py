#Letters to divide:
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
names = ["Sandra", "Aspacia", "Tamara", "Ro"]

#----Calculations----
lettersNum = len(letters)
namesNum = len(names)
indexes = list(range(0,lettersNum))
    
def chooser(name, ammount):
    print(f"{name}:")
    for i in range(ammount):
        ch = choice(indexes)
        print(letters[ch], end=" ")
        indexes.remove(ch)
    print("\n")
#----/Calculations----

for i in range(namesNum-1):
    name = choice(names)
    chooser(name, int(lettersNum/namesNum))
    names.remove(name)
#Last with extra letters
chooser(names[0], lettersNum - (namesNum-1) *(int(lettersNum/namesNum)))

#Report if not all letters chosen
if len(indexes) > 0:
    print("GAH!")