import datetime
import re
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

def dadosOficio(conteudo, remessa):
    oficioRegex = re.compile('\d\d\d\d\d\d\d')
    numeroOficio = oficioRegex.search(conteudo)
    oficio = numeroOficio.group()

    dataRegex = re.compile(r'(\d\d\s(de)\s(\w)+\s(de)\s\d\d\d\d)')
    dataOficio = dataRegex.search(conteudo)
    data = (dataOficio.group())

    contaRegex = re.compile(r'(Conta: )(\w)+')
    contaOficio = contaRegex.search(conteudo)
    conta = (str(contaOficio.group())[7:])

    beneficiarioRegex = re.compile(r'(Requerente: )(.)+')
    requerenteOficio = beneficiarioRegex.search(conteudo)
    benficiario = (str(requerenteOficio.group())[12:])

    dataremessa = remessa[:8]
    dataremessa = dataremessa[:2] + '/' + dataremessa[2:4] + '/' + dataremessa[4:]
    data = data.lower().replace('de ', '')
    data = datetime.datetime.strptime(data, '%d %B %Y')
    data = datetime.datetime.strftime(data, '%d/%m/%Y')

    dados = [oficio, data, dataremessa, remessa, "E-mail", "TRF3", "TRF3", conta, benficiario]
    #dados.insert(2, "E-mail")
    #dados.insert(3, "TRF3")
    # dados.insert(4, "TRF3")
    return dados
