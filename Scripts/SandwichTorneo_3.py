upper = "AÁBCDEFGHIJKLMNÑOPQRSTUÜV&"
lower = "aábcdefghijklmnñopqrstuüv"
nums  = "0136"
punct = ".,"

def letterSandwicher(letters, bread):
    sandwich = bread
    for letter in letters:
        sandwich += letter + bread
    return sandwich
    
print(letterSandwicher(upper,"H"))
print(letterSandwicher(upper,"O"))

print(letterSandwicher(lower,"n"))
print(letterSandwicher(lower,"o"))

print(letterSandwicher(nums,"H"))
print(letterSandwicher(nums,"O"))

print(letterSandwicher(punct,"H"))
print(letterSandwicher(punct,"O"))