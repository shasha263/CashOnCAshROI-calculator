class CashoncashRoI():
    def __init__(self):
        self.homeprice = 0
        self.total_income=0
        self.rental_Inc=0
        self.total_expense=0
        self.cash_flow1=0
        self.total_investment=0
        
    def income(self):
        try:
            self.homeprice = float(input('What is the market value of your property? : $'))     
            self.rental_Inc= float(input('What is your approximate rental Income? : $'))  
            other_Inc= float(input('Do you expect any other types of Income? (Such as: Laundry/ Storage)?\n Please enter 0 for none: $ '))
            self.total_income= self.rental_Inc + other_Inc
            print(f'Total Income per month:$ {self.total_income}')          
      
        except:
            print("Invalid Input")
            return 
          
       


    def expenses(self):
        try:
            tax = float(input('What is the property tax (in percentage) of your property? %'))    
            tax1= (self.homeprice*tax)/(100*12)
            #print((f'Tax amount/month is:$ {tax1}'))
            insurance= float(input('What is your total insurance amount/month?: $'))   
            #print((f'Insurance amount/month is:$ {insurance}'))   
            utilities= float(input('Total Utility expense ( Please enter $0 if tenant will pay for the utilities): $'))   
            #print((f'Total Utility Cost:$ {utilities}'))              
            hoa_fee = float(input('How much is HOA(Home Owner Association) Fee/month?: $')) 
            #print((f'HOA Fee/month is:$ {hoa_fee}'))  
            vacant= int(input('Approximate vacant days: ')) 
            vacant1=vacant*(self.rental_Inc/30)
            #print((f'Vacancy Expense:$ {vacant1}'))  
            repair=float(input('Approximate repair cost/month?: $')) 
            #print((f'Repair Cost/month :$ {repair}'))  
            capx=float(input('How much you want to set aside for CapX/month?: $')) 
            #print((f'CapX cost/month:$ {capx}'))  
            property_mgt= float(input('Property Management Fee ( Please enter $0 if you want to manage your own property): $'))    
            #print(f'Property Management Fee:$ {property_mgt}')
            mortgage=float(input('How much will be approximate Mortgage amount per month?: $')) 
            #print((f'Mortgage Amount:$ {mortgage}'))         
            self.total_expense= tax1+ insurance + utilities+hoa_fee+vacant1+repair+capx+property_mgt+mortgage
            print((f'Total monthly Expense:$ {self.total_expense}'))                       
                  
        except:
            print("Invalid Input")    
            return           

    def cash_flow(self):
        #print((f'Total monthly Income:$ {self.rental_Inc}')) 
        #print((f'Total monthly Expense:$ {self.total_expense}')) 
        self.cash_flow1 = self.rental_Inc - self.total_expense
        print((f'Total monthly Cashflow:$ {self.cash_flow1}')) 
       

    def roi(self):
        try:
            down_payment = float(input('What percentage of downpayment you are planning to put in? : %'))    
            down_payment1= (self.homeprice*down_payment)/100
            #print((f'Total Downpayment amount:$ {down_payment1}'))
            closing_cost= float(input('What is your approximate closing cost?: $'))   
            #print((f'Insurance amount/month is:$ {closing_cost}'))   
            rehab= float(input('Total Rehab Budget: $'))   
            #print((f'Total Rehab Cost:$ {rehab}'))              
            misc = float(input('Approximate miscellaneous Cost: $')) 
            #print((f'Miscellaneous Cost is:$ {misc}'))  
                
            self.total_investment= down_payment1 + closing_cost +rehab +misc
            #print((f'Total Investment:$ {self.total_investment}'))         

            annual_cflow = self.cash_flow1*12
            #print((f'Total annual Cash Flow:$ {annual_cflow}'))         

            cash_Roi = (annual_cflow/self.total_investment)*100
            print((f'Cash On Cash ROI:{cash_Roi} %'))         
                 
        except:
            print("Invalid Input")       
            return


class Main():

    def showInstructions():
        print("""
          Welcome to Shaharima's CashOnCashROI Calculator:
          """)

    def run():
        coroi=CashoncashRoI()

        Main.showInstructions()
        coroi.income()
        coroi.expenses() 
        coroi.cash_flow()  
        coroi.roi()     


Main.run()

     