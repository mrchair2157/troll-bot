import random

words = open("words.txt","r")
tmp = ""
Pronouns = ""
while tmp != "END":
    Pronouns = Pronouns + tmp
    tmp = words.readline()
print(
words.close()

#WC = random.randint(5,17)
#sentince = ""
#for x in range(WC):
#    sentince = sentince + ' ' + random.choice(LOW)
#    x = x + 1
#
#sentince = sentince + "."
#print(sentince)
