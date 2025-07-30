# A Form class that uses a nested Validator with a @staticmethod

class Form:
    def __init__(self,data):
        self.data = data

    def is_valid(self):
        return self.Validator.validate(self.data)

    class Validator:
        @staticmethod
        def validate(data):
            return bool(data and isinstance(data,dict) and "name" in data)
        
data1 = {"name": "John"}
data2 = {"age": 30}

print(Form.Validator.validate(data1))
print(Form.Validator.validate(data2))
