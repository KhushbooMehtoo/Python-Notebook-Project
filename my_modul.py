#my Module for My-noteBook
from yachalk import chalk

class Messages:
    def  __init__(self):
        #Welcomming Messages...
        self.welcome_mesg={
            'CREATE':"[x]::::::::::CREATE MODE::::::::::[x]",
            'READ':"[x]::::::::::READ MODE::::::::::[x]",
            'UPDATE':"[x]::::::::::UPDATE MODE::::::::::[x]",
            'DELETE':"[x]::::::::::DELETE MODE::::::::::[x]"
        }

        #Display updates messages....
    def display(self):
        self.display={
            'SAVED':"Note saved successfully!",
            'UPDATED':"Updated successfully!",
            'DELETED':"Deleted successfully!",
            'NOT':"ID does not exist!",
            'ALREADY_EXIST':"ID is already exist"
        }

        #Start Notes with......
    def start_with(self):
        print(chalk.magenta("Start with.\n 1.Create\n 2.Read \n 3.Update \n 4.Delete"))

    


