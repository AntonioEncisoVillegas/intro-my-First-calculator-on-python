# description
""" 
PyCalc: simple calculator
Author: Antonio Encio Villegas
Date: June 2021 
Functionality :
      -symple mathematical operations (sum,substraction,multiplication,division)
"""
# imports

# globals

# function 
def print_menu():
    print("---------------------")
    print(" Welcome to PyCalc")
    print("---------------------")

    print("1 - sum")
    print("2 - substract ")
    print("3 - multiplication ")
    print("4 - Division ")
    print("5 - is it odd  ")
    print("6 - print a message N times")
    
    print("q - Quit")
    print("---------------------")

def clear():
    print("\n\n\n\n\n")

# instructions 
selected_option = ""
while(selected_option != "q"):
     clear()
     print_menu()
 
     selected_option = input("Select an option: ")

     
     num1 = float(input (" Provide num1 "))
     num2 = float(input (" Provide num2 "))
     text =  str (input (" Say something ") )


     if(selected_option == "1"):
         res = num1 + num2
         print(f"The result is: {res}")

     elif(selected_option == "2"):
          res = num1 - num2
          print(f"The result is: {res}") 

     elif(selected_option == "3"):
          res = num1 * num2
          print(f"The result is: {res}") 

     elif(selected_option == "4"):
         if(num2 == 0 ):
            print(" Error : Dividion by zero is not allowed ")
         else: 
            res = num1 / num2
            print(f"The result is: {res}") 

     elif(selected_option == "5" ):
         if(num1 + num2  % 2) == 0:
             print(f" is Even number  {num1}  ")
         else:
             print(f" id Odd :  {num2}")
             
     elif(selected_option == "6" ):
         a_string = " Thanks for using my super calculator " * 5
         
         print(a_string)
         
  




     input("n\Press Enter to continue...")

print ("Good byte!!")

    
    
