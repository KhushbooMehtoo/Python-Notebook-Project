# my to do....

class Todo:

    def __init__(self):
        self.id = ""
        self.note=""

    def start_with(self):
        print("Start with.\n 1.Create\n 2.Read \n 3.Update \n 4.Delete")

    def get_details(self):
        self.id = input("Enter the id: ")
        self.note = input("Enter notes here")

    def display_profile(self):
        print(f"\nUser Notes:")
        print(f"Id: {self.id}")
        print(f"Note: {self.note}")

        
    def start(self):
        
        select =int(input(" Enter frome (1-4): "))

        if select==1:
            print("Create Mode.")

        elif select==2:
            print("Read Mode.")
        
        elif select==3:
            print("Updated....")

        elif select==4:
            print("Deleted!")
        else:
            print("Invalid!.Select Again")

user1 = Todo()

user1.start_with()
user1.start()
user1.get_details()
user1.display_profile()