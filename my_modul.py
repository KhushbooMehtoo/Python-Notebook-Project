#my Module for My-noteBook
class Messages:
    def  __init__(self):
        self.welcome_mesg={
            'CREATE':"[x]::::::::::CREATE MODE::::::::::[x]",
            'READ':"[x]::::::::::READ MODE::::::::::[x]",
            'UPDATE':"[x]::::::::::UPDATE MODE::::::::::[x]",
            'DELETE':"[x]::::::::::DELETE MODE::::::::::[x]"
        }
    def display(self):
        self.display={
            'UPDATED':"Updated successfully!",
            'DELETED':"Deleted successfully!",
            'NOT':"ID does not exist!"
        }
    


