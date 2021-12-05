def income():
        homeprice = 0
        rental_Inc=0
        try:
            homeprice = float(input('What is the market value of your property? : $'))     
            rental_Inc= float(input('What is your approximate rental Income? : $'))  
            other_Inc1= float(input('Do you expect any other types of Income? (Such as: Laundry/ Storage)?\n Please enter 0 for none: $ '))
            total_income= rental_Inc + other_Inc1
            print(f'Total Income per month:$ {total_income}')          
      
        except:
            print("Invalid Input")
            return False

income()
