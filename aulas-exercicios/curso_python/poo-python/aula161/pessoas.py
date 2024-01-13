import contas
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    c1 = Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(112, 223, 100)
    print(c2)
    print(c2.conta)