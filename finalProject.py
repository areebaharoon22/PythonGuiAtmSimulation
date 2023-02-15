'''
Application Name: finalProject.py
Description: "This application writes a GUI program that stimulates an ATM."
Author: Areeba Haroon
Course Name: CIS2531
Section: NET02
Instructor: Muhammad Morovati
Date: 8/4/2022


--------- READ ME ---------
Please use the following default username and pin to access the atm
USERNAME: cis2531 (case sensitive)
PIN: 2022
Savings Account initial default balance: $5000
Checking Account initial default balance: $1000

'''
#importing tkinter module as tk
import tkinter as tk
#importing font tkinter module as font to access fonts
import tkinter.font as font
#importing locale module to format currency
import locale
locale.setlocale( locale.LC_ALL, '' )

#Required classes
class Account:
    def __init__(self, userID, pin):
        self.__userID = userID 
        self.__pin = pin 
    
    #writing Mutators (set methods) for each attribute
    def set_userID(self, userID):
        self.__userID = userID
        
    def set_pin(self, pin):
        self.__pin = pin
    
    #writing Accessor (get methods) for each attribute     
    def get_userID(self):
        return self.__userID
    
    def get_pin(self):
        return self.__pin
    
    
class SavingAccount:
    def __init__(self, savBal):
        self.__savBal = savBal 
    
    #writing Mutators (set methods) for each attribute
    def set_savBal(self, savBal):
        self.__savBal = savBal
        
    #writing Accessor (get methods) for each attribute     
    def get_savBal(self):
        return self.__savBal
    
    
class CheckingAccount:
    def __init__(self, checkBal):
        self.__checkBal = checkBal 
    
    #writing Mutators (set methods) for each attribute
    def set_checkBal(self, checkBal):
        self.__checkBal = checkBal
        
    #writing Accessor (get methods) for each attribute     
    def get_checkBal(self):
        return self.__checkBal
     
    
#COMMANDS METHODS TO SWITCH BETWEEN FRAMES (MAKE IT VISIBLE)
def show_chooseAccount():
    ''' This functions shows "choose account" frame and make other frames invisible.
    '''
    frame_chooseAccount.pack(fill='both', expand=1) #visible
    #all invisible
    frame_mainWindow.forget()
    frame_savingMenu.forget()
    frame_checkingMenu.forget() 
    
#savings Account   
def show_savingMenu():
    ''' This functions shows "saving menu" frame and make other frames invisible.
    '''
    frame_savingMenu.pack(fill='both', expand=1) #visible
    #all invisible
    frame_mainWindow.forget()
    frame_chooseAccount.forget()
    frame_Sav_depositCash.forget()
    frame_Sav_withdrawCash.forget()
    frame_Sav_depositCheck.forget()
    
def Show_sav_depositCash():
    ''' This functions shows "Savings- deposit Cash" frame and make other frames invisible.
    '''
    frame_Sav_depositCash.pack(fill='both', expand=1) #visible
    #all invisible
    frame_mainWindow.forget()
    frame_chooseAccount.forget()
    frame_savingMenu.forget()
       
def Show_sav_withdrawCash():
    ''' This functions shows "Savings- withdraw Cash" frame and make other frames invisible.
    '''
    frame_Sav_withdrawCash.pack(fill='both', expand=1) #visible
    #all invisible
    frame_mainWindow.forget()
    frame_chooseAccount.forget()
    frame_savingMenu.forget()
    frame_Sav_depositCash.forget()
    
def Show_sav_depositCheck():
    ''' This functions shows "Savings- deposit check" frame and make other frames invisible.
    '''
    frame_Sav_depositCheck.pack(fill='both', expand=1) #visible
    #all invisible
    frame_mainWindow.forget()
    frame_chooseAccount.forget()
    frame_savingMenu.forget()
    frame_Sav_depositCash.forget()
    frame_Sav_withdrawCash.forget()
    
#checking Accounts
def show_checkingMenu():    
    ''' This functions shows "checking menu" frame and make other frames invisible.
    '''
    frame_checkingMenu.pack(fill='both', expand=1) #visible
    #all invisible
    frame_mainWindow.forget()
    frame_chooseAccount.forget()
    frame_check_depositCash.forget()
    frame_check_withdrawCash.forget()
    frame_check_depositCheck.forget()
    
    
def Show_check_depositCash():
    ''' This functions shows "Checking- deposit Cash" frame and make other frames invisible.
    '''
    frame_check_depositCash.pack(fill='both', expand=1) #visible
    #all invisible
    frame_mainWindow.forget()
    frame_chooseAccount.forget()
    frame_savingMenu.forget()
    frame_checkingMenu.forget()
    
def Show_check_withdrawCash():
    ''' This functions shows "Checking- withdraw Cash" frame and make other frames invisible.
    '''
    frame_check_withdrawCash.pack(fill='both', expand=1) #visible
    #all invisible
    frame_mainWindow.forget()
    frame_chooseAccount.forget()
    frame_checkingMenu.forget()
    frame_check_depositCash.forget()

def Show_check_depositCheck():
    ''' This functions shows "Checking- deposit check" frame and make other frames invisible.
    '''
    frame_check_depositCheck.pack(fill='both', expand=1) #visible
    #all invisible
    frame_mainWindow.forget()
    frame_chooseAccount.forget()
    frame_checkingMenu.forget()
    frame_check_depositCash.forget()
    frame_check_withdrawCash.forget()
    

#BUTTONS METHODS    
def Verify_UserId_pin():
    ''' This functions shows choose account frame if user input is correct.
    '''
    userId = entryUserID.get()
    pin = entryPin.get()
    
    
    if (userId == my_account.get_userID() and pin == my_account.get_pin()):
        frame_chooseAccount.pack(fill='both', expand=1)
        frame_mainWindow.forget()
        
    elif (userId == my_account.get_userID() and pin != my_account.get_pin()):
        tk.messagebox.showinfo('Error!!! Wrong pin!',
                            'pin is incorrect! Please try again')    
    else:
        tk.messagebox.showinfo('Error!',
                            'User ID and pin is incorrect! Please try again!')

#saving Accounts    
def Saving_DepositCash():
    ''' This functions deposites cash into the savings account and shows confirmation mesg box.
    '''
    newDeposit = entryDepositCash_sav.get()
    deposit = my_saving.get_savBal()
    #new balance
    updateBal = float(newDeposit) + float(deposit)
    
    
    tk.messagebox.showinfo('Saving Account',
                           'Cash Deposited Successfully!\n New Balance: ' + '${:0,.2f}'.format(updateBal))
    
    my_saving.set_savBal(updateBal)
    
def Saving_DepositCheck():
    ''' This functions deposites check into the savings account and shows confirmation mesg box.
    '''
    newDeposit = entryDepositCheck_sav.get()
    deposit = my_saving.get_savBal()
    #new balance
    newBal = float(newDeposit) + float(deposit)
    
    
    tk.messagebox.showinfo('Saving Balance',
                           'Check Deposited Successfully!\nNew Balance: ' + '${:0,.2f}'.format(newBal))
    
    my_saving.set_savBal(newBal)
    
def Saving_WithdrawCash():
    ''' This functions withdraws cash from the savings account (if balance is enough) and shows confirmation mesg box (or error mesg).
    '''
    withdrawVal = float(entryWithdrawCash_sav.get())
    balance = float(my_saving.get_savBal())
    
    if withdrawVal <= balance:
        newbal = balance - withdrawVal
        tk.messagebox.showinfo('Saving Account',
                           'A withdrawal has been made Successfully!\nNew Balance: ' + '${:0,.2f}'.format(newbal))
        my_saving.set_savBal(newbal)
    elif withdrawVal > balance:
        tk.messagebox.showinfo('Error!!!',
                           'Withdrawal ammount is more than what is available!!!\nCurrent Balance Available: ' + '${:0,.2f}'.format(balance))
    
        
def View_SavingBal():
    ''' This functions shows the current balance of savings account through a mesg box.
    '''
    
    tk.messagebox.showinfo('Saving Balance',
                            '\'Savings Account\'\nCurrent Balance: ' + '${:0,.2f}'.format(my_saving.get_savBal()))

#checking Accounts    
def View_checkingBal():
    ''' This functions shows the current balance of checking account through a mesg box.
    '''
    
    tk.messagebox.showinfo('Checking Balance',
                            '\'Checking Account\'\nCurrent Balance: ' + '${:0,.2f}'.format(my_checking.get_checkBal()))
    
def Checking_DepositCash():
    ''' This functions deposites cash into the checking account and shows confirmation mesg box.
    '''
    newDeposit = entryDepositCash_check.get()
    deposit = my_checking.get_checkBal()
    #new balance
    updateBal = float(newDeposit) + float(deposit)
   
    
    tk.messagebox.showinfo('Checking Account',
                           'Cash Deposited Successfully!\n New Balance: ' + '${:0,.2f}'.format(updateBal))
    
    my_checking.set_checkBal(updateBal)

def Checking_WithdrawCash():
    ''' This functions withdraws cash from the Checking account (if balance is enough) and shows confirmation mesg box (or error mesg).
    '''
    withdrawVal = float(entryWithdrawCash_check.get())
    balance = float(my_checking.get_checkBal())
    
    if withdrawVal <= balance:
        newbal = balance - withdrawVal
        tk.messagebox.showinfo('Checking Account',
                           'A withdrawal has been made Successfully!\nNew Balance: ' + '${:0,.2f}'.format(newbal))
        my_checking.set_checkBal(newbal)
    elif withdrawVal > balance:
        tk.messagebox.showinfo('Error!!!',
                           'Withdrawal ammount is more than what is available!!!\nCurrent Balance Available: ' + '${:0,.2f}'.format(balance))

def Checking_DepositCheck():
    ''' This functions deposites check into the Checking account and shows confirmation mesg box.
    '''
    newDeposit = entryDepositCheck_check.get()
    deposit = my_checking.get_checkBal()
    #new balance
    newBal = float(newDeposit) + float(deposit)
    
    tk.messagebox.showinfo('Checking Balance',
                           'Check Deposited Successfully!\nNew Balance: ' + '${:0,.2f}'.format(newBal))
    
    my_checking.set_checkBal(newBal)



#main
if __name__ == '__main__':
    
    #creating the main window
    main_window = tk.Tk()
    #window title
    main_window.title('Final Project (ATM)')
    #size of window
    main_window.geometry('700x500')
    #stopping the user from resizing
    main_window.resizable(False, False)
    
    
    #Creating different fonts
    big_font = font.Font(family='Georgia',
                         size='24',
                         weight='bold')
    small_font = font.Font(family='Georgia',
                           size='12')
                           
    #Making instances of the classes
    #(I used default values so I wouldn't need to take input from the use but user input can be possible!)
    my_account = Account('cis2531', '2022')
    my_saving = SavingAccount(5000)
    my_checking = CheckingAccount(1000)
    
    #creating different frames to change between window screens 
    frame_mainWindow = tk.Frame(main_window) 
    frame_chooseAccount = tk.Frame(main_window)
    #saving
    frame_savingMenu = tk.Frame(main_window) 
    frame_Sav_depositCash = tk.Frame(main_window) 
    frame_Sav_withdrawCash = tk.Frame(main_window) 
    frame_Sav_depositCheck = tk.Frame(main_window)
    #checking
    frame_checkingMenu = tk.Frame(main_window)
    frame_check_depositCash = tk.Frame(main_window) 
    frame_check_withdrawCash = tk.Frame(main_window) 
    frame_check_depositCheck = tk.Frame(main_window)
    
    #displays Main Page
    '''Displaying the content of main page frame (first window)
        "Enter user Id and pin window"
        Uses:
        frame:frame_mainWindow, method:Verify_UserId_pin
    '''  
    #displaying the logo image of ATM
    atm_logo_Pg1 = tk.PhotoImage(file='atm.png')
    lbl_atmLogo_Pg1 = tk.Label(frame_mainWindow,
                           image=atm_logo_Pg1).grid(row=0, column=0, sticky = 's', pady=20)
    #labels 
    lblUserID = tk.Label(frame_mainWindow,
                         text='Enter User ID:',
                         font=small_font)
    lblPin = tk.Label(frame_mainWindow,
                         text='Enter Pin #:',
                         font=small_font)
    #putting it on the screen using grid
    lblUserID.grid(row=1, column=0, sticky = 'e', pady=20)
    lblPin.grid(row=2, column=0, sticky = 'e', pady=10)
    
    #entrys
    entryUserID = tk.Entry(frame_mainWindow,
                           width = 20)
    entryUserID.grid(row=1, column=1, sticky = 'w', pady=20)
    
    entryPin = tk.Entry(frame_mainWindow,
                           width = 5)
    entryPin.grid(row=2, column=1, sticky = 'w', pady=10)
    
    #buttons 
    btnEnter = tk.Button(frame_mainWindow,
                         text='Enter',
                         font=small_font,
                         bg='lightblue',
                         command=Verify_UserId_pin) #function/method
    btnEnter.grid(row=3, column=0, sticky = 'e', ipadx=5, ipady=5, pady=30)
    
    btnExit = tk.Button(frame_mainWindow,
                         text='Exit',
                         bg='red',
                         command=main_window.destroy)
    
    btnExit.grid(row=3, column=1, sticky = 'e', ipadx=5, ipady=5, pady=30)
    #to make this frame visible
    frame_mainWindow.pack(fill='both', expand=1)
    

    #displays Choose Account Page
    '''Displaying the content of Choose Account window frame
        "Choosing an account window"
        Uses:
        frame:frame_chooseAccount, method:Verify_UserId_pin
    '''
    #displaying the logo image of ATM
    atm_logo_Pg2 = tk.PhotoImage(file='atm.png')
    lbl_atmLogo_Pg2 = tk.Label(frame_chooseAccount,
                           image=atm_logo_Pg2).pack(pady=20)
    
    #labels 
    lblWelcome = tk.Label(frame_chooseAccount,
                         text='Welcome! Mohammad Morovati', #it will display the default name 
                         font=big_font).pack(pady=20)
    lblChooseAccount = tk.Label(frame_chooseAccount,
                         text='Please choose an account!',
                         font=small_font).pack(pady=10)
    
    #buttons 
    btnSavings = tk.Button(frame_chooseAccount,
                         text='Savings',
                         font=small_font,
                         bg='lightblue',
                         command=show_savingMenu).pack(pady=10, ipady=5)
    
    
    btnChecking = tk.Button(frame_chooseAccount,
                         text='Checking',
                         font=small_font,
                         bg='lightblue',
                         command=show_checkingMenu).pack(pady=10, ipady=5)
    
    btnExit = tk.Button(frame_chooseAccount,
                         text='Exit Application',
                         font=small_font,
                         bg='pink',
                         command=main_window.destroy).pack(pady=10, ipady=5)
    
    #SAVING ACCOUNT
    #displays Saving Menu Page
    '''Displaying the content of Saving menu window frame
        "Inside Savings Account (main menu page) where you select Deposite cash, check, and withdraw check"
        Uses:
        frame:frame_savingMenu,
        method:Show_sav_withdrawCash, Show_sav_withdrawCash, Show_sav_depositCheck, View_SavingBal, show_chooseAccount
    '''
    #displaying the logo image of ATM
    atm_logo_Pg3 = tk.PhotoImage(file='atm.png')
    lbl_atmLogo_Pg3 = tk.Label(frame_savingMenu,
                           image=atm_logo_Pg3).pack(pady=10)
    
    #labels 
    lblSelection_sav = tk.Label(frame_savingMenu,
                         text='(Savings Account) Make a Selection!', 
                         font=small_font).pack(pady=5)
    
    
    #buttons 
    btnDepositCash_sav = tk.Button(frame_savingMenu,
                         text='Deposit Cash',
                         font=small_font,
                         bg='lightblue',
                         command=Show_sav_depositCash).pack(pady=5, ipady=5)
    
    
    btnWithdrawCash_sav = tk.Button(frame_savingMenu,
                         text='Withdraw Cash',
                         font=small_font,
                         bg='lightblue',
                         command=Show_sav_withdrawCash).pack(pady=5, ipady=5)
    
    btnDepositCheck_sav = tk.Button(frame_savingMenu,
                         text='Deposit Check',
                         bg='lightblue',
                         font=small_font,
                         command=Show_sav_depositCheck).pack(pady=5, ipady=5)
    
    
    btnViewBal_sav = tk.Button(frame_savingMenu,
                         text='View Balance',
                         font=small_font,
                         bg='lightblue',
                         command=View_SavingBal).pack(pady=5, ipady=5)
    
    btnGoBack_sav = tk.Button(frame_savingMenu,
                         text='Go Back',
                         font=small_font,
                         bg='lightyellow',
                         command=show_chooseAccount).pack(pady=5)
    
    btnExit_sav = tk.Button(frame_savingMenu,
                         text='Exit Application',
                         font=small_font,
                         bg='lightpink',
                         command=main_window.destroy).pack(pady=5)
    
 
    #displays Saving Deposite Cash page
    '''Displaying the content of Saving (deposit cash) frame
        "Inside Savings Account (deposit cash button frame)"
        Uses:
        frame:frame_Sav_depositCash, method:Saving_DepositCash, show_savingMenu
    '''
    #labels 
    lblDepositCash_sav = tk.Label(frame_Sav_depositCash,
                         text='Deposit Cash',
                         fg='blue',
                         font=big_font).grid(row=0, column=0, pady=40)
    
    lblEnterAmount_sav = tk.Label(frame_Sav_depositCash,
                         text='Enter Amount:',  
                         font=small_font).grid(row=1, column=0, pady=20, sticky = 'e')
    #entry
    entryDepositCash_sav = tk.Entry(frame_Sav_depositCash,
                           width = 15) 
    entryDepositCash_sav.grid(row=1, column=1, sticky = 'w', pady=20, padx=20)
    
    #buttons
    btnDepositCash_sav = tk.Button(frame_Sav_depositCash,
                         text='Deposit',
                         bg='lightblue',
                         font=small_font,
                         command=Saving_DepositCash).grid(row=2, column=1, sticky = 'w', pady=20, padx=20)
    
    btnReturnToMain_sav = tk.Button(frame_Sav_depositCash,
                         text='Return to Main Menu',
                         bg='lightpink',
                         font=small_font,
                         command=show_savingMenu).grid(row=3, column=0, pady=20, sticky = 'e')
    
    btnExitApplication_sav = tk.Button(frame_Sav_depositCash,
                         text='Exit Application',
                         bg='red',
                         font=small_font,
                         command=main_window.destroy).grid(row=3, column=1, sticky = 'w', pady=20, padx=20)
    
    #displays Saving Withdraw Cash page
    '''Displaying the content of Saving (Withdraw cash) frame
        "Inside Savings Account (withdraw cash button frame)"
        Uses:
        frame:frame_Sav_withdrawCash, method:Saving_WithdrawCash, show_savingMenu
    '''   
    #labels 
    lblWithdrawCash_sav = tk.Label(frame_Sav_withdrawCash,
                         text='Withdraw Cash',
                         fg='blue',
                         font=big_font).grid(row=0, column=0, pady=40)
    
    lblEnterAmount_sav = tk.Label(frame_Sav_withdrawCash,
                         text='Enter Amount:', 
                         font=small_font).grid(row=1, column=0, pady=20, sticky = 'e')
    #entry
    entryWithdrawCash_sav = tk.Entry(frame_Sav_withdrawCash,
                           width = 15)
    entryWithdrawCash_sav.grid(row=1, column=1, sticky = 'w', pady=20, padx=20)
    
    #buttons
    btnWithdrawCash_sav = tk.Button(frame_Sav_withdrawCash,
                         text='Withdraw',
                         bg='lightblue',
                         font=small_font,
                         command=Saving_WithdrawCash).grid(row=2, column=1, sticky = 'w', pady=20, padx=20)
    
    btnReturnToMain_sav = tk.Button(frame_Sav_withdrawCash,
                         text='Return to Main Menu',
                         bg='lightpink',
                         font=small_font,
                         command=show_savingMenu).grid(row=3, column=0, pady=20, sticky = 'e')
    
    btnExitApplication_sav = tk.Button(frame_Sav_withdrawCash,
                         text='Exit Application',
                         bg='red',
                         font=small_font,
                         command=main_window.destroy).grid(row=3, column=1, sticky = 'w', pady=20, padx=20)
    
    
    #displays Saving Deposit Check page
    '''Displaying the content of Saving (deposit check) frame
        "Inside Savings Account (deposit check button frame)"
        Uses:
        frame:frame_Sav_depositCheck, method:Saving_DepositCheck, show_savingMenu
    '''    
    #labels 
    lbldepositCheck_sav = tk.Label(frame_Sav_depositCheck,
                         text='Deposit Check',
                         fg='blue',
                         font=big_font).grid(row=0, column=0, pady=40)
    
    lblEnterAmount_sav = tk.Label(frame_Sav_depositCheck,
                         text='Enter Amount:', 
                         font=small_font).grid(row=1, column=0, pady=20, sticky = 'e')
    
    #entry 
    entryDepositCheck_sav = tk.Entry(frame_Sav_depositCheck,
                           width = 15) 
    entryDepositCheck_sav.grid(row=1, column=1, sticky = 'w', pady=20, padx=20)
    
    #buttons 
    btnDepositCheck_sav = tk.Button(frame_Sav_depositCheck,
                         text='Deposit',
                         bg='lightblue',
                         font=small_font,
                         command=Saving_DepositCheck).grid(row=2, column=1, sticky = 'w', pady=20, padx=20)
    
    btnReturnToMain_sav = tk.Button(frame_Sav_depositCheck,
                         text='Return to Main Menu',
                         bg='lightpink',
                         font=small_font,
                         command=show_savingMenu).grid(row=3, column=0, pady=20, sticky = 'e')
    
    btnExitApplication_sav = tk.Button(frame_Sav_depositCheck,
                         text='Exit Application',
                         bg='red',
                         font=small_font,
                         command=main_window.destroy).grid(row=3, column=1, sticky = 'w', pady=20, padx=20)
    
    #CHECKING ACCOUNT
    #displays checking Menu Page
    '''Displaying the content of checking menu window frame
        "Inside checking Account (main menu page) where you select Deposite cash, check, and withdraw check"
        Uses:
        frame:frame_checkingMenu,
        method:Show_sav_withdrawCash, Show_sav_withdrawCash, Show_sav_depositCheck, View_SavingBal, show_chooseAccount
    '''
    #displaying the logo image of ATM
    atm_logo_Pg4 = tk.PhotoImage(file='atm.png')
    lbl_atmLogo_Pg4 = tk.Label(frame_checkingMenu,
                           image=atm_logo_Pg4).pack(pady=10)
    
    #labels 
    lblSelection_check = tk.Label(frame_checkingMenu,
                         text='(Checking Account) Make a Selection', 
                         font=small_font).pack(pady=5)
    
    
    #buttons 
    btnDepositCash_check = tk.Button(frame_checkingMenu,
                         text='Deposit Cash',
                         font=small_font,
                         bg='lightblue',
                         command=Show_check_depositCash).pack(pady=5, ipady=5)
    
    btnWithdrawCash_check = tk.Button(frame_checkingMenu,
                         text='Withdraw Cash',
                         font=small_font,
                         bg='lightblue',
                         command=Show_check_withdrawCash).pack(pady=5, ipady=5)
    
    btnDepositCheck_check = tk.Button(frame_checkingMenu,
                         text='Deposit Check',
                         bg='lightblue',
                         font=small_font,
                         command=Show_check_depositCheck).pack(pady=5, ipady=5)
    
    
    btnViewBal_check = tk.Button(frame_checkingMenu,
                         text='View Balance',
                         font=small_font,
                         bg='lightblue',
                         command=View_checkingBal).pack(pady=5, ipady=5)
    
    btnGoBack_check = tk.Button(frame_checkingMenu,
                         text='Go Back',
                         font=small_font,
                         bg='lightyellow',
                         command=show_chooseAccount).pack(pady=5)
    
    btnExit_check = tk.Button(frame_checkingMenu,
                         text='Exit Application',
                         font=small_font,
                         bg='lightpink',
                         command=main_window.destroy).pack(pady=5)

    #displays Checking Deposite Cash page
    '''Displaying the content of Checking (deposit cash) frame
        "Inside Checking Account (deposit cash button frame)"
        Uses:
        frame:frame_check_depositCash, method:Checking_DepositCash, show_checkingMenu
    '''
    #labels 
    lblDepositCash_check = tk.Label(frame_check_depositCash,
                         text='Deposit Cash',
                         fg='blue',
                         font=big_font).grid(row=0, column=0, pady=40)
    
    lblEnterAmount_check = tk.Label(frame_check_depositCash,
                         text='Enter Amount:',  
                         font=small_font).grid(row=1, column=0, pady=20, sticky = 'e')
    #entry
    entryDepositCash_check = tk.Entry(frame_check_depositCash,
                           width = 15) 
    entryDepositCash_check.grid(row=1, column=1, sticky = 'w', pady=20, padx=20)
    
    #buttons
    btnDepositCash_check = tk.Button(frame_check_depositCash,
                         text='Deposit',
                         bg='lightblue',
                         font=small_font,
                         command=Checking_DepositCash).grid(row=2, column=1, sticky = 'w', pady=20, padx=20)
    
    btnReturnToMain_check = tk.Button(frame_check_depositCash,
                         text='Return to Main Menu',
                         bg='lightpink',
                         font=small_font,
                         command=show_checkingMenu).grid(row=3, column=0, pady=20, sticky = 'e')
    
    btnExitApplication_check = tk.Button(frame_check_depositCash,
                         text='Exit Application',
                         bg='red',
                         font=small_font,
                         command=main_window.destroy).grid(row=3, column=1, sticky = 'w', pady=20, padx=20)
    
    #displays Checking Withdraw Cash page
    '''Displaying the content of Checking (Withdraw cash) frame
        "Inside Checking Account (withdraw cash button frame)"
        Uses:
        frame:frame_check_withdrawCash, method:Checking_WithdrawCash, show_checkingMenu
    '''   
    #labels 
    lblWithdrawCash_check = tk.Label(frame_check_withdrawCash,
                         text='Withdraw Cash',
                         fg='blue',
                         font=big_font).grid(row=0, column=0, pady=40)
    
    lblEnterAmount_check = tk.Label(frame_check_withdrawCash,
                         text='Enter Amount:', 
                         font=small_font).grid(row=1, column=0, pady=20, sticky = 'e')
    #entry
    entryWithdrawCash_check = tk.Entry(frame_check_withdrawCash,
                           width = 15)
    entryWithdrawCash_check.grid(row=1, column=1, sticky = 'w', pady=20, padx=20)
    
    #buttons
    btnWithdrawCash_check = tk.Button(frame_check_withdrawCash,
                         text='Withdraw',
                         bg='lightblue',
                         font=small_font,
                         command=Checking_WithdrawCash).grid(row=2, column=1, sticky = 'w', pady=20, padx=20)
    
    btnReturnToMain_check = tk.Button(frame_check_withdrawCash,
                         text='Return to Main Menu',
                         bg='lightpink',
                         font=small_font,
                         command=show_checkingMenu).grid(row=3, column=0, pady=20, sticky = 'e')
    
    btnExitApplication_check = tk.Button(frame_check_withdrawCash,
                         text='Exit Application',
                         bg='red',
                         font=small_font,
                         command=main_window.destroy).grid(row=3, column=1, sticky = 'w', pady=20, padx=20)
    
    
    #displays Checking Deposit Check page
    '''Displaying the content of Checking (deposit check) frame
        "Inside Checking Account (deposit check button frame)"
        Uses:
        frame:frame_check_depositCheck, method:Checking_DepositCheck, show_checkingMenu
    '''    
    #labels 
    lbldepositCheck_check = tk.Label(frame_check_depositCheck,
                         text='Deposit Check',
                         fg='blue',
                         font=big_font).grid(row=0, column=0, pady=40)
    
    lblEnterAmount_check = tk.Label(frame_check_depositCheck,
                         text='Enter Amount:', 
                         font=small_font).grid(row=1, column=0, pady=20, sticky = 'e')
    
    #entry 
    entryDepositCheck_check = tk.Entry(frame_check_depositCheck,
                           width = 15) 
    entryDepositCheck_check.grid(row=1, column=1, sticky = 'w', pady=20, padx=20)
    
    #buttons 
    btnDepositCheck_check = tk.Button(frame_check_depositCheck,
                         text='Deposit',
                         bg='lightblue',
                         font=small_font,
                         command=Checking_DepositCheck).grid(row=2, column=1, sticky = 'w', pady=20, padx=20)
    
    btnReturnToMain_check = tk.Button(frame_check_depositCheck,
                         text='Return to Main Menu',
                         bg='lightpink',
                         font=small_font,
                         command=show_checkingMenu).grid(row=3, column=0, pady=20, sticky = 'e')
    
    btnExitApplication_check = tk.Button(frame_check_depositCheck,
                         text='Exit Application',
                         bg='red',
                         font=small_font,
                         command=main_window.destroy).grid(row=3, column=1, sticky = 'w', pady=20, padx=20)
    

    #loop to keep window open
    tk.mainloop()
    
    
    
    
    
    
    