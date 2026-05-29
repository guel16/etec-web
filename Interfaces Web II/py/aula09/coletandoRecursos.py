inventario = 0
meta = 64 

while inventario < meta:
    coletado = 8 # 8 blocos por mineração
    inventario += coletado
    print (f"Coloetados +{coletado} blocos. Inventario: {inventario}")

    print(f"Stack completo! Total: {inventario} blocos")