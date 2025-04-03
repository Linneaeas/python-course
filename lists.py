#BASIC LIST
"""
acronyms = ["LOL", "IDK", "SMH", "TBH"]
print(acronyms[3])
"""
#APPEND(ADD) 
"""
acronyms = ["LOL"]
acronyms.append("IDK")
acronyms.append("SMH")
acronyms.append("TBH")
print(acronyms)
"""
#REMOVE OR DEL
"""
acronyms = ["LOL", "IDK", "SMH", "TBH", "BFN"]
#acronyms.remove("BFN") 
del acronyms[4]
print(acronyms)
"""
#IF
"""
acronyms = ["LOL", "IDK", "SMH", "TBH"]
word = "BFN"
if word in acronyms:
    print(word+" is in the list")
else:
    print(word+" is not in the list")
"""
#FOR LOOP
"""
acronyms = ["LOL", "IDK", "SMH", "TBH"]
for acronym in acronyms:
    print(acronym)
"""

