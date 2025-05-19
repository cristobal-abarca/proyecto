from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de usuarios previamente registrados
usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro

        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template(
            'ejercicio1.html',
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total_con_descuento=total_con_descuento
        )
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        if usuario in usuarios and usuarios[usuario] == contraseña:
            mensaje = f"Bienvenido {'Administrador' if usuario == 'juan' else 'Usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', mensaje=mensaje)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)