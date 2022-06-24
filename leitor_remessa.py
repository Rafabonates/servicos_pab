"""
Este programa abre remessas do TRF 3a Região em formato ZIP e devolve os dados em formato de
tabela para inclusão no controle

Criado por Rafael em 05/06/2022
v.0.0.1

"""
import os
import ipywidgets as widgets

from funcoes import read_files
from funcoes import list_data
dados = read_files('09072020-RPPR.zip')
assert isinstance(dados, object)
# print(dados)
list_data(dados)

# TODO alterar formatação das colunas

# TODO Criar interface gráfica

# TODO subir no servidor da rede (voila)

