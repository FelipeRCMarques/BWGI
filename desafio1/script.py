from datetime import datetime, timedelta
from collections import defaultdict
from copy import deepcopy

def reconcile_accounts(transactions1, transactions2):
    t1 = deepcopy(transactions1)
    t2 = deepcopy(transactions2)

    # Indexa transações da lista 2 por (departamento, valor, beneficiário)
    index2 = defaultdict(list)
    for i, row in enumerate(t2):
        key = tuple(row[1:4])  # (Departamento, Valor, Beneficiário)
        date = datetime.strptime(row[0], "%Y-%m-%d")
        index2[key].append((date, i))

    matched2 = set()
    result1 = []

    # Para cada transação da lista 1, tenta encontrar match na lista 2
    for row in t1:
        key = tuple(row[1:4])
        date1 = datetime.strptime(row[0], "%Y-%m-%d")
        candidates = index2.get(key, [])

        # Filtra por datas próximas (±1 dia) e não usados
        valid = [(abs((date1 - d).days), d, idx) for d, idx in candidates
                 if abs((date1 - d).days) <= 1 and idx not in matched2]

        if valid:
            # Escolhe o match mais próximo e mais antigo
            valid.sort()
            _, _, idx = valid[0]
            matched2.add(idx)
            result1.append(row + ["FOUND"])
        else:
            result1.append(row + ["MISSING"])

    # Agora constrói o resultado da lista 2
    result2 = []
    for i, row in enumerate(t2):
        status = "FOUND" if i in matched2 else "MISSING"
        result2.append(row + [status])

    return result1, result2