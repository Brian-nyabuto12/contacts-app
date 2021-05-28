from contact import Contact

def main():
     
    print("hello welcome to yellow pages")
    print("what is your Name?") 

    user_input = input()

    print(f"welcome to yellow pages friend {user_input}.")

    print("type in 1 to save new contact,or 2 to view all contact or type 3 to delete")
    choice = input()

    while True:
        if choice == 1:
            print("enter new contact")
        elif choice == 2:
            print("view all contact")
        elif choice == 3:
            print("delete contact")  
        else:
            print("sorry dont understand your choice")          
             
if __name__ == "__main__":
    main()