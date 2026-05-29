def criar_playlist(nome_playlist, *musicas):
    print (f"Nome:  {nome_playlist}")
    for i, musica in enumerate(musicas, start=1):
        print (f"Música: {i}: {musica}")
    
criar_playlist("Viagem SP", "Hotel California", "Boate Azul" , "Sinonimos")