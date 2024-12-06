from pydantic import BaseModel


class TextLemmatizationResponse(BaseModel):
    result: list[str]
