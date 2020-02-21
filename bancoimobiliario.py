import random

propriedades = [
    {'id':0,'nome': 'Propriedade1', 'valorCompra': random.randint(50,150),'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':1,'nome': 'Propriedade2', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':2,'nome': 'Propriedade3', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':3,'nome': 'Propriedade4', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':4,'nome': 'Propriedade5', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':5,'nome': 'Propriedade6', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':6,'nome': 'Propriedade7', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':7,'nome': 'Propriedade8', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':8,'nome': 'Propriedade9', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':9,'nome': 'Propriedade10', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':11,'nome': 'Propriedade11', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':12,'nome': 'Propriedade12', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':13,'nome': 'Propriedade13', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':14,'nome': 'Propriedade14', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':15,'nome': 'Propriedade15', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':16,'nome': 'Propriedade16', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':17,'nome': 'Propriedade17', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':18,'nome': 'Propriedade18', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':19,'nome': 'Propriedade19', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
    {'id':20,'nome': 'Propriedade20', 'valorCompra': random.randint(50,150), 'valorAluguel': random.randint(10,25),'idDono':''},
]

#modo 1 calculista, 2 moderado , 3 agressivo
jogadores = [
    {'id':1,'modo':1,'dinheiroConta':300,'casaAtual':0},
    {'id':2,'modo':2,'dinheiroConta':300,'casaAtual':0},
    {'id':3,'modo':3,'dinheiroConta':300,'casaAtual':0},
    {'id':4,'modo':random.randint(1,3),'dinheiroConta':300,'casaAtual':0}
]


for pessoa in jogadores:
    if pessoa['id'] == 3:
        print(pessoa['modo'])

i=1
for i in range(200):
    print("jogada numero:" + str(i))
    for pessoa in jogadores:
        print("jogador:" + str(pessoa['id']) + "jogando")
        #apenas ira jogar se ainda estiver no jogo
        if pessoa['dinheiroConta'] > 0:
            #jogando o dado
            valorDado = random.randint(1,6)
            novaCasa = pessoa['casaAtual'] + valorDado
            if novaCasa > 20:
                novaCasa = novaCasa - 20
                pessoa['dinheiroConta'] = pessoa['dinheiroConta'] + 100

            for propriedade in propriedades:
                if propriedade['id'] == novaCasa:
                    print('jogador ' + str(pessoa['id']) + ' foi a casa' + str(novaCasa))
                    #Pagar aluguel
                    if propriedade['idDono'] != '':
                        if propriedade['idDono'] != pessoa['id']:
                            #subtraindo dinheiro
                            pessoa['dinheiroConta'] = pessoa['dinheiroConta'] - propriedade['valorAluguel']

                            #transferindo dinheiro
                            for recebedor in jogadores:
                                if recebedor['id'] == propriedade['idDono']:
                                    recebedor['dinheiroConta'] = recebedor['dinheiroConta'] + propriedade['valorAluguel']
                                    print("Personagem " + str(pessoa['id']) + " pagou aluguel ao personagem " + str(recebedor['id']) +  "no valor de $" + str (propriedade['valorAluguel']))
                    elif pessoa['modo'] == 1:
                        print("entrou verificacao modo1")
                        if pessoa['dinheiroConta'] / 3 > propriedade['valorCompra']:
                            pessoa['dinheiroConta'] = pessoa['dinheiroConta'] - propriedade['valorCompra']
                            propriedade['idDono'] = pessoa['id'] 
                            print("Personagem " + str(pessoa['id']) + " comprou a propriedade " + str(propriedade['nome']) + "por $" + str(propriedade['valorCompra']))
                    elif pessoa['modo'] == 2:                        
                        print("entrou verificacao modo2")
                        if pessoa['dinheiroConta'] / 2 > propriedade['valorCompra']:
                            pessoa['dinheiroConta'] = pessoa['dinheiroConta'] - propriedade['valorCompra']
                            propriedade['idDono'] = pessoa['id'] 
                            print("Personagem " + str(pessoa['id']) + " comprou a propriedade " + str(propriedade['nome']) + "por $" + str(propriedade['valorCompra']))
                    elif pessoa['modo'] == 3:                        
                        print("entrou verificacao modo3")
                        if pessoa['dinheiroConta']  > propriedade['valorCompra']:
                            pessoa['dinheiroConta'] = pessoa['dinheiroConta'] - propriedade['valorCompra']
                            propriedade['idDono'] = pessoa['id'] 
                            print("Personagem " + str(pessoa['id']) + " comprou a propriedade " + str(propriedade['nome']) + "por $" + str(propriedade['valorCompra']))
                    pessoa['casaAtual'] = novaCasa
            else:
                print("Personagem " + str(pessoa['id']) + "esta fora da partida")


for pessoa in jogadores:
    print("Personagem " + str(pessoa['id']) + " terminou com $" + str(pessoa['dinheiroConta']))
                  