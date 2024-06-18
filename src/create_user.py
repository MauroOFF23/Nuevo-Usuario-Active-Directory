# src/create_user.py

import ldap
from src.config import LDAP_ADDRESS, LDAP_USERNAME, LDAP_PASSWORD

def create_user(address, username, password, new_user):
    conn = ldap.initialize(f'ldap://{address}')
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    
    try:
        conn.simple_bind_s(username, password)
        dn = f"CN={new_user['username']},OU=Alumnos,DC=pod3test,DC=local"
        attrs = [
            ('objectClass', [b'user']),
            ('sAMAccountName', [new_user['username'].encode('utf-8')]),
            ('userPrincipalName', [new_user['username'].encode('utf-8') + b'@pod3test.local']),
            ('givenName', [new_user['first_name'].encode('utf-8')]),
            ('sn', [new_user['last_name'].encode('utf-8')]),
            ('displayName', [new_user['display_name'].encode('utf-8')]),
            ('userPassword', [new_user['password'].encode('utf-8')])
        ]
        conn.add_s(dn, attrs)
        print("Usuario creado exitosamente.")
    except ldap.LDAPError as e:
        print(f"Error al crear usuario: {e}")
    finally:
        conn.unbind_s()

if __name__ == "__main__":
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    display = input("Display Name: ")
    password = input("Contraseña: ")

    new_user = {
        'username': 'UPD003',
        'first_name': nombre,
        'last_name': apellido,
        'display_name': display,
        'password': password
    }

    create_user(LDAP_ADDRESS, LDAP_USERNAME, LDAP_PASSWORD, new_user)
