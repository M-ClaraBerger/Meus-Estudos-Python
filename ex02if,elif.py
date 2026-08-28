nome = str(input('Qual é o seu nome? Apenas resposta direta com nome e sobrenome!')).strip()
if nome  =='Eduardo':
    print('Que nome maravilhoso você tem!')
elif nome == 'Pedro' or nome== 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é tão normal!')

print('Tenha um bom dia, {}!'.format(nome))
