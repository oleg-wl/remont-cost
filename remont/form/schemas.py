import datetime
from pydantic import BaseModel, Field

class PurchaseValidation(BaseModel):
    type_id: int 
    info: str
    date: str = Field(pattern=(r"\d{4}-\d{2}-\d{2}"))
    amount: float