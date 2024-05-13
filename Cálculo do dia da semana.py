# Ler data
dia = int(input("dia: "))
mes = int(input("mes: "))
ano = int(input("ano: "))

if mes == 1 or mes == 2:
    mes += 12
    ano -= 1

# Calcular dia da semana
# s = (d + \lfloor (13 \cdot (m + 1)) / 5 \rfloor + a + \lfloor a/4 \rfloor - \lfloor a/100 \rfloor + \lfloor a/400 \rfloor ) mod 7
dia_da_semana = ( dia + (( 13 * (mes+1) ) // 5) + ano + (ano//4) - (ano//100) + (ano//400) ) % 7

# Exibir resposta
print( dia_da_semana )
