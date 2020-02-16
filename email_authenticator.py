#!/usr/bin/python3
# -*- coding: utf-8 -*-


authenticator = False
email = str(input("Ingresa un correo a verificar: "))

for valor in email:
    if (
            valor == '@' or
            valor == '@gmail.com' or
            valor == '@outlook'
        ):
        authenticator = True

if (authenticator == True):
    print("Es un correo electrónico válido ;)")
else:
    print("No es un correo electrónico válido >;(")


