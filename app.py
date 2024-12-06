from fastapi import FastAPI
from models.request import LemmatizeTextRequest
from models.response import TextLemmatizationResponse
from services.lemmatizer import lemmatize_text

app = FastAPI(debug=True)


@app.post("/api/lemmatize", response_model=TextLemmatizationResponse)
async def lemmatize(request: LemmatizeTextRequest):
    result = lemmatize_text(request.text)
    return TextLemmatizationResponse(result=result)
