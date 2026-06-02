# Relatório Individual para auxílio do Relatório RADz
<details>
<summary>Criei um arquivo isolado (backend.py) onde vou concentrar toda a lógica do banco de dados e as funções (o CRUD).</summary>
- Comecei às 12 horas. Fazendo assim, eu já consigo ir programando e testando o banco sozinho, sem precisar esperar a interface visual ficar pronta. Isso vai dar uma agilizada monstra na nossa entrega, focando total na metodologia RAD.
- Comecei a montar o banco usando o sqlite3 direto no Python. Criei uma função para conectar e gerar o arquivo .db e já mandei um comando SQL (CREATE TABLE) para montar a nossa tabela produtos. Para os campos, segui certinho o que foi pedido: o ID como chave primária (INTEGER), o nome do produto (TEXT), a quantidade (INTEGER) e o preço (REAL para aceitar os centavos). Deixei o ID para se preencher sozinho (autoincremento) para facilitar a nossa vida na hora de inserir os dados. Rodei o script aqui e o arquivo do banco já foi gerado.
</details>

<details>
<summary>Início do desenvolvimento do CRUD com a função de Inserção (Create) e tratamento de erros:</summary>
- Já criei a função de cadastrar produtos (inserir_produto) utilizando queries dinâmica com o delimitador ? para parametrizar os dados, o que previne vulnerabilidades como o SQL Injection. 
- Também implementei a estrutura try/except/finally para garantir que qualquer erro de transação seja capturado sem quebrar o sistema e que a conexão com o banco seja sempre encerrada corretamente, preservando a integridade do arquivo .db
</details>

<details>
<summary>Criação da função de Listagem de dados (Read do CRUD).</summary>
Como eu fiz:
  - Desenvolvi a função listar_produtos utilizando o comando SELECT * para varrer a tabela. 
  - Para transformar os dados brutos do SQLite em uma estrutura que a nossa interface gráfica consiga ler no futuro, utilizei o método fetchall(), que converte os registros em uma lista do Python. Mantive o padrão de segurança com try/except/finally, garantindo que, em caso de falha na leitura, a função retorne uma lista vazia, evitando que a aplicação inteira trave (crash) durante a exibição na tela.
</details>

<details>
<summary>Desenvolvimento da função de atualização de dados (Update do CRUD).</summary>
Como eu fiz: 
  - Criei a função atualizar_produto utilizando a instrução SQL UPDATE. 
- Para garantir a integridade dos dados e evitar atualizações em massa por acidente, utilizei a cláusula WHERE id = ? para filtrar a alteração. Assim, o sistema só altera a linha exata que o utilizador selecionou. z
- Mantive o uso de parâmetros (?) nas variáveis nome, quantidade e preco para continuar a blindar a aplicação contra ataques de injeção de SQL. z
- A estrutura de tratamento de erros também foi mantida para garantir a estabilidade.
</details>

<details>
<summary>Fechamos o ciclo do CRUD com a função de Deletar.</summary>
Como eu fiz: z
  - Criei a função deletar_produto usando o comando DELETE FROM. Assim como no Update, a trava de segurança aqui foi usar o WHERE id = ? para ter certeza de que o sistema só vai apagar o produto exato que o usuário clicar na tela, evitando deletar a tabela inteira por acidente. 
- Também apliquei um truquezinho do Python nas tuplas de um item só (id_produto,) para o delimitador de segurança funcionar redondo. 
- Agora é só partir pros tratamentos de erro de digitação do usuário e depois plugar na tela!
</details>

<details>
<summary>Blindagem do banco com validação e limpeza de dados (Tratamento de Erros)</summary>
Como eu fiz: z
  - Como o professor exigiu, apliquei as travas de segurança antes dos dados baterem no banco de dados. Lá nas funções de Inserir e Atualizar, adicionei o método .strip() no nome do produto pra arrancar qualquer espaço em branco inútil que o usuário possa digitar sem querer no começo ou no final do campo. z
- Também forcei a conversão da Quantidade pra número inteiro (int) e do Preço pra número real (float). Coloquei um bloco except ValueError pra segurar a bronca e avisar se a interface mandar letras em vez de números, evitando que o sistema inteiro quebre. Banco 100% blindado.
</details>

<details>
<summary>Desenvolvimento da primeira camada de integração (Ponte de Cadastro) entre o backend e a interface.</summary>
Como eu fiz: z
  - Para ligar a interface Tkinter à base de dados SQLite, comecei a desenvolver funções intermediárias (pontes). A primeira foi a acao_cadastrar(). z
- Esta função utiliza o método .get() para extrair os dados inseridos pelo utilizador nas caixas de texto (Entry) da interface. Em seguida, implementei uma validação simples para impedir o envio de campos vazios, recorrendo à biblioteca messagebox para emitir alertas visuais. z
- Por fim, injetei estes dados diretamente na função principal do meu backend (inserir_produtos) e configurei a limpeza automática dos campos do ecrã após o sucesso da operação. O botão "Cadastrar" já está mapeado com o parâmetro command para acionar todo este fluxo.
</details>

<details>
<summary>Implementação da ponte de listagem para sincronizar a base de dados com a Treeview</summary>
Como eu fiz: z
  - Desenvolvi a função intermediária atualizar_tabela(). Esta função tem a responsabilidade de varrer os dados através do método listar_produtos() do backend e iterar sobre os resultados para preencher a componente Treeview do Tkinter. 
- Para evitar duplicação visual, adicionei um loop que limpa a interface (tree.delete) antes de a recarregar.
- Configurei também gatilhos para que esta função seja executada automaticamente na inicialização da aplicação (antes do mainloop()) e imediatamente após o registo de um novo produto na função acao_cadastrar(), garantindo que o utilizador tenha sempre feedback visual em tempo real do estado do stock.
</details>

<details>
<summary>Criação da ponte de exclusão (Delete) com integração de validação de interface.</summary>
Como eu fiz: z
  - Desenvolvi a função intermediária acao_excluir(). A lógica principal consiste em capturar o foco atual da Treeview (via tree.selection()). Se uma linha estiver selecionada, o sistema extrai o ID do produto (índice 0). 
- Para cumprir a exigência do professor de não permitir exclusões acidentais, implementei a janela de confirmação utilizando messagebox.askyesno(). Apenas mediante a confirmação do usuário (retorno True), o ID é passado para a minha função de backend deletar_produto(). Ao final, a interface é notificada do sucesso e a função atualizar_tabela() é chamada novamente para refletir a remoção do item na tela em tempo real. 
- Adicionei também a chamada solta da função criar_tabela() antes da inicialização do Tkinter para garantir que o banco e as tabelas sejam sempre verificados/criados na inicialização do sistema em qualquer máquina.
</details>

<details>
<summary>Conclusão da integração backend/frontend com a implementação da lógica de Update</summary>
Como eu fiz:
  - Como a arquitetura do projeto é baseada em Single Page Application (Tela Única no Tkinter), dividi o processo de Update em duas pontes lógicas. A primeira ponte (acao_editar) captura a tupla de dados da linha focada na Treeview e os injeta de volta nos campos Entry para manipulação do usuário. 
- A segunda ponte (acao_atualizar) é acionada após a alteração dos dados: ela retém o ID do produto selecionado, extrai os novos valores dos Entry via método .get(), e os passa como parâmetros para a função principal de Update
no SQLite. 
- Com isso, o ciclo completo do CRUD!
</details>
