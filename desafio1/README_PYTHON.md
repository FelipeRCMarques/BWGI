
# Desafio de Conciliação de Transações em Python

## Objetivo

Fazer o batimento entre duas listas de transações financeiras, retornando ambas com uma nova coluna indicando se a transação foi encontrada (FOUND) na outra lista ou não (MISSING). A comparação leva em conta:

- Mesmos valores de departamento, valor e beneficiário.
- Datas idênticas, do dia anterior ou posterior.
- Preferência por correspondências com datas **anteriores** e **mais próximas**.
- Cada transação pode ser usada apenas uma vez.

## Estrutura da Função

```python
def reconcile_accounts(list1, list2):
```

- `list1`, `list2`: listas de listas, onde cada sublista representa uma transação com:
  `[data (YYYY-MM-DD), departamento, valor, beneficiário]`.

A função retorna duas novas listas com uma 5ª coluna: `"FOUND"` ou `"MISSING"`.

## Decisões técnicas

### normalize_transaction
```python
def normalize_transaction(tx):
    return (tx[1], tx[2], tx[3])
```
Ignora a data ao comparar transações.

---

### parse_date
```python
def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")
```
Converte uma string de data para objeto datetime.

---

### matched1 / matched2

Listas booleanas que indicam se uma transação já foi usada no pareamento, garantindo que cada transação seja utilizada apenas uma vez.

---

### Uso de enumerate

Permite acessar o índice da transação (`i`) para marcar como utilizada em `matched2[i]`.

---

### Uso de abs

```python
date_diff = abs(date2 - date1)
```
Facilita a checagem se a transação está em um intervalo de até 1 dia. Alternativas com `.days` e comparação de intervalo também seriam válidas.

---

### Lógica de correspondência

- Busca transações com mesmos campos (exceto data).
- Aceita diferença de até 1 dia na data.
- Prioriza:
  1. Transações **do dia anterior**.
  2. Transações **com menor diferença de data**.

---

## Retorno

Cada lista original é retornada com uma nova coluna:

```python
[['2020-12-04', 'Tecnologia', '16.00', 'Bitbucket', 'FOUND'], ...]
```

---

## Exemplo de uso

```python
import csv
from pathlib import Path
from pprint import pprint

transactions1 = list(csv.reader(Path('transactions1.csv').open()))
transactions2 = list(csv.reader(Path('transactions2.csv').open()))

out1, out2 = reconcile_accounts(transactions1, transactions2)

pprint(out1)
pprint(out2)
```
