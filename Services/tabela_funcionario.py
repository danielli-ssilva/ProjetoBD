import sqlite3

conexao = sql3.connect("Empresa.db");
cursor = conexao.cursor();

cursor.execute(
    CREATE TABLE funcionario (
        codigo INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL,
        dias_trablhados INTEGER,
        valorDia REAL,
        salarioBase REAL,
        comissao REAL
    );
)

cursor.close()
print("Tabela funcionario criada!")