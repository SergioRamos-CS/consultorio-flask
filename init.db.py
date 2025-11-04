import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
    
cur = connection.cursor()

cur.execute("INSERT INTO posts (nome, fone, email, mensagem) VALUES (?, ?, ?, ?)",
            ('Teste', '13991671829', 'srramosagmailpcom', 'Primeira mensagem de teste')
           )

cur.execute("INSERT INTO posts (nome, fone, email, mensagem) VALUES (?, ?, ?, ?)",
            ('Maria', '13991671830', 'mariaexemploemailcom', 'Segunda mensagem de teste')
           )

connection.commit()
connection.close()