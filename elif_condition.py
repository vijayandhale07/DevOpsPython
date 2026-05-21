
'''
x = 40 

if ( x > 40 ):
    print("x is greater than 40")
elif ( x == 40 ):
    print("x is equal to 40")
else:
    print("x is less than 40")
'''

vaccine = ("Pfizer", "Moderna", "AstraZeneca", "Johnson & Johnson")

for vac in vaccine:
    if vac == "Pfizer":
        print("Pfizer is an mRNA vaccine.")
    elif vac == "Moderna":
        print("Moderna is an mRNA vaccine.")
    elif vac == "AstraZeneca":
        print("AstraZeneca is a viral vector vaccine.")
    elif vac == "Johnson & Johnson":
        print("Johnson & Johnson is a viral vector vaccine.")       
    else:
        print("Unknown vaccine type.")
        