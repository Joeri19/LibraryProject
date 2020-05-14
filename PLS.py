def StartMenu():
    print("What would you like to do?\n\n1 - Search for a book\n2 - Loan a book\n3 - Return a loaned book\n4 - Add a book\n5 - Add a customer\n6 - Make a backup of the system\n7 - Restore the system from a backup\n8 - Quit the program")
    MainMenuChoice = input()
    if MainMenuChoice == "1":
        print("Mooi")
    elif MainMenuChoice == "5":
        NewCustomer()

def NewCustomer():
    print("\nPlease enter the user's number.")
    aNumber = input()
    print("\nPlease enter the user's gender.")
    aGender = input()
    print("\nPlease enter the user's nameset.")
    aNameSet = input()
    print("\nPlease enter the user's given name.")
    aGivenName = input()
    print("\nPlease enter the user's surname.")
    aSurname = input()
    print("\nPlease enter the user's street adress")
    aStreetAddress = input()
    print("\nPlease enter the user's zipcode")
    aZipCode = input()
    print("\nPlease enter the user's city")
    aCity = input()
    print("\nPlease enter the user's email address")
    aEmailAddress = input()
    print("\nPlease enter the user's username")
    aUsername = input()
    print("\nPlease enter the user's telephonenumber")
    aTelephoneNumber = input()
    newUser = AddCustomer(aNumber, aGender, aNameSet, aGivenName, aSurname, aStreetAddress, aZipCode, aCity, aEmailAddress, aUsername, aTelephoneNumber)



class AddCustomer():
    def __init__(self, Number, Gender, NameSet, GivenName, Surname, StreetAddress, ZipCode, City, EmailAddress, Username, TelephoneNumber):
        self.Number = Number
        self.Gender = Gender
        self.NameSet = NameSet
        self.GivenName = GivenName
        self.Surname = Surname
        self.StreetAddress = StreetAddress
        self.ZipCode = ZipCode
        self.City = City
        self.EmailAddress = EmailAddress
        self.Username = Username
        self.TelephoneNumber = TelephoneNumber


print("Welcome to the library system")
StartMenu()