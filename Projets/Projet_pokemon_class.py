class Pokemon:
    def __init__(self,name,pv,type):
        self.name=name
        self.pv=pv
        self.type=type
    def KO(self):
        if self.pv<=0:
            return f"{self.name} est"

