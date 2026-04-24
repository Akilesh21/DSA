class NegativeZeroModelYear(Exception):
    def __init__(self,value,message="Model year cannot be equal or greater than 2021"):
        self.value=value
        self.message=message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message}-->{self.value}'
class CarModeYearAsString(Exception):
    #Exception if the car value comes as negative
    def __init__(self,value,message="Model year can not be strings.Try Passing int values"):
        self.value=value
        self.message=message
        super().init__(self.message)
    def __str__(self):
        return f'{self.message}-->{self.value}'

class Vehicle():
    def __init__(self,make,model,fuel):
        self.make=make
        self.model=model
        self.fuel=fuel
        self.current_year=2021
        self.value=None
    def get_value(self):
        try:
            if type(self.model)==str:
                status="custom"
                raise CarModeYearAsString(self.model)
            elif self.model>=self.current_year:
                status="custom"
                raise NegativeZeroModelYear(self.model)
            else:
                self.age=self.current_year-self.model
                self.value=1000*(1/self.age)
                status="success"
        except TypeError:
            self.age=self.current_year-int(self.model)
            self.value=1000*(1/self.age)
            status="inbuilt"
        else:
            print("code ran without any exceptions")
        finally:
            if status=="custom":
                print("code has inbuilt exceptions")
            elif status=="inbuilt":
                print("code has inbuilt exceptions,please rectify that")
            else:
                print("The value without any exception",self.value)

myobj=Vehicle("Tesla",2019,"electric")
myobj.get_value()