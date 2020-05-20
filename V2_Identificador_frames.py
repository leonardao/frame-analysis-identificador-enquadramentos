# -*- coding: utf-8 -*-
import openpyxl
import re
import unicodedata
import string
import time

def depurador ( tweet_original ):

    # Elimina nomes de @usuário, #hashtags e "RT".
    limpo = ' '.join ( re.sub ( "(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|(\w+:\/\/\S+)|(RT)", " ", tweet_original ).split () )

    # Elimina letras com acento e converte tudo em minúsculas.
    limpo = ''.join ( ( frase for frase in unicodedata.normalize ( 'NFD', limpo ) if unicodedata.category ( frase ) != 'Mn') ).lower ()

    # Elinima pontuação e substitui por espaço.
    for i in limpo:
        if i in string.punctuation:
            limpo = limpo.replace ( i, " " )

    # Elimina espaço repetido entre palavras
    limpo = limpo.replace ( "   ", " " )
    limpo = limpo.replace ( "  ", " " )

    return limpo

contador = time.time()

# Lê a planilha XLSX.
base_tweets = openpyxl.load_workbook ( "Exemplo_base_tweets_COVID-19.xlsx" )

# Lê a aba "tweets" do arquivo XLSX.
tweets = base_tweets ['tweets']

# Frames e suas listas de palavras-chave
kw_respo = ['criar', 'criou', 'configur', 'da origem', 'dar origem', 'deu origem', 'dei origem', 'dara origem', 'darão origem', 'elabor', 'estabelece', 'fundou', 'fundar', 'fundara', 'fundei', 'invent', 'produz', 'prepar', 'conduz', 'coorden', 'dirigi', 'desempenh', 'empreende', 'execut', 'prend', 'apreend', 'autor', 'promov', 'realiz', 'caus', 'efeito', 'afet', 'consequência', 'culmin', 'desencad', 'deix', 'ter sido', 'efeito', 'gerar', 'gerou', 'gerando', 'gerei', 'medida', 'provoc', 'responsabilidade', 'result', 'torn', 'graças', 'culpa', 'reduz', 'aument', 'quebr', 'alter', 'modifi', 'transform', 'preso', 'presa', 'detid', 'acusa', 'julg', 'conden', 'puni', 'absolv', 'inocent']
kw_confl = ['paz', 'pacificaç', 'briga', 'brigou', 'conflit', 'confront', 'desentend', 'discussão', 'discut', 'debate', 'bate boca', 'rixa', 'disput', 'desavença', 'hostil', 'agress', 'violen', 'contenda', 'insult', 'mordida', 'morder', 'morde', 'tumult', 'xing', 'insult', 'ofend', 'oponente', 'adversário', 'desafi', 'enfrent', 'peite', 'peita', 'peitar', 'peitou', 'diverg', 'revog', 'suspend', 'obstrui', 'demit', 'estrangul', 'asfixi', 'interv', 'batalh', 'facção', 'luta', 'lutei', 'lutou', 'guerra', 'exército', 'arma', 'combat', 'inimigo', 'aliado', 'soldado', 'linha de frente', 'bélico', 'dispar', 'bala perdida', 'balas perdidas', 'balea', 'tiros', 'tiro de', 'projéteis', 'projétil', 'granada', 'explo', 'enfrent', 'golpe', 'defesa', 'defend', 'atacar', 'atacou', 'ataq', 'UPP', 'delegacia', 'batalhão', 'invad', 'invas', 'comando', 'BOPE', 'facada', 'esfaq', 'bloque', 'derrub', 'elimin', 'estratégia', 'tática', 'modo de', 'modo para', 'maneira de', 'maneira para', 'manobr', 'comissão', 'método', 'substitui', 'eleiç', 'isola', 'distância social', 'jogo', 'gol', 'a favor', 'contra', 'concord', 'discord', 'intrigas', 'uma intriga', 'a  intriga', 'de intriga', 'da intriga', 'alguma intriga', 'ofend', 'ofensa', 'revolta', 'espião', 'espio', 'vazajato', 'vaza jato', 'litigio', 'divórci', 'ditadura', 'autoritarismo', 'regime militar', 'plutocracia', 'cleptocracia', 'necropolítica', 'toma lá dá cá', 'negociata', 'Mensalão', 'Petrolão', 'delação', 'fraude', 'propina', 'perdão']
kw_human = ['mort', 'vida', 'sentir', 'emoção', 'sonho', 'pesadelo', 'velório', 'enterro', 'parto', 'aptidão', 'apto', 'apta', 'capacit', 'incompet', 'o dom', 'um dom', 'cesta básica', 'habilid', 'incapa', 'poder', 'talento', 'chor', 'riso', 'rir', 'riu', 'doce', 'amargo', 'perfume', 'fedor', 'sabor', 'vista', 'áspero', 'espetacul', 'terror', 'astral', 'calma', 'consol', 'emoc', 'entusiasm', 'experiencia', 'ira', 'orgulho', 'prazer', 'sensação', 'sentiment', 'tranquiliz', 'paix', 'ódio', 'desfrut', 'distrai', 'diverti', 'confundi', 'deslumbr', 'intrigando', 'introgou', 'preocup', 'abala', 'abat', 'aborrec', 'admir', 'aflição', 'aflit', 'afobad', 'agitad', 'agonia', 'agoniz', 'alarma', 'alegr', 'amarg', 'ambi', 'medo', 'amedront', 'amor', 'angústi', 'ansi', 'antipáti', 'psicopat', 'assust', 'atordoa', 'atorment', 'o bem', 'um bem', 'o mal ', 'um mau', 'um mal ', 'brav', 'chato', 'chate', 'choca', 'doído', 'acontent', 'contente', 'cordial', 'curios', 'decaden', 'decepcion', 'deleit', 'demoli', 'depress', 'desagrad', 'desanim', 'desapont', 'desconcert', 'desconfi', 'desconfort', 'desconsol', 'descontent', 'descontr', 'desencoraj', 'desesper', 'desgost', 'desola', 'desorient', 'devast', 'diversão', 'diverti', 'doloros', 'dor', 'embaraçad', 'embaraço', 'emocion', 'encant', 'enfurec', 'enjo', 'entedi', 'entret', 'entristec', 'envergonh', 'esmagado', 'espant', 'estress', 'estupefa', 'eufori', 'exasper', 'exaust', 'excita', 'extas', 'fart', 'fascin', 'felic', 'felis', 'feliz', 'ferid', 'furi', 'gratific', 'horror', 'humil', 'inconsol', 'indign', 'dign', 'inquiet', 'insípid', 'sem sal', 'interesseir', 'ira', 'irrit', 'jubil', 'lívid', 'lúgubr', 'de luto', 'maravilh', 'mau', 'melancóli', 'miserável', 'nervos', 'ofend', 'ofensa', 'perplex', 'perturb', 'petrific', 'preocup', 'radiante', 'raiv', 'relax', 'repuls', 'ressenti', 'revolta', 'saquea', 'saqueio', 'satisf', 'simpati', 'sofr', 'sombri', 'surpreend', 'surpres', 'transtorn', 'traumatiz', 'trist', 'vexação', 'zangad', 'jovem', 'idoso', 'bebê', 'criança', 'adulto', 'menino', 'garoto', 'homem', 'mulher', 'cara', 'caráter', 'companheiro', 'cidadão', 'cavalheiro', 'dama', 'colega', 'pessoa', 'moç', 'casal', 'irmã', 'pai', 'mãe', 'filh', 'avó', 'tia', 'tio', 'sobrinh', 'net', 'ninguém', 'alguém', 'quem', 'povo', 'persona', 'individu', 'galera', 'gente', 'aventur', 'banhista', 'foli', 'gamer', 'geek', 'jogador', 'naturista', 'turista', 'viajante', 'visitante', 'caipira', 'escrav', 'mendig', 'pedinte', 'senhor', 'cigano', 'índio', 'negro', 'alagoan', 'alemã', 'american', 'austríac', 'bolivian', 'brasileir', 'britânic', 'californian', 'carioca', 'espanhol', 'estrangeir', 'ET', 'francês', 'holandês', 'chinês', 'japonês', 'inca', 'índio', 'inglês', 'zelador', 'bandid', 'traficante', 'milician', 'assassin', 'ladra', 'estelionatári', 'golpista', 'maconheir', 'cheirad', 'drogad', 'alcoólatra', 'viciad', 'tabagista', 'anoréxic', 'bulímic', 'compulsiv', 'gulos', 'gostos', 'put', 'vagabund', 'piranha', 'fdp', 'filho da puta', 'filha da puta', 'viad', 'bixa', 'gay', 'lésbica', 'travesti', 'traveco', 'LGBT', 'LGBTI+', 'homossexual', 'preguiç', 'nervos', 'vaid', 'ambic', 'safad', 'vergonh', 'um merda', 'herói', 'gordo', 'gorda', 'obeso', 'obesa', 'magr', 'sarad', 'bonit', 'feio', 'feia', 'mito', 'iranian', 'irlandês', 'italian', 'mexican', 'nova iorquin', 'otoman', 'persa', 'português', 'quenian', 'turc', 'batist', 'budista', 'católic', 'cristã', 'espírita', 'fanático', 'fiel', 'infiel', 'islami', 'judeu', 'laico', 'mórmon', 'mulçuman', 'pagã', 'protestante', 'umbandist', 'macumbeir', 'batista', 'abade', 'sacerdote', 'profet', 'presbíter', 'acadêmic', 'advogad', 'agente duplo', 'agente', 'alfaiate', 'alun', 'ambientalista', 'antropólog', 'apóstol', 'arqueólog', 'arquitet', 'artesã', 'artista', 'assistente', 'astrólog', 'astronauta', 'atendente', 'ator', 'atriz', 'autor', 'bancário', 'barman', 'beat', 'bibliotecári', 'biólog', 'bispo', 'boleir', 'bombeir', 'cabeleireir', 'caçador', 'camareir', 'cantor', 'capitã', 'cardeal', 'carpinteir', 'cartógraf', 'chefe', 'cientista', 'cirurgiã', 'comerciante', 'comissári', 'consultor', 'contador', 'correspondente', 'costureir', 'coveir', 'cozinheir', 'dançarin', 'delegad', 'dentista', 'deputad', 'desenhista', 'desenvolvedor', 'detetive', 'diácon', 'diretor', 'docente', 'dona de casa', 'editor', 'educador', 'empregad', 'empresári', 'enfermeir', 'engenheir', 'escritor', 'escriturári', 'especialista', 'especulador', 'espiã', 'esteticista', 'estudante', 'executiv', 'explorador', 'extrativist', 'farmacêutic', 'faxineir', 'fazendeir', 'físico', 'fisioterapeuta', 'fotógraf', 'freira', 'frentista', 'funcionári', 'gaitista', 'garço', 'garimpeir', 'gerente', 'guarda-costas', 'guia turístico', 'o guia', 'a guia', 'historiador', 'instrumentista', 'jardineir', 'joalheiro', 'jornalista', 'juiz', 'lançador', 'linguista', 'mágico', 'magistrad', 'magnata', 'malabarist', 'manobrist', 'maqueir', 'maquinista', 'matemático', 'mecânico', 'médic', 'médium', 'mergulhador', 'mineir', 'ministr', 'missionári', 'monge', 'monsenhor', 'motorista', 'músico', 'neurocientista', 'oficial', 'operador', 'operário', 'padeir', 'padre', 'palestrante', 'palhaç', 'paraquedist', 'pastor', 'pedreir', 'pesquisador', 'piloto', 'pintor', 'pirata', 'poet', 'polícia', 'policial', 'político', 'porta-voz', 'prefeit', 'produtor', 'professor', 'profissional', 'programador', 'psicólog', 'psiquiatra', 'químico', 'radialista', 'recepcionista', 'repórter', 'secretári', 'segurança', 'senador', 'seringueir', 'servente', 'servidor', 'sociologo', 'sociologa', 'espectador', 'socorrista', 'soldado', 'tabeliã', 'taxista', 'técnico', 'toxicologista', 'trabalhador', 'vendedor', 'veterinári', 'voluntári']
kw_moral = ['absurd', 'étic', 'mau', 'canalha', 'degenerad', 'deprava', 'descente', 'desonr', 'honr', 'generos', 'horror', 'imoral', 'imprópri', 'escrup', 'iníqu', 'insidios', 'íntegro', 'just', 'maldos', 'moral', 'nefast', 'obscen', 'peca', 'pervers', 'réprob', 'repulsiv', 'virtuos', 'bom', 'julga', 'lament', 'atroz', 'bárbaro', 'bondoso', 'compaixão', 'compassiv', 'cruel', 'desrespeit', 'horrível', 'incivil', 'corrupt', 'decente', 'dign', 'miser', 'normal', 'novo', 'porcaria', 'a verdade', 'violent', 'dissimulad', 'sincer', 'brutal', 'selvag', 'arrepend', 'culpa', 'perdão', 'perdoa', 'perdoe', 'peniten', 'remorso', 'macumbeir', 'batist', 'budis', 'candomblé', 'catolic', 'cristã', 'espirit', 'fanatic', 'fiel', 'infiel', 'isla', 'judaismo', 'judeu', 'judia', 'laic', 'mórmon', 'mulçuman', 'pagão', 'religiões pagãs', 'religião pagã', 'protestant', 'umband', 'abade', 'sacerdote', 'profeta', 'presbíter', 'satanista', 'padre', 'coroinha', 'crente', 'pentecostal', 'credo', 'crença', 'devot', 'fé ', 'fiel', 'peca', 'Deus', 'Jesus', 'Cristo', 'Santíssim', 'Trindade', 'cruz ', 'missa', 'batismo', 'funeral', 'comunhão', 'Maria Madalena', 'Nossa Senhora', 'Virgem Maria', 'Maria de Nazaré', 'sant', 'pecador', 'anjo', 'querubim', 'Lúcifer', 'Demôni', 'Diab', 'Capeta', 'Capiroto', 'angé', 'infern', 'para o céu', 'aos céus', 'ao céu', 'pro céu', 'paraíso', 'purgatório', 'demiurgo', 'igreja', 'sinagoga', 'terreiro', 'despacho', 'encruzilhada', 'templo', 'altar', 'hóstia', 'orixá', 'espírit', 'alma', 'chakra', 'Exu', 'Ogum', 'Oxóssi', 'Xangô', 'Oxumaré', 'Oyá', 'Iansã', 'Oxum', 'Iemanjá', 'Oxalá', 'preto velho', 'erê', 'egum', 'pomba-gira', 'queer', 'aborto', 'gostos', 'put', 'vagabund', 'piranha', 'fdp', 'filho da puta', 'filha da puta', 'viad', 'bixa', 'gay', 'lésbica', 'travesti', 'traveco', 'LGBT', 'LGBTI+', 'homossexual', 'safad', 'sem vergonha', 'virgem', 'cabaço', 'família', 'casal', 'adoção', 'casamento', 'matrimonio', 'divórci', 'casal', 'união estável', 'pátria', 'nossa bandeira', 'jamais será vermelha', 'verde e amarelo', 'ilegal', 'legali', 'devido processo', 'golpe', 'AI5', 'ditadura', 'autoritarismo', 'regime militar', 'democracia', 'plutocracia', 'cleptocracia', 'necropolítica', 'toma lá dá cá', 'negociata', 'Mensalão', 'Petrolão', 'delação', 'fraude', 'propina', 'igualdade', 'liberdade', 'justiça', 'bondade', 'carid', 'doação', 'esmola', 'ensinar a pescar', 'vilão', 'malfeitor', 'delinquente', 'bandid', 'maçã podre']
kw_econo = ['economi', 'dinheiro', 'fundo', 'verba', 'crise', 'recess', 'PIB', 'Produto Interno Bruto', 'balança comercial', 'mercosul', 'bolsa em queda', 'bolsa em alta', 'bolsa de valores', 'incentivo fiscal', 'renúncia fiscal', 'invest', 'queda prod', 'aumento prod', 'produtiv', 'imposto', 'subsídi', 'negócio', 'empres', 'multinacional', 'empreend', 'emprego', 'trabalh', 'desemprego', 'demissão', 'demit', 'contrat', 'mercado', 'bolsa de estudos', 'bolsa família', 'bolsa de pesquisa', 'empobrecer', 'enriquecer', 'misér', 'fome', 'desigual', 'pobre', 'riqueza', 'rico', 'superavit', 'juros', 'taxa', 'alíquota', 'parcela', 'mensalidade', 'anuidade', 'contas', 'embarg', 'lucro', 'dividendo', 'liquidez', 'cheque', 'moeda', 'câmbio', 'dólar', 'euro', 'finanç', 'fundo de investimento', 'CDB', 'CDI', 'debenture', 'imobiliár', 'imóvel', 'valor', 'conta', 'poupança', 'produto', 'produção', 'cliente', 'compra', 'comsum', 'pagamento', 'pagar', 'cobrar', 'dívida', 'débito', 'crédito', 'crediário', 'comerci', 'leilão', 'promoç', 'venda de', 'vender', 'vendo', 'cobrar', 'preço', 'serviço', 'tarifa', 'custo', 'custo benefício', 'conta', 'boleto', 'máquina de cartão', 'maquinha de cartão', 'insumo', 'mercadoria', 'financia', 'fali', 'importa', 'exporta', 'privatiz', 'alug', 'agro', 'pecuári', 'agricultura', 'pequeno produtor', 'pequenos produtores', 'grandes produtores', 'grande produtor', 'indústria', 'loja', 'black friday', 'mercadinho', 'mercado']

resultado = []

# ciclo que passa as linha da aba "tweets".
for linha_t in range ( 2, tweets.max_row + 1 ):

    # Pega o tweet da planilha depura o texto e o transforma em uma lista de palavras.
    texto = str ( tweets.cell ( row = linha_t, column = 1 ).value )
    #print ( "TWEET [{}]: {}".format ( linha_t - 1, texto ) )
    texto = depurador ( texto ).split()

    # Frame da ATRIBUIÇÃO DE RESPONSABILIDADE: Busca no tweet as palavras-chave
    for tweet in texto:
        for keyword in kw_respo:
            keyword = depurador ( keyword )
            if re.match ( keyword, tweet ):
                resultado.append ( tweet )
    if resultado:
        #print ( 'Resultado: {}'.format ( resultado ) )
        tweets.cell ( linha_t, 2, value = ", ".join ( resultado ) )
    else:
        tweets.cell ( linha_t, 2, value = "0" )
    resultado.clear()

    # Frame do CONFLITO: Busca no tweet as palavras-chave
    for tweet in texto:
        for keyword in kw_confl:
            keyword = depurador ( keyword )
            if re.match ( keyword, tweet ):
                resultado.append ( tweet )
    if resultado:
        #print ( 'Resultado: {}'.format ( resultado ) )
        tweets.cell ( linha_t, 3, value = ", ".join ( resultado ) )
    else:
        tweets.cell ( linha_t, 3, value = "0" )
    resultado.clear()

    # Frame do INTERESSE HUMANO: Busca no tweet as palavras-chave
    for tweet in texto:
        for keyword in kw_human:
            keyword = depurador ( keyword )
            if re.match ( keyword, tweet ):
                resultado.append ( tweet )
    if resultado:
        #print ( 'Resultado: {}'.format ( resultado ) )
        tweets.cell ( linha_t, 4, value = ", ".join ( resultado ) )
    else:
        tweets.cell ( linha_t, 4, value = "0" )
    resultado.clear ()

    # Frame da MORALIDADE: Busca no tweet as palavras-chave
    for tweet in texto:
        for keyword in kw_moral:
            keyword = depurador ( keyword )
            if re.match ( keyword, tweet ):
                resultado.append ( tweet )
    if resultado:
        #print ( 'Resultado: {}'.format ( resultado ) )
        tweets.cell ( linha_t, 5, value = ", ".join ( resultado ) )
    else:
        tweets.cell ( linha_t, 5, value = "0" )
    resultado.clear ()

    # Frame das CONSEQUÊNCIAS ECONÔMICAS: Busca no tweet as palavras-chave
    for tweet in texto:
        for keyword in kw_econo:
            keyword = depurador ( keyword )
            if re.match ( keyword, tweet ):
                resultado.append ( tweet )
    if resultado:
        #print ( 'Resultado: {}'.format ( resultado ) )
        tweets.cell ( linha_t, 6, value = ", ".join ( resultado ) )
    else:
        tweets.cell ( linha_t, 6, value = "0" )
    resultado.clear ()

# Salva e fecha arquivos
base_tweets.save (filename = "Exemplo_base_tweets_COVID-19.xlsx")
print("--- %s segundos ---" % (time.time() - contador))