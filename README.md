🟦 Pydantic

Pydantic is a Python library used for data validation and parsing using Python type hints. It is widely used in FastAPI, OpenAI Agents SDK, and other modern Python frameworks because it ensures data integrity and helps define schemas clearly.

🔹 Core Ideas

Validation at runtime → ensures inputs match type hints (e.g., int, str, List[str]).

Schema generation → can automatically generate JSON schemas for APIs.

Data coercion → if possible, converts input types (e.g., "123" → int(123)).

Error reporting → gives detailed validation errors when data doesn’t match.

🔹 Two main ways in exam scope
1. BaseModel

Most common Pydantic style.

Defines models with type hints and validations.

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

u = User(id="1", name="Faria", email="faria@example.com")
print(u.id)  # 1 (string auto-converted to int ✅)


Use Case: Input validation, API schemas, OpenAI Agents SDK tool output_type.

2. @pydantic.dataclasses.dataclass

A drop-in replacement for Python’s @dataclass.

Brings Pydantic validation into standard dataclasses.

from pydantic.dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float

item = Item(name="Shirt", price="499")
print(item.price)  # 499.0 (string → float ✅)


Key Difference DataClass vs BaseModel:

BaseModel = richer features (dict conversion, .model_dump(), .json()).

dataclass = lighter, feels more like native Python dataclasses.

🔹 In Agents SDK

You can use Pydantic models as output_type for structured responses.

class WeatherResponse(BaseModel):
    city: str
    temperature: float


If an agent tool has output_type=WeatherResponse, the model enforces correct structure.
✅ Summary

Pydantic = Data validation, schema, structured output (BaseModel vs dataclasses).

🟦 Type Hints for Validation & Schema Definition

Pydantic relies on Python type hints to:

Validate inputs at runtime.

Auto-generate schemas (useful in APIs and Agents SDK).

Example:

from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    name: str
    tags: List[str]

# Validation & coercion
p = Product(id="1", name="Shirt", tags=["clothing", 123])
print(p.id)     # 1 (string → int)
print(p.tags)   # ["clothing", "123"] (int → str)


✔ Schema auto-generated:

{
  "id": "integer",
  "name": "string",
  "tags": ["string"]
}

🟦 Using Dataclasses as output_type in Agents

In OpenAI Agents SDK, tools often return structured data.
You can use either BaseModel or Pydantic dataclasses for output_type.

Example with dataclass
from pydantic.dataclasses import dataclass
from openai import Agent

@dataclass
class WeatherResponse:
    city: str
    temperature: float

async def get_weather(city: str) -> WeatherResponse:
    return WeatherResponse(city=city, temperature=30.5)

agent = Agent(
    tools=[get_weather],
    output_type=WeatherResponse  # dataclass works!
)


✔ Benefits:

Natural Python style.

Still validated by Pydantic.

Useful if you prefer dataclass syntax over BaseModel.

✅ Quick Takeaways for Exam

Use BaseModel for richer validation, schema, and API modeling.

Use @pydantic.dataclasses.dataclass if you want lightweight dataclasses with validation.

Both can be used as output_type in Agents; BaseModel is stricter, dataclass is simpler.

🟦 3. Validation Errors

Agar data galat hai to error aayega:

try:
    u = User(id="abc", name="Faria", age="15")
except Exception as e:
    print(e)


Output:

1 validation error for User
id
  Input should be a valid integer

🟦 4. @pydantic.dataclasses.dataclass

Ye Python dataclass jaisa hi lagta hai, but validation ke sath.

from pydantic.dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

p = Product(name="Shirt", price="499")

print(p)            # Product(name='Shirt', price=499.0)
print(type(p.price)) # <class 'float'>


✔ "499" automatically float ban gaya.

🟦 5. Agents SDK me output_type

Agar tum agent bana rahe ho aur chahti ho structured response aaye, to output_type use karte hain.

from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temperature: float

# Ye function tool banega
def get_weather(city: str) -> WeatherResponse:
    return WeatherResponse(city=city, temperature=29.5)

print(get_weather("Karachi"))
# city='Karachi' temperature=29.5


✅ Summary

BaseModel = heavy features, schema, API, .json()

dataclass = light, pythonic, sirf validation

Dono ko Agents SDK me output_type me use kar sakte ho.

🔹 model_dump() kya hai?

model_dump() → Pydantic ka method jo instance ko Python dict banata hai.
(Yani JSON style data, APIs ke liye useful)

print(u.model_dump())


Output:

{'name': 'John', 'age': '30', 'exam_date': 20240615}


⚡ Why useful?

API banate waqt hum data ko JSON/dict format me bhejte hain.

Ye ensure karta hai ke data type safe aur clean hai.

🟦 Quick Difference

u → ek object hai (class instance).

u.model_dump() → ek dict hai (object ka clean data version).

✅ Summary

Conversion (coercion): "30" string ko int banane ki koshish karta hai agar field int ho.

Tumhare code me: age ko tumne str define kiya, isliye wo string hi raha.

model_dump(): Object ko dict me convert karta hai, JSON banane ke liye perfect.