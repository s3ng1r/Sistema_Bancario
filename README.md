# DioBank - Sistema de Gerenciamento Financeiro

Este é um sistema de banco chamado DioBank, desenvolvido para permitir que os clientes realizem operações bancárias básicas. O código foi implementado em Python e oferece as seguintes funcionalidades: depósito, saque, consulta de extrato e encerramento de operação

## Funcionalidades

### Depósito

- O cliente pode realizar depósitos em sua conta.
- O valor do depósito é verificado para garantir que seja um número positivo.
- O saldo da conta é atualizado com o valor do depósito.
- Um registro da transação é adicionado ao extrato.

### Saque

- Os clientes podem fazer saques de sua conta.
- Várias verificações são realizadas:
  - Verifica se o valor do saque não excede o saldo disponível.
  - Verifica se o valor do saque não excede o limite diário de saques.
  - Verifica se o número máximo de saques por dia não foi excedido.
  - Verifica se o valor do saque é um número positivo.
- Se todas as verificações passarem, o valor do saque é deduzido do saldo da conta.
- Um registro da transação é adicionado ao extrato.

### Extrato

- Os clientes podem visualizar seu extrato, que contém informações sobre transações realizadas.
- O extrato exibe as entradas de depósito e saque, formatadas com os valores correspondentes.
- O saldo atual da conta é exibido no final do extrato.

### Encerramento de Operação

- Uma mensagem de despedida personalizada é exibida com base no nome do cliente.

## Implementações

O segundo código apresenta uma evolução do sistema DioBank com melhorias e recursos adicionais:

- Agora o sistema saúda o cliente com um cumprimento amigável e pergunta como o cliente gostaria de ser chamadom colocando o nome com primeira letra maiúscula.
- O nome do cliente é armazenado e usado para personalizar as mensagens.
- As opções do menu são exibidas com letras maiúsculas para facilitar a seleção e caso o cliente coloque uma letra minúscula o código converte para maiúscula.
- Na opção de guardar dinheiro foi adicionada:
  - Verifica se o valor é numérico ou se é válido.
  - Uma confirmação é solicitada antes de concluir a operação.
- A opção de retirar dinheiro foi melhorada:
  - Verifica se o valor é numérico ou se é válido.
  - Uma confirmação é solicitada antes de concluir a operação.
- O extrato foi aprimorado:
  - As entradas de depósito e retirada são alinhadas para facilitar a leitura.
  - O saldo final é exibido no centro do extrato.
  
## Conclusão

O DioBank é um sistema de gerenciamento financeiro que oferece diversas funcionalidades para os clientes realizarem operações bancárias de forma simples e segura. Com melhorias e recursos adicionais implementados, o sistema se tornou mais amigável e eficiente, proporcionando uma experiência aprimorada para os usuários.
