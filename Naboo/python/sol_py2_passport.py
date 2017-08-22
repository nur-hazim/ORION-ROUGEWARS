#ANSWER ======================================================================
monthsLeft = int(input("Number of months left before passport expires:"))
monthsToEntry = int(input("Months to intended travel date:"))

if (monthsLeft - monthsToEntry) < 6 :        #Check if user's passport is valid for entry 
    print("You need to renew your passport") #Modify to display that user's passport is valid for entry
else:
    print("Your passport is valid") #Modify to display that user needs to renew his passport        