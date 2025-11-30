class Student:
    def __init__(self,name,marks):
        self._name=name
        self._marks=marks

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,str):
        self._name=str

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self,lista):
        self._marks=lista

    def is_passed(self):
        sum=0
        for value in self._marks:
            sum+=value
        if sum/len(self._marks)>50:
            return True
        else:
            return False
    
Arek = Student("Arek",[100,60])
Maciek = Student("Maciek",[40,20])

print(Arek.is_passed())
print(Maciek.is_passed())

