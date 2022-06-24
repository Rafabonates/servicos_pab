"""
Created on 05/06/2022

@author Rafael
"""

import zipfile
import os, shutil
# import pandas as pd
from pdfminer.high_level import extract_text
from leitorPDF import dadosOficio
import random
from typing import Optional
from rich.table import Table
from rich.console import Console


def extract_files(remessa, endereco):  # extrai os arquivos da remessa zipada
    with zipfile.ZipFile(remessa, 'r') as zip_ref:
        zip_ref.extractall("{0}/extraction".format(endereco + '/..'))


def get_data(oficio):  # extrai os dados de PDFs
    assert isinstance(oficio, object)
    conteudo = extract_text(oficio)
    # print(conteudo)
    return conteudo


def read_files(remessa):  # itera os arquivos extraidos e retorna uma lista com os dados
    dados = []
    numero = 1
    endereco = os.path.abspath(remessa)
    extract_files(remessa, endereco)
    enderecooficios = os.path.abspath(remessa + '/..') + '/extraction'
    for oficio in range(1, len(os.listdir(enderecooficios))):
        # print(range(len(os.listdir(enderecooficios))))
        # print(oficio)
        # if not oficio.endswith(".pdf"):
        #    continue
        # print(os.path.abspath(oficio))
        # numero = random.randint(1, 2000)
        oficionovo = (str(numero) + '.pdf')
        # print(oficionovo)
        # os.rename((enderecooficios + '/' + oficio), (enderecooficios + '/' + oficionovo))
        # conteudo = get_data(enderecooficios + '/' + oficionovo)
        # print(conteudo)
        oficiolido = os.listdir(enderecooficios)[oficio]
        if not oficiolido.endswith(".pdf"):
            continue
        # print(oficiolido)
        os.rename((enderecooficios + '/' + oficiolido), (enderecooficios + '/' + oficionovo))
        # conteudo = get_data(enderecooficios + '/' + oficionovo)
        conteudo = get_data(enderecooficios + '/' + oficionovo)
        dados.append(dadosOficio(conteudo, remessa))
        numero =+ 1

    try:
        shutil.rmtree(enderecooficios)
    except PermissionError:
        print(enderecooficios)

    return dados



def list_data(dados, style: Optional[str] = None):
    """Lists beers in database"""
    table = Table(title="Remessa TRF")
    headers = ["oficio", "data", "data_remessa", "remessa", "meio", "Tribunal", "orgao", "conta", "nome"]
    for header in headers:
        table.add_column(header, style="magenta", no_wrap=True, min_width=10)
    for linha in dados:
        table.add_row(*linha)
        # linha.date = linha.date.strftime("%Y-%m-%d")
        # values = [str(getattr(linha, header)) for header in headers]
        # table.add_row(linha)
    console = Console()
    console.print(table)
