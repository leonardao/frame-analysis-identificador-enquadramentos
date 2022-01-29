<p align="center">
 <img src="https://github.com/leonardao/frame-analysis-identificador-enquadramentos/blob/master/logo-comp-ppgcom-puc-rio.webp" width="200" alt="Logo COMP Grupo de Pesquisa em Comunicação, Internet e Política PPGCOM PUC-Rio">
</p>
<h2 align="center">Identificador de enquadramentos genéricos e específicos da comunicação política</h2>
<p align="center">:newspaper:<b> Grupo de Pesquisa em Comunicação, Internet e Política da PUC-Rio</b></p>
<p align="center">Programa de Pós-graduação em Comunicação</p>
<br>

- Doutorando: Leonardo Magalhães Firmino (PUC-Rio)
- Orientador: Prof. Arthur Ituassu (PUC-Rio)
- Coorientador: Prof. Daniel Schwabe (PUC-Rio)

## Qual o objetivo?
Software de análise para a pesquisa de doutorado do autor (defendida no dia 3 de fevereiro de 2022) que identifica de forma automatizada enquadramentos genéricos da comunicação política em qualquer tipo de unidade de análise textual em língua portuguesa. Os quadros (ou _frames_) são pontos de vista selecionados e destacados na comunicação ao tratar assuntos específicos. Portanto, para Entman (1993, p.52), enquadrar uma questão significa: 

"_selecionar alguns aspectos da realidade percebida e torná-los mais relevantes em um texto comunicativo, a fim de promover uma definição de problema particular, interpretação causal, avaliação moral e/ou recomendação de tratamento para a questão descrita_".

O presente _script_ em Python identifica 3 _frames_ genéricos e 3 específicos sobre o tema da saúde.

Os 3 _frames_ genéricos podem ser aplicados a qualquer tema de estudo, como proposto por Semetko e Valkenburg (2000):
- Conflito
- Atribuição de responsabilidade
- Moralidade

Os três _frames_ específicos servem apenas para o estudo tema da saúde em contextos de epidemias como a da Covid-19: 
- Consequências da pandemia
- Medidas de contenção
- Métodos de tratamento

## Como utilizar o identificador
O método de identificação utlizado é _dictionary_ _based_. Para cada _frame_ definiu-se um conjunto de palavras-chave que, se presentes no texto do _tweet_, nos diz qual enquadramento foi utilizado no discurso. 

Embora a pesquisa doutoral do autor tenha analisado cerca de 36 milhões de _tweets_, com o fim de facilitar o trabalho daqueles que queiram testar o presente identificador de enquadramentos, esta versão do _script_ que está sendo disponibilizada foi desenvolvida para a aplicação em volumes pequenos de dados, devendo ser usada em planilhas em formado _.xlsx_. 

Para utilizar o presente _software_ é suficiente **copiar para a primeira coluna da planilha _base_tweets.xlsx_ todos os _tweets_ (ou textos) que se queira analisar**, mantendo os cabeçalhos e o nome da aba da planilha intactos. **Salve, feche o arquivo e rode o programa _identificador_frames.py_ ou o _notebook_dentificador_de_frames.ipynb_**. Ao finalizar a análise, **abra novamente a planilha _base_tweets.xlsx_ para ver o resultado**, que estará visível nas colunas ao lado de cada _tweet_.

<p align="center"><b>Exemplo:</b></p>
<p align="center">
<img src="https://www.dropbox.com/s/9qh9isoobx2p7jn/Exemplo-planilha-git-hub.png" alt="Exemplo de identificação de enquadramentos nos tweets">
</p>

### Em detalhes:
Temos 2 arquivos básicos que regulam o funcionamento do identificador de _frames_: 

- _base_tweets.xlsx_
- _keyword_frames.csv_

O arquivo _base_tweets.xlsx_ deve conter todos os _tweets_ a analisar na coluna "_Tweets_". Atualmente o arquivo já vem com um exemplo de _tweets_. Para classificar o seu próprio _corpus_ textual, elimine os que est'~ao no arquivo, em seguida copie e cole a lista dos novos textos na coluna "_Tweets_", mas **sempre mantenha a primeira linha como cabeçalho**. Ao lado de cada _tweet_ estão as colunas de resutado da análise. São 6 colunas (uma para cada enquadramento). Quando o _frame_ foi identificado no texto do _tweet_ o resultado será a **palavra_chave** que o identificou, caso contrário o valor da cela será **"0"**. Caso prefira um resultado de tipo 0 e 1, modifique o código em Python do _notebook_ ou do arquivo _.py_.

O arquivo _keyword_frames.csv_ contém todas as palavras-chave que irão identificar os enquadramentos nos tweets. Este arquivo pode ser editado para atualizar o método de identificação- Para garantir o correto funcionamento do programa, **não mude a estrutura do arquivo** e limite-se somente a adicionar ou eliminar palavras-chave da lista. Não deixe celas fazias entre uma palavra-chave e outra. Com o fim de deixar o programa mais leve, as palavras-chave estão no formato de **radical, sufixo e desinência**, ou seja, o começo e o final das palavras. Este método permite identificar diversas possíveis conjugações verbais e variações de conceitos com um conjunto menor de palavras.


## Quais são os 3 enquadramentos genéricos da Comunicação Política, segundo Semetko e Valkenburg?

### 1. Conflito: 
Semetko e Valkenburg (2000) apontaram em seu estudo como o conflito constitui um enquadramento generalista, que pode ser usado em qualquer notícia para enfatizar “o conflito entre indivíduos, grupos ou instituições como um meio de capturar o interesse do público” (p. 95).

Este frame consiste em palavras que descrevem um encontro conflitivo entre forças opostas (_lado_1_ e _lado_2_, conceptualizadas coletivamente como _lados_) sobre um _problema_ ou _assunto_ disputado e/ou para atingir uma _finalidade_ específica. Tal _finalidade_ é alcançada empregando certas _ações_. Pode haver um _pensador_ que julga como positivas ou negativas as ações empregadas pelos lados em disputa.

### 2. Atribuição de responsabilidade: 
Para Semetko e Valkenburg (2000), este enquadramento apresenta uma pauta ou problema de forma a atribuir responsabilidades por consequências derivadas ou soluções a um governo, indivíduo ou grupo.

De forma específica, neste frame um _ator_ é responsável por ter realizado intencionalmente ou não uma _ação_, ou por ser o ou um instigador primário por trás de uma _causa_. Pode haver uma avaliação positiva ou negativa do _efeito_ da _ação_.

### 3. Moralidade:
O enquadramento da moralidade trata um evento ou questão no contexto de valores, prescrições morais, mensagens normativas e princípios religiosos ou culturais (Semetko & Valkenburg, 2000, p. 96). A moralidade como enquadramento noticioso tem sido objeto de vários estudos e é comumente usada no contexto de questões como religião, minorias, drogas, pátria, família, sexualidade, reprodução e gênero.

Neste frame, um _valor_ é descrito por um juiz (geralmente implícito) no que diz respeito à moralidade de um _comportamento_. As palavras neste enquadramento descrevem o status de uma ação em relação a um _código de leis_ ou regras. Um _objeto_ também pode estar em violação ou cumprimento do código em virtude de sua existência, localização ou posse.


## Quais são os 3 enquadramentos específicos para o estudo do tema da saúde em contextos epidêmicos?

### 1. Consequências da pandemia: 
No que se refere ao frame das consequências da pandemia, ele inclui a dimensão dos riscos, gravidade, efeitos e impactos de doenças infecciosas, tanto do ponto de vista individual como social e econômico.

No caso da pandemia de Covid-19, se estabelece uma relação causal entre o vírus e o contexto de pandemia com efeitos individuais e coletivos. Os efeitos individuais geralmente estão associados à saúde de alguém que foi infectado, como a manifestação de sintomas, a sua recuperação ou morte. Um típico uso do frame das consequências da pandemia é a divulgação diária da contagem de óbitos, infectados e ocupação dos leitos nos hospitais.

Esse frame possui duas dimensões muito parecidas ao que a literatura sobre quadros genéricos define como “interesse humano” e “consequências econômicas” (SEMETKO; VALKENBURG, 2000). Por essa razão esses dois frames não foram adotados para a análise de quadros genéricos. Se optou por utilizar alguns aspectos que os identificam como dimensões do frame das consequências da pandemia. Nesse sentido, ditos frames serão identificados apenas quando houver uma relação causal entre a Covid-19 e a condição econômica e de saúde, tanto do ponto de vista individual como coletivo.

Segundo Semetko e Valkenburg (2000, p. 95), a dimensão do interesse humano: 

“_traz um rosto humano ou uma perspectiva emocional na apresentação de um evento, questão ou problema (...) refere-se a um esforço para personalizar as notícias, dramatizar ou 'emocionalizar' as notícias, a fim de capturar e reter o interesse do público”_.

Já no que se refere à dimensão econômica da pandemia, se ressalta o impacto financeiro da crise sanitária no país, região, instituição, grupo ou indivíduo.

### 2. Medidas de contenção: 
O quadro das medidas de contenção expressa a dimensão da prevenção de doenças infecciosas. Ele se refere a toda ação ou recurso material, político e social que tem por objetivo prevenir, frear ou mitigar os impactos das epidemias.

Em concreto, esse frame se manifesta nos textos quando se faz referências a:

- Benefícios ou malefícios de se adotar ou não as medidas de contenção; 
- Abordagens e ações individuais, coletivas ou sistêmicas;
- Equipamentos de proteção individual (EPI), como máscaras e protetores de rosto, com um foco preponderantemente sobre o comportamento individual;
- Ações de higiene, tanto pessoal como de objetos e ambientes, como o uso de álcool em gel e outros desinfetantes;
- Medidas médicas, como imunidade em geral, vacinas, e hospitais de campanha;
- Aglomerações ou ações de distanciamento social, como quarentena e lockdown, com uma abordagem coletiva ao problema, no sentido que uma epidemia é apresentada como um problema que exige soluções sociais e políticas, porque as causas estão a um nível mais sistêmico.

### 3. Métodos de tratamento:
O frame dos métodos de tratamento é identificado através de menções a todo recurso biomédico capaz de curar, evitar ou atenuar os sintomas e as consequências provocados pela infecção de Covid-19 em uma pessoa já doente. 

Nos textos, esse quadro é identificado quando se faz referência à:
- Respiradores artificiais;
- Hospitais de campanha e unidades de tratamento;
- Medicamentos, como os do chamado Kit Covid (cloroquina, azitromicina, ivermectina) e outros (antibióticos, paracetamol, entre outros);
- Disputa de narrativas sobre como tratar a doença.


### Referência bibliográfica
SEMETKO, Holli A; VALKENBURG, Patti M. Framing European Politics: A Content Analysis of Press and Television News. **Journal of Communication**, pp. 93-109, 2000.
ENTMAN, Robert M. Framing: Toward Clarification of a Fractured Paradigm. **Journal of Communication**, [s. l.], v. 43, n. 4, p. 51–58, 1993. 
