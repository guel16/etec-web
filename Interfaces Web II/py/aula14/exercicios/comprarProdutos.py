def avaliar_produtos(**kwargs):
    notas= list(kwargs.notas())
    minimo = (min.notas())
    media = (len.notas())
    maximo = (max.notas())

minimo, media, maximo = avaliar_produtos(
    qualidade=9, preco=6, entrega=8, embalagem=7
)
print(minimo, media, maximo)