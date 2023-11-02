# Object Oriented Programming

## Descrição
Esse repositório possui como objetivo armazenar os projetos realizados durante o meu aprofundamento em Python no tópico 'Programação Orientada a Objetos'.

- [Projeto 1](#section-1)
- [Projeto 2]
- [Projeto 3]
- [Projeto 4]
- [Projeto 5]
- [Projeto 6]

### Projeto 1 

Este projeto em Python é uma implementação da classe `BankAccount` que simula a funcionalidade e características de uma conta bancária. Ele inclui recursos como depósito, saque, cálculo de juros e geração de números de confirmação. A classe `BankAccount` permite criar e gerenciar contas bancárias, interagir com elas e recuperar detalhes de transações.

Os principais métodos e atributos da classe BankAccount incluem:

- Identificação da Conta: Cada conta é identificada de forma única por um número de conta.
- Informações do Titular da Conta: Você pode definir o primeiro e o último nome do titular da conta.
- Fuso Horário Preferencial: As contas têm um deslocamento de fuso horário preferencial associado.
- Saldos: Os saldos são mantidos e podem ser verificados. Os saldos não podem ser definidos diretamente.
- Depósitos e Saques: Você pode fazer depósitos e saques, e o sistema garante que os saques não levem a saldos negativos.
- Juros Mensais: A classe inclui uma taxa de juros mensal que pode ser aplicada a todas as contas de forma uniforme, e há um método para calcular e adicionar juros ao saldo.
- Números de Confirmação: Cada depósito e saque gera um número de confirmação, que inclui o tipo de transação, número da conta, horário da transação e identificar único que incrementa a cada operação.
- Detalhes da Transação: Você pode recuperar informações detalhadas da transação com base em um número de confirmação.
