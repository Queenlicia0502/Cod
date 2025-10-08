# take marks as input fromuser 
Print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("math :"))
english = int(input("english :"))
science = int(input("science :"))
japenese = int(input("japanese : "))


# Let's calculate the percentage ofmarks
sum = math+english+science+japanese
print("sun of math,english,scienece,japanese")

perc = (sum/400)*100

print(end="Prcentage Mark = ")
print(perc)