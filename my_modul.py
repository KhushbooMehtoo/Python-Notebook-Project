#my Module for My-noteBook
from yachalk import chalk

class Messages:
    def  __init__(self):
        #Welcomming Messages...
        self.welcome_mesg={
            'CREATE':chalk.rgb(140, 82, 255)("[x]::::::::::CREATE MODE::::::::::[x]"),
            'READ':chalk.rgb(140, 82, 255)("[x]::::::::::READ MODE::::::::::[x]"),
            'UPDATE':chalk.rgb(140, 82, 255)("[x]::::::::::UPDATE MODE::::::::::[x]"),
            'DELETE':chalk.rgb(140, 82, 255)("[x]::::::::::DELETE MODE::::::::::[x]")
        }

        #Display updates messages....
    def display(self):
        self.display={
            'SAVED':chalk.green("Note saved successfully!"),
            'UPDATED':chalk.green("Updated successfully!"),
            'DELETED':chalk.red("Deleted successfully!"),
            'NOT':chalk.red("ID does not exist!"),
            'ALREADY_EXIST':chalk.red("ID is already exist")
        }

        #Start Notes with......
    def start_with(self):
        print(chalk.rgb(255, 105, 180)("Start with.\n 1.Create\n 2.Read \n 3.Update \n 4.Delete"))

    


