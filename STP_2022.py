import Register_and_Login as rl
def exit():
     quit()



     

def ch1():
    fr=open("C:/pythonstp/ch1.txt","r")
    ch=fr.read()
    print(ch)

    

  

def ch2():
    fr=open("C:/pythonstp/ch2.txt","r")
    ch=fr.read()
    print(ch)


    
   
          
def ch3():
    fr=open("C:/pythonstp/ch3.txt","r")
    ch=fr.read()
    print(ch)


    


    
def ch4():
    fr=open("C:/pythonstp/ch4.txt","r")
    ch=fr.read()
    print(ch)

    


    
   
def ch5():
    fr=open("C:/pythonstp/ch5.txt","r")
    ch=fr.read()
    print(ch)

    


    
   
def ch6():
    fr=open("C:/pythonstp/ch6.txt","r")
    ch=fr.read()
    print(ch)

    


    
  

def ch7():
    fr=open("C:/pythonstp/ch7.txt","r")
    ch=fr.read()
    print(ch)


    


   

def ch8():
    fr=open("C:/pythonstp/ch8.txt","r") 
    ch=fr.read()
    print(ch)



    


    


def ch9():
    fr=open("C:/pythonstp/ch9.txt","r")
    ch=fr.read()
    print(ch)


  

def ch10():
    fr=open("C:/pythonstp/ch10.txt","r")
    ch=fr.read()
    print(ch)



    


    
def ch11():
    fr=open("C:/pythonstp/ch11.txt","r")
    ch=fr.read()
    print(ch)



    


   

def ch12():
    fr=open("C:/pythonstp/ch12.txt","r")
    ch=fr.read()
    print(ch)


    



    
print("Welcome")

print("Project name: Assignment with Solutions")

print("register")

print("login")

print("exit")

while(1):
     ch=input("enter your choice:")

     if(ch=="register"):
         rl.register()
         break
     elif(ch=="login"):
         rl.login()
         break
     elif(ch=="exit"):
         exit()
     else:
          print("Invalid choice enter again!!\n")


if(ch=="register" or ch=="login"):
   

     print("ASSIGNMENT ")
     print("1. Write a program to check the given number is prime or not?")
     print("2. Write a program to  find the largest number among the three input numbers?")
     print("3. Write a program to create a simple calculator?")
     print("4. Write a program to find the L.C.M. of two input number?")
     print("5. Write a program to find the factorial of a number provided by the user?")
     print("6. Write a program to swap two variables?")
     print("7. Write a program to check if the input number is odd or even?")
     print("8. Write a program to check if year is a leap year or not?")
     print("9. Write a program to display the Fibonacci sequence up to n-th term?")
     print("10 Write a program to check if the number is an Armstrong number or not ?")
     print("11.Write a program to find the ASCII value of the given character?")
     print("12.Write a program to find the area of triangle ?")

     ch=eval(input("Enter your question number"))

    
    


     if(ch==1):
        ch1()
     elif(ch==2):
        ch2()
     elif(ch==3):
        ch3()
     elif(ch==4):
        ch4()
     elif(ch==5):
        ch5()
     elif(ch==6):
        ch6()
     elif(ch==7):
        ch7()
     elif(ch==8):
        ch8()
     elif(ch==9):
        ch9()
     elif(ch==10):
        ch10()
     elif(ch==11):
        ch11()
     elif(ch==12):
        ch12()







    
else:
    print("QUIT")
    exit()
         


