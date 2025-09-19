#!/usr/bin/env python3
import json
import pathlib

ZAP_JSON = pathlib.Path("zap.json")
OUT_MD = pathlib.Path("security-evidence.md")

items: list[str] = []

if ZAP_JSON.exists():
    try:
        data = json.loads(ZAP_JSON.read_text(encoding="utf-8"))

        # O ZAP pode usar "site" (obj ou lista) ou "sites"
        sites = data.get("site") or data.get("sites") or []
        if isinstance(sites, dict):
            sites = [sites]

        for site in sites:
            for a in site.get("alerts", []):
                name = a.get("alert", "Alerta")
                risk = a.get("riskcode", "?")
                evid = []
                for inst in a.get("instances", []):
                    uri = inst.get("uri")
                    ev = inst.get("evidence")
                    if uri or ev:
                        evid.append(f"- URI: {uri or '-'}; Evidence: {ev or '-'}")
                if evid:
                    items.append(f"### {name} (risk {risk})\n" + "\n".join(evid))
    except Exception as e:
        items.append(f"_Erro lendo zap.json: {e}_")
else:
    items.append("_zap.json não encontrado (ZAP provavelmente não gerou JSON)._")

MITIG = """\
## Mitigações sugeridas
- Validar/normalizar entradas do usuário.
- Autenticação forte e RBAC em endpoints críticos.
- HTTPS + security headers (CSP, HSTS, X-Content-Type-Options).
- Queries parametrizadas/ORM (evitar injeção).
- Remover dados sensíveis de respostas e aplicar rate limiting.
"""

OUT_MD.write_text("# Evidências DAST (ZAP)\n\n" + "\n\n".join(items) + "\n\n" + MITIG, encoding="utf-8")
print(f"Escrito {OUT_MD}")
