acs8000-simple/
├─ playbook.yml
└─ vars.yml

ACS8000 Firmware Upgrade (Simple Project)

---------Automatización básica para:
Mostrar versión actual de firmware
Comparar contra versión objetivo
Descargar firmware si es necesario
Instalar firmware
Solicitar usuario y contraseña por prompt
Verificar versión final

---------Usa API REST oficial del ACS8000 vía ansible.builtin.uri.
Estructura del Proyecto
acs8000-simple/
├── playbook.yml
├── vars.yml
└── README.md

Requisitos
Ansible 2.9+ (recomendado 2.12+)
Python 3
Acceso HTTPS al ACS8000 (puerto 48048 por defecto)
Usuario con permisos API en el ACS
Firmware disponible en servidor FTP/SFTP/SCP/HTTPS
Verificar versión de Ansible:
ansible --version  

---------Inventory Requerido
Tu inventario debe tener un grupo llamado acs8000.
Ejemplo inventory.yml:

all:
  children:
    acs8000:
      hosts:
        acs8000-01:
          ansible_host: 10.20.30.40
        acs8000-02:
          ansible_host: 10.20.30.41

---------Configuración – vars.yml
Aquí defines:
Versión objetivo
Parámetros API
Servidor donde está el firmware
Tiempo de polling

---------Ejemplo:

acs_target_version: "2.32.1"
acs_api_scheme: "https"
acs_api_port: 48048
acs_api_base: "/api/v1"
acs_validate_certs: false

acs_fw_download:
  protocol: "https"
  ipAddress: "10.20.30.80"
  username: "fwuser"
  password: "fwpass"
  directory: "/pub/firmware/"
  filename: "ACS8xxx_v2.32.1.fl"

acs_poll_delay: 10
acs_poll_retries: 90

---------Flujo del Playbook
Cómo Ejecutarlo
Desde la carpeta del proyecto:
ansible-playbook -i inventory.yml playbook.yml

Te pedirá:
ACS API username:
ACS API password:


---------Flujo del Playbook
Login → obtiene JWT token
Consulta versión actual
Compara con versión objetivo
Si es menor:
Descarga firmware
Espera a que termine
Ejecuta instalación
Espera resultado
Verifica versión final
Si la versión ya está actualizada:
Upgrade needed? False
No hace nada más.

---------Tiempo de Upgrade
Depende del modelo y tamaño del firmware.
Controlado por:
acs_poll_delay: 10
acs_poll_retries: 90

Total máximo espera = delay x retries

---------Ejemplo:
10 × 90 = 900 segundos (15 minutos)

Consideraciones Importantes
 Validar Upgrade Path

Algunas versiones requieren upgrade intermedio.

Revisar release notes oficiales de Vertiv antes de subir directo.

2️⃣ Certificados Self-Signed

Si el ACS usa certificado no confiable:

acs_validate_certs: false

En producción se recomienda certificado válido.

---------Ejecutar uno por uno (recomendado)

Para evitar actualizar todos al mismo tiempo:
Agregar en playbook.yml:
serial: 1
4️ Reboot

El ACS puede reiniciarse durante instalación.

Ansible seguirá consultando hasta que la API responda.

---------Troubleshooting
Error 401 Unauthorized
Usuario incorrecto
Usuario sin permisos API
Download failed
El ACS no puede alcanzar el servidor firmware
Usuario/Password incorrecto del servidor
Firewall bloqueando
Install failed
Imagen corrupta
Espacio insuficiente
Upgrade path incorrecto

--------- Ejemplo de Salida Esperada
TASK [Show versions]
ok: [acs8000-01] =>
  current: 2.30.0
  target: 2.32.1

TASK [Print decision]
ok: [acs8000-01] =>
  Upgrade needed? True

TASK [Show version after]
ok: [acs8000-01] =>
  after: 2.32.1
🔐 Seguridad

Password API no se guarda (vars_prompt + no_log)

Credenciales de servidor firmware están en vars.yml
→ Se recomienda usar Ansible Vault:

ansible-vault encrypt vars.yml

Ejecutar con:
ansible-playbook -i inventory.yml playbook.yml --ask-vault-pass
