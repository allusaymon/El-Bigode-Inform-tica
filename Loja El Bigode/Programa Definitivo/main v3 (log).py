import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from log_auditoria import AuditLogger

def conectar():
    conexao = sqlite3.connect('estoque.db')
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome       TEXT    NOT NULL,
            Quantidade INTEGER NOT NULL,
            Preco      REAL    NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

def inserir_produtos(Nome, Quantidade, Preco):
    conexao = None
    try:
        Nome       = str(Nome).strip().capitalize()
        Quantidade = int(Quantidade)
        Preco      = float(Preco)
        if Quantidade < 0:
            messagebox.showerror("Erro de Validação", "A quantidade não pode ser negativa!")
            return False
        if Preco < 0:
            messagebox.showerror("Erro de Validação", "O preço não pode ser negativa!")
            return False
        conexao = conectar()
        cursor  = conexao.cursor()
        cursor.execute(
            'INSERT INTO produtos (Nome, Quantidade, Preco) VALUES (?, ?, ?)',
            (Nome, Quantidade, Preco)
        )
        conexao.commit()
        return True
    except ValueError:
        messagebox.showerror("Erro de Digitação", "Quantidade deve ser número inteiro e Preço deve ser decimal.")
        return False
    except sqlite3.Error as erro:
        print(f"Erro ao inserir no banco: {erro}")
        return False
    finally:
        if conexao:
            conexao.close()

def listar_produtos():
    try:
        conexao = conectar()
        cursor  = conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        return cursor.fetchall()
    except sqlite3.Error as erro:
        print(f"Erro ao buscar produtos: {erro}")
        return []
    finally:
        if 'conexao' in locals() and conexao:
            conexao.close()

def atualizar_produto(id_produto, novo_Nome, nova_Quantidade, novo_Preco):
    conexao = None
    try:
        novo_Nome      = str(novo_Nome).strip().capitalize()
        nova_Quantidade = int(nova_Quantidade)
        novo_Preco      = float(novo_Preco)
        if nova_Quantidade < 0:
            messagebox.showerror("Erro de Validação", "A quantidade não pode ser negativa!")
            return False
        if novo_Preco < 0:
            messagebox.showerror("Erro de Validação", "O preço não pode ser negativa!")
            return False
        conexao = conectar()
        cursor  = conexao.cursor()
        cursor.execute('''
            UPDATE produtos
               SET Nome = ?, Quantidade = ?, Preco = ?
             WHERE id = ?
        ''', (novo_Nome, nova_Quantidade, novo_Preco, id_produto))
        conexao.commit()
        return True
    except ValueError:
        messagebox.showerror("Erro de Digitação", "Quantidade deve ser número inteiro e Preço deve ser decimal.")
        return False
    except sqlite3.Error as erro:
        print(f"Erro ao atualizar: {erro}")
        return False
    finally:
        if conexao:
            conexao.close()

def deletar_produto(id_produto):
    conexao = None
    try:
        conexao = conectar()
        cursor  = conexao.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = ?', (id_produto,))
        conexao.commit()
        return True
    except sqlite3.Error as erro:
        print(f"Erro ao deletar: {erro}")
        return False
    finally:
        if conexao:
            conexao.close()

def acao_cadastrar():
    nome_digitado  = entry_nome.get()
    qtd_digitada   = entry_qtd.get()
    preco_digitado = entry_preco.get()
    if not nome_digitado.strip() or not qtd_digitada or not preco_digitado:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return
    sucesso = inserir_produtos(nome_digitado, qtd_digitada, preco_digitado)
    if sucesso:
        logger.log_insert(nome_digitado, qtd_digitada, preco_digitado)
        messagebox.showinfo("Sucesso", "Produto inserido no sistema!")
        entry_nome.delete(0, tk.END)
        entry_qtd.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        atualizar_tabela()

def atualizar_tabela():
    for linha in tree.get_children():
        tree.delete(linha)
    for produto in listar_produtos():
        id_prod, nome, qtd, preco = produto[0], produto[1], produto[2], produto[3]
        status = "✅ REGISTRADO" if qtd > 0 else "⚠️ SEM ESTOQUE"
        tree.insert("", "end", values=(id_prod, nome, qtd, f"{preco:.2f}", status))

def acao_excluir():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um produto na tabela para excluir!")
        return
    valores      = tree.item(item_selecionado, 'values')
    id_produto   = valores[0]
    nome_produto = valores[1]
    confirmacao = messagebox.askyesno("Confirmar Exclusão", f'Tem certeza que deseja apagar "{nome_produto}" definitivamente?')
    if confirmacao:
        sucesso = deletar_produto(id_produto)
        if sucesso:
            logger.log_delete(nome_produto)
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
            atualizar_tabela()

def acao_editar():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um produto para editar!")
        return
    valores = tree.item(item_selecionado, 'values')
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, valores[1])
    entry_qtd.delete(0, tk.END)
    entry_qtd.insert(0, valores[2])
    entry_preco.delete(0, tk.END)
    entry_preco.insert(0, valores[3])

def acao_atualizar():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione o produto na tabela antes de clicar em Atualizar!")
        return
    valores    = tree.item(item_selecionado, 'values')
    id_produto = valores[0]
    novo_nome  = entry_nome.get()
    nova_qtd   = entry_qtd.get()
    novo_preco = entry_preco.get()
    sucesso = atualizar_produto(id_produto, novo_nome, nova_qtd, novo_preco)
    if sucesso:
        logger.log_update(novo_nome, nova_qtd, novo_preco)
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_qtd.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        atualizar_tabela()

criar_tabela()
logger = AuditLogger()

root = tk.Tk()
root.title("El Bigode - Estoque")
root.geometry("1920x1080")
root.resizable(True, True)

cor_de_fundo = "#181C2B"
cor_preto    = "#0B0F1D"
cor_branco   = "#FFFFFF"
cor_borda    = "#1E90FF"
root.configure(bg=cor_de_fundo)

style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel",  background=cor_preto, foreground=cor_branco)
style.configure("TButton", font=("Arial", 12, "bold"), padding=8, background="#16139D", foreground="#FFFFFF")
style.map("TButton", foreground=[('pressed', "#000000"), ('active', "#1500FF")], background=[('active',  "#002184")])

frame_topo = tk.Frame(root, bg=cor_preto, bd=0, highlightthickness=1, highlightbackground=cor_borda, highlightcolor=cor_borda)
frame_topo.pack(fill="x", padx=20, pady=20, ipady=10)

titulo    = ttk.Label(frame_topo, text="EL BIGODE", font=("Bahnschrift Condensed", 70, "bold"))
titulo.pack(pady=(10, 0))
subtitulo = ttk.Label(frame_topo, text="I N F O R M Á T I C A", font=("Segoe UI", 20, "bold"))
subtitulo.pack(pady=(0, 10))

frame_form = tk.Frame(root, bg=cor_preto, bd=0, highlightthickness=1, highlightbackground=cor_borda, highlightcolor=cor_borda)
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

botoes = tk.Frame(root, bg=cor_de_fundo)
botoes.pack(pady=(10, 20))

ttk.Button(botoes, text="➕ CADASTRAR", command=acao_cadastrar).grid(row=0, column=0, padx=15)
ttk.Button(botoes, text="🔄 ATUALIZAR", command=acao_atualizar).grid(row=0, column=1, padx=15)
ttk.Button(botoes, text="🗑 EXCLUIR",   command=acao_excluir  ).grid(row=0, column=2, padx=15)
ttk.Button(botoes, text="✏️ EDITAR",    command=acao_editar   ).grid(row=0, column=3, padx=15)

frame_tabela = tk.Frame(root, bg="#B4B4B4", bd=1)
frame_tabela.pack(fill="both", expand=True, padx=5)

style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
style.configure("Treeview", background="#1A2761", foreground=cor_branco, fieldbackground=cor_de_fundo, rowheight=30, font=("Arial", 11), borderwidth=0)
style.configure("Treeview.Heading", background="#FFFFFF", font=("Arial", 12, "bold"))
style.map("Treeview.Heading", background=[('pressed', "#0C1644"), ('active', "#909090")], foreground=[('pressed', "#FFFFFF"), ('active', '#FFFFFF')])

colunas = ("ID", "NOME", "QUANTIDADE", "PREÇO (R$)", "STATUS")
tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)
tree.pack(fill="both", expand=True)

tree.heading("ID",          text="ID");          tree.column("ID",          width=80,  anchor="center")
tree.heading("NOME",        text="NOME");         tree.column("NOME",        width=350, anchor="w")
tree.heading("QUANTIDADE",  text="QUANTIDADE");   tree.column("QUANTIDADE",  width=100, anchor="center")
tree.heading("PREÇO (R$)",  text="PREÇO (R$)");  tree.column("PREÇO (R$)",  width=120, anchor="center")
tree.heading("STATUS",      text="STATUS");       tree.column("STATUS",      width=150, anchor="center")

atualizar_tabela()
root.mainloop()