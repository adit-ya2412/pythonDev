class DailyLimitExceededError(Exception):
    def __init__(self, message="Daily Limit Exceeded, Amount must be less than or equal to 50K"):
        self.message=message
        super().__init__(self.message)
    
    def __str__(self):
        return f"Error in operation {self.message}"
class InsufficientBalanceError(Exception):
    def __init__(self, message="Insufficient Balance"):
      self.message=message
      super().__init__(self.message)

    def __str__(self):
        return f"Error in operation {self.message}"

class InvalidAmountError(Exception):
    def __init__(self, message="Invalid Amunt ,must be greater than 0 "):
        self.message=message
        super().__init__(self.message)
    def __str__(self):
        return f"Error in operation {self.message}"