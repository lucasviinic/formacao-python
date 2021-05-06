class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>> Código: {self.codigo} Saldo: R$ {self.saldo} <<]"


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

conta_do_bill = ContaCorrente(13002)
conta_do_bill.deposita(500)

conta_da_dani = ContaCorrente(29239)
conta_da_dani.deposita(500)

contas = [conta_do_bill, conta_da_dani]
for conta in contas:
    print(conta)

deposita_para_todas(contas)
for conta in contas:
    print(conta)

contas.insert(0, 76)
print(contas[0], contas[1], contas[2])

bill = ("Bill", 74, 1947)
melinda = ("Melinda", 70, 1943)





















