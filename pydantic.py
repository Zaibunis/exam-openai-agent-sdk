from pydantic import BaseModel, Field, ValidationError, field_validator, StrictInt
from pydantic.dataclasses import dataclass
from pydantic_settings import BaseSettings
from pydantic import TypeAdapter
from datetime import datetime


#🔹 model_dump() kya hai?

#model_dump() → Pydantic ka method jo instance ko Python dict banata hai.
#(Yani JSON style data, APIs ke liye useful)
#print(u.model_dump())

class User(BaseModel):
    name:str
    age:int
    exam_date:int

u = User(name="John", age="30", exam_date=20240615)
print(u.exam_date, u , type(u.exam_date))
print(u.model_dump())


class User(BaseModel):
     id: int 
     name: str

user = User(id="123", name="Ali") 
print(user)

#⚙️ Installation

#👉 Pehle Pydantic install karo:

#pip install pydantic

#Agar tum environment variables (settings) use karna chahte ho:

#pip install pydantic-settings

#🏗️ Models

#👉 A Model ek Python class hoti hai jo BaseModel inherit karti hai. Isme tum fields define karte ho (like id, name), aur Pydantic automatically data validate karta hai.

class User(BaseModel): 
    id: int 
    name: str 
    signup_ts: datetime | None = None

data = {"id": "123", "name": "Ali", "signup_ts": "2024-01-01 10:30"} 
user = User(**data)
print(user)

#🎯 Fields

#👉 Field() ka use hota hai rules set karne ke liye. Jaise min/max length, min/max numbers, default values, etc.

class User(BaseModel): 
    username: str = Field(..., min_length=3, max_length=20) 
    age: int = Field(..., ge=18, le=100)

u = User(username="Ali123", age=25)

#❌ Validation Errors

#👉 Agar data galat ho, Pydantic detailed error deta hai jisme batata hai:

#Kis field me error hai

#Kis type ki problem hai

class User(BaseModel): 
    id: int 
    name: str

try: User(id="abc", name=123) 
except ValidationError as e: 
    print(e.errors())

#🛠️ Custom Validators

#👉 Tum apne khud ke rules bana sakte ho using @field_validator.

class User(BaseModel): 
    name: str 
    age: int

@field_validator("age")
def check_age(cls, value):
    if value < 18:
        raise ValueError("User must be 18+")
    return value
u = User(name="Ali", age=20) 

#📤 Serialization

#👉 Models ko dict ya JSON string me convert karna easy hai.

class User(BaseModel): 
    id: int 
    name: str

u = User(id=1, name="Ali")

print(u.model_dump()) # dict print(u.model_dump_json()) # JSON string

#🔒 Strict vs Lax Mode

#👉 Default (lax) mode me "123" → 123 convert ho jata hai. Strict mode me ye allowed nahi hota.

class Model(BaseModel): 
    x: StrictInt

Model(x=123) # ✅ Model(x="123") # ❌ Error

#🏷️ Aliases

#👉 JSON keys aur Python attributes different ho sakte hain. alias use karke unhe map kar sakte ho.

class User(BaseModel): 
    full_name: str = Field(..., alias="fullName")

data = {"fullName": "Ali Khan"} 
u = User(**data)

print(u.full_name) # Ali Khan

#⚡ Settings Management

#👉 BaseSettings environment variables ko handle karta hai easily

class Settings(BaseSettings): 
    database_url: str 
    debug: bool = False

s = Settings() # Reads from env vars print(s.database_url)

#📦 Dataclasses

#👉 Normal Python @dataclass ko validation powers milti hain Pydantic ke sath.

@dataclass 
class Item: 
 id: int 
 name: str

i = Item(id="123", name="Coffee") 
print(i) # id=123 name='Coffee'

#📑 JSON Schema

#👉 Tumhara model ka schema automatically ban jata hai.

class User(BaseModel): 
    id: int 
    name: str

print(User.model_json_schema())

#🎯 TypeAdapter

#👉 Chhoti cheeze validate karni ho (jaise list[int]) to model banane ki zaroorat nahi.

ta = TypeAdapter(list[int]) 
print(ta.validate_python(["1", 2, 3]))

