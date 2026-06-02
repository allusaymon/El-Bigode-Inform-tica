# Relatório Individual para auxílio do Relatório RAD
Será dividido entre:
- Parte que fiz ANTES de obter o código do trabalho completo.
- Parte que fiz DEPOIS de obter o código do trabalho completo.

# Antes de Obter o Código Completo:
O objetivo do desenvolvimento do Log de Auditoria é garantir a rastreabilidade completa do sistema, mapeando onde as informações são geradas ou modificadas para que nenhuma ação relevante passe despercebida. 

Como o meu papel dependia diretamente do fluxo final das outras ramificações do projeto, precisei aguardar que os meus colegas de equipe finalizassem a estrutura do back-end e do front-end. Durante esse período de espera, foquei na análise teórica dos requisitos e no planejamento lógico da interceptação de dados para que, assim que o código integrado me fosse entregue, a implementação física ocorresse sem gargalos ou atrasos.

- **Mapear:** Estudei as diretrizes do professor e defini que o log precisaria monitorar os momentos exatos em que as operações do CRUD fossem validadas com sucesso.
- **Definir Infraestrutura:** Planejar formato de saída que seria gravado no arquivo de texto simples (`log_estoque.txt`), garantindo que a estrutura gerasse registros leves, portáteis e em ordem cronológica com um carimbo de data e hora inaterável.

# Depois de Obter o Código Completo:
Assim que a equipe disponibilizou o main.py principal unificado, iniciei e concluí todo o desenvolvimento prático, refatoração e publicação do sistema de auditoria em um único ciclo de trabalho.

<details>
<summary>01/06</summary>
  
- **Desenvolvimento do Módulo Isolado (`log_auditoria.py`):** Programei do zero a classe independente `AuditLogger`. Utilizando de um fork pessoal, optei por manter esse módulo em um arquivo separado seguindo o princípio de responsabilidade única, evitando poluir o script principal de interface da equipe.

- **Implementação de Regras do Log:** - Desenvolvi os métodos de gravação de arquivos: `log_insert`, `log_update` e `log_delete`.
  - Formatei as mensagens de saída utilizando o padrão de timestamp exigido: `[DD/MM/AAAA HH:MM:SS]`.
  - Adicionei tratamento de exceções com blocos `try/except` internos para capturar erros de tipo (`ValueError`/`TypeError`), garantindo que falhas de entrada do operador não quebrem o processo de escrita do log.

- **Automação de Diretório com Diretório Relativo:** Ajustei a variável global do arquivo de log para salvar utilizando diretórios relativos: `../Dados/log_estoque.txt`. Com isso, o próprio Python cria a pasta e o arquivo de texto de forma automatizada na máquina de qualquer integrante do grupo assim que o programa roda, eliminando a necessidade de criação manual.

- **Integração, Limpeza e Testes:**
  - Conectei o módulo ao arquivo unificado através da importação: `from log_auditoria import AuditLogger`.
  - Posicionei as chamadas dos métodos cirurgicamente dentro das funções da interface gráfica (`acao_cadastrar`, `acao_atualizar` e `acao_excluir`), assegurando que o log só registre a movimentação após o banco de dados confirmar o sucesso da operação.
  - Realizei testes de concorrência com o banco para garantir estabilidade e limpei o código removendo linhas de testes antigas e comentários desnecessários.

- **Publicação e Versionamento no GitHub:** Realizei o envio das alterações. Criei uma branch de trabalho segura para evitar conflitos com o progresso já feito pelo grupo, fiz o upload dos arquivos limpos e abri um *Pull Request* que foi revisado e integrado (*Merged*) com sucesso diretamente na branch principal (`main`).
</details>
