from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# HTML de la página de login
HTML_LOGIN = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Taller de Mecanizado</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #f5f5f5;
            color: #222;
        }
        header {
            background-color: #444242;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
        }
        header h1 {
            font-size: 24px;
        }
        nav a {
            color: white;
            margin-left: 20px;
            text-decoration: none;
            font-weight: bold;
        }
        .hero {
            background-color: #671cd6;
            color: white;
            padding: 100px 40px;
            text-align: center;
        }
        .hero-content h2 {
            font-size: 40px;
            margin-bottom: 10px;
        }
        .hero-content p {
            font-size: 18px;
            margin-bottom: 30px;
        }
        .form-container {
            margin-top: 20px;
        }
        .input-field {
            padding: 10px 15px;
            margin: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 2px solid #444242;
            width: 200px;
        }
        .btn.primary {
            background-color: #B51FDF;
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            border: none;
            border-radius: 30px;
            cursor: pointer;
        }
        .info {
            padding: 60px 40px;
            background-color: #FFFFFF;
            text-align: center;
        }
        .mensaje {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }
        .mensaje.error {
            color: #EBF477;
        }
        footer {
            background-color: #444242;
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Taller de Mecanizado</h1>
        <nav>
            <a href="#">Bienvenid@, Administrador!</a>
        </nav>
    </header>
    <section class="hero">
        <div class="hero-content">
            <h2>Mecánica confiable, rápida y moderna</h2>
            <p>Reparación, mantenimiento y diagnóstico para tu vehículo.</p>
            <form method="POST" class="form-container">
                <input type="text" name="documento" placeholder="Documento" class="input-field" required>
                <input type="password" name="contrasena" placeholder="Contraseña" class="input-field" required>
                <button type="submit" class="btn primary">Iniciar sesión</button>
            </form>
            {% if mensaje %}
                <div class="mensaje error">{{ mensaje }}</div>
            {% endif %}
        </div>
    </section>
    <section class="info">
        <h3>¡Estamos para ayudarte!</h3>
        <p>Revisión gratuita en la primera visita. Profesionales certificados.</p>
    </section>
    <footer>
        <p>&copy; 2025 Taller Mecánico Pro. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

HTML_ADMIN = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Administrador - Taller de Mecanizado</title>
    <style>
        html, body {
            height: 100%;
            display: flex;
            flex-direction: column;
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #f8f8f8;
            color: #222;
        }
        header {
            background-color: #444242;
            color: white;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .banner {
            background-color: #671CD6;
            color: white;
            padding: 60px 40px;
            text-align: center;
        }
        .opciones {
            display: flex;
            justify-content: center;
            padding: 40px 20px;
            background-color: #ffffff;
            gap: 50px;
        }
        .columna {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }
        .columna button {
            background-color: #b51fdf;
            color: white;
            padding: 25px 30px;
            border: none;
            border-radius: 20px;
            font-size: 20px;
            cursor: pointer;
            min-width: 220px;
        }
        .columna button:hover {
            background-color: #9316b8;
        }
        .cerrar-sesion-contenedor {
            display: flex;
            justify-content: center;
            margin: 20px auto 40px;
        }
        .cerrar-sesion-contenedor button {
            background-color: #EBF477;
            color: black;
            padding: 25px 40px;
            border: 2px solid black;
            border-radius: 20px;
            font-size: 20px;
            cursor: pointer;
            width: 220px;
        }
        footer {
            background-color: #444242;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: auto;
        }
    </style>
</head>
<body>
    <header>
        <h1>Taller de mecanizado</h1>
    </header>
    <section class="banner">
        <h2>Bienvenido Administrador</h2>
        <p>Selecciona una opción para continuar</p>
    </section>
    <section class="opciones">
        <form method="post" style="display: flex; gap: 50px;">
            <div class="columna">
                <button type="submit" name="opcion" value="historial">Historial de abonos</button>
                <button type="submit" name="opcion" value="buscar">Buscar trabajo</button>
                <button type="submit" name="opcion" value="trabajos">Trabajos por aprobar</button>
            </div>
            <div class="columna">
                <button type="submit" name="opcion" value="registrar">Registrar cliente</button>
                <button type="submit" name="opcion" value="pagos">Historial de pagos</button>
            </div>
        </form>
    </section>
    <div class="cerrar-sesion-contenedor">
        <form method="post">
            <button type="submit" name="opcion" value="cerrar">Cerrar sesión</button>
        </form>
    </div>
    <footer>
        &copy; 2025 Taller de mecanizado. Todos los derechos reservados.
    </footer>
</body>
</html>
"""



# HTML para el formulario de registro de cliente
HTML_REGISTRO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registrar Cliente - Taller de Mecanizado</title>
    <style>
        /* Todo igual, sin cambiar estética */
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #f8f8f8;
            color: #222;
        }
        header {
            background-color: #444242;
            color: white;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .banner {
            background-color: #671CD6;
            color: white;
            padding: 100px 40px;
            text-align: center;
        }
        .formulario {
            background: white;
            padding: 60px 20px;
            text-align: center;
        }
        .fila-triple {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }
        .fila-triple input {
            flex: 1;
            min-width: 200px;
            max-width: 250px;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #444242;
            font-size: 16px;
        }
        .formulario button {
            background-color: #b51fdf;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            margin-top: 25px;
            cursor: pointer;
        }
        .popup {
            position: fixed;
            top: 30px;
            right: 30px;
            background-color: #ebf477;
            color: black;
            border: 1px solid #ebf477;
            padding: 20px 25px;
            border-radius: 10px;
        }
        .popup .close {
            position: absolute;
            top: 8px;
            right: 12px;
            font-weight: bold;
            cursor: pointer;
        }
        footer {
            background-color: #444242;
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
</head>
<body>
<header>
    <h1>Taller de mecanizado</h1>
    <nav><a href="#">Inicio</a></nav>
</header>
<section class="banner">
    <h2>Tu coche en buenas manos</h2>
    <p>Expertos en mantenimiento y reparación automotriz</p>
</section>
<section class="formulario" id="formulario">
    <h3>Registrar</h3>
    <form method="post" action="#formulario">
        <div class="fila-triple">
            <input type="text" name="nombre" placeholder="Nombre completo" required>
            <input type="text" name="documento" placeholder="Número de documento" required>
            <input type="tel" name="telefono" placeholder="Teléfono" required>
            <input type="text" name="especificaciones" placeholder="Especificaciones (máx. 30)" maxlength="30">
        </div>
        <button type="submit">Registrar</button>
    </form>
</section>
{% if registrado %}
<div class="popup" id="popup">
    <span class="close" onclick="document.getElementById('popup').style.display='none'">&times;</span>
    ¡El cliente se ha registrado correctamente!
</div>
{% endif %}
<footer>
    &copy; 2025 Taller de mecanizado. Todos los derechos reservados.
</footer>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    mensaje = ""
    if request.method == "POST":
        usuario = request.form.get("documento")
        contrasena = request.form.get("contrasena")
        if usuario == "123456789" and contrasena == "admin123":
            return redirect(url_for("admin"))
        else:
            mensaje = "Usuario o contraseña incorrectos"
    return render_template_string(HTML_LOGIN, mensaje=mensaje)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        opcion = request.form.get("opcion")
        if opcion == "cerrar":
            return redirect(url_for("home"))
        elif opcion == "registrar":
            return redirect(url_for("registrar_cliente"))
    return render_template_string(HTML_ADMIN)

@app.route("/registrar", methods=["GET", "POST"])
def registrar_cliente():
    registrado = False
    if request.method == "POST":
        nombre = request.form.get("nombre")
        documento = request.form.get("documento")
        telefono = request.form.get("telefono")
        especificaciones = request.form.get("especificaciones")
        print(f"Cliente registrado: {nombre}, {documento}, {telefono}, {especificaciones}")
        registrado = True
    return render_template_string(HTML_REGISTRO, registrado=registrado)

if __name__ == "__main__":
    app.run(debug=True)

