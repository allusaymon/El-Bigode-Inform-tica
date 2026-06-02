# El-Bigode-Inform-tica
Trabalho de RAD - Mini Sistema de Controle de Estoque 

Objetivo: Desenvolver um protótipo ágil de uma aplicação Desktop com Interface Gráfica (GUI) para gerenciar o estoque de uma loja. O sistema deve interagir com um banco de dados relacional, manter um log de auditoria em um arquivo .txt e seguir os princípios de Desenvolvimento Rápido de Aplicações.

OBS: Comumente, o github é utilizado para organizar inúmeros arquivos em um único repositório, a fim de visualizar ou compreender algum projeto. O professor exigiu que nosso projeto fosse de tela única, o que torna também possível criá-lo em um único arquivo, sem precisar de muitas pastas.
Ainda sim, optamos por criar este repositório pra facilitar a consulta dos códigos. Abaixo está a divisão da equipe e também o manual do professor, que tecnicamente tudo que contém nele terá no nosso trabalho.
<details>
<summary>Equipe de Desenvolvimento: </summary>

### Programador Backend & Banco de Dados
- **Francisco Mateus**

### "Gestor de Produtos" -  Relatório RAD
- **João Guilherme Gomes**

### Programador Frontend & Interface Tkinter
- **Iarlley Gabriel**

### Log de Auditoria
- **Matheus Vinicius**

### Análise de Qualidade - Prototipagem e Testes
- **Saymon Madson**
</details>

# Notas de Atualização / Checklist
- Front-end v1 feito - 31/05/26
- Back-end feito - 31/05/2026
- Simulação de Qualidade v2 feita - 01/06/26
- Log feito - 01/06/2026
- Relatório RAD em andamento - 
(todos os relatorios individuais estão na pasta "Dados")


# 1. Requisitos de Interface (Tela Única)
- Atenção: Para agilizar o desenvolvimento (foco no RAD), a aplicação deve
obrigatoriamente rodar em uma Única Tela (Single Window). Não crie
janelas secundárias.
- A interface (construída com a biblioteca tkinter) deve conter, na mesma
janela: um formulário para entrada de dados (Entry), botões de ação (Button)
e a grade de exibição (Treeview).

# 2. Funcionalidades do CRUD
- Create: Cadastrar novo produto no banco lendo os campos do formulário.
- Read: Exibir todos os produtos cadastrados atualizados no Treeview.
- Update: Ao clicar em um item no Treeview, os dados devem retornar para o
formulário para edição e salvamento.
- Delete: Remover produto com confirmação via messagebox.
  
# 3. Log de Auditoria (Persistência em Arquivo)
- Toda alteração de dados (Create, Update, Delete) deve gerar uma nova linha
em um arquivo chamado log_estoque.txt.
- A abertura do arquivo deve utilizar o modo de adição ('a') para garantir que o
histórico anterior não seja apagado.
• Exemplos do formato esperado no arquivo .txt:
o [05/05/2026 14:30:15] INSERÇÃO - Produto "Monitor" (Qtd: 10)
cadastrado com sucesso.
o [05/05/2026 15:45:00] ATUALIZAÇÃO - Produto "Monitor" alterado
(Nova Qtd: 8, Novo Preço: 850.00).
o [06/05/2026 09:12:30] EXCLUSÃO - Produto "Teclado Mecânico"
removido do sistema.

# 4. Tratamento de Erros e Validação
- Utilize blocos try/except para impedir que o sistema quebre (crash) caso o
usuário digite texto em campos numéricos de quantidade ou preço.
- Utilize manipulação de strings (como o método .strip()) para limpar as
entradas do usuário antes de salvar no banco.

# 5. Relatório de Implementação Ágil (RAD)
Junto com o código-fonte, a equipe/aluno deve entregar um breve relatório em PDF
(1 a 2 páginas) detalhando a experiência com a metodologia RAD:
- Decisões Rápidas: Quais escolhas de código, arquitetura ou bibliotecas
ajudaram a acelerar a entrega do protótipo?
- Estratégia de Teste: Como os dados foram testados no banco inicialmente?
(Por exemplo, o uso de bibliotecas de geração de dados fictícios como
Faker).
- Visão de Futuro: O RAD foca em iterações contínuas. Quais seriam as duas
primeiras funcionalidades de negócio adicionadas em um próximo ciclo de
desenvolvimento (Versão 2.0)?

# 6. Critérios de Avaliação
• Funcionalidade CRUD no Banco de Dados (40%)
• Sistema de Logs e Tratamento de Erros (20%)
• Relatório e Aplicação do RAD (20%)
• Interface (Tela Única, Intuitiva e Funcional) (20%)

# 7. Entregáveis (O que deve ser enviado)
O aluno/equipe deve submeter no SAVA um único arquivo compactado (.zip ou .rar),
nomeado no padrão Nome_Sobrenome_RAD.zip. Dentro deste arquivo, devem
constar obrigatoriamente:
1. Código-Fonte (.py ou .ipynb): O script principal contendo a aplicação.
2. Banco de Dados: O arquivo .db do SQLite.
3. Relatório RAD (.pdf): O documento de 1 a 2 páginas.
4. Arquivo de Log (.txt): O arquivo log_estoque.txt gerado durante os seus
testes
