# Name: Rhakez Elvano Stonie
# NIM: 2611532013
# Question: 3

#Bagian A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

#Bagian B
text = "Rhakez Elvano Stonie"
count = 0
for char in (text.lower()):
    if char in "aiueo":
        count += 1
print("Vowels:", count)