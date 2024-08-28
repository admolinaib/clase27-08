dataBaseName = "gestorbd"
userName = "root"
usserPassword = "root"
connectionPort = 3306
server = "localhost"

#creando la conexion
dataBaseConnection = f"mysql+mysqlconnector://{userName}:{usserPassword}@{server}:{connectionPort}/{dataBaseName}"

print(dataBaseConnection)