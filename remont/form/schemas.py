import datetime
from pydantic import BaseModel, Field, field_validator

class PurchaseValidation(BaseModel):
    
    type_id: int 
    info: str
    date: str = Field(pattern=(r"\d{4}-\d{2}-\d{2}"))
    amount: float

    @field_validator('amount')
    def positive_amount(cls, value):
        if value < 0:
            raise ValueError('Сумма должна быть положительной')

        return value

    @field_validator('info')
    def notnull_info(cls, value):
        if len(value) <= 0:
            raise ValueError('Поле инфо не должно быть пустым')

        return value