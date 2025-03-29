import re
'''
somaTempMax = 0
qtdMesEscaldante = 0
mediaTempMaxAnual = 0
mesMaiorTemp = 0 #Valor da temperatura do mês mais quente
tempMax = 50
mesMaisEscaldante = str
mesEscaldante = 0
mesFrio = 0
mesMaisFrio = str
numMesFrio = 0
'''
dicMeses = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
#arrEntradas = (10.0, -20.0, 33.1, 40.0, -20.0,15,48,25,-2,1,24,33)
arrEntradas = []
mes = 1
while mes < 13:
   temp = input(f"Digite a temperatura máxima do mês {mes}:")
   if temp == 'exit':
      break
   #Substituir , por .
   temp = temp.replace(',','.')
   #Retirar os espaços vazios
   temp = temp.strip()
   #Extrair apenas os números, ponto e menos, usando expressão regular.
   temp = re.findall(r'[0-9\.\-]', f'{temp}')
   #concatenar os algorismos de temp para obter a tempMax
   tempMax = ''
   if len(temp) > 0:
      for a in temp:
         tempMax = f'{tempMax}{a}'
   #comprimento do valor digitado, validado
   temp_len = len(str(tempMax))

   if temp_len > 0 and float(tempMax) > -60.0 and float(tempMax) < 50.0:
      arrEntradas.append(float(tempMax))
      mes += 1
   else:
      print(f"Erro: Digite um valor numérico entre -60 e 50 ou exit para sair.")

'''
for mes in range(1,13):
   tempMax = input(f"Digite a temperatura máxima do mês {mes}:")
   if (len(tempMax)==0):
      print(f"Erro: Digite um valor numérico entre -60 e 50.")
      tempMax = input(f"Digite a temperatura máxima do mês {mes}:")
   elif (float(tempMax) or int(tempMax)):
      arrEntradas.append(tempMax)
   else:
      print(f"Erro: Digite um valor numérico entre -60 e 50.")
      mes = mes - 1
'''
print(arrEntradas)

#1: Calcular a média anual de temperatura dada no arrEntradas
tempAcumulada = 0
qtdMesEscaldante = 0
tempMaisEscaldante = -60
tempMaisFrio = 50
for temp in arrEntradas:
   if temp > 33:
      qtdMesEscaldante += 1

   if temp > tempMaisEscaldante:
      tempMaisEscaldante = temp

   if temp < tempMaisFrio:
      tempMaisFrio = temp

   tempAcumulada += temp

tempMedia = tempAcumulada / len(arrEntradas)
print(f"Temp acumulada: {tempAcumulada} \nTemp média: {tempMedia}")
print(f"Quantidade de meses escaldantes: {qtdMesEscaldante}")
#print(f"Temp mais escaldante: {tempMaisEscaldante}")
#print(f"Mês mais escaldante: {arrEntradas.index(tempMaisEscaldante)+1}")
print(f"Mês mais quente: {dicMeses.get(arrEntradas.index(tempMaisEscaldante)+1)}")
#print(f"Temp mais frio: {tempMaisFrio}")
print(f"Mês mais frio: {dicMeses.get(arrEntradas.index(tempMaisFrio)+1)}")