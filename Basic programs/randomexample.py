'''
import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=("ram","gayathri","anusha","john","vicky")
mylist1={"ram","gayathri","anusha","john","vicky"}
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)'''
import string
import random
s=10
ran=' '.join(random.sample(string.ascii_uppercase+string.digits,k=s))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran)
print(ran1)