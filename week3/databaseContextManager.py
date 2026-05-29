class DatabaseConnection:
    def __enter__(self):
        print("Database Connection Opened")
        return self
    
    def __exit__(self, exc_type, exc, tb):

        if exc_type:
            print(f"Exception Occured :{exc}")
        
        print("Database Connection Closed")
        return True

    def execute_query(self,query):
        print(query)


class FileHandler:
    
    def __init__(self,file_name):
        self.file_name=file_name


    def __enter__(self):
        print("Opening File Stram")
        self.file=open(self.file_name,"r")
        return self.file
    
    def __exit__(self, exc_type, exc, tb):
        self.file.close()

        print("File Stream Closed")

        if exc_type:
            print(f"Exception Occured {exc}")



with FileHandler("recoveryCode.txt") as file:
    print(file.readline())

with DatabaseConnection() as db :
    db.execute_query("Select * from users")
    10/0



class Transaction:
    def __enter__(self):
        print("Transaction Started")
        return self
    
    def commit(self):
        self.isCommited=True
        print("Transactions Commited")

    def rollback(self):
        print("Transactions Roll backed")
    
    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            print(f"Exception Occured {exc}")
            self.rollback()
            return True
        else :
            self.commit()
        

with Transaction() as tx:
    print("Updating balance")

with Transaction() as tx:
    print("Updating balance")
    10/0