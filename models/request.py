from pydantic import BaseModel


class LemmatizeTextRequest(BaseModel):
    text: str
