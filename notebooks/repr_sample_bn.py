# %%
from pydantic import BaseModel, Field

def my__repr__(self) -> str:
    return f'{self.name} --> {self.age}'

class MyModel(BaseModel):
    name: str = Field(..., description="name")
    age: int


class MyClass:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    __repr__ = my__repr__




class MyDataClass:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    name: str
    age: int
    __str__ = my__repr__


# %%

o = MyModel(name='kuku', age=120)

print(o)

c = MyClass(name='kuku', age=120)
print(c)


d= MyDataClass(name='kuku', age=120)
print(d)
