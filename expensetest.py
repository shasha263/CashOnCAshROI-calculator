def expense():
        homeprice = 200000
        rental_Inc=2000
        try:
            tax = float(input('What is the property tax (in percentage) of your property? %'))    
            tax1= (homeprice*tax)/(100*12)
            print((f'Tax amount/month is:$ {tax1}'))
            insurance= float(input('What is your total insurance amount/month?: $'))   
            print((f'Insurance amount/month is:$ {insurance}'))   
            utilities= float(input('Total Utility expense ( Please enter $0 if tenant will pay for the utilities): $'))   
            print((f'Total Utility Cost:$ {utilities}'))              
            hoa_fee = float(input('How much is HOA(Home Owner Association) Fee/month?: $')) 
            print((f'HOA Fee/month is:$ {hoa_fee}'))  
            vacant= int(input('Approximate vacant days: ')) 
            vacant1=vacant*(rental_Inc/30)
            print((f'Vacancy Expense:$ {vacant1}'))  
            repair=float(input('Approximate repair cost/month?: $')) 
            print((f'Repair Cost/month :$ {repair}'))  
            capx=float(input('How much you want to set aside for CapX/month?: $')) 
            print((f'CapX cost/month:$ {capx}'))  
            property_mgt= float(input('Property Management Fee ( Please enter $0 if you want to manage your own property): $'))    
            print(f'Property Management Fee:$ {property_mgt}')
            mortgage=float(input('How much will be approximate Mortgage amount per month?: $')) 
            print((f'Mortgage Amount:$ {mortgage}'))         
            total_expense= tax1+ insurance + utilities+hoa_fee+vacant1+repair+capx+property_mgt+mortgage
            print((f'Total monthly Expense:$ {total_expense}'))                       
                  
        except:
            print("Invalid Input")                     

    
expense()