#Imports packages datetime and re
import datetime, re


#Constant that holds value of percentage of levy if customer pays with credit card
CREDIT_CARD_LEVY = 0.05

#Constant that holds value of reduction if customer pays with cash
CASH_REDUCTION = 0.05

#Constant that holds value of cost of booking one day
ONE_DAY_BILL = 260

#Constant that holds value of cost per day if the customer books from 2 to 4 days
TWO_FOUR_DAYS_BILL = 240

#Constant that holds value of cost per day if the customer books from 5 to 8 days
FIVE_EIGHT_DAYS_BILL = 210

#Constant that holds value of cost per day if the customer books for 9 or more days
NINE_LONGER_DAYS_BILL = 200

#Constant that holds value of cost per session musician booked per day 
SESSION_MUSICIAN_COST = 100

#List that holds value of band member names
bandMemberNames=[]

#List that holds value of band member instruments
bandMemberInstruments=[]

#Variable that holds payment options menu presented to the customer
MENU = "Will you pay by\n1: Credit Card (5% Levy)\n2: Cash (5% Discount)\n"\
       "3: Cheque"

print('Welcome to start-up recording studio, we will start your aplication process!!!')

'''
Loop that takes customer contact name input and validates if lenght is higher than 1 character
'''
contactNameBoolean=False 
while not contactNameBoolean:
	contactName = input('\nPlease insert your group\'s contact name:')
	contactNameBoolean=len(contactName)>1
	if not contactNameBoolean:
		print('\nplease insert a name with at least 2 characters')
	
		
		
'''
Loop that takes customer group manage email input and
validates if email as @ character and if has . character after @
with text after the . character also
'''
managerEmailBoolean=False
while not managerEmailBoolean:
	managerEmail = input('\nPlease insert the email of the group\'s manager:')
	if not re.match(r"[^@]+@[^@]+\.[^@]+", managerEmail):
		print('Email not valid, please insert a valid email.')
	else:
		managerEmailBoolean=True

'''
Loop that takes customer group manager phone number input and
validates if it's an integer and if length is higher than 9 this validation
takes in account irish phone numbers
'''		
managerPhoneNumberBoolean=False
while not managerPhoneNumberBoolean:
	try:
		managerPhoneNumber = int(input('\nInsert the mobile phone number of the group\'s manager:'))
		managerPhoneNumberBoolean=len(str(managerPhoneNumber))>9
		if not managerPhoneNumberBoolean:
			print('\Please enter a valid phone number')
	except:
		print('\nYou didn\'t insert a valid numeric character, please enter a valid phone number')

'''
Loop that takes customer start date input and
validates if it's in the format dd/mm/yyyy and if
date is higher or equal to the current day
'''		
requestDateBoolean=False
while not requestDateBoolean:
	try:
		requestDate = input('\nWhat start date are you looking for (dd/mm/yyyy)?\n')
		datetime.datetime.strptime(requestDate, '%d/%m/%Y')
		if requestDate>=datetime.datetime.now().strftime ("%d/%m/%Y"):
			requestDateBoolean=True
		else:
			print('The date you inserted is lower than the current day please insert a correct date.')
		
	except:
		print("Incorrect date format, please insert date in the following format dd/mm/yyyy, ex: 05/11/2017")

print("\nOur studio can only accomodate up to 8 musicians\n")

'''
Loop that takes customer total band members input and
validates if it's an integer and if total band members don't exceed the total members
and if the number of band member is lower than 0
'''				
numberBandMembersBoolean=False
while not numberBandMembersBoolean:
	try:
		numberBandMembers = int(input('\nHow many members of the band?\n'))
		numberBandMembersBoolean=numberBandMembers>0 and numberBandMembers<=8
		if numberBandMembers>8:
			print('\nSorry, but our studio can only accomodate up to 8 musicians')
		elif numberBandMembers<1:
			print('\nSorry, but you need to book at least for 1 musician')
	except:
		print('\nYou didn\'t insert a valid number, please enter total band members again')

'''
Loop that takes customer total booking days input and
validates if it's an integer and if booking days are higher than 0
'''			
numberBookingDaysBoolean = False
while not numberBookingDaysBoolean:
	try:
		numberBookingDays = int(input('\nHow many days you want to book the studio?\n'))
		numberBookingDaysBoolean=numberBookingDays>0
		if not numberBookingDaysBoolean:
			print('\nYou have to book for at least one day')
	except:
		print('\nPlease enter a valid number of days')

#Condition that calculares cost of booking days
if numberBookingDays==1:	
	bookingDaysCost = ONE_DAY_BILL
elif numberBookingDays>1 and numberBookingDays<=4:
	bookingDaysCost = TWO_FOUR_DAYS_BILL*numberBookingDays
elif numberBookingDays>4 and numberBookingDays<=8:
	bookingDaysCost = FIVE_EIGHT_DAYS_BILL*numberBookingDays
else:
	bookingDaysCost = NINE_LONGER_DAYS_BILL*numberBookingDays

'''
Loop that takes customer band member names and band member instrumet input and
validates if it's length of input inserted is higher than one character and
appends input to band member names and instruments lists
'''			
bandAccumulator=1
while bandAccumulator <=numberBandMembers:
	bandMemberBoolean=False
	while not bandMemberBoolean:
		bandMember = input('\nWhat is band member #'+str(bandAccumulator)+'\'s name?\n')
		bandMemberBoolean=len(bandMember)>1
		if not bandMemberBoolean:
			print('\nplease insert a name with at least 2 character')
		else:
			bandMemberNames.append(bandMember)
	
	
	bandInstrumentBoolean = False
	while not bandInstrumentBoolean:
		bandInstrument = input('\nWhat is '+bandMemberNames[bandAccumulator-1] +'\'s instrument?\n')
		bandInstrumentBoolean=len(bandInstrument)>1
		if not bandInstrumentBoolean:
			print('\nplease insert an instrument with at least 2 character')
		else:
			bandMemberInstruments.append(bandInstrument)
	bandAccumulator+=1

spareMusicians=8-numberBandMembers#variable that holds value if there is still room for session musicans

'''
Condition that tests if there is still room for session musicans and
loop that if condition True takes user input on number of session musicians
booked validates if its a positive integer and calculates the session musicians
cost
'''
if spareMusicians>0:
	sessionMusiciansBoolean = False
	while not sessionMusiciansBoolean:
		try:
			sessionMusicians = int(input("\nThere is room for "+ str(spareMusicians) +" session musicans - how many do you want?\n"))
			sessionMusiciansBoolean = sessionMusicians >= 0 and sessionMusicians < spareMusicians
			if sessionMusicians < 0:
				print("\nHey there is no negative musicians, please insert a correct value!!!")
			elif sessionMusicians>spareMusicians:
				print("\nHey you have excedeed the amount of musicians allowed per session! You can only add up to "+str(spareMusicians)+"session musicians" )
		except:
			print('\nPlease enter a valid integer')

	sessionMusiciansCost = sessionMusicians*100*numberBookingDays
else:
	sessionMusiciansCost = 0
	sessionMusicians = 0
	
#Ouputs payment options			
print(MENU)

'''
Loop that takes customer payment option input and
validates if it's a valid option
'''	
menuBoleean = False
while not menuBoleean:
	try:
		menuChoice = int(input("\nPlease insert 1 to select Credit Card, 2 to select"\
		+"Cash and 3 to select Cheque as a payment method?\n"))
		menuBoleean = menuChoice>0 and menuChoice<=3
		if not menuBoleean:
			print("\nHey you select a non existent payment method")
	except:
		print("\nPlease insert only the correspondent number to select the payment option")

		
bookingApplication = "Booking application"
bandMembers = "Band Members"

#Creates txt file with customer contact name in append mode
bookingRequest = open(contactName+'.txt','a')

#Ouputs bands contact name, email, phone number and date requested to book
print("\n"+bookingApplication+"\n"+len(bookingApplication)*"-"+"\nRequested by: "+contactName\
+" (Contact: "+managerEmail+" & "+str(managerPhoneNumber)+")"+"\n\nDate requested --> "+requestDate)

#Writes to Txt file bands contact name, email, phone number and date requested to book
bookingRequest.write("\n"+bookingApplication+"\n"+len(bookingApplication)*"-"\
+"\nRequested by: "+contactName+" (Contact: "+managerEmail+" & "+str(managerPhoneNumber)+")"+"\n\nDate requested --> "+requestDate+"\n")

#Ouputs bands contact name, email, phone number and date requested to book
print("\n"+bandMembers+"\n"+len(bandMembers)*"-")

#Writes to Txt file bands contact name, email, phone number and date requested to book
bookingRequest.write("\n"+bandMembers+"\n"+len(bandMembers)*"-"+"\n")

'''
Loop that outputs and writes to txt file the band member names
and instruments
'''	
bandMemberNamesAccumulator=1
for name in bandMemberNames:
	print("\n"+str(bandMemberNamesAccumulator)+": "+bandMemberNames[bandMemberNamesAccumulator-1]\
	+" - "+bandMemberInstruments[bandMemberNamesAccumulator-1])
	bookingRequest.write("\n"+str(bandMemberNamesAccumulator)+": "+bandMemberNames[bandMemberNamesAccumulator-1]\
	+" - "+bandMemberInstruments[bandMemberNamesAccumulator-1]+"\n")
	bandMemberNamesAccumulator+=1

#Ouputs and writes to txt file the number of session musicians included
print("\nIncludes "+str(sessionMusicians)+" session musicians per day.")
bookingRequest.write("\nIncludes "+str(sessionMusicians)+" session musicians per day.\n")

'''
Condition that checks payment option selected by user and calculates total cost accordingly
Outupts and writes to txt file the total cost and payment option
'''
if menuChoice==1:
	totalCost = (bookingDaysCost+sessionMusiciansCost)*(1+CREDIT_CARD_LEVY)
	print("\nPayment will be "+str(totalCost)+" Euros to be paid by Credit Card\n")
	bookingRequest.write("\nPayment will be "+str(totalCost)+" Euros to be paid by Credit Card\n")
elif menuChoice==2:
	totalCost = (bookingDaysCost+sessionMusiciansCost)*(1-CASH_REDUCTION)
	print("\nPayment will be "+str(totalCost)+" Euros to be paid by Cash")
	bookingRequest.write("\nPayment will be "+str(totalCost)+" Euros to be paid by Cash\n")
else:
	totalCost = bookingDaysCost+sessionMusiciansCost
	print("\nPayment will be "+str(totalCost)+" Euros to be paid by Cheque")
	bookingRequest.write("\nPayment will be "+str(totalCost)+" Euros to be paid by Cheque\n")

#Ouputs and writes to txt file the date of submission of booking request
print("\nDate of submission---->"+datetime.datetime.now().strftime ("%d/%m/%Y"))
bookingRequest.write("\nDate of submission---->"+datetime.datetime.now().strftime ("%d/%m/%Y"))

#Closes the txt file
bookingRequest.close()


	


