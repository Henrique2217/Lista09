def ober_resultados_vendas(vendedores : dict) -> dict:
    media = sum(vendedores.values()) / len(vendedores)
    meida_75 = media * 0.75


