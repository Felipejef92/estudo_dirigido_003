# Exercício 9 – POO e Levantamento de Requisitos (Reflexão)

**Tema escolhido:** *Controle diário de corridas de um motorista de aplicativo*

---

## 1. Identificação do problema

Motoristas de aplicativo precisam acompanhar diariamente:

* Número de corridas
* Ganhos do dia
* Gastos com combustível
* Tempo total rodado
* Saldo final real (lucro do dia)

Sem controle, é difícil saber:

* Se o dia foi lucrativo
* Se vale a pena rodar em certos horários
* Quanto realmente sobra após combustível

---

## 2. Principais entidades

### Corrida

Representa uma corrida realizada.

### Motorista

Representa o motorista que realiza as corridas.

### DiaDeTrabalho

Controla o resumo diário.

---

## 3. Atributos principais

### Classe Corrida

* valor
* distancia_km
* origem
* destino

### Classe Motorista

* nome
* placa
* saldo_total

### Classe DiaDeTrabalho

* data
* lista_corridas
* gasto_combustivel

---

## 4. Métodos principais

### Corrida

Apenas armazena dados.

### Motorista

* adicionar_lucro
* exibir_relatorio

### DiaDeTrabalho

* adicionar_corrida
* calcular_ganhos
* calcular_lucro_liquido
* listar_corridas

---

## 5. Mini-pseudocódigo

```
Criar Motorista
Criar DiaDeTrabalho

Adicionar 3 corridas ao dia
Registrar gasto de combustível

Mostrar:
- lista de corridas
- ganho total
- gasto
- lucro final


## 6. Conclusão

Antes de programar, precisamos modelar o problema real:

* Quais são as entidades?
* Quais atributos elas têm?
* Quais comportamentos possuem?
* Como interagem?

Assim, POO se torna uma forma de organizar o mundo real dentro do sistema.
