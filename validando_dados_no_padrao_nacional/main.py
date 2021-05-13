import requests
from acesso_cep import BuscaEndereco

cep = 50660180
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
