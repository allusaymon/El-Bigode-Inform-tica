

import sqlite3 
import tkinter as tk 
from tkinter import ttk, messagebox

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



    
    






# ==========================================
# frontend
# ==========================================
criar_tabela()

# Configurações da janela 
root = tk.Tk()
root.title("El Bigode - Estoque")
root.geometry("1920x1080")
root.resizable(True, True)
# CORES PRINCIPAIS
cor_de_fundo = "#181C2B"
root.configure(bg=cor_de_fundo)
cor_preto = "#0B0F1D"
cor_branco = "#FFFFFF"
cor_borda = "#1E90FF"

# Configuração do Estilo
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background=cor_preto, foreground=cor_branco)
#Configuração dos botões e efeitos
style.configure("TButton", font=("Arial", 12, "bold"), padding=8, background="#16139D", foreground="#FFFFFF")
style.map("TButton", foreground=[('pressed', "#000000"), ('active', "#1500FF")])

### cor do quadradão no titulo
frame_topo = tk.Frame(root, bg=cor_preto, bd=0, highlightthickness=1, highlightbackground="#1E90FF", highlightcolor=cor_borda)
frame_topo.pack(fill="x", padx=20, pady=20, ipady=10)

#titulo principal
titulo = ttk.Label(frame_topo, text="EL BIGODE", font=("Bahnschrift Condensed", 70, "bold"))
titulo.pack(pady=(10, 0))
subtitulo = ttk.Label(frame_topo, text="I N F O R M Á T I C A", font=("Segoe UI", 20, "bold"))
subtitulo.pack(pady=(0, 10))

# CADASTRO DO PRODUTO (FORMULARIO)
frame_form = tk.Frame(root, bg="#0B0F1D", bd=0, highlightthickness=1, highlightbackground="#1E90FF", highlightcolor=cor_borda)
frame_form.pack(fill="x", padx=20, pady=20, ipady=15)
fonte_titulo = ("Arial", 14, "bold")
fonte_caixas = ("Arial", 14)

ttk.Label(frame_form, text="NOME DO PRODUTO:", font=fonte_titulo).grid(row=0, column=0, sticky="w", padx=10, pady=15)
entry_nome = ttk.Entry(frame_form, width=35, font=fonte_caixas)
entry_nome.grid(row=0, column=1, columnspan=3, padx=10, sticky="w", pady=15)

ttk.Label(frame_form, text="QUANTIDADE:", font=fonte_titulo).grid(row=1, column=0, sticky="w", padx=10, pady=10)
entry_qtd = ttk.Entry(frame_form, width=10, font=fonte_caixas)
entry_qtd.grid(row=1, column=1, padx=10, sticky="w", pady=10)

ttk.Label(frame_form, text="PREÇO (R$):", font=fonte_titulo).grid(row=1, column=2, sticky="w", padx=20, pady=10)
entry_preco = ttk.Entry(frame_form, width=15, font=fonte_caixas)
entry_preco.grid(row=1, column=3, padx=10, sticky="w", pady=10)

## CADASTRO DO PRODUTO (BOTÕES)
botoes = tk.Frame(root, bg=cor_de_fundo)
botoes.pack(pady=(10, 20))

cadastrar_botao = ttk.Button(botoes, text="➕ CADASTRAR", command=acao_cadastrar)
cadastrar_botao.grid(row=0, column=0, padx=15)

atualizar_botao = ttk.Button(botoes, text="🔄 ATUALIZAR", command=acao_atualizar)
atualizar_botao.grid(row=0, column=1, padx=15)

excluir_botao = ttk.Button(botoes, text="🗑 EXCLUIR", command=acao_excluir)
excluir_botao.grid(row=0, column=2, padx=15)

editar_botao = ttk.Button(botoes, text="✏️ EDITAR", command=acao_editar)
editar_botao.grid(row=0, column=3, padx=15)

# TABELA DOS PRODUTOS/INFORMAÇÕES E BOTÕES
frame_tabela = tk.Frame(root, bg="#B4B4B4", bd=1)
frame_tabela.pack(fill="both", expand=True, padx=5)

style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

style.configure("Treeview", background="#1A2761", 
                foreground=cor_branco, fieldbackground=cor_de_fundo, 
                rowheight=30, font=("Arial", 11), borderwidth=0)
style.configure("Treeview.Heading",
                background="#FFFFFF",
                font=("Arial", 12, "bold"))
style.map("Treeview.Heading",
        background=[('pressed', "#0C1644"), ('active', "#909090")],
        foreground=[('pressed', "#FFFFFF"), ('active', '#FFFFFF')])
style.map("TButton", background=[('active', "#002184")])

colunas = ("ID", "NOME", "QUANTIDADE", "PREÇO (R$)", "STATUS")
tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)
tree.pack(fill="both", expand=True)

tree.heading("ID", text="ID")
tree.column("ID", width=80, anchor="center")

tree.heading("NOME", text="NOME")
tree.column("NOME", width=350, anchor="w")

tree.heading("QUANTIDADE", text="QUANTIDADE")
tree.column("QUANTIDADE", width=100, anchor="center")

tree.heading("PREÇO (R$)", text="PREÇO (R$)")
tree.column("PREÇO (R$)", width=120, anchor="center")

tree.heading("STATUS", text="STATUS")
tree.column("STATUS", width=150, anchor="center")
atualizar_tabela()
root.mainloop()



