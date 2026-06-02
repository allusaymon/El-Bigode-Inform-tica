import os
from datetime import datetime

LOG_FILE = "log_estoque.txt"

class AuditLogger:
    def __init__(self, filepath: str = LOG_FILE):
        self.filepath = filepath
        self._gravar("SISTEMA - Sistema El Bigode Informática iniciado.")

    def log_insert(self, produto: str, quantidade, preco=None) -> None:
        try:
            produto = str(produto).strip()
            quantidade = int(quantidade)
            if preco is not None:
                preco = float(preco)
                mensagem = f'INSERÇÃO - Produto "{produto}" (Qtd: {quantidade}, Preço: R$ {preco:.2f}) cadastrado com sucesso.'
            else:
                mensagem = f'INSERÇÃO - Produto "{produto}" (Qtd: {quantidade}) cadastrado com sucesso.'
            self._gravar(mensagem)
        except (ValueError, TypeError) as e:
            self._gravar(f'ERRO - Falha ao logar inserção de "{produto}": {e}')

    def log_update(self, produto: str, nova_qtd, novo_preco) -> None:
        try:
            produto = str(produto).strip()
            nova_qtd = int(nova_qtd)
            novo_preco = float(novo_preco)
            mensagem = f'ATUALIZAÇÃO - Produto "{produto}" alterado (Nova Qtd: {nova_qtd}, Novo Preço: R$ {novo_preco:.2f}).'
            self._gravar(mensagem)
        except (ValueError, TypeError) as e:
            self._gravar(f'ERRO - Falha ao logar atualização de "{produto}": {e}')

    def log_delete(self, produto: str) -> None:
        produto = str(produto).strip()
        mensagem = f'EXCLUSÃO - Produto "{produto}" removido do sistema.'
        self._gravar(mensagem)

    def get_all_logs(self) -> list:
        try:
            if not os.path.exists(self.filepath):
                return []
            with open(self.filepath, "r", encoding="utf-8") as f:
                return [linha.rstrip("\n") for linha in f if linha.strip()]
        except OSError as e:
            print(f"[AuditLogger] Erro ao ler o log: {e}")
            return []

    def get_stats(self) -> dict:
        linhas = self.get_all_logs()
        return {
            "total"       : len(linhas),
            "insercoes"   : sum(1 for l in linhas if "INSERÇÃO"    in l),
            "atualizacoes": sum(1 for l in whitespaces if "ATUALIZAÇÃO" in l),
            "exclusoes"   : sum(1 for l in linhas if "EXCLUSÃO"    in l),
            "erros"       : sum(1 for l in linhas if "ERRO"        in l),
            "sistema"     : sum(1 for l in linhas if "SISTEMA"     in l),
        }

    def get_log_path(self) -> str:
        return os.path.abspath(self.filepath)

    def _timestamp(self) -> str:
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def _gravar(self, mensagem: str) -> None:
        linha = f"[{self._timestamp()}] {mensagem}\n"
        try:
            with open(self.filepath, "a", encoding="utf-8") as f:
                f.write(linha)
        except OSError as e:
            print(f"[AuditLogger] FALHA AO GRAVAR NO LOG: {e}")