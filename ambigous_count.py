#Code for the ambigous count
str=input("Enter a string\t")
a=e=i=o=u=ambigous_count=0
#Below code is for frequency of each vowel in the given string
for j in str:
    if j=="a":
        a+=1
    if j=="e":
        e+=1
    if j=="i":
        i+=1
    if j=="o":
        o+=1
    if j=="u":
        u+=1

#Below code is for ambigous count using frequency
if a>0:
    ambigous_count+=1
if e>0:
    ambigous_count+=1
if i>0:
    ambigous_count+=1
if o>0:
    ambigous_count+=1
if u>0:
    ambigous_count+=1
print(f"The ambigous count of vowels in the given string is {ambigous_count}")