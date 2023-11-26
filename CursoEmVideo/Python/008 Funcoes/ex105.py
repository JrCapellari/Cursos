def notas(*n, sit=False):
    d = dict()
    d['Total'] = len(n)
    d['Maior'] = max(n)
    d['Menor'] = min(n)
    d['Media'] = sum(n) / len(n)
    if sit:
        if d['Media'] >= 7:
            d['Status'] = 'BOM'
        elif d['Media'] >= 5:
            d['Status'] = 'RAZOÁVEL'
        else:
            d['Status'] = 'RUIM'

    return d


# PROGRAMA PRINCIPAL
resp = notas(5, 8.2, 2.8, 7, 9.1, sit=True)
print(resp)
