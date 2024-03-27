'''
while True:
    try:
        n=int(input("please enter an integer:"))
        m=int(input("please enter an integer:"))
        z=n/m
        break
    except Exception as e:
        print("Not an integer! Please again 123")
        print(e)
    except ValueError:
        print("Not an integer! Please again 456")
    finally:
        print("You successfull entered an integer!")
        print(z)
        '''
try:
    klu1= open("file.txt","w+")
    try:
        klu1.write("qwertyuiopasdfghjklzxcvbnm")
    finally:
        klu1.close()
except IOError:
    print("file is not found")
else:
    print("the file opened successfully")
    klu1.close()