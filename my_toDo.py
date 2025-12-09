# my to do....


class Todo:
     
    def __init__(self):
          self.storage={
               1:"khush",
               2:"atul"
          }

    def check_id(self):
        if self.id in self.storage:
            return True
        else:
            return False
          
    def create_mode(self):
        print("[x]::::::::::CREATE MODE::::::::::[x]")
        self.id = input("Create the id: ")
        self.note = input("Enter notes: ")

        self.storage[self.id]=self.note
        print("Note saved successfully!")
        self.start()
        
    def read_mode(self):
        print("[x]::::::::::READ MODE::::::::::[x]")
        self.id = input("Enter the id: ")   

        if self.check_id():
           print(self.storage[self.id])
           self.start()

        else:
            print("ID does not exist")

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
            self.create_mode()


    def delete_mode(self):
        print("[x]::::::::::DELETE MODE::::::::::[x]")
        self.id = input("Enter the id: ")

        if self.id in self.storage:
           del self.storage[self.id]

           print("Deleted successfully!")
           self.start()

        else:
            print("ID does not exist.")
   
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
