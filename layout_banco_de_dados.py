import PySimpleGUI as sg
import mysql.connector

sg.theme('topanga')

layout = [
    [sg.Text('Please enter your Name, Address, Senha, Phone')],
    [sg.Text('Name', size=(15, 1)), sg.InputText()],
    [sg.Text('Address', size=(15, 1)), sg.InputText()],
    [sg.Text('Senha', size=(15, 1)), sg.InputText(password_char='*')],
    [sg.Text('Phone', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('User Registration', layout)
event, values = window.read()
window.close()

if event == 'Submit':
    Name = values[0]
    Address = values[1]
    Senha = values[2]
    Phone = values[3]

    try:
        conn = mysql.connector.connect(
            host='localhost',  
            user='root',  
            password='',  
            database='python'  
        )
        print("Conexão com o banco de dados estabelecida com sucesso.")

        cursor = conn.cursor()
        cursor.execute("SHOW TABLES LIKE 'JV'")
        result = cursor.fetchone()

        if result:
            print("A tabela 'JV' já existe. Ignorando a criação da tabela.")
        else:
            create_table_query = """
            CREATE TABLE JV (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Address VARCHAR(255),
                Senha VARCHAR(255),
                Phone VARCHAR(255)
            )
            """
            cursor.execute(create_table_query)
            print("Tabela 'JV' criada com sucesso.")
        insert_query = "INSERT INTO JV (Name, Address, Senha, Phone) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (Name, Address, Senha, Phone))
        conn.commit()
        conn.close()
        print("Usuário registrado com sucesso no banco de dados.")
    except mysql.connector.Error as error:
        print("Erro ao conectar ao banco de dados:", error)
