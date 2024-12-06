from pydantic import BaseModel

class TextLemmatizationResponse(BaseModel):
    result: str
