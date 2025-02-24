# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

_format = "%Y-%m-%d"
loan_date = datetime.strptime("2022-12-20", _format)
last_date = loan_date + relativedelta(years=5)
loan_value = 1_000_000
installments_dates = []

while loan_date < last_date:
    installments_dates.append(loan_date)
    loan_date += relativedelta(months=1)

installments = len(installments_dates)
installments_value = f"R$ {(loan_value / installments):,.2f}"

print(f"Total de Parcelas: {
      installments} | Valor das Parcelas: {installments_value}")
print()
for i in range(1, installments + 1):
    installments_date = datetime.strftime(installments_dates[i-1], "%d/%m/%Y")
    print(f"Parcela: {i} | Valor: {
          installments_value} | Date: {installments_date}")
