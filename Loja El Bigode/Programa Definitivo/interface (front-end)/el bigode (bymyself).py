import tkinter as tk 
from tkinter import ttk

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

cadastrar_botao = ttk.Button(botoes, text="➕ CADASTRAR")
cadastrar_botao.grid(row=0, column=0, padx=15)

atualizar_botao = ttk.Button(botoes, text="🔄 ATUALIZAR")
atualizar_botao.grid(row=0, column=1, padx=15)

excluir_botao = ttk.Button(botoes, text="🗑 EXCLUIR")
excluir_botao.grid(row=0, column=2, padx=15)

editar_botao = ttk.Button(botoes, text="✏️ EDITAR")
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

root.mainloop()
