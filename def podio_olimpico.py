def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
    # Implemente aqui a lógica da função
    i = 1
    podio = ''
    list2 = []
    if tempo_chegada1 > tempo_chegada2:
        if tempo_chegada1 > tempo_chegada3:
            if tempo_chegada3 > tempo_chegada2:
                list2 = [nome_corredor2, nome_corredor3, nome_corredor1]
            else:

                list2 = [nome_corredor3, nome_corredor2, nome_corredor1]
        else:
            list2 = [nome_corredor2, nome_corredor1, nome_corredor3]
    else:
        if tempo_chegada2 < tempo_chegada3:
            list2 = [nome_corredor1, nome_corredor2, nome_corredor3]
        elif tempo_chegada3 > tempo_chegada1:
            list2 = [nome_corredor1, nome_corredor3, nome_corredor2]
        else:
            list2 = [nome_corredor3, nome_corredor1, nome_corredor2]
    list = [tempo_chegada1, tempo_chegada2, tempo_chegada3]
    list = sorted(list)
    while i != 4: 
        podio += f'{i} - {list2[i-1]} - {list[i-1]} minutos\n'
        i += 1
    return podio
    

tempo_chegada1 = 3
tempo_chegada2 = 2
tempo_chegada3 = 1
nome_corredor1 = 'a'
nome_corredor2 = 'b'
nome_corredor3 = 'c'
print(podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3))