from pydantic import BaseModel, ConfigDict
from typing import Optional

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool = True

class ItemCreate(ItemBase):
    pass

class ItemDB(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
