def roi():
        homeprice = 200000
        rental_Inc=2000
        cash_flow1=300
        try:
            down_payment = float(input('What percentage of downpayment you are planning to put in? : %'))    
            down_payment1= (homeprice*down_payment)/100
            print((f'Total Downpayment amount:$ {down_payment1}'))
            closing_cost= float(input('What is your approximate closing cost?: $'))   
            print((f'Insurance amount/month is:$ {closing_cost}'))   
            rehab= float(input('Total Rehab Budget: $'))   
            print((f'Total Rehab Cost:$ {rehab}'))              
            misc = float(input('Approximate miscellaneous Cost: $')) 
            print((f'Miscellaneous Cost is:$ {misc}'))  
                
            total_investment= down_payment1 + closing_cost +rehab +misc
            print((f'Total Investment:$ {total_investment}'))         

            annual_cflow = cash_flow1*12
            print((f'Total annual Cash Flow:$ {annual_cflow}'))         

            cash_Roi = (annual_cflow/total_investment)*100
            print((f'Cash On Cash ROI:{cash_Roi} %'))         
                 
        except:
            print("Invalid Input")       
            return

    
roi()
