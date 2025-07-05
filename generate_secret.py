import secrets
import string

# Generar una clave secreta segura de 50 caracteres
characters = string.ascii_letters + string.digits + string.punctuation
secret_key = ''.join(secrets.choice(characters) for _ in range(50))

print("Clave secreta generada:")
print(secret_key)
