<p align="center">
<img src="https://static.wixstatic.com/media/ade03f_47f0c9f925a34da58dcb9d53bda330f5~mv2.jpg/v1/fill/w_296,h_130,al_c,lg_1,q_80/ade03f_47f0c9f925a34da58dcb9d53bda330f5~mv2.webp" width="200" alt="Front-end Brasil">
</p>
<h2 align="center">Identificador de enquadramentos da comunicação política</h2>
<p align="center">:newspaper:<b> Grupo de Pesquisa em Comunicação, Internet e Política da PUC-Rio</b></p>
<p align="center">Programa de Pós-graduação em Comunicação</p>
<br>

- Doutorando: Leonardo Magalhães Firmino (PUC-Rio)
- Orientador: Prof. Arthur Ituassu (PUC-Rio)
- Coorientador: Prof. Daniel Schwabe (PUC-Rio)

## Qual o objetivo?
Software para a tese tese de doutorado do autor que identifica de forma automatizada enquadramentos genéricos da comunicação política em tweets. Os enquadramentos (ou _frames_) são formas discursivas de tratar assuntos específicos no texto. São levados em consideração os cinco frames genéricos, segundo o modelo de Semetko e Valkenburg (2000):
- Conflito
- Atribuição de responsabilidade
- Interesse humano
- Moralidade
- Consequências econômicas

## Como utilizar o identificador
O método de identificação utlizado é _dictionary based_. Para cada _frame_ definiu-se um conjunto de palavras-chave que, se presentes no texto do _tweet_, nos diz qual enquadramento foi utilizado no discurso. 

Para utilizar o presente _software_ é suficiente copiar para o arquivo _base_tweets.xlsx_ todos os tweets que se quer analisar, mantendo os cabeçalhos da planilha intactos. Salve, feche o arquivo e rode o programa _identificador_frames.py_. Ao finalizar a análise, abra novamente a planilha _base_tweets.xlsx_ para ver o resultado, que estará visível nas colunas ao lado de cada _tweet_.

### Em detalhes:
Temos dois arquivos básicos que regulam o funcionamento do identificador de _frames_: 

- _base_tweets.xlsx_
- _keyword_frames.xlsx_

O arquivo _base_tweets.xlsx_ deve conter todos os _tweets_ a analisar na coluna "_Tweets_". Copie e cole a lista de _tweets_ nesta coluna, mas **sempre mantenha a primeira linha como cabeçalho**. Ao lado de cada _tweet_ estão as colunas de resutado da análise. São cinco colunas (uma para cada enquadramento). Quando o _frame_ foi identificado no texto do _tweet_ o resultado será "1", caso contrário o valor da cela será a palavra-chave que foi usada como identificador do _frame_.

O arquivo _keyword_frames.xlsx_ contém todas as palavras-chave que irão identificar os enquadramentos nos tweets. Este arquivo pode ser editado para atualizar o método de identificação- Para garantir o correto funcionamento do programa, **não mude a estrutura do arquivo** e limite-se somente a adicionar ou eliminar palavras-chave da lista. Não deixe celas fazias entre uma palavra-chave e outra.

## Quais são os cinco enquadramentos genéricos da Comunicação Política, segundo Semetko e Valkenburg?

### 1. Conflito: 
Semetko e Valkenburg (2000) apontaram em seu estudo como o conflito constitui um enquadramento generalista, que pode ser usado em qualquer notícia para enfatizar “o conflito entre indivíduos, grupos ou instituições como um meio de capturar o interesse do público” (p. 95).

Este frame consiste em palavras que descrevem um encontro conflitivo entre forças opostas (_lado_1_ e _lado_2_, conceptualizadas coletivamente como _lados_) sobre um _problema_ ou _assunto_ disputado e/ou para atingir uma _finalidade_ específica. Tal _finalidade_ é alcançada empregando certas _ações_. Pode haver um _pensador_ que julga como positivas ou negativas as ações empregadas pelos lados em disputa.

### 2. Atribuição de responsabilidade: 
Para Semetko e Valkenburg (2000), este enquadramento apresenta uma pauta ou problema de forma a atribuir responsabilidades por consequências derivadas ou soluções a um governo, indivíduo ou grupo.

De forma específica, neste frame um _ator_ é responsável por ter realizado intencionalmente ou não uma _ação_, ou por ser o ou um instigador primário por trás de uma _causa_. Pode haver uma avaliação positiva ou negativa do _efeito_ da _ação_.

### 3. Interesse humano:
Segundo Semetko e Valkenburg (2000), o enquadramento do interesse humano “traz um rosto humano ou um ângulo emocional para a apresentação de um evento, questão ou problema […] refere-se a um esforço para personalizar as notícias, dramatizar ou 'emocionalizar'as notícias, a fim de capturar e reter o interesse do público” (p. 95).

Este quadro contém palavras gerais para indivíduos, ou seja, humanos. A _pessoa_ é concebida como independente de outros indivíduos específicos com os quais tem relações e independente de sua participação em qualquer atividade particular. Este quadro contém palavras para indivíduos como visto em termos de sua _vocação_. Uma _idade_ específica também pode ser especificada. Um _experienciador_ tem um _estado_ emocional particular, que pode ser descrito em termos de um _estímulo_ específico que o provoca, ou um _tópico_ que categoriza o tipo de _estímulo_. Em vez de expressar diretamente o _experienciador_, ele pode (metonímiamente) ter em seu lugar um _evento_ particular (com participantes da _emoção_). Eles podem ter uma _idade_, _descritor_, _origem_, _caracteristicas persistentes_ ou _etnia_.

### 4. Moralidade:
O enquadramento da moralidade trata um evento ou questão no contexto de valores, prescrições morais, mensagens normativas e princípios religiosos ou culturais (Semetko & Valkenburg, 2000, p. 96). A moralidade como enquadramento noticioso tem sido objeto de vários estudos e é comumente usada no contexto de questões como religião, minorias, drogas, pátria, família, sexualidade, reprodução e gênero.

Neste frame, um _valor_ é descrito por um juiz (geralmente implícito) no que diz respeito à moralidade de um _comportamento_. As palavras neste enquadramento descrevem o status de uma ação em relação a um _código de leis_ ou regras. Um _objeto_ também pode estar em violação ou cumprimento do código em virtude de sua existência, localização ou posse.

### 5. Consequências econômicas: 
Conforme definido por Semetko e Valkenburg (2000), o frame das consequências econômicas “relata um evento, problema ou problema em termos das consequências que ele terá economicamente sobre um indivíduo, grupo, instituição, região ou país” (p. 96).

Uma _região política_, geralmente uma nação, tem um sistema econômico, a _economia_, definida pelo nível de produção e consumo de bens e serviços, que é afetada por algum _causador_ interno ou externo. O _dinheiro_ refere-se a um meio usado para trocar mercadorias e serviços. Na maioria dos casos, é emitido pelo governo, seu _criador_, na forma de moedas e notas. Quantidades particulares podem ter um uso designado ou planejado, ou podem ter vindo de alguma _origem_.

### Referência bibliográfica
SEMETKO, Holli A; VALKENBURG, Patti M. Framing European Politics: A Content Analysis of Press and Television News. Journal of Communication, pp. 93-109, 2000.
