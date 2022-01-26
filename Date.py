"""
This function get number of day in year and return the date in the format of Shamsi 
"""

def Num_date (n):
    if n<=186:
        f=1
        while n>31 :
            n=n-31
            f=f+1
  

    if (186<n<=365):
        f=7
        n=n-186
        while n>30 :
         n=n-30
         f=f+1
    

    if f==1: f="farvardin"
    elif f==2: f="ordibehesht"
    elif f==3: f="Khordad"
    elif f==4: f="Tir"
    elif f==5: f="Mordad"
    elif f==6: f="shahrivar"
    elif f==7: f="Mehr"
    elif f==8: f="Aban"   
    elif f==9: f="Azar"
    elif f==10:f="Dey"
    elif f==11:f="Bahman"
    elif f==12:f="Esfand" 
    return(print(n,'/',f))

#Test 
Num_date(365)