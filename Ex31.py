from datetime import datetime
data_nasc=input("Introduz a tua data de aniversário \n")

data_nasc=datetime.strptime(data_nasc, '%y-%n')



data_atual=datetime.now()


print(data_atual.date())