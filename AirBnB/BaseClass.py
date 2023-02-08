from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        """
        Constructor Method
        """
        id = uuid4()
        created_at = datetime.today()
        updated_at = 0

    def save(self):
        """
        Saving Method
        """
        updated_at = datetime.today()
        

    def to_dict(self):
        """
        Method to return a dictionary contall key/values of __dict__ of the instance
        """

if __name__ == '__main__':
    model1 = BaseModel(1)
    print(model1.id)