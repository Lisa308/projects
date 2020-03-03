#Lsa mazorodze H180685A
#Assignment2
#Python program that implements Luhn algorithm to check for validity of credit card
def creditcard():
    c_num = input("Enter the credit card ")
    lc_num=list(c_num) #Converts string to input list

    cal_num=[] #Array variable to store calculated value
    u_num =0 #Interger verify number>10

    check =0 #variable sum up all digits

    if len(lc_num) !=16:  #validate length
        print("Not a valid credit card number")
        quit()

    else:
        for i in range(len(lc_num)):
            if((i%2)==0): #for loop for even numbers
                num=int((lc_num[i]))*2 #Multiply number by 2

                if(num>=10):
                    u_num=num%10+1 

                    cal_num.append(u_num)
                else:
                    cal_num.append(num)
            else:
                
                cal_num.append(int(lc_num[i]))

    print("Given number.", lc_num)
    print("Converted list.", cal_num)
    for n in range(len(cal_num)):
        check=check+cal_num[n]
    if(check%10 == 0):
        print("valid credit card")
        return("Valid credit card")
    else:
        print("Invalid credit card")
        return("Invalid credit card")
    
creditcard()  

# credit card 4137894711755904 = valid credit card
# credit card 6499802450273568 = invalid credit card
# credit card 8504172191273888 = valid credit card
# credit card 0043668783485480 = valid credit card
  
                
        
    
    
    
    
