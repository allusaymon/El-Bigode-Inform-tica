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
- De cara, é possível ver que a coluna de status possuí um único valor chamado "Registado". Me pergunto o porquê desta coluna existir, afinal, se o objetivo é validar o produto como registrado e não-registrado... Porquê
- Executei o código completo e a primeira coisa que pensei foi: Esta interface não parece ter suporte para o scroll de linhas que havia testado anteriormente no banco de dados falso. Será que há? 
- Inseri o laço que havia feito anteriormente no protótipo, dentro da função "inserir_produtos" e removi a trava de segurança da função ação_cadastrar para isso (ela impedia que qualquer produto fosse adicionado sem que antes os campos de entrada deixassem de ser vazios, o que é ótimo!) 
- Os produtos foram adicionados e concluí que: A tabela exibe/renderiza apenas 10 produtos antes do scroll, algo fruto do tamanho de pixels de sua dimensões, assim como formatação do Treeview. Para o banco de dados falso, ele renderizava até 32 produtos de uma vez, no entanto, é verdade que não é necessário tanto espaço na interface: O objetivo foi concluído e foi verificado que o algoritmo possuí suporte a exibir uma grande massa de dados.

**Testando o CRUD**  
- 
  
- (deixa pra verificar depois: que estranho... Quando fui usar o "cadastrar", consegui adicionar um produto ao banco sem nenhum problema... Mas na hora de editar o produto, automaticamente apareceu nos campos o nome do produto, o preço dele... Mas a quantidade estava em branco. Porquê? Digo, claramente eu inseri uma quantidade específica, mas o programa apagou ela do campo vazio antes que eu pudesse talvez alterá-la?)z
- (o terminal do python agiu estranho nesses atos. Como se eu tivesse visto a prova de algo, o terminal estava exibindo prints simples de auditoria: "Banco de dados criado", "Produto X cadastrado", mas... "Erro: **Quantidade** deve ser um número inteiro e Preço deve ser decimal.". Pensei "oh, talvez eu tenha tentado cadastrar deixando os campos vazios, né? Posso tentar de novo... Mas a mesma mensagem de erro apareceu novamente, mesmo que os valores inseridos fossem validos e fossem enviados até para o banco. O que estava acontecendo?)

- verifiquei que o programa possuí formatação específica para o campo "nome do produto". Quer dizer que se o usuário final quiser inserir "tEcLado lEgAL dA rAZEr", vai constar exatamente assim na tabela: Isso não pode ser assim. 
</details>
