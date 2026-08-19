from login_menu import *

while True:
    usuarioLog = fazerLogin()

    if usuarioLog:
        menuUser(usuarioLog)