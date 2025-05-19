from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registrar Cliente - Taller de Mecanizado</title>
    <style>
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

        header h1 {
            margin: 0;
        }

        nav a {
            color: white;
            margin-left: 20px;
            text-decoration: none;
            font-weight: bold;
        }

        .banner {
            background-color: #671CD6;
            color: white;
            padding: 100px 40px;
            text-align: center;
        }

        .banner h2 {
            font-size: 40px;
            margin-bottom: 10px;
        }

        .banner p {
            font-size: 20px;
        }

        .formulario {
            background: white;
            padding: 60px 20px;
            text-align: center;
        }

        .formulario h3 {
            font-size: 28px;
            margin-bottom: 20px;
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
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            z-index: 1000;
            max-width: 300px;
        }

        .popup .close {
            position: absolute;
            top: 8px;
            right: 12px;
            color: black;
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
    <nav>
        <a href="#">Inicio</a>
    </nav>
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
def index():
    registrado = False
    if request.method == "POST":
        nombre = request.form.get("nombre")
        documento = request.form.get("documento")
        telefono = request.form.get("telefono")
        especificaciones = request.form.get("especificaciones")
        print(f"Cliente registrado: {nombre}, {documento}, {telefono}, {especificaciones}")
        registrado = True

    return render_template_string(html, registrado=registrado)

if __name__ == "__main__":
    app.run(debug=True)



