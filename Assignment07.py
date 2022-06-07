# ------------------------------------------------- #
# Title: Assignment07
# Description: Using the pickle module and try/except.
# ChangeLog: (Who, When, What)
# Timothy McDowell, 6.1.2022, Created Script
# ------------------------------------------------- #

# import the new module to use in script
import pickle
message = []

# function for reading the pickle file
def read_pickle(file):
    file_obj = open(file, "rb")
    data_obj = pickle.load(file_obj)
    file_obj.close()
    return data_obj
    
# funtion for writing to the pickle file
def write_pickle(file, data):
    file_obj = open(file, "wb")
    pickle.dump(data, file_obj)
    file_obj.close()

# Option menu with try/except handling 
while True:
    print(
            "\n\nWhat's your choise?\n\n",
            "1. Read file\n",
            "2. Write to file\n",
            "3. Exit program\n"  
        )
    option = int(input("Enter number: "))
    
    if option == 1:
            
        read_file = input("What is the file to read? \n")
                
        try:
            print("\n\n///////////////YOUR SECRET MESSAGE IS///////////////////")
            print(read_pickle(read_file))
            print("////////////////////////////////////////////////////////")
                  
        except:
            print("That data is not available, pick another file\n\n")
            
    if option == 2:
        write_file = input("What's the name of your file? ")
        try:
            data = input("What's your message? ")
        except EOFError:
            message.append(data)
            write_pickle(write_file, message)
            break
        
    if option == 3:
        print("Goodbye")
        break
        
        