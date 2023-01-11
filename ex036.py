vcasa = float(input('Qual o valor da casa que você quer financiar? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você quer pagar a casa? '))
meses = anos * 12
trinta = salario / 100 * 30

if vcasa > meses * trinta:
    print('Hmm, você não pode pagar por esse financiamento')

else:
    print('Perfeito, seu financiamento ficará divido em {} parcelas de R${:.2f}'.format(meses, vcasa/meses))
