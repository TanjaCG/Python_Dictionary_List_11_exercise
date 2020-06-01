characteristics = {
    'hair': {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"},
    'face': {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"},
    'eye': {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"},
    'gender': {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"},
    'race': {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}
}

people = {
    'Eva': ["female", "white", "blonde", "blue", "oval"],
    'Larisa': ["female", "white", "brown", "brown", "oval"],
    'Matej': ["male", "white", "black", "blue", "oval"],
    'Miha': ["male", "white", "brown", "green", "square"]
}


with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

criminal = []

# search for DNA
for i in characteristics["gender"]:
    if characteristics["gender"][i] in dna:
        print(i)
        criminal.append(i)

for i in characteristics["race"]:
    if characteristics["race"][i] in dna:
        print(i)
        criminal.append(i)

for i in characteristics["hair"]:
    if characteristics["hair"][i] in dna:
        print(i)
        criminal.append(i)

for i in characteristics["eye"]:
    if characteristics["eye"][i] in dna:
        print(i)
        criminal.append(i)

for i in characteristics["face"]:
    if characteristics["face"][i] in dna:
        print(i)
        criminal.append(i)

print(criminal)

# search for criminal
for suspect in people:
    if people[suspect] == criminal:
        print("The person guilty for eating all the ice-cream is {0}." .format(suspect))
