import random
def register():
        def name():
                global Ch
                Ch=0
                global n1
                n1=""
                global n
                n=input("Enter your username:")        
                f=open("C:/pythonstp/records.txt","r")
                Ext=eval(f.read())
                for y in Ext:
                        if n==Ext[y][0]:
                                print("This username is already taken!\n1.Suggest a username.\n2.Enter your own.")
                                Ch=eval(input("Enter your choice 1 or 2:"))
                if Ch==1:
                                c=1
                                a=["","",""]
                                g=0
                                for x in range(0,3):
                                        g=str(random.randint(1000,9999))
                                        print(str(c)+"."+n+g)
                                        a[x]=n+g
                                        c+=1
                                ch=eval(input("Enter your choice 1,2 or 3:"))
                                if ch==1:
                                        n=a[0]
                                elif ch==2:
                                        n=a[1]
                                elif ch==3:
                                        n=a[2]
                                else:
                                        print("Invalid!")
                                print("Your Username is:",n)
                if Ch==2: 
                        n1=input("Enter your username:")
                        while n1==n:
                                if n1==n:
                                        n1=input("Nice try :)! but enter a different name:")
                        n=n1

                f.close()
        name()
                                                
        def email():
                global e
                e=input("Enter your email address:")
                if e.count("@"and".")==0:
                        print("Invalid email! Try again")
                        email()
                if len(e)<=4:
                        print("Invalid email try again")
                        email()
        email()
        def passw():
                global p
                p=input("Enter your password:")
                cp=input("Confirm password:")
                if p!=cp:
                        print("password do not match! Enter password again")
                        passw()
        passw()
        def phone():
                global ph
                ph=input("Enter your contact number:")
                if len(ph)!=10:
                        print("Invalid entry! Enter again.")
                        phone()
        phone()
        Rec={}
        strr=""
        f=open("C:/pythonstp/records.txt","r")
        strr=f.read()
        if len(strr)==0:
                uid=n+"_"+"0"
                Uid = uid
                Rec[uid]=[n,e,p,ph]
        else:
                Rec=eval(strr)
                uid=n+"_"+str(len(Rec))
                Uid = uid
                Rec[uid]=[n,e,p,ph]
        print("Your unique for to login is:"+uid)
        StringRec=str(Rec)
        f.close()
        f=open("C:/pythonstp/records.txt","w")
        f.write(StringRec)
        f.close()
        return



def login():
        check={}
        print("|=============================================================================|")
        print("                               WELCOME!!!                                    ")
        f=open("C:/pythonstp/records.txt","r")
        Rec=eval(f.read())
        check=Rec
        def uniid():
                global Uid
                Uid=input("Enter your unique ID:")
                if Uid not in check.keys():
                        print("The entered Unique ID is wrong! Try again.")
                        def traceback():
                                trace=input("Are you registered?[y/n]:")
                                if trace=="n" or trace=="N":
                                        print("Let's get you registered!\n")
                                        register()
                                        print('\n Thanks for registering!!Now you will be redirected to the login page.\n')
                                        login()
                                elif trace=='y' or trace=='Y':
                                        def traceback2():
                                                trace2=input("Forgot UID or password?[y/n]:")
                                                if trace2=="y" or trace=='Y':
                                                        print("The UID has been sent to your email.\nTo change your password go to the link provided in the mail.\n")
                                                        login()
                                                elif trace2=='n' or trace=='N':
                                                        print("OK!Try again.\n")
                                                        uniid()
                                                else:
                                                        print("Invalid entry!\n")
                                                        traceback2()
                                        traceback2()
                                else:
                                        print("Invalid entry!\n")
                                        traceback()
                        traceback()
                                                                
                                                
                                                
                else:
                 while(1):
                         c = 0
                         PassWord=input("Enter your password:")
                         if PassWord==Rec[Uid][2]:
                                print("Hello "+Rec[Uid][0]+"!")
                                break
                         elif c==3:
                                 traceback2()
                                 break
                         else:
                                print("Oops! The password you entered is wrong. Try again")
                                c+=1
        f.close()                        
        uniid()
        
        return
                
        
                

