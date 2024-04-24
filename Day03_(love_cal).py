name1=input("Enter Your Name:")
name2=input("Enter your partner:")
combine_name=name1+name2
lover_name=combine_name.lower()
t=lover_name.count("t")
r=lover_name.count("r")
u=lover_name.count("u")
e=lover_name.count("e")
First_digit=t+r+u+e

l=lover_name.count("l")
o=lover_name.count("o")
v=lover_name.count("v")
e=lover_name.count("e")

Second_digit=l+o+v+e

score=int(str(First_digit)+str(Second_digit))
if score <10 or score>90 :
    print(f'your score is {score} , you are together')
elif score >= 40 and score <=50 :
    print(f'your score is {score} ,both are good frd')
else :
    print(f'you score is {score}')      