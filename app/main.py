from fastapi import FastAPI, HTTPException
from .schemas import UserProfile, PortfolioRecommendation
from .recommend import build_portfolio
from .utils import anonymize_email

app = FastAPI(title="InvestSmart API (demo segurança)", version="0.2.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/profile/recommend", response_model=PortfolioRecommendation)
def recommend_portfolio(profile: UserProfile, email: str | None = None):
    if email and "@" not in email:
        raise HTTPException(status_code=422, detail="email inválido")
    _uid = anonymize_email(email) if email else "anon"
    return build_portfolio(profile)
