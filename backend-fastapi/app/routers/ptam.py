from fastapi import APIRouter, Response
from jinja2 import Template
from weasyprint import HTML

router = APIRouter()

PTAM_HTML_PATH = "templates/ptam.html"

@router.get("/{ptam_id}/pdf")
def get_ptam_pdf(ptam_id: str):
    # Demo context (em produção, busque do DB pelo ptam_id)
    context = {
        "avaliador_nome": "Heitor Reis Leite Filho",
        "avaliador_creci": "11357-MA",
        "data_emissao": "2025-11-03",
        "imovel_titulo": "Apto 2Q no Turu",
        "imovel_endereco_completo": "Rua X, 123 - Turu, São Luís - MA",
        "valor_avaliacao": "215.000,00",
        "faixa_min": "205.000,00",
        "faixa_max": "225.000,00",
        "data_referencia": "2025-11-03",
        "imovel_tipo": "Apartamento",
        "area_m2": "62,5",
        "quartos": 2,
        "banheiros": 1,
        "vagas": 1,
        "estado_conservacao": "Bom",
        "posicao": "Nascente",
        "matricula": "—",
        "observacoes_metodologia": "Amostra de 3 comparáveis em raio de 1km; ajustes por área e conservação.",
        "comps": [
            {"address":"Rua Y, 456, Turu","distance_m":850,"area_m2":60,"price":"210.000,00","ajustes_percent":"(+3%)","preco_ajustado":"216.300,00","peso":"0,35"},
            {"address":"Av. Z, 100, Turu","distance_m":1200,"area_m2":64,"price":"220.000,00","ajustes_percent":"(-1%)","preco_ajustado":"217.800,00","peso":"0,40"},
            {"address":"Rua W, 30, Turu","distance_m":600,"area_m2":61,"price":"208.000,00","ajustes_percent":"(+2%)","preco_ajustado":"212.160,00","peso":"0,25"}
        ],
        "fotos": []
    }
    with open(PTAM_HTML_PATH, "r", encoding="utf-8") as f:
        tpl = Template(f.read())
    html = tpl.render(**context)
    pdf_bytes = HTML(string=html).write_pdf()
    return Response(content=pdf_bytes, media_type="application/pdf")
