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

<details>
<summary>31/05</summary>
- a
  
</details>
