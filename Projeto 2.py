def cria_posicao(x, y):
    """
    :param x: inteiro
    :param y: inteiro
    :return: posicao
    """
    if isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0:
        return (x, y)
    else:
        raise ValueError('cria_posicao: argumentos invalidos')


def cria_copia_posicao(p):
    """
    :param p: posicao
    :return: copia nova da posicao
    """
    if eh_posicao(p):
        return (obter_pos_x(p), obter_pos_y(p))
    else:
        raise ValueError('cria_posicao: argumentos invalidos')


def obter_pos_x(p):
    """
    :param p: posicao
    :return: componente x da posicao p (inteiro)
    """
    return p[0]


def obter_pos_y(p):
    """
    :param p: posicao
    :return: componente y da posicao p (inteiro)
    """
    return p[1]


def eh_posicao(arg):
    """
    :param arg: argumento universal
    :return: devolve True se o argumento for uma posicao e False caso contrario
    """
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(obter_pos_x(arg), int) \
           and isinstance(obter_pos_y(arg), int) and obter_pos_x(arg) >= 0 \
           and obter_pos_y(arg) >= 0


def posicoes_iguais(p1, p2):
    """
    :param p1: posicao
    :param p2: posicao
    :return: True se as posicoes sao iguais, False caso contrario
    """
    return obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2)


def posicao_para_str(p):
    """
    :param p: posicao
    :return: cadeia de carateres que representa o seu argumento isto eh '(x,y)'
    """
    return '(' + str(obter_pos_x(p)) + ', ' + str(obter_pos_y(p)) + ')'


def obter_posicoes_adjacentes(p):
    """
    :param p: posicao
    :return: tuplo com todas as posicoes adjacentes, comecando pela posicao de cima seguindo no sentido horario
    """
    x = obter_pos_x(p)
    y = obter_pos_y(p)
    aux = tuple(filter(lambda x: x[0] >= 0 and x[1] >= 0, ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y))))
    return tuple(cria_posicao(i[0], i[1]) for i in aux)


def ordenar_posicoes(t):
    """
    :param t: tuplo contendo posicoes
    :return: tuplo contendo as mesmas posicoes de t ordenadas de acordo com a ordem de leitura do prado
    """
    aux = tuple((obter_pos_x(i), obter_pos_y(i)) for i in t)
    aux_ordenado = tuple(sorted(aux, key=lambda x: (x[1], x[0])))
    return tuple(cria_posicao(i[0], i[1]) for i in aux_ordenado)


def cria_animal(s, r, a):
    """
    :param s: str nao vazia correspondente a especie do animal
    :param r: int maior que 0 correspondente a frequencia de reproducao
    :param a: int maior ou igual que 0 corresponden a frequencia de alimentacao
    :return: animal correspondente ao tuplo (s, r, a)
    """
    if isinstance(s, str) and len(s) != 0 and isinstance(r, int) and r > 0 \
            and isinstance(a, int) and a >= 0:
        return [s, r, a, 0, 0]
    else:
        raise ValueError('cria_animal: argumentos invalidos')


def cria_copia_animal(a):
    if eh_animal(a):
        return [obter_especie(a), obter_freq_reproducao(a), obter_freq_alimentacao(a), obter_idade(a), obter_fome(a)]


def obter_especie(a):
    """
    :param a: animal
    :return: especie do animal
    """
    return a[0]


def obter_freq_reproducao(a):
    """
    :param a: animal
    :return: frequencia de reproducao do animal
    """
    return a[1]


def obter_freq_alimentacao(a):
    """
    :param a: animal
    :return: frequencia de alimentacao do animal
    """
    return a[2]


def obter_idade(a):
    """
    :param a: animal
    :return: idade do animal
    """
    return a[3]


def obter_fome(a):
    """
    :param a: animal
    :return: fome do animal
    """
    return a[4]


def aumenta_idade(a):
    """
    :param a: animal
    :return: animal 'a', cuja idade aumenta uma unidade
    """
    a[3] += 1
    return a


def reset_idade(a):
    """
    :param a: animal
    :return: animal 'a', cuja idade passou a ser 0
    """
    a[3] = 0
    return a


def aumenta_fome(a):
    """
    :param a: animal
    :return: animal 'a', cuja fome aumentou uma unidade
    """
    if obter_freq_alimentacao(a) > 0:
        a[4] += 1
    return a


def reset_fome(a):
    """
    :param a: animal
    :return: animal 'a', cuja fome passou a ser 0
    """
    if obter_freq_alimentacao(a) > 0:
        a[4] = 0
    return a


def eh_animal(arg):
    """
    :param arg: argumento universal
    :return: True caso o argumento seja um animal, False caso contrario
    """
    return isinstance(arg, list) and len(arg) == 5 and isinstance(obter_especie(arg), str) \
           and len(obter_especie(arg)) != 0 and isinstance(obter_freq_reproducao(arg), int) \
           and obter_freq_reproducao(arg) > 0 and isinstance(obter_freq_alimentacao(arg), int) \
           and obter_freq_alimentacao(arg) >= 0 and isinstance(obter_idade(arg), int) \
           and 0 <= obter_idade(arg) and isinstance(obter_fome(arg), int) and 0 <= obter_fome(arg)


def eh_predador(arg):
    """
    :param arg: argumento universal
    :return: True se o argumento for um predador, False caso contrario
    """
    return eh_animal(arg) and obter_freq_alimentacao(arg) > 0


def eh_presa(arg):
    """
    :param arg: argumento universal
    :return: True se o argumento for uma presa, False caso contrario
    """
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


def animais_iguais(a1, a2):
    """
    :param a1: animal
    :param a2: animal
    :return: True se os animais a1 e a2 forem iguais, False caso contrario
    """
    return eh_animal(a1) and eh_animal(a2) and obter_especie(a1) == obter_especie(a2) \
           and obter_freq_reproducao(a1) == obter_freq_reproducao(a2) \
           and obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2) and obter_idade(a1) == obter_idade(a2) \
           and obter_fome(a1) == obter_fome(a2)


def animal_para_char(a):
    """
    :param a: animal
    :return: primeiro carater da especide do animal 'a', maiuscula caso a seja predador e miniscula se for presa
    """
    return obter_especie(a)[0].upper() if eh_predador(a) else obter_especie(a)[0].lower()


def animal_para_str(a):
    """
    :param a: animal
    :return: cadeia de carateres que corresponde a 'especie [idade/freq de reproducao;fome/freq de alimentacao]'
    """
    if eh_predador(a):
        return obter_especie(a) + ' [' + str(obter_idade(a)) + '/' + str(obter_freq_reproducao(a)) \
               + ';' + str(obter_fome(a)) + '/' + str(obter_freq_alimentacao(a)) + ']'
    else:
        return obter_especie(a) + ' [' + str(obter_idade(a)) + '/' + str(obter_freq_reproducao(a)) + ']'


def eh_animal_fertil(a):
    """
    :param a: animal
    :return: True caso o animal 'a' tenha atingido a idade de reproducao, False caso contrario
    """
    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """
    :param a: animal
    :return: True caso o animal tenha atingido um valor de fome igual ou superior a frquencia de alimentacao, False caso contrario
    """
    return obter_freq_alimentacao(a) != 0 and obter_fome(a) >= obter_freq_alimentacao(a)


def reproduz_animal(a):
    """
    :param a: animal
    :return: animal da mesma especie de 'a' com idade e fome igual a 0
    """
    reset_idade(a)
    return cria_animal(obter_especie(a), obter_freq_reproducao(a), obter_freq_alimentacao(a))


def cria_prado(d, r, a, p):  # validar se os pontos podem pertencer ao padro
    """
    :param d: posicao correspondente a posicão que ocupa a montanha do canto inferior direito do prado
    :param r: tuplo de 0 ou mais posicoes correspondentes aos rochedos que nao sao as montanhas dos limites exteriores do prado
    :param a: tuplo de 1 ou mais animais
    :param p: tuplo da mesma dimensao do tuplo a com as posicoes correspondentes ocupadas pelos animais
    :return: matriz (lista de listas) cuja entrada é -2 se for uma montanha do limite exterior, -1 se for um rochedo, animal se for um animal, 0 se a posicacao estiver vazia
    """
    if eh_posicao(d) and isinstance(r, tuple) and ((all(eh_posicao(i) for i in r) \
                                                    and all(0 < obter_pos_x(i) < obter_pos_x(d) \
                                                            and 0 < obter_pos_y(i) < obter_pos_y(d) for i in r)) \
                                                   or r == ()) and isinstance(a, tuple) and len(a) >= 1 \
            and all(eh_animal(i) for i in a) and isinstance(p, tuple) and len(p) == len(a) \
            and all(eh_posicao(i) for i in p) and all(0 < obter_pos_x(i) < obter_pos_x(d) \
                                                      and 0 < obter_pos_y(i) < obter_pos_y(d) for i in p) \
            and all(i not in r for i in p):
        prado = {'x': obter_pos_x(d), 'y': obter_pos_y(d), 'rochedos': r,
                 'animais': {p[i]: a[i] for i in range(len(a))}}
        return prado
    else:
        raise ValueError('cria_prado: argumentos invalidos')


def cria_copia_prado(m):
    if eh_prado(m):
        return {'x': m['x'], 'y': m['y'], 'rochedos': m['rochedos'], 'animais': m['animais']}


def obter_tamanho_x(m):
    """
    :param m: prado
    :return: inteiro correspondente a dimensao Nx do prado
    """
    return m['x'] + 1


def obter_tamanho_y(m):
    """
    :param m: prado
    :return: inteiro correspondente a dimensao Ny do prado
    """
    return m['y'] + 1


def obter_numero_predadores(m):
    """
    :param m: prado
    :return: inteiro correspondente ao numero de predadores no prado
    """
    res = 0
    for animal in m['animais'].values():
        res += 1 if eh_predador(animal) else 0
    return res


def obter_numero_presas(m):
    """
    :param m: prado
    :return: inteiro correspondente ao numero de presas no prado
    """
    res = 0
    for animal in m['animais'].values():
        res += 1 if eh_presa(animal) else 0
    return res


def obter_posicao_animais(m):
    """
    :param m: prado
    :return: tuplo contendo as posicoes do prado ocupadas por animais, ordenadas em ordem de leitura do prado
    """
    return ordenar_posicoes(tuple(m['animais'].keys()))


def obter_animal(m, p):
    """
    :param m: prado
    :param p: posicao
    :return: animal que se encontra na posicao p do prado m
    """
    return m['animais'][p]


def eliminar_animal(m, p):
    """
    :param m: prado
    :param p: posicao do animal que pretendemos eliminar
    :return: prado cujo animal na posicao p foi eliminado
    """
    del (m['animais'][p])
    return m


def mover_animal(m, p1, p2):
    """
    :param m: prado
    :param p1: posicao "antiga"
    :param p2: posicao "nova"
    :return: prado onde o animal que se encontrava na posicao p1 se moveu para p2
    """
    m['animais'][p2] = m['animais'][p1]
    if not posicoes_iguais(p1, p2):
        eliminar_animal(m, p1)
    return m


def inserir_animal(m, a, p):
    """
    :param m: prado
    :param a: animal a ser adicionado ao prado
    :param p: posicao do prado onde o animal 'a' vai ser adicionado
    :return: devolve, se possivel, o prado, m, com o animal, a, na posicao, p
    """
    m['animais'][p] = a
    return m


def eh_prado(arg):
    """
    :param arg: argumento universal
    :return: True caso o argumento for um prado, False caso contrario
    """
    return isinstance(arg, dict) and len(arg) == 4 and 'x' in arg and isinstance(arg['x'], int) and arg['x'] >= 0 \
           and 'y' in arg and isinstance(arg['y'], int) and arg['y'] >= 0 and 'rochedos' in arg \
           and (all(eh_posicao(i) for i in arg['rochedos']) or arg['rochedos'] == ()) and 'animais' in arg \
           and isinstance(arg['animais'], dict) and ((all(eh_posicao(i) for i in arg['animais'].keys()) and \
                                                      all(eh_animal(i) for i in arg['animais'].values()) or arg[
                                                          'animais'] == {}))


def eh_posicao_animal(m, p):
    """
    :param m: prado
    :param p: posicao
    :return: True se existir um animal na posicao p, False caso contrario
    """
    return eh_prado(m) and p in obter_posicao_animais(m)


def eh_posicao_obstaculo(m, p):
    """
    :param m: prado
    :param p: posicao
    :return: True caso a posicao p corresponda a um obstaculo no prado m, False caso contrario
    """
    return eh_prado(m) and p in tuple(cria_posicao(obter_pos_x(i), obter_pos_y(i)) for i in m['rochedos'])\
           or obter_pos_x(p) == 0 or obter_pos_x(p) == obter_tamanho_x(m) - 1\
           or obter_pos_y(p) == 0 or obter_pos_y(p) == obter_tamanho_y(m) - 1

def eh_posicao_livre(m, p):
    """
    :param m: prado
    :param p: posicao
    :return: True se a posicao p estiver livre no prado m, False caso contrario
    """
    return eh_prado(m) and eh_posicao(p) and not eh_posicao_animal(m, p) and not eh_posicao_obstaculo(m, p)


def prados_iguais(p1, p2):
    """
    :param p1: prado
    :param p2: prado
    :return: True se o prado p1 for igual ao p2, False caso contrario
    """
    return eh_prado(p1) and eh_prado(p2) and p1 == p2


def prado_para_str(m):
    """
    :param m: prado
    :return: cadeia de carateres correspondente a representacao do prado
    """
    prado = ''
    for l in range(obter_tamanho_y(m)):
        prado += '\n' if l != 0 else ''
        for c in range(obter_tamanho_x(m)):
            if (c, l) in ((0, 0), (0, obter_tamanho_y(m) - 1), (obter_tamanho_x(m) - 1, 0),
                          (obter_tamanho_x(m) - 1, obter_tamanho_y(m) - 1)):
                prado += '+'
            elif (c == 0 or c == obter_tamanho_x(m) - 1) and 0 < l < obter_tamanho_y(m) - 1:
                prado += '|'
            elif (l == 0 or l == obter_tamanho_y(m) - 1) and 0 < c < obter_tamanho_x(m) - 1:
                prado += '-'
            elif (c, l) in m['rochedos']:
                prado += '@'
            elif (c, l) in obter_posicao_animais(m):
                prado += animal_para_char(obter_animal(m, (c, l)))
            else:
                prado += '.'
    return prado

def obter_valor_numerico(m, p):
    """
    :param m: prado
    :param p: posicao
    :return: devolve o valor numerico da posicao p correspondente a ordem de leitura no prado m
    """
    return obter_tamanho_x(m) * obter_pos_y(p) + obter_pos_x(p)


def obter_movimento(m, p):
    """
    :param m: prado
    :param p: posicao inicial
    :return: retorna a proxima posicao do animal na posicao p do prado m
    """
    N = obter_valor_numerico(m, p)
    p_adj = tuple(filter(lambda x: eh_posicao_livre(m, x), obter_posicoes_adjacentes(p)))
    if eh_presa(obter_animal(m, p)):
        return p if p_adj == () else p_adj[N % len(p_adj)]
    if eh_predador(obter_animal(m, p)):
        p_adj_presas = tuple(filter(lambda x: eh_presa(obter_animal(m, x)), filter(lambda x: eh_posicao_animal(m, x), obter_posicoes_adjacentes(p))))
        if p_adj_presas != ():
            return p_adj_presas[N % len(p_adj_presas)]
        elif p_adj != ():
            return p_adj[N % len(p_adj)]
        else:
            p


def geracao(m):
    """
    :param m: prado
    :return: prado após uma geracao
    """
    aux = tuple()  # Lista auxiliar que serve para guardar as posicoes dos predadores quando comem presas, impedindo\
    # que estes se movam duas vezes por geracao
    for p1 in obter_posicao_animais(m):
        p2 = obter_movimento(m, p1)
        a = aumenta_idade(obter_animal(m, p1))
        if eh_posicao_animal(m, p2) and p2 not in aux:  # isto implica que o animal, a, eh um predador e que vai comer
            m = inserir_animal(m, reset_fome(a), p1)  # uma presa
            m = mover_animal(m, p1, p2)  # come a presa
            aux += (p2, )
        elif p2 not in aux:  # se p2 nao eh uma posicao de um animal entao eh um espaco livre, e a condicao\
            # 'p2 not in aux' garante que nao se trata de um predador que comeu uma presa que ainda nao se tinha mexido\
            # (caso contrario o perdador movimentava-se 2 vezes, uma na vez dele e a outra na vez da presa)
            m = inserir_animal(m, aumenta_fome(a), p1) if eh_predador(a) else inserir_animal(m, a, p1)
            m = eliminar_animal(m, p1) if eh_animal_faminto(a) and eh_predador(a) else mover_animal(m, p1, p2)
        m = inserir_animal(m, reproduz_animal(a), p1) if eh_animal_fertil(a) and not posicoes_iguais(p1, p2) else m
    return cria_copia_prado(m)


def simula_ecossistema(f, g, v):
    """
    :param f: cadeia de carateres correspondente ao nome do ficheiro de configuracao da simulacao
    :param g: inteiro correspondente ao numero de geracoes a simular
    :param v: booleano se for True ativa o modo verboso se False ativa o modo quiet
    :return: tuplo com numero de predadores e numero de presas em m, respetivamente
    """
    with open(f, 'r') as file:
        conf = file.readlines()
        a = tuple(cria_animal(eval(conf[i])[0], eval(conf[i])[1], eval(conf[i])[2]) for i in range(2, len(conf)))
        p = tuple(cria_posicao(eval(conf[i])[3][0], eval(conf[i])[3][1]) for i in range(2, len(conf)))
        m = cria_prado(eval(conf[0]), eval(conf[1]), a, p)
    for i in range(g + 1):
        if v and (i == 0 or obter_numero_predadores(m) != numero_predadores_antigo \
                  or obter_numero_presas(m) != numero_presas_antigo):
            print('Predadores: ' + str(obter_numero_predadores(m)) + ' vs Presas: ' + str(obter_numero_presas(m)) \
                  + ' (Gen. ' + str(i) + ')')
            print(prado_para_str(m))
        elif i == 0 or (i == g and not v):
            print('Predadores: ' + str(obter_numero_predadores(m)) + ' vs Presas: ' + str(obter_numero_presas(m)) \
                  + ' (Gen. ' + str(i) + ')')
            print(prado_para_str(m))
        numero_predadores_antigo = obter_numero_predadores(m)
        numero_presas_antigo = obter_numero_presas(m)
        m = cria_copia_prado(geracao(m)) if not i == g else cria_copia_prado(m)
    return (obter_numero_predadores(m), obter_numero_presas(m))




