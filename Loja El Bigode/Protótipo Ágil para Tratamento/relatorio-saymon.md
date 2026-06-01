# Relatório Individual para auxílio do Relatório RAD
Será dividido entre:
- Parte que fiz ANTES de obter o código do trabalho completo
- Parte que fiz DEPOIS de obter o código do trabalho completo (testes de qualidade e etc estarão aqui!)

# Antes de Obter o Código Completo:
O objetivo da Garantia de Qualidade é a análise minunciosa do projeto para prevenir a parada do sistema em qualquer tipo de erro que pode existir no sistema que estamos criando.

Ainda sim, é possível analisar e prevenir qualquer possibilidade de erro sem ter a necessidade de obter o código-fonte completo do projeto!

De acordo com nossa Análise de Requisitos (presente na pasta "Dados" no início do diretório), me foi dado o papel de criar:
- Criar uma **simulação do projeto**, um protótipo da versão back-end dele.
- Aplicar a prevenção de erros nele, criando um padrão simples de segurança pro projeto para futuros testes!
- Tudo isso em prol de facilitar o momento em que a implementação real ocorrer e possamos usar destas mesmas estratégias no futuro código-fonte!

<details>
<summary>27/05</summary>
- Estudei as anotações do professor e defini uma agenda do que precisava fazer:
  
  1. Criar um Banco de Dados Falso para o protótipo.
  2.  Criar uma interface básica Treeview para testes, incluindo campos vazios simples.
  3. Criar testes de validação de conexão ao banco de dados falso. 

A intenção era **testar** como uma tabela SQL conseguiria se comportar dentro de uma interface Treeview, caso ela tivesse MUITAS LINHAS. Tal ideia se tratava de um teste básico de READ do quarteto CRUD (Create, Read, Update e Delete).
</details>


<details>
<summary>30/05</summary>
- Criei um algoritmo que se conectava ao banco de dados através do sqlite3. Conforme orientação do professor, ele possuía uma tabela de 3 colunas (nome, quantidade e preço)!
  
- Incrementei o algoritmo dando origem a um laço que criava 50 linhas na coluna "nome" através da biblioteca estrangeira Faker. Para acompanhar, usei a biblioteca Random pra preencher as outras duas colunas...
- Por fim, utilizei um código de Treeview do professor para **testar** se: Mesmo com dimensões baixas numa Interface Gráfica do Usuário, mesmo com poucas especificações no pady e até com mínimo suporte a tabela através de headings e columns... Se era possível exibir um banco de dados massivo, capaz de visualizar por inteiro todos seus dados.
- Resultado: Pude perceber que através do suporte a tabela da GUI, o próprio banco de dados se adaptou e criou um modelo de scroll onde mostrava todos os "produtos". Isso foi bom, já que este projeto é de tela única e seria um problema caso a tabela criasse "páginas" para separar suas 50 linhas.

- Por fim, criei entrys para nome, quantidade e preço acima da tabela. A intenção, além de incrementar o protótipo, era auxiliar para a criação da função "adicionar_produto" e "delete", sendo que para o segundo...
- Criei um pequeno messagebox que perguntava se o usuário final tinha certeza se queria deletar um produto específico do banco. Como a Análise de Qualidade possuí papel em prevenir que o banco de dados saia prejudicado através de uma manipulação suja nos dados... Já que não há como desenvolver um backup de produtos e deixá-los invisíveis na tabela dentro do escopo do trabalho, pelo menos essa messagebox antes de eliminar completamente o produto deveria ter. 
</details>

# Depois de Obter o Código Completo:
<details>
<summary>31/05</summary>
- De cara, é possível ver que a coluna de status possuí um único valor chamado "Registado". Me pergunto o porquê desta coluna existir, afinal, se o objetivo é validar o produto como registrado e não-registrado... Porquê não existe o valor não-registrado? O certo não seria esse status mudar devido a alguma alteração no valor da quantidade ou no preço? É uma parte incompleta do código que trará confusão para o usuário final. Ainda sim, irei mudar o "Registado" para "Registrado".

- Executei o código completo e a primeira coisa que pensei foi: Esta interface não parece ter suporte para o scroll de linhas que havia testado anteriormente no banco de dados falso. Será que há? 

- Inseri o laço que havia feito anteriormente no protótipo, dentro da função "inserir_produtos" e removi a trava de segurança da função ação_cadastrar para isso (ela impedia que qualquer produto fosse adicionado sem que antes os campos de entrada deixassem de ser vazios, o que é ótimo!) 

- Os produtos foram adicionados e concluí que: A tabela exibe/renderiza apenas 10 produtos antes do scroll, algo fruto do tamanho de pixels de sua dimensões, assim como formatação do Treeview. Para o banco de dados falso, ele renderizava até 32 produtos de uma vez, no entanto, é verdade que não é necessário tanto espaço na interface: O objetivo foi concluído e foi verificado que o algoritmo possuí suporte a exibir uma grande massa de dados. Dessa forma, excluí o laço criado após o teste.

**Testando o CRUD**  
CREATE: 
- Está ótimo! A aplicação está mantendo uma conexão congruente com o banco de dados, criando ele instantaneamente com suas devidas colunas. Cada coluna possuí tipos específicos de dados para elas e restrições que deixam o código bem completo... Chegando até a apagar espaços vazios nas extremidades do campo de texto. No entanto...
- Algo me incomodou na inserção do nome de novos produtos no banco: Não há formatação padrão para o campo de entrada de texto "nome". Isso significa que se o usuário final quiser inserir "tEcLado lEgAL dA rAZEr", vai constar exatamente assim na tabela: Isso não pode ser assim. 
- Mudei isso: Em todas as funções, na parte da trava de segurança no tratamento de tipo dos dados, adicionei a ferramenta capitalize() para deixar todo o texto minúsculo, mas com a primeira letra maíscula.Z
- Outra coisa grave é o fato de poder inserir números negativos nas colunas de "Quantidade" e no "Preço": Não existe preço negativo, muito menos estoque negativo.z
- Da mesma forma: Em todas as funções, na parte da trava de segurança no tratamento de tipo dos dados, adicionei logo abaixo uma estrutura de decisão que trava até a conexão com o banco caso o preço ou a quantidade sejam negativos.

READ:
- Existe uma função específica no código apenas para listar os produtos da tabela e ela é retornada na função "atualizar_tabela" através do botão de mesmo nome. Isso é perfeito e definitivamente o usuário final irá querer visualizar o que diretamente está acontecendo no banco de dados a cada consulta.z

UPDATE:
- É interessante em como o messagebox foi utilizado aqui para avisar que é preciso selecionar uma linha, para então atualizá-la: Intuitivo e auxilia bem o usuário final. No entanto, após usar o botão "editar", os campos de entrada de texto se preencheram com as informações do produto selecionado para edição ao uso do botão "Atualizar"... Menos o campo de texto de "quantidade", no qual continuou vazio. Isso gerará uma confusão para o usuário final, então eu resolvi. Na função de editar ação, havia sido esquecido justamente as linhas de comando para ler o que estava no campo de qualidade e deletá-lo após um save na edição.

DELETE:
- Perfeito. Como dito anteriormente, é preocupante que haja uma forma de deletar definitivamente uma linha de um banco de dados real, sem nenhum direito a backup ou algo do gênero... Mas devido ao escopo simples do projeto, não há o que fazer. Ainda sim, a aplicação cumpre seu papel de importância ao exibir um messagebox NO MOMENTO que a interação com o botão ocorre, questionando a certeza da ação. Isso não acontece nos outros botões, mostrando a atenção especial que este recebeu.

</details>

<details>
<summary>01/06</summary>
- Revisado o código do log.
</details>
