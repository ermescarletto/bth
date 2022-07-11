from lib2to3.pgen2 import token
import requests
import json

#Variáveis iniciais



def get_logradouro():

    inicio = 1
    qtregistros = 99
    mais_paginas = True
    token_entidade = "236dc420-6dec-4859-a83a-24bef725487e"
    conta_registros = 0 
    lote = 0
    #Parametros da requisição

    url = "https://e-gov.betha.com.br/glb/service-layer/v2/api/logradouros/"
    querystring = {"iniciaEm": inicio,"nRegistros": qtregistros}
    payload = ""
    headers = {"Authorization": "Bearer "+ token_entidade}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)


    logradouros_json = json.loads(response.text)

    mais_paginas = logradouros_json['maisPaginas']
    print("Possui mais registros?:" + str(logradouros_json['maisPaginas']))
    print("Quantidade de registros retornados no lote:" + str(len(logradouros_json['conteudo'])))


    while mais_paginas:
        lote += 1
        querystring = {"iniciaEm": inicio,"nRegistros": qtregistros}
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        logradouros_json = json.loads(response.text)
        print("Lote = " + str(lote))
        print("Registros = " + str(conta_registros))
        print("Possui mais registros?:" + str(logradouros_json['maisPaginas']))
        print("Quantidade de registros retornados no lote:" + str(len(logradouros_json['conteudo'])))
        for logradouro in logradouros_json['conteudo']:
            logradouros = open('logradouros.json', 'a', encoding='utf-8')
            logradouros.write(str(logradouro).replace("'",'"'))
            logradouros.write('\n')          
            inicio = logradouro['idGerado']['iLogradouros']
            logradouros.close
            conta_registros += 1

        mais_paginas = logradouros_json['maisPaginas']
        
        
get_logradouro()












