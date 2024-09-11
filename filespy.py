from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


# создаём модель данных, которая обычно расположена в файле models.py
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []

# Внешние данные, имитирует входящий JSON
external_data = {
    "id": "124",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
# имитируем распаковку входящих данных в коде приложения
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)