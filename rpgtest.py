def drawline():
    print('\n--------------------------------------------------------------------------------------------------\n')

def devconsole():
    while True:
        item = input('Item\n->')
        qtd = int(input('Quantidade\n->'))
        if item == 'poção':
            inventory['pot'] += qtd
        if item == 'shard':
            inventory['shard'] += qtd
        if item == 'dinheiro':
            inventory['dinheiro'] += qtd
        if item == 'exp':
            status['exp'] += qtd
        if item == 'sair':
            break
        else:
            continue

def cheat():
    os.system("cls")
    inventory['dinheiro'] += 5000
    inventory['kit_capt'] += 5
    inventory['shard'] += 500
    somadores['atq_soma'] += 20
    somadores['def_soma'] += 20
    status['exp'] += 1170
    inventory['pot'] += 200
    drawline()
    print('\n\tSeus Status foram buffados.\n\tSeja bem vindo, tester...\n\n\n')
    drawline()
    computarexp()
    atribuirpontos()

def calcularpontos():
    game['pts_final'] = (2 * game['pts_kill']) + (3 * game['pts_capt']) - (100 * game['pts_revive']) + (5 * status['lvl']) + (50 * game['pts_alatreon'])
    print('\tPontuação: ',game['pts_final'])

def mostrarinventario():
    os.system("cls")
    drawline()
    print(f'Poção: {inventory["pot"]}')
    print(f'Kit de Captura: {inventory["kit_capt"]}')
    print(f'Reviver: {inventory["revive"]}')
    print(f'Dinheiro: {inventory["dinheiro"]}$')
    print(f'Fragmentos: {inventory["shard"]}')
    drawline()

def mostrarstatus():
    os.system("cls")
    print('\tAtributos:')
    print(f'Força: {atributos["atr_for"]}')
    print(f'Destreza: {atributos["atr_dex"]}')
    print(f'Constituição: {atributos["atr_con"]}')
    print('\tSomadores:')
    print(f'Bônus Arma: {status["atq_arma"]}')
    print(f'Bônus Armadura: {status["def_armor"]}')
    print(f'Bônus Healing: {somadores["bonus_heal"]}')
    print(f'Bônus Exp: {somadores["bonus_exp"]}')
    print(f'Bônus Dinheiro: {somadores["bonus_din"]}')
    print('\tStatus:')
    print(f'Vida Total: {status["vida_total"]}')
    print(f'Ataque: {somadores["atq_soma"]}')
    print(f'Defesa: {somadores["def_soma"]}')
    print(f'Dano Base: {somadores["dano_player"]}')
    print(f'Nível: {status["lvl"]}')
    print(f'Experiência: {status["exp"]}/{status["lvl"]+10}')
    calcularpontos()
    drawline()

def computarexp():
    os.system("pause")
    os.system("cls")
    while status['exp'] >= (status['lvl'] + 10):
        status['exp'] -= (status['lvl'] + 10)
        print('\n\tVocê Evoluiu de nível!!!')
        status['lvl'] += 1
        status['pts_restante'] += 3

def atribuirpontos():
    while status['pts_restante'] != 0:
        print(f'Você tem {status["pts_restante"]} Pontos!\n')
        atr_add_for = int(input('\nAdicionar pontos em Força:\n->'))
        atr_add_dex = int(input('\nAdicionar pontos em Destreza:\n->'))
        atr_add_con = int(input('\nAdicionar pontos em Constituição:\n->'))
        
        if (atr_add_for + atr_add_con + atr_add_dex) == status['pts_restante']:
            status['pts_restante'] = 0
            atributos['atr_con'] += atr_add_con
            atributos['atr_for'] += atr_add_for
            atributos['atr_dex'] += atr_add_dex
        else:
            print('\n\n\tValores inválidos!\n')
            continue
    somadores['atq_soma'] = (atributos['atr_dex']/2) + status['atq_arma']
    somadores['def_soma'] = (atributos['atr_con']/2) + status['def_armor']
    somadores['dano_player'] = (atributos['atr_for']/2) + (status['lvl']/2)
    status['vida_total'] = status['lvl'] + (atributos['atr_con']*2)
    status['vida_atual'] = status['vida_total']

    drawline()
    print('Atributo de Força: ', atributos['atr_for'])
    print('Atributo de Constituição: ', atributos['atr_con'])
    print('Atributo de Destreza: ', atributos['atr_dex'],'\n')
    print('\n\nNível ', status['lvl'])
    print('Ataque ', somadores['atq_soma'])
    print('Defesa ', somadores['def_soma'])
    print('Vida ', status['vida_total'])
    print('Dano Base ', somadores['dano_player'])
    drawline()

def adicionar_atributos_inicial():
    while status['pts_restante'] != 0:
        status['pts_restante'] = 10
        print('\n\nPontos de atributo Restantes: ', status['pts_restante'])
        atributos['atr_for'] = int(input('\nAloque seus pontos de Força\n->'))
        status['pts_restante'] -= atributos['atr_for']

        print('\nPontos de atributo Restantes: ', status['pts_restante'])
        atributos['atr_dex'] = int(input('\nAloque seus pontos de Destreza\n->'))
        status['pts_restante'] -= atributos['atr_dex']

        print('\nPontos de atributo Restantes: ', status['pts_restante'])
        atributos['atr_con'] = int(input('\nAloque seus pontos de Constituição\n->'))
        status['pts_restante'] -= atributos['atr_con']         
    #retorno
    somadores['atq_soma'] = (atributos['atr_dex']/2) + status['atq_arma']
    somadores['def_soma'] = (atributos['atr_con']/2) + status['def_armor']
    somadores['dano_player'] = (atributos['atr_for']/2) + (status['lvl']/2)
    status['vida_total'] = status['lvl'] + (atributos['atr_con']*2)
    # 
    drawline()
    print('\n\nAtaque ', somadores['atq_soma'])
    print('Defesa ', somadores['def_soma'])
    print('Vida ', status['vida_total'])
    print('Dano Base ', somadores['dano_player'])

def selecionar_alatreon():
    lvl_min = status['lvl'] - 5
    lvl_max = status['lvl'] + 5
    monstro['lvl_monstro'] = random.randint(lvl_min,lvl_max)
    monstro['nome_monstro'] = 'Alatreon'
    monstro['atq_monstro'] = 35
    monstro['def_monstro'] = 20 + (monstro['lvl_monstro'] / 2)
    monstro['vida_monstro'] = 275 + (monstro['lvl_monstro'] * 4)
    monstro['dano_monstro'] = 25
    monstro['mult_exp'] = 4
    monstro['mult_din'] = 7

def selecionar_monstro():
    select = random.randint(1,100)
    lvl_min = status['lvl'] - 5
    lvl_max = status['lvl'] + 5
    monstro['lvl_monstro'] = random.randint(lvl_min,lvl_max)
    if monstro['lvl_monstro'] <= 0:
        monstro['lvl_monstro'] = 1
    if select == 100:
        monstro['nome_monstro'] = 'Alatreon'
        monstro['atq_monstro'] = 35
        monstro['def_monstro'] = 20 + (monstro['lvl_monstro'] / 2)
        monstro['vida_monstro'] = 275 + (monstro['lvl_monstro'] * 3)
        monstro['dano_monstro'] = 25
        monstro['mult_exp'] = 4
        monstro['mult_din'] = 3
    elif select >= 90 and select <= 99:
        monstro['nome_monstro'] = 'Shagaru'
        monstro['atq_monstro'] = 10 + (monstro['lvl_monstro']/2)
        monstro['def_monstro'] = 15
        monstro['vida_monstro'] = 200 + (monstro['lvl_monstro']*2)
        monstro['dano_monstro'] = 10
        monstro['mult_exp'] = 2
        monstro['mult_din'] = 2
    elif select >= 70 and select <= 89:
        monstro['nome_monstro'] = 'Deviljho'
        monstro['atq_monstro'] = 7
        monstro['def_monstro'] = 5
        monstro['vida_monstro'] = 70 + monstro['lvl_monstro']
        monstro['dano_monstro'] = 6 + monstro['lvl_monstro']
        monstro['mult_exp'] = 1
        monstro['mult_din'] = 4
    elif select >= 50 and select < 70:
        monstro['nome_monstro'] = 'Gammoth'
        monstro['atq_monstro'] = 4
        monstro['def_monstro'] = 5
        monstro['vida_monstro'] = 50 + (2 * monstro['lvl_monstro'])
        monstro['dano_monstro'] = 5
        monstro['mult_exp'] = 1 + (status['lvl'] / 4)
        monstro['mult_din'] = 1
    else:
        monstro['nome_monstro'] = 'Jagras'
        monstro['atq_monstro'] = 2
        monstro['def_monstro'] = -2 + (monstro['lvl_monstro']/2)
        monstro['vida_monstro'] = 20
        monstro['dano_monstro'] = 1
        monstro['mult_exp'] = 0.5
        monstro['mult_din'] = 1
    print('Você encontrou um ', monstro['nome_monstro'],'Nível ', monstro['lvl_monstro'])
    print('\tVida Total: ',monstro['vida_monstro'])
    print('\tAtaque: ',monstro['atq_monstro'])
    print('\tDefesa: ',monstro['def_monstro'])

def lojinha():
    while True:
        print('\nVocê encontra um Mercador Andarilho!\nO que deseja comprar?\nDinheiro:', inventory['dinheiro'])
        shop = input('\t-Poção: 10$\n\t-10x Poção: 100$\n\t-Revive: 750$\n\t-Kit Captura: 100$\n\t-Sinal de Alatreon: 1500$\n\t-Especial\n\t-Sair\n->').lower()
        if shop == 'sair':
            os.system("cls")
            print('\nVocê volta ao seu acampamento...')
            break
        elif shop == 'poção' or shop == 'pocao' or shop == 'pot':
            if inventory['dinheiro'] >= 10:
                inventory['dinheiro'] -= 10
                inventory['pot'] += 1
            else:
                print('Dinheiro insuficiente!')
                continue
        elif shop == '10x poção' or shop == '10xpocao' or shop == '10xpot' or shop == '10x pot':
            if inventory['dinheiro'] >= 100:
                inventory['dinheiro'] -= 100
                inventory['pot'] += 10
            else:
                print('Dinheiro insuficiente!')
                continue
        elif shop == 'sinal de alatreon' or shop == 'alatreon' or shop == 'sinal alatreon':
            if inventory['dinheiro'] >= 1500:
                inventory['dinheiro'] -= 1500
                inventory['sinal_alatreon'] += 1
            else:
                print('Dinheiro insuficiente!')
                continue
        elif shop == 'revive':
            if inventory['dinheiro'] >= 750:
                inventory['dinheiro'] -= 750
                inventory['revive'] += 1
            else:
                print('Dinheiro insuficiente!')
                continue
        elif shop == 'kit captura' or shop == 'kit capt':
            if inventory['dinheiro'] >= 100:
                inventory['dinheiro'] -= 100
                inventory['kit_capt'] += 1
            else:
                print('Dinheiro insuficiente!')
                continue
        elif shop == 'especial':
            print('\nNesta sessão, tu deve pagar com fragmentos de monstros...')
            print('\n\n\t-Melhoria arma: 2$\n\t-Melhoria armadura: 4$\n\t-Melhoria Poção: 5$\n\t-Booster Xp: 7$\n\t-Booster Dinheiro: 7$\n\t-Sinalizador de Captura: 50$')
            print(f'Você tem {inventory["shard"]} Fragmentos...')
            shop_es = input('\n->').lower()
            if shop_es == 'melhoria arma' or shop_es == 'arma':
                if inventory['shard'] >= 2:
                    status['atq_arma'] += 1
                    inventory['shard'] -= 2
                    somadores['atq_soma'] = (atributos['atr_dex']/2) + status['atq_arma']
                else:
                    print('Shards Insuficientes!')
                    continue
            elif shop_es == 'melhoria armadura' or shop_es == 'armadura':
                if inventory['shard'] >= 4:
                    status['def_armor'] += 1
                    inventory['shard'] -= 4
                    somadores['def_soma'] = (atributos['atr_con']/2) + status['def_armor']
                else:
                    print('Shards Insuficientes!')
                    continue
            elif shop_es == 'melhoria poção' or shop_es == 'poção':
                if inventory['shard'] >= 5:
                    somadores['bonus_heal'] += 1
                    inventory['shard'] -= 5
                else:
                    print('Shards Insuficientes!')
                    continue
            elif shop_es == 'booster xp' or shop_es == 'xp':
                if inventory['shard'] >= 7:
                    somadores['bonus_exp'] += 2
                    inventory['shard'] -= 7
                else:
                    print('Shards Insuficientes!')
                    continue
            elif shop_es == 'booster dinheiro' or shop_es == 'dinheiro':
                if inventory['shard'] >= 7:
                    somadores['bonus_din'] += 2
                    inventory['shard'] -= 7
                else:
                    print('Shards Insuficientes!')
                    continue
            elif shop_es == 'sinalizador de captura' or shop_es == 'sinal captura':
                if inventory['shard'] >= 50:
                    inventory['sinal'] = 1
                    inventory['shard'] -= 50
                else:
                    print('Shards Insuficientes!')
                    continue

            else:
                print('Itém Inválido!')
                continue
        else:
            print('Itém Inválido!')
            continue

def batalha():
    #sistema de batalha
    print('\tVocê engaja em combate com um ', monstro['nome_monstro'],'De Nível ', monstro['lvl_monstro'])
    pt_captura = monstro['vida_monstro'] * 0.15
    captura = 0
    while monstro['vida_monstro'] > 0 and status['vida_atual'] > 0:
        if monstro['vida_monstro'] <= pt_captura and inventory['sinal'] == 1:
            drawline()
            print('\tO Monstro pode ser Capturado!!!!!')
        print('-----------------------------')
        run = int(input('\tEmbate!!!\n\t1 - Fugir\n\t2 - Lutar\n\t3 - Heal\n\t4 - Capturar\n->'))
        if run == 1:
            print('\tVocê fugiu do perigo, e está novamente a salvo em seu acampamento...')
            break
        elif run == 3:
            inventory['pot'] -= 1 
            rolagem = random.randint(1,6)
            status['vida_atual'] += (rolagem * (status['lvl'] + somadores['bonus_heal']))
            if status['vida_atual'] > status['vida_total']:
                status['vida_atual'] = status['vida_total']
            print('\nVocê Toma uma poção!\nSua Vida atual é: ', status['vida_atual'])
            drawline()
            print('Quantidade de poções restantes: ', inventory['pot'])
            drawline()
        elif run == 4:
            if inventory['kit_capt'] > 0:
                inventory['kit_capt'] -= 1
                if monstro['vida_monstro'] <= pt_captura:
                    monstro['vida_monstro'] = 0
                    captura = 1
                    game['pts_capt'] += 1
                    exp_gain = ((rolagem + somadores['bonus_exp']) * monstro['mult_exp']) / 2
                    status['exp'] += exp_gain
                    rolagem4 = random.randint(1,4)
                    shard_gain = rolagem4 * 2
                    inventory['shard'] += shard_gain
                    print(f'\n\nVocê capturou o monstro com sucesso, e recebeu:\nExperiência: {exp_gain}\nFragmentos: {shard_gain}')
                    os.system("pause")
                else:
                    print('\n Você ainda não pode capturar o monstro!!!')
                    print(f'Kits restantes: {inventory["kit_capt"]}')
        elif run == 2:
            #Vez do Jogador
            print('\n\nSeu Turno!')
            rolagem = random.randint(1,20)
            ataque = somadores['atq_soma'] + rolagem
            print('Seu ataque foi ', ataque)
            rolagem = random.randint(1,20)
            defesa = rolagem + monstro['def_monstro']
            print('A Defesa inimiga foi ', defesa)
            pt_crit = defesa + 15
            if defesa > ataque:
                print('\nO Monstro se defendeu!')
            elif ataque >= pt_crit:
                dano_causado = (status['lvl'] + somadores['dano_player']) * 2
                print(f'Um Crítico! Você causa {dano_causado} de Dano!!!')
                monstro['vida_monstro'] -= dano_causado
            else:
                rolagem = random.randint(1,status['lvl'])
                dano_causado = rolagem + somadores['dano_player']
                print(f'Você causa {dano_causado} de Dano!')
                monstro['vida_monstro'] -= dano_causado
            #Vez do monstro
            print('\nTurno do Monstro!')
            rolagem = random.randint(1,20)
            ataque = monstro['atq_monstro'] + rolagem
            print('O Ataque do Monstro foi ', ataque)
            rolagem = random.randint(1,20)
            defesa = rolagem + somadores['def_soma']
            print('Sua Defesa foi ', defesa)
            pt_crit = defesa + 15
            judge = random.randint(1,4)
            if defesa > ataque:
                print('\nVocê conseguiu se defender!')
            elif ataque >= pt_crit:
                dano_causado = (monstro['lvl_monstro'] + monstro['dano_monstro']) * 2
                print(f'Um Crítico! Você recebe {dano_causado} de Dano!!!')
                status['vida_atual'] -= dano_causado
            elif monstro['nome_monstro'] == 'Alatreon' and judge == 1 and monstro['vida_monstro'] <= 200:
                dano_causado = monstro['dano_monstro'] + (monstro['vida_monstro'] * 2)
                print(f'Alatreon usou o Escalon Judment! Você sofreu {dano_causado} de Dano!')
            else:
                rolagem2 = random.randint(1,monstro['lvl_monstro'])
                dano_causado = rolagem2 + monstro['dano_monstro']
                print(f'Você recebe {dano_causado} de Dano!')
                status['vida_atual'] -= dano_causado
            print('\n\n\tVocê tem ',status['vida_atual'],'De Vida!')
            print('\tVida monstro: ', monstro['vida_monstro'])
        else:
            continue
    #checagem final//experiencia
    os.system("cls")        
    if monstro['vida_monstro'] <= 0 and captura == 0:
        print('\n\nO Monstro se desfaz em partículas de luz...')
        rolagem = random.randint(1,10)
        rolagem2 = random.randint(1,20)
        rolagem3 = random.randint(1,5)
        exp_gain = (rolagem + somadores['bonus_exp']) * monstro['mult_exp']
        din_gain = (rolagem2 + somadores['bonus_din']) * monstro['mult_din']
        game['pts_kill'] += 1
        inventory['dinheiro'] += din_gain
        status['exp'] += exp_gain
        if monstro['nome_monstro'] == 'Alatreon':
            game['pts_alatreon'] += 1
        print(f'\n\nVocê Recebe {exp_gain} de Experiência, e {din_gain} moedas.\n')
        if monstro['nome_monstro'] == 'Shagaru':
            rolagem3 = 1
            mult_shard = 2
        else:
            mult_shard = 1
        if rolagem3 == 1:
            rolagem4 = random.randint(1,3)
            shard_gain = rolagem4 * mult_shard
            print(f'\nVocê dropou {shard_gain} shards!')
            inventory['shard'] += shard_gain
        computarexp()
        atribuirpontos()
        drawline()
    if status['vida_atual'] <= 0:
        if inventory['revive'] > 0:
            print('\n\n\A Jornada ainda não chegou ao fim!\nVocê acorda novamente em seu acampamento...')
            game['pts_revive'] += 1
            inventory['revive'] -= 1
            status['lvl'] -= 1
            status['exp'] = 0
            atributos['atr_for'] -= 1
            atributos['atr_dex'] -= 1
            atributos['atr_con'] -= 1
            status['vida_atual'] = 3
            print('\nVocê se sente um pouco mais fraco doque antes, mas ainda consegue continuar...')
        else:
            print('Game Over.')
            game['game_over'] = 1

#Código principal
#Variáveis
import random
import os
inventory = {'dinheiro': 0,'pot': 5,'revive': 2,'kit_capt': 0,'shard': 0,'sinal': 0,'sinal_alatreon': 0}
somadores = {'atq_soma': 0,'def_soma': 0,'dano_player': 0,'bonus_heal': 0,'bonus_din': 0,'bonus_exp': 0}
atributos = {'atr_for': 0,'atr_con': 0,'atr_dex': 0}
status = {'vida_total': 1,'vida_atual': 1,'exp': 0,'lvl': 1,'pts_restante': 10,'atq_arma': 1,'def_armor': 1}
monstro = {'vida_monstro': 0,'lvl_monstro': 1,'nome_monstro': 'null','dano_monstro': 1,'atq_monstro': 1,'def_monstro': 1,'mult_exp': 1,'mult_din': 1}
game = {'game_over': 0,'pts_final': 0,'pts_kill': 0,'pts_capt': 0,'pts_revive': 0,'pts_alatreon': 0}

#Ciclo Lógico do game
adicionar_atributos_inicial()
status['vida_atual'] = status['vida_total']
os.system("cls")

while game['game_over'] == 0:
    escolha = input('\n\nVocê descansa em seu acampamento, e se sente revigorado...\nO que deseja fazer?\n\t-Caçar\n\t-Comprar\n\t-Inventário\n\t-Status\n\t-Chamar um Alatreon\n\t-Ir Embora\n->').lower()
    drawline()
    if escolha == 'caçar' or escolha == 'cacar':
        selecionar_monstro()
        batalha()
    elif escolha == 'chamar um alatreon' or escolha == 'chamar alatreon' or escolha == 'chamar' or escolha == 'alatreon':
        os.system("cls")
        danger = input('\tVocê têm certeza? Esta ação irá custar um sinal de Alatreon.\n->').lower()
        if (danger == 'sim' or danger == 's' or danger == 'ss') and inventory['sinal_alatreon'] > 0:
            print('\n\nVocê atrai o grande Alatreon!\nPrepare-se para a luta!!!!\n\n')
            os.system("pause")
            os.system("cls")
            inventory['sinal_alatreon'] -= 1
            selecionar_alatreon()
            batalha()
        else:
            print('Escolha inválida! // Item insuficiente')
            os.system("pause")
            continue
    elif escolha == 'system_comando':
        os.system("cls")
        drawline()
        test = input('Insira a palavra chave:\n\t->')
        if test == 'talaodecheque' or test == 'xopanni':
            cheat()
            continue
    elif escolha == 'comprar':
        lojinha()
    elif escolha == 'inventário' or escolha == 'inventario' or escolha == 'inv':
        mostrarinventario()
    elif escolha == 'status' or escolha == 'stts':
        mostrarstatus()
    elif escolha == 'ir embora':
        os.system("cls")
        drawline()
        calcularpontos()
        print(f'Monstros mortos: {game["pts_kill"]}')
        print(f'Alatreons mortos: {game["pts_alatreon"]}')
        print(f'Monstros capturados: {game["pts_capt"]}')
        print(f'Revives utilizados: {game["pts_revive"]}')
        print(f'Nível atingido: {status["lvl"]}')
        print('\n\n\n\tNunca um adeus.....')
        drawline()
        os.system("pause")
        game['game_over'] = 1
    elif escolha == 'console_desenvolvedor_011':
        drawline()
        devconsole()
        os.system("cls")