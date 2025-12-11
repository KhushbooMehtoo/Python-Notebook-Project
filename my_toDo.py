# my to do....
#import messages frome my_module
import my_modul
mes=my_modul.Messages() 
mes.display()  #obje of my_module
mes.start_with()
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
        print(mes.welcome_mesg['CREATE'])
        
        self.id = input("Create the id: ")
        if self.check_id():
           print(mes.display['ALREADY_EXIST'])
           self.create_mode()
        else:
           self.note = input("Enter notes: ")

           self.storage[self.id]=self.note
           print(mes.display['SAVED'])
           self.start()
        
    def read_mode(self):
        print(mes.welcome_mesg['READ'])

        print("1. Read Single Note")
        print("2. Read All Notes")

        choice = input("Choose (1/2): ")

        # ---- Read Single ----
        if choice == "1":
            id = input("Enter the id: ")
            if self.check_id(id):
                print(f"{id} : {self.storage[id]}")
            else:
                print(mes.display['NOT'])

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
        print(mes.welcome_mesg['UPDATE'])

        self.id = input("Enter the id: ")
        if self.check_id():
           self.note=input("Enter the New note: ")
           self.storage[self.id]=self.note
           print(mes.display['UPDATED'])
           self.start()

        else:
            print(mes.display['NOT'])
            print("Enter again")
            self.create_mode()
            
    def delete_mode(self):
        print(mes.welcome_mesg['DELETE'])

        self.id = input("Enter the id: ")
        if self.id in self.storage:
           del self.storage[self.id]
           print(mes.display['DELETED'])

        else:
            print(mes.display['NOT'])
            self.start()
   
    # Select operations...   
    def start(self):
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
