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

print("Digite a seguir as temperaturas máxima de cada mês do ano utilizando seu respectivo número. Exemplo: Mês 1 é janeiro, Mês 2 é fevereiro e assim por diante")

for cont in range(1,13):
   tempMax = float(input(f"Digite a temperatura máxima do mês {cont}:"))
   if tempMax < -60 or tempMax > 50:
      print("Intervalo válido é de -60º Celsius a 50º Celsius.")
      print("Temperatura fora do intervalo válido! Digite novamente.")
      break

   somaTempMax = somaTempMax + tempMax
   mediaTempMaxAnual = somaTempMax/12

   # Quantidade de meses escaldantes
   if tempMax > 33:
      qtdMesEscaldante += 1

   # Mês mais escaldante do ano
   if mesMaiorTemp < tempMax:
      mesMaiorTemp = tempMax
      if cont == 1:
       mesMaisEscaldante = str("Janeiro")
      elif cont == 2:
       mesMaisEscaldante = str("Fevereiro")
      elif cont == 3:
       mesMaisEscaldante = str("Março")
      elif cont == 4:
       mesMaisEscaldante = str("Abril")
      elif cont == 5:
       mesMaisEscaldante = str("Maio")
      elif cont == 6:
       mesMaisEscaldante = str("Junho")
      elif cont == 7:
       mesMaisEscaldante = str("Julho")
      elif cont == 8:
       mesMaisEscaldante = str("Agosto")
      elif cont == 9:
       mesMaisEscaldante = str("Setembro")
      elif cont == 10:
       mesMaisEscaldante = str("Outubro")
      elif cont == 11:
       mesMaisEscaldante = str("Novembro")
      else:
       mesMaisEscaldante = str("Dezembro")

   # Mês menos quente do ano
   if cont == 1:
      mesFrio = tempMax
      numMesFrio = cont
   else:
      if mesFrio > tempMax:
         mesFrio = tempMax
         numMesFrio = cont

   if numMesFrio == 1:
      mesMaisFrio = str("Janeiro")
   elif numMesFrio == 2:
      mesMaisFrio = str("Fevereiro")
   elif numMesFrio == 3:
      mesMaisFrio = str("Março")
   elif numMesFrio == 4:
      mesMaisFrio = str("Abril")
   elif numMesFrio == 5:
      mesMaisFrio = str("Maio")
   elif numMesFrio == 6:
      mesMaisFrio = str("Junho")
   elif numMesFrio == 7:
      mesMaisFrio = str("Julho")
   elif numMesFrio == 8:
      mesMaisFrio = str("Agosto")
   elif numMesFrio == 9:
      mesMaisFrio = str("Setembro")
   elif numMesFrio == 10:
      mesMaisFrio = str("Outubro")
   elif numMesFrio == 11:
      mesMaisFrio = str("Novembro")
   else:
      mesMaisFrio = str("Dezembro")

else:
   print(f"Media anual de temperatura máxima: {mediaTempMaxAnual}º celsius")
   print(f"Quantidade de meses escaldantes: {qtdMesEscaldante}")
   print(f"Mês mais escaldante do ano: {mesMaisEscaldante}")
   print(f"Mês menos quente do ano:{mesMaisFrio}")
