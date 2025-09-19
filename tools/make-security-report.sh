#!/usr/bin/env bash
set -euo pipefail
OUT="security-report.md"
echo "# Relatório SAST/DAST/SCA – InvestSmart" > "$OUT"
echo "" >> "$OUT"
echo "**Data:** $(date -u +"%Y-%m-%d %H:%M UTC")" >> "$OUT"
echo "" >> "$OUT"
[ -f semgrep-results.json ] && echo "## Semgrep\n- Ver o arquivo semgrep-results.json" >> "$OUT"
[ -f pip-audit.json ] && echo "## SCA (pip-audit)\n- Ver pip-audit.json" >> "$OUT"
[ -f zap-baseline-report.html ] && echo "## DAST (ZAP/Nikto)\n- Ver zap-baseline-report.html, nikto.txt e security-evidence.md" >> "$OUT"
echo "\n## SLA de correção\n- Crítico: 24h\n- Alto: 3 dias\n- Médio: 2 semanas\n- Baixo: backlog" >> "$OUT"
