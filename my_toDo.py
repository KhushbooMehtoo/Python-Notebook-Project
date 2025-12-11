# my to do....

class Todo:
     
     #Dictionary
    def __init__(self):
          self.storage={
    
          }
    #Use for check ID is exist or not.

    def check_id(self):
        if self.id in self.storage:
            return True
        else:
            return False
        
    #CRUD Operations.....      
    def create_mode(self):
        print("[x]::::::::::CREATE MODE::::::::::[x]")
        
        self.id = input("Create the id: ")
        if self.check_id():
           print("ID is already exist")
           self.create_mode()
        else:
        #    self.id = input("Create the id: ")
           self.note = input("Enter notes: ")

           self.storage[self.id]=self.note
           print("Note saved successfully!")
           self.start()
        
    def read_mode(self):
        print("[x]::::::::::READ MODE::::::::::[x]")

        print("1. Read Single Note")
        print("2. Read All Notes")

        choice = input("Choose (1/2): ")

        # ---- Read Single ----
        if choice == "1":
            id = input("Enter the id: ")
            if self.check_id(id):
                print(f"{id} : {self.storage[id]}")
            else:
                print("ID does not exist!")

        # ---- Read All ----
        elif choice == "2":
            if not self.storage:
                print(" No notes available.")
            else:
                print("\nAll Notes:")
                print("------------------")
                print("| ID |   NOTE   |")
                print("------------------")
                for id, note in self.storage.items():
                    print(f"| {id} | {note} |")
                    print("------------------")

        else:
            print("Invalid choice!")

        self.start()
       

    def update_mode(self):
        print("[x]::::::::::UPDATE MODE::::::::::[x]")

        self.id = input("Enter the id: ")
        if self.check_id():
           self.note=input("Enter the New note: ")
           self.storage[self.id]=self.note
           print("Updated successfully!")
           self.start()

        else:
            print("ID does not exist")
            print("Enter again")
            self.create_mode()
            
    def delete_mode(self):
        print("[x]::::::::::DELETE MODE::::::::::[x]")

        self.id = input("Enter the id: ")
        if self.id in self.storage:
           del self.storage[self.id]
           print("Deleted successfully!")

        else:
            print("ID does not exist.")
            self.start()
   
    # Select operations...   
    def start(self):
        print("Start with.\n 1.Create\n 2.Read \n 3.Update \n 4.Delete")
        select =int(input(" Enter frome (1-4): "))

        if select==1:
            self.create_mode()

        elif select==2:
            self.read_mode()
        
        elif select==3:
            self.update_mode()

        elif select==4:
             self.delete_mode()

        else:
            print("Invalid!.Select Again")
            self.start() 

user1 = Todo()
print(user1.start())
