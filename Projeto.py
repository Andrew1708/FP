def cria_posicao(x, y):
    """
    A representacao da TAD posicao eh um tuplo de comprimento 2 cuja primeira entrada corresponde a posicao de x e a\
    segunda entrada a posicao de y
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
        raise ValueError('cria_copia_posicao: argumentos invalidos')


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
    # Tuplo auxiliar que filtra posicoes adjacentes possiveis (cujas pos_x e pos_y sao maiores ou iguais a 0)
    aux = tuple(filter(lambda x: x[0] >= 0 and x[1] >= 0, ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y))))
    return tuple(cria_posicao(i[0], i[1]) for i in aux)


def ordenar_posicoes(t):
    """
    :param t: tuplo contendo posicoes
    :return: tuplo contendo as mesmas posicoes de t ordenadas de acordo com a ordem de leitura do prado
    """
    aux = tuple((obter_pos_x(i), obter_pos_y(i)) for i in t)  # Tuplo auxiliar com todas a posicoes de t
    # Ordena-se o tuplo aux com a funcao sorted, primeiro apenas tendo em conta pos_y (do menor para o maior)\
    # depois as posicoes com o mesma pos_y sao ordenadas tendo em conta pos_x (do menor para o maior)
    aux_ordenado = tuple(sorted(aux, key=lambda x: (x[1], x[0])))
    return tuple(cria_posicao(i[0], i[1]) for i in aux_ordenado)


def cria_animal(s, r, a):
    """
    A representacao da TAD animal eh um lista de comprimento 5 cuja primeira entrada eh uma string correspondente ao\
    nome da especie (s), a segunda eh um inteiro correspondente a frequencia de reproducao (r), a terceira um inteiro\
    correspondente a frequencia de alimentacao (a), a quarta um inteiro correspondente a idade do animal (incializada a\
    zero) e a quinta um inteiro correspondente a fome do animal (tambem inicializada a zero)
    :param s: str nao vazia correspondente a especie do animal
    :param r: int maior que 0 correspondente a frequencia de reproducao
    :param a: int maior ou igual que 0 corresponden a frequencia de alimentacao
    :return: animal
    """
    if isinstance(s, str) and len(s) != 0 and isinstance(r, int) and r > 0 \
            and isinstance(a, int) and a >= 0:
        return [s, r, a, 0, 0]
    else:
        raise ValueError('cria_animal: argumentos invalidos')


def cria_copia_animal(a):
    """
    :param a: animal
    :return: animal copia de a
    """
    if eh_animal(a):
        return [obter_especie(a), obter_freq_reproducao(a), obter_freq_alimentacao(a), obter_idade(a), obter_fome(a)]
    else:
        raise ValueError('cria_copia_animal: argumentos invalidos')


def obter_especie(a):
    """
    :param a: animal
    :return: cadeia de carateres correspondente a especie do animal
    """
    return a[0]


def obter_freq_reproducao(a):
    """
    :param a: animal
    :return: inteiro correspondente a frequencia de reproducao do animal
    """
    return a[1]


def obter_freq_alimentacao(a):
    """
    :param a: animal
    :return: inteiro correspondente a frequencia de alimentacao do animal
    """
    return a[2]


def obter_idade(a):
    """
    :param a: animal
    :return: inteiro correspondente a idade do animal
    """
    return a[3]


def obter_fome(a):
    """
    :param a: animal
    :return: inteiro correspondente a fome do animal
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
    # Apenas os animais predadores (com frequencia de alimentacao > 0) eh que tem fome
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
    :return: primeiro carater da especie do animal 'a', maiuscula caso a seja predador e miniscula se for presa
    """
    return obter_especie(a)[0].upper() if eh_predador(a) else obter_especie(a)[0].lower()


def animal_para_str(a):
    """
    :param a: animal
    :return: cadeia de carateres que corresponde a 'especie [idade/freq de reproducao;fome/freq de alimentacao]' no\
    caso de a ser predador, 'especie [idade/freq de reproducao]' no caso de ser presa
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
    A representacao do TAD prado consite num dicionario de 4 chaves: as chaves 'x' e 'y' que contem os valores pos_x\
    e pos_y, respetivamente, de d; a chave 'rochedos' cujo valor eh d; a chave 'animais' cuja valor eh um dicionario\
    cujas chaves sao posicoes que contem animais (dado por p) e o valor o respetivo animal que se encontra nessa\
    posicao (dado por a)
    :param d: posicao correspondente a posicão que ocupa a montanha do canto inferior direito do prado
    :param r: tuplo de 0 ou mais posicoes correspondentes aos rochedos que nao sao as montanhas dos limites exteriores\
    do prado
    :param a: tuplo de 1 ou mais animais
    :param p: tuplo da mesma dimensao do tuplo a com as posicoes correspondentes ocupadas pelos animais
    :return: prado
    """
    if eh_posicao(d) and isinstance(r, tuple) and ((all(eh_posicao(i) for i in r) \
                                                    and all(0 < obter_pos_x(i) < obter_pos_x(d) \
                                                            and 0 < obter_pos_y(i) < obter_pos_y(d) for i in r)) \
                                                   or r == ()) and isinstance(a, tuple) and len(a) >= 1 \
            and all(eh_animal(i) for i in a) and isinstance(p, tuple) and len(p) == len(a) \
            and all(eh_posicao(i) for i in p) and all(0 < obter_pos_x(i) < obter_pos_x(d) \
                                                      and 0 < obter_pos_y(i) < obter_pos_y(d) for i in p) \
            and all(i not in r for i in p):
        prado = {'x': obter_pos_x(d), 'y': obter_pos_y(d), 'rochedos': r,\
                 'animais': {p[i]: a[i] for i in range(len(a))}}
        return prado
    else:
        raise ValueError('cria_prado: argumentos invalidos')


def cria_copia_prado(m):
    if eh_prado(m):
        return {'x': m['x'], 'y': m['y'], 'rochedos': m['rochedos'], 'animais': m['animais']}
    else:
        raise ValueError('cria_copia_prado: argumentos invalidos')


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
    res = 0  # Variavel que serve como contador
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
    m['animais'][p2] = m['animais'][p1]  # Adicionamos o animal que estava em p1 em p2
    if not posicoes_iguais(p1, p2):  # Eliminamos o animal que se encontrava na posicao p1, mas no caso das posicoes
        eliminar_animal(m, p1)  # p1 e p2 serem iguais, i.e., o animal nao se move, nao o apagamos
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
           and (all(eh_posicao(i) and 0 < obter_pos_x(i) < arg['x'] and 0 < obter_pos_y(i) < arg['y']\
                    for i in arg['rochedos']) or arg['rochedos'] == ()) and 'animais' in arg\
           and isinstance(arg['animais'], dict)\
           and ((all(eh_posicao(i) and 0 < obter_pos_x(i) < arg['x'] and 0 < obter_pos_y(i) < arg['y']\
                     for i in arg['animais'].keys())\
                 and all(eh_animal(i) for i in arg['animais'].values())) or arg['animais'] == {})


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
    return eh_prado(m) and not eh_posicao_animal(m, p) and not eh_posicao_obstaculo(m, p)


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
            p = cria_posicao(c, l)
            # Cantos correspondem aos pontos (0, 0), (0, Ny - 1), (Nx - 1, 0) e (Nx - 1, Ny - 1)
            if p in (cria_posicao(0, 0), cria_posicao(0, obter_tamanho_y(m) - 1),\
                     cria_posicao(obter_tamanho_x(m) - 1, 0),\
                     cria_posicao(obter_tamanho_x(m) - 1, obter_tamanho_y(m) - 1)):
                prado += '+'
            # Arestas verticais
            elif (obter_pos_x(p) == 0 or obter_pos_x(p) == obter_tamanho_x(m) - 1)\
                    and 0 < obter_pos_y(p) < obter_tamanho_y(m) - 1:
                prado += '|'
            # Arestas horizontais
            elif (obter_pos_y(p) == 0 or obter_pos_y(p) == obter_tamanho_y(m) - 1)\
                    and 0 < obter_pos_x(p) < obter_tamanho_x(m) - 1:
                prado += '-'
            # Rochedos
            elif eh_posicao_obstaculo(m, p):
                prado += '@'
            # Animais
            elif eh_posicao_animal(m, p):
                prado += animal_para_char(obter_animal(m, p))
            # Espacos livres
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
    # Tuplo com as posicoes adjacente ao ponto p que se encontram livres
    p_adj = tuple(filter(lambda x: eh_posicao_livre(m, x), obter_posicoes_adjacentes(p)))
    if eh_posicao_animal(m,p) and eh_presa(obter_animal(m, p)) and p_adj != ():
        p = p_adj[N % len(p_adj)]
    if eh_posicao_animal(m,p) and eh_predador(obter_animal(m, p)):
        # Tuplo contendo todas as posicoes adjacentes ao ponto p que contem presas, pois, no caso do animal em p ser um\
        # predador ele ira dar prioridade as presas
        p_adj_presas = tuple(filter(lambda x: eh_presa(obter_animal(m, x)),\
                                    filter(lambda x: eh_posicao_animal(m, x), obter_posicoes_adjacentes(p))))
        if p_adj_presas != ():
            p = p_adj_presas[N % len(p_adj_presas)]
        # No caso de nao haver presas a volta do predador, este move-se para um local livre
        elif p_adj != ():
            p = p_adj[N % len(p_adj)]
    # No fim, se o p nao for alterado, a funcao devolve o ponto inicial,  i.e., o animal nao se move
    return cria_posicao(obter_pos_x(p), obter_pos_y(p))


def geracao(m):
    """
    :param m: prado
    :return: prado após uma geracao
    """
    aux = ()  # Lista auxiliar que serve para guardar as posicoes dos predadores quando comem presas, para que, no caso\
    # do predador comer uma presa que não se tenha movido na geracao este nao se movimente 2 vezes.
    for p1 in obter_posicao_animais(m):  # Posicao inicial
        p2 = obter_movimento(m, p1)  # Posicao final
        a = aumenta_idade(obter_animal(m, p1))
        if eh_presa(a):
            # No caso do animal ser fertil e as posicoes p1 e p2 serem diferentes (i.e., o animal move-se): inserimos\
            # o animal com reset de idade, movemo-lo para a posicao p2 e adicionamos a cria deste animal em p1.\
            # Caso contrario, apenas inserimos o animal envelhecido e movemo-lo para p2.
            m = inserir_animal(mover_animal(inserir_animal(m, reset_idade(a), p1), p1, p2), reproduz_animal(a), p1)\
                if eh_animal_fertil(a) and not posicoes_iguais(p1, p2)\
                else mover_animal(inserir_animal(m, a, p1), p1, p2)
        # Verificamos que se trata de um predador e que este aida nao se moveu
        if eh_predador(a) and not any(posicoes_iguais(p1, i) for i in aux):
            a = aumenta_fome(a)
            # Significa que vai comer uma presa - a primeira condicao so se verifica quando p2 for a posicao de uma\
            # presa ou se o predador nao se mexer (p1 == p2), a segunda condicao previne essa situacao
            if any(posicoes_iguais(p2, i) for i in obter_posicao_animais(m)) and not posicoes_iguais(p1, p2):
                # Resetamos a fome do predador e movemo-lo para p2, caso seja fertil, reproduz-se e faz reset na idade
                m = inserir_animal(mover_animal(inserir_animal(m, reset_idade(reset_fome(a)), p1), p1, p2), reproduz_animal(a), p1)\
                    if eh_animal_fertil(a) else mover_animal(inserir_animal(m, reset_fome(a), p1), p1, p2)
                aux += (p2, )
            # No caso do predador nao comer ninguem
            else:
                # Se estiver faminto eh eliminado
                if eh_animal_faminto(a):
                    m = eliminar_animal(m, p1)
                else:
                    # Caso contrario move-se e, se for fertil e p1 != p2, reproduz-se e faz reset na idade
                    m = inserir_animal(mover_animal(inserir_animal(m, reset_idade(a), p1), p1, p2), reproduz_animal(a),
                                       p1) \
                        if eh_animal_fertil(a) and not posicoes_iguais(p1,p2)\
                    else mover_animal(inserir_animal(m, a, p1), p1, p2)
    return m


def simula_ecossistema(f, g, v):
    """
    :param f: cadeia de carateres correspondente ao nome do ficheiro de configuracao da simulacao
    :param g: inteiro correspondente ao numero de geracoes a simular
    :param v: booleano se for True ativa o modo verboso se False ativa o modo quiet
    :return: tuplo com numero de predadores e numero de presas em m, respetivamente
    """
    with open(f, 'r') as file:
        conf = file.readlines()
        # Tuplo que contem os animais
        a = tuple(cria_animal(eval(conf[i])[0], eval(conf[i])[1], eval(conf[i])[2]) for i in range(2, len(conf)))
        # Tuplo que contem as respetivas posicoes dos animais
        p = tuple(cria_posicao(eval(conf[i])[3][0], eval(conf[i])[3][1]) for i in range(2, len(conf)))
        m = cria_prado(eval(conf[0]), eval(conf[1]), a, p)
    for i in range(g + 1):
        # 'i==0' pois queremos sempre visualizar o prado na geracao: 0
        if v:  #and (i == 0 or obter_numero_predadores(m) != numero_predadores_antigo \
                  #or obter_numero_presas(m) != numero_presas_antigo):
            print('Predadores: ' + str(obter_numero_predadores(m)) + ' vs Presas: ' + str(obter_numero_presas(m)) \
                  + ' (Gen. ' + str(i) + ')')
            print(prado_para_str(m))
        elif i == 0 or (i == g and not v):
            print('Predadores: ' + str(obter_numero_predadores(m)) + ' vs Presas: ' + str(obter_numero_presas(m)) \
                  + ' (Gen. ' + str(i) + ')')
            print(prado_para_str(m))
        # Guarda o numero de predadores e de presas da geracao atual, para podermos comparar com a proxima
        numero_predadores_antigo = obter_numero_predadores(m)
        numero_presas_antigo = obter_numero_presas(m)
        m = geracao(m) if not i == g else m  # No fim, nao avancamos na geracao de modo a retornar o numero de presas\
        # e predadores da geracao: g
    return (obter_numero_predadores(m), obter_numero_presas(m))

