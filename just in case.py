def prado_para_str_aux(m):
    """
    :param m: prado
    :return: cadeia de carateres correspondente a representacao do padro
    """
    for l in range(obter_tamanho_y(m)):
        for c in range(obter_tamanho_x(m)):
            if (c, l) in ((0, 0), (0, obter_tamanho_y(m) - 1), (obter_tamanho_x(m) - 1, 0), (obter_tamanho_x(m) - 1, obter_tamanho_y(m) - 1)):
                print('+', end='')
            elif (c == 0 or c == obter_tamanho_x(m) - 1) and 0 < l < obter_tamanho_y(m) - 1:
                print('|', end='')
            elif (l == 0 or l == obter_tamanho_y(m) - 1) and 0 < c < obter_tamanho_x(m) - 1:
                print('-', end='')
            elif (c, l) in m['rochedos']:
                print('@', end='')
            elif (c, l) in obter_posicao_animais(m):
                print(animal_para_char(obter_animal(m,(c,l))), end='')
            else:
                print('.', end='')
        print()


        if eh_animal_fertil(a):
            if eh_predador(a) and eh_posicao(p2) and p2 not in p3:
                a = cria_copia_animal(aumenta_fome(a))
                if eh_posicao_animal(m, p2) and eh_presa(obter_animal(m, p2)):
                    m = inserir_animal(m, cria_copia_animal(reset_idade(reset_fome(a))), p1)
                    m = mover_animal(m, p1, p2)
                    m = inserir_animal(m, reproduz_animal(a), p1)
                    p3 += (cria_copia_posicao(p2), )
                elif eh_posicao_livre(m, p2):
                    if eh_animal_faminto(a):
                        m = eliminar_animal(m, p1)
                    else:
                        m = inserir_animal(m, cria_copia_animal(reset_idade(a)), p1)
                        m = mover_animal(m , p1, p2)
                        m = inserir_animal(m, reproduz_animal(a), p1)
            else:
                m = inserir_animal(m, cria_copia_animal(reset_idade(a)), p1)
                m = mover_animal(m, p1, p2)
                m = inserir_animal(m, reproduz_animal(a), p1)
        else:
            if eh_predador(a) and eh_posicao(p2) and p2 not in p3:
                a = cria_copia_animal(aumenta_fome(a))
                if eh_posicao_animal(m, p2) and eh_presa(obter_animal(m, p2)):
                    m = inserir_animal(m, cria_copia_animal(reset_fome(a)), p1)
                    m = mover_animal(m, p1, p2)
                    p3 += (cria_copia_posicao(p2), )
                elif eh_posicao_livre(m, p2):
                    if eh_animal_faminto(a):
                        m = eliminar_animal(m, p1)
                    else:
                        m = inserir_animal(m, cria_copia_animal(a), p1)
                        m = mover_animal(m , p1, p2)
            else:
                m = inserir_animal(m, cria_copia_animal(a), p1)
                m = mover_animal(m, p1, p2)
    return cria_copia_prado(m)

    p_adj_livre = tuple(cria_copia_posicao(i) for i in obter_posicoes_adjacentes(p) if eh_posicao_livre(m,i))
    p_adj_presas = tuple(cria_copia_posicao(i) for i in obter_posicoes_adjacentes(p) if eh_posicao_animal(m, i) and eh_presa(obter_animal(m, i)))
    if (eh_presa(obter_animal(m,p)) and p_adj_livre != ()) or (eh_predador(obter_animal(m, p)) and p_adj_presas == ()):
        p = p_adj_livre[obter_valor_numerico(m, p) % len(p_adj_livre)]
        return cria_posicao(obter_pos_x(p), obter_pos_y(p))
    elif eh_predador(obter_animal(m,p)) and p_adj_presas != ():
        p = p_adj_presas[obter_valor_numerico(m,p) % len(p_adj_presas)]
        return cria_posicao(obter_pos_x(p), obter_pos_y(p))
    else:
        return cria_posicao(obter_pos_x(p), obter_pos_y(p))