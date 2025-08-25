import paramiko

def obtener_version_servidor(hostname, username, password):
    try:
        # Crear una instancia del cliente SSH
        cliente_ssh = paramiko.SSHClient()
        
        # Añadir la clave del servidor automáticamente (esto es inseguro en producción)
        cliente_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Conectar al servidor
        cliente_ssh.connect(hostname, username=username, password=password)
        
        # Ejecutar el comando para obtener la versión del servidor
        stdin, stdout, stderr = cliente_ssh.exec_command('lsb_release -a')
        
        # Leer la salida del comando
        version = stdout.read().decode()
        
        # Cerrar la conexión SSH
        cliente_ssh.close()
        
        return version
    
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Solicitar host, usuario y contraseña
    hostname = input("Host del servidor (IP o dominio): ")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    
    # Obtener la versión del servidor
    version = obtener_version_servidor(hostname, username, password)
    
    # Mostrar la versión
    print("\nVersión del servidor:")
    print(version)

if __name__ == "__main__":
    main()