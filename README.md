# InvestSmart (demo) — Segurança em CI/CD

Projeto demo em **FastAPI** que recomenda uma carteira simples. Inclui pipeline **SAST + DAST + SCA** com *gates* de deploy.

## Rodar local
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest
```

## Endpoints
- `GET /health`
- `POST /profile/recommend`

Exemplo de request:
```json
{"age":30,"risk_tolerance":"moderado","liquidity_available":5000,"goals":{"curto":6,"medio":24,"longo":60}}
```

## CI/CD – o que está incluso
- **SAST**: Semgrep (OWASP Top 10, Python, secrets) → artefatos `.sarif` e `.json`.
- **SCA**: pip-audit (CVE) + pip-licenses (licenças) → `pip-audit.json`/`.sarif`, `licenses.csv`.
- **DAST**: ZAP baseline + Nikto contra app rodando em staging local → `zap-baseline-report.html`, `zap.json`, `nikto.txt`, `security-evidence.md` (payloads + mitigações).
- **Deploy simulado**: só executa se SAST/SCA/DAST passarem.

## Como usar (GitHub)
1. Crie um repositório vazio e faça push deste projeto (branch `main`).
2. Abra um Pull Request para ver anotações via SARIF (opcional).
3. Baixe os relatórios em **Actions → Artifacts**.

## Mapeamento com o pedido do professor
- **T1 SAST** ✔︎ Semgrep no CI com relatórios e severidade.
- **T2 DAST** ✔︎ ZAP + Nikto, artefatos e `security-evidence.md` com *payloads*.
- **T3 SCA** ✔︎ pip-audit (CVE) + licenças.
- **T4 Integração/Monitoramento** ✔︎ gatilhos por push/PR, *gates* de deploy e documentação.
