"""
Este programa abre remessas do TRF 3a Região em formato ZIP e devolve os dados em formato de
tabela para inclusão no controle

Criado por Rafael em 05/06/2022
v.0.0.1

"""

from funcoes import list_data
from funcoes import read_files

from tkinter.filedialog import askopenfilename, Tk

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

dados = read_files(filename)
assert isinstance(dados, object)
# print(dados)
list_data(dados)



#import plyer
#arquivo = plyer.filechooser()
#print(arquivo)

# TODO alterar formatação das colunas

# TODO Criar interface gráfica

# TODO subir no servidor da rede (voila)

