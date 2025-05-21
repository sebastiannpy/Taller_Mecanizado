from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Página de inicio (login) con tu nuevo diseño
HTML = """
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
            transition: background-color 0.3s;
        }
        .btn.primary:hover {
            background-color: #B51FDF;
        }
        .info {
            padding: 60px 40px;
            background-color: #FFFFFF;
            text-align: center;
            color: black;
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

# Página del administrador (sin cambios)
html_admin = """
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
            gap: 80px;
            padding: 40px 60px 20px;
            background-color: #ffffff;
            max-width: 700px;
            margin: 0 auto;
        }
        .columna {
            display: flex;
            flex-direction: column;
            gap: 30px;
            width: 250px;
        }
        .columna button {
            background-color: #b51fdf;
            color: white;
            padding: 25px 30px;
            border: none;
            border-radius: 20px;
            font-size: 20px;
            cursor: pointer;
            transition: background 0.3s;
            width: 100%;
            box-sizing: border-box;
        }
        .columna button:hover {
            background-color: #9316b8;
        }
        .cerrar-sesion-contenedor {
            display: flex;
            justify-content: center;
            margin: 20px auto 40px;
            max-width: 700px;
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
            box-sizing: border-box;
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
        <form method="post" style="display: flex; gap: 80px;">
            <div class="columna">
                <button type="submit" name="opcion" value="historial">Historial de abonos</button>
                <button type="submit" name="opcion" value="buscar">Buscar trabajo</button>
                <button type="submit" name="opcion" value="trabajos">Trabajos por aprobar</button>
            </div>
            <div class="columna">
                <button type="submit" name="opcion" value="registrar">Registrar cliente</button>
                <button type="submit" name="opcion" value="solicitar">Solicitar trabajo</button>
                <button type="submit" name="opcion" value="cerrar_interno">Historial de pagos</button>
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
    return render_template_string(HTML, mensaje=mensaje)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        opcion = request.form.get("opcion")
        if opcion == "cerrar" or opcion == "cerrar_interno":
            return redirect(url_for("home"))
    return render_template_string(html_admin)

if __name__ == "__main__":
    app.run(debug=True)
