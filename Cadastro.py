import mysql.connector
import pandas as pd

engine = mysql.connector.connect(
    host='localhost',
    database='nomeDoBanco',
    user='root',
    password='senha'
)
cursor = engine.cursor()


def mostrar_registros():
    cursor.execute('select Nome from funcionarios order by Nome')
    registros = cursor.fetchall()
    df = pd.DataFrame(registros)
    print(df)
    print()
    print(f'{cursor.rowcount} registros')


def cadastrar():
    cursor.execute(f'insert into funcionarios values(default, "{nome}")')
    engine.commit()


mostrar_registros()
print()
opc = str(input('Deseja cadastrar um novo funcionário?(S/N) ')).upper()[0]
if opc == 'S':
    while True:
        nome = str(input('Digite o nome ou 0 para encerrar: '))
        if nome == '0':
            print('Programa encerrado!')
            cursor.close()
            engine.close()
            exit()
        else:
            cadastrar()
else:
    print('Programa encerrado!')
    cursor.close()
    engine.close()
    exit()
