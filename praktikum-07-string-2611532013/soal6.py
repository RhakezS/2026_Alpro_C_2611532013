# Name: Rhakez Elvano Stonie
# NIM: 2611532013
# Question: 6 

full_name = "Rhakez Elvano Stonie"
nim = "2611532013"

name = full_name.strip()
pos = name.find(" ")

if pos == -1:
    first_name = name
else:
    first_name = name[:pos]

username = first_name.lower() + nim[-3:]
print("Username:", username)