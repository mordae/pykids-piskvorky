from flask import Flask, request, redirect, render_template

a = Flask(__name__, template_folder='.')

plocha = []

for x in range(20):
    radek = []
    for y in range(20):
        radek.append(' ')
    plocha.append(radek)


# Když uživatel vleze na hlavní stránku projektu.
@a.route('/')
def index():
    # Bydlí tady: https://pad.pirati.cz/p/piskvorky.html
    return render_template('piskvorky.html', plocha=plocha)

# Když vleze na /tah.
@a.route('/tah')
def kontrola():
    x = int(request.args['x'])
    y = int(request.args['y'])

    # Zpracujeme jeho tah a do buňky, pokud byla volná dáme 'O'.
    if plocha[x][y] == ' ':
        plocha[x][y] = 'O'

    # Následně vymyslíme tah počítače a dáme někam 'X'.

    return redirect('/')

if __name__ == '__main__':
    a.debug = True
    a.run()


