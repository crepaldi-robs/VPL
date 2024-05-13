UID = input()
password = input()

ok = False
if UID == 'turing' and password == 'tmachine':
    ok = True
if UID == 'llace' and password == 'anengine':
    ok = True
if UID == 'hopper' and password == 'business':
    ok = True

if ok:
    print('Bem-vindo!')
else:
    print('Login ou senha incorreto')