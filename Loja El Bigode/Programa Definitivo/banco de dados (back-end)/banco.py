import sqlite3 

def conectar():
    conexao = sqlite3.connect('estoque.db')
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Quantidade INTEGER NOT NULL,
    Preco REAL NOT NULL
    )
    ''')
    conexao.commit()
    conexao.close()
    print("Banco de dados e tabela criados")

def inserir_produtos(Nome,Quantidade,Preco):
    try:
        #trava de segurança e limpeza
        Nome =str(Nome).strip()
        Quantidade = int(Quantidade)
        Preco = float(Preco)
        
        conexao =conectar()
        cursor = conexao.cursor()

        comando_sql = 'INSERT INTO produtos (Nome, Quantidade, Preco) VALUES (?, ?, ?)'
        cursor.execute (comando_sql, (Nome, Quantidade, Preco))
        conexao.commit()
        print(f"Produto {Nome} cadastrado com sucesso no Banco")
    except ValueError:                  
        print("Erro: Quantidade deve ser um número inteiro e Preço deve ser um número decimal.")
    except sqlite3.Error as erro:
        print(f"ocorreu um erro ao inserir no banco: {erro}")


    finally:
        if conexao:
            conexao.close()   

def listar_produtos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        comando_sql = 'SELECT * FROM produtos'
        
        cursor.execute(comando_sql)
        lista_de_produtos = cursor.fetchall()
        return lista_de_produtos
    except sqlite3.Error as erro:
        print(f" Ocorreu um erro ao buscar os produtos: {erro}")
        return []
    finally:
        if 'conexao' in locals() and conexao:
            conexao.close()

    
def atualizar_produto(id_produto, novo_Nome, nova_Quantidade, novo_Preco):
    try:
        #trava de segurança e limpeza
        novo_Nome = str(novo_Nome).strip()
        nova_Quantidade = int(nova_Quantidade)
        novo_Preco = float(novo_Preco)

        conexao = conectar()
        cursor = conexao.cursor()

        comando_sql = '''
            UPDATE produtos
            SET Nome = ?, Quantidade = ?, Preco = ?
            WHERE id = ?
        '''
        cursor.execute(comando_sql, (novo_Nome, nova_Quantidade, novo_Preco, id_produto))
        conexao.commit()
        print(f"Produto com ID {id_produto} atualizado com sucesso no banco!")
    except ValueError:                  
        print("Erro: Quantidade deve ser um número inteiro e Preço deve ser um número decimal.")
    except sqlite3.Error as erro:
        print(f"Ocorreu um erro ao atualizar o produto: {erro}")

    finally:
        if 'conexao' in locals() and conexao:
            conexao.close()

def deletar_produto(id_produto):
    try:
 
        conexao =conectar()
        cursor = conexao.cursor()
        comando_sql = 'DELETE FROM produtos WHERE id = ?'
        cursor.execute(comando_sql, (id_produto,))

        conexao.commit()
        print(f"Produto com ID {id_produto} deletado com sucesso do banco")
    except sqlite3.Error as erro:
        print(f" Ocorreu um erro ao deletar o produto: {erro}")
    finally:
        if 'conexao' in locals() and conexao:
            conexao.close()


# ==========================================
# AS NOSSAS FUNÇÕES DE PONTE
# ==========================================
def acao_cadastrar():
    nome_digitado = entry_nome.get()
    qtd_digitada = entry_qtd.get()
    preco_digitado = entry_preco.get()

    if nome_digitado == "" or qtd_digitada == "" or preco_digitado == "":
        messagebox.showwarning("Aviso", "Por favor, preenche todos os campos!")
        return
    inserir_produtos(nome_digitado, qtd_digitada, preco_digitado)
    messagebox.showinfo("Sucesso", "Produto inserido no sistema!")
    entry_nome.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    atualizar_tabela()

def atualizar_tabela():
    for linha in tree.get_children():
        tree.delete(linha)
    produtos_salvos = listar_produtos()

    for produto in produtos_salvos:
        id_prod = produto[0]
        nome = produto[1]
        qtd = produto[2]
        preco = produto[3]

        status = "REGISTADO"

        tree.insert("", "end", values=(id_prod, nome, qtd, f"{preco:.2f}", status))

def acao_excluir():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Por favor, selecione um produto na tabela para excluir!")
        return
    confirmacao = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja apagar este produto definitivamente?")

    if confirmacao:
        valores = tree.item(item_selecionado, 'values')
        id_produto = valores[0]
        
        deletar_produto(id_produto)

        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        atualizar_tabela()

def acao_editar():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Por favor, selecione um produto para editar!")
        return
    valores = tree.item(item_selecionado, 'values')

    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, valores[1])

    entry_preco.delete(0, tk.END)
    entry_preco.insert(0, valores[3])

def acao_atualizar():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione o produto na tabela antes de clicar em Atualizar!")
        return

    valores = tree.item(item_selecionado, 'values')
    id_produto = valores[0]

    novo_nome = entry_nome.get()
    nova_qtd = entry_qtd.get()
    novo_preco = entry_preco.get()
    atualizar_produto(id_produto, novo_nome, nova_qtd, novo_preco)

    messagebox.showinfo("Sucesso", "Produto atualizado com sucesso no banco!")
    entry_nome.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    atualizar_tabela()
