# Name: Rhakez Elvano Stonie
# NIM: 2611532013
# Question: 4

phone = "082611532013"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)