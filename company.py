
class Company():
    def __init__(self, value, type):
        self.value=value
        self.type=type
        self.ownership=[0,0]

    def return_value(self):
        return self.value
