
costPrice = float(input("Please enter the cost price of the article : "))

sellingPrice = float(input("Please enter the selling price of the article : "))

if costPrice < sellingPrice :
    profit = sellingPrice - costPrice
    print("Seller incurred Profit of ₹", profit)

elif costPrice > sellingPrice :
     loss = costPrice- sellingPrice
     print("Seller made a loss of ₹", loss)
    
else :
     print("Seller neither made loss nor profit")

   
