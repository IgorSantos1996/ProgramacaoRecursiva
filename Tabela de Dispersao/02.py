'''
Outro exemplo de tabela de dispersão
'''

cache = {}

def pega_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados
        return dados

    