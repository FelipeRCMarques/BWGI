import csv
from pathlib import Path
from pprint import pprint
from script import reconcile_accounts

transactions1 = list(csv.reader(Path('transactions1.csv').open()))
transactions2 = list(csv.reader(Path('transactions2.csv').open()))

out1, out2 = reconcile_accounts(transactions1, transactions2)

pprint(out1)
pprint(out2)