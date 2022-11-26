#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class bank():
    def register(self):
        
        #name of account
        for i in range(1,10):
            name=input("Enter name:")
            if name.isalpha()==True:
                break
            else:
                print("Enter a valid name!!!")
                print()
        
        
        
        #mobile number 
        for i in range(0,10):
            number=input("enter number:")
            if number.isdigit()==True and len(number)==10:
                break
            else:
                print("Enter a valid 10 digit mobile number!!!")
                print()
        
        
        #creating password
        for i in range(0,10):
            password=input("create a 6 digit password:")
            if password.isdigit()==True and len(password)==6:
                break
            else:
                print("Enter a valid password!!!")
                print()
            
                  
            
        #checking or creating file
        
        error=False
        try:
            with open(f"{name}.txt","r") as file:
                content=file.read()
                print("Account already exists!!")
                error=True
        except Exception as ne:
            pass
                

        if error==False:
            with open(f"{name}.txt","w") as file:
                content=file.write(f"{name}\n{number}\n{password}\n100")
                print("Account created successfully!!!")
        
        
        
        
    
    
    def login(self):
        
        #name of account
        for i in range(1,10):
            name=input("Enter name:")
            if name.isalpha()==True:
                break
            else:
                print("Enter a valid name!!!")
                print()
        
        
        #mobile number 
        for i in range(0,10):
            number=input("enter number:")
            if number.isdigit()==True and len(number)==10:
                break
            else:
                print("Enter a valid 10 digit mobile number!!!")
                print()
         
        
        #password
        for i in range(0,10):
            password=input("create a 6 digit password:")
            if password.isdigit()==True and len(password)==6:
                break
            else:
                print("Enter a valid password!!!")
                print()
                
                
                
        try:
            with open(f"{name}.txt","r") as file:
                content=file.read()
                #print(content)
                listing=content.split()
                #print(listing)
                amount=int(listing[3])
                #print(amount)
                
                
                
                if f"{name}\n{number}\n{password}" in content:
                    print("account login successfull!!!")
                    print()
                    
                    for menu in range(1,100):
                        _option=input("Select an option:\n1.Check Balance\n2.Add Money\n3.Withdraw Money\n4.Transfer Money\n5.Logout\n")
                    
                        if _option=="1":
                            print("Balance:",amount)
                        if _option=="2":
                            add=input("Enter Amount to be added:")
                            amount=amount+int(add)
                            with open(f"{name}.txt","w") as file:
                                _content=file.write(f"{name}\n{number}\n{password}\n{amount}")
                                print("Amount added successfully!!")
                        if _option=="3":
                            for i in range(0,10):
                                withdraw=input("Enter Amount Withdraw amount:")
                                if withdraw.isdigit()==True:
                                    break
                                else:
                                    print("Enter a valid amount!!!")
                                    print()
                    
                            if amount>=int(withdraw):
                                amount=amount-int(withdraw)
                                with open(f"{name}.txt","w") as file:
                                    _content=file.write(f"{name}\n{number}\n{password}\n{amount}")
                                    print("Amount withdrawed Successfully!!")
                            else:
                                print("Insufficient balance!!")
                        if _option=="4":
                        
                            for i in range(1,10):
                                beneficiaryName=input("Enter Beneficiary name:")
                                if beneficiaryName.isalpha()==True:
                                    break
                                else:
                                    print("Enter a valid name!!!")
                                    print()
                        
                            for i in range(0,10):
                                transferAmount=input("Enter amount to be transfered:")
                                if password.isdigit()==True:
                                    break
                                else:
                                    print("Enter a valid amount!!!")
                                    print()
                        
                        
                            try:
                                with open(f"{beneficiaryName}.txt","r") as file:
                                    beneficiaryContent=file.read()
                                    beneficiaryListing=beneficiaryContent.split()
                                    beneficiaryAmount=beneficiaryListing[3]
                                
                            
                                    beneficiaryFinalAmount=int(beneficiaryAmount)+int(transferAmount)
                                
                                    if amount>= int(transferAmount):
                                        amount=amount-int(transferAmount)
                                        with open(f"{name}.txt","w") as file:
                                            content1=file.write(f"{name}\n{number}\n{password}\n{amount}")
                                        with open(f"{beneficiaryName}.txt","w") as file:
                                            content2=file.write(f"{beneficiaryListing[0]}\n{beneficiaryListing[1]}\n{beneficiaryListing[2]}\n{beneficiaryFinalAmount}")
                                        print("Amount Transfered Successfully!!")
                                    else:
                                        print("Insufficient Balance!!")
                                        
                                        
                            except Exception as ne:
                                print(ne)
                                print("Beneficiary does not exists!!")        
                            
                        if _option=="5":
                            print("Account Logout Successfully!!")
                            break
                    
                    
                        print()
                        for i in range(1,100):
                            menuoption=input("1.Go back to Main Menu\n2.Logout\n")
                            if menuoption=="1" or menuoption=="2":
                                break
                            else:
                                print("Enter a valid option!!!")
                            
                            
                        if menuoption=="1":
                            pass
                        if menuoption=="2":
                            print("Account Logout Successfully!!")
                            break
                    
                else:
                    print("wrong details!!!")
                    
        except Exception as ne:
            print(ne)
            print("Account does not exists!")
            
            
        #print("Select an option:\n1.Back to main menu\n2.Logout")    
        
        

print(10*"*"+"Welcome to Siddhant Bank"+ 10*"*"+"\n"+ "select an option:\n1.Login existing Account\n2.Create new account")
print()


for i in range(1,100):
    option=input("enter option number 1 or 2:")
    if option=='1' or option=='2':
        break
    else:
        print("choose a valid option!!")
        print()
        
        
        
if option=="2":
    option2=bank()
    option2.register()
    
if option=="1":
    option1=bank()
    option1.login()        
    
    
    
    
    
    
    
    
    


# In[ ]:




