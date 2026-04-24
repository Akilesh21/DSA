class intro:
    """introduction of classes and objects"""
    def __init__(self,date,time,name):
        self.date = date
        self.time = time
        self.name = name
obj = intro(input(),float(input()),input()) 
print(obj.date)       
print(obj.time)
print(obj.name)