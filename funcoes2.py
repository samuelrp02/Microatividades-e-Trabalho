def LoginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem vindo, Administrador')
    else:
        print('Bem vindo, Usuário')

LoginUsuario('Admin')
LoginUsuario('admin')
LoginUsuario('User')
LoginUsuario('usuário')
LoginUsuario('etc')