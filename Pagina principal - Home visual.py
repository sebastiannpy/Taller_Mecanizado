from flask import Flask, render_template_string

app = Flask(__name__)

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

        header h1 {
            margin: 0;
        }

        .banner {
            background-color: #671CD6;
            color: white;
            padding: 60px 40px;
            text-align: center;
        }

        .banner h2 {
            font-size: 36px;
            margin-bottom: 10px;
        }

        .opciones {
            display: flex;
            justify-content: center;
            gap: 80px; /* espacio entre columnas */
            padding: 40px 60px 20px; /* un poco menos abajo para separar del botón nuevo */
            background-color: #ffffff;
            max-width: 700px;
            margin: 0 auto;
        }

        .columna {
            display: flex;
            flex-direction: column;
            gap: 30px; /* espacio entre botones vertical */
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

        /* Contenedor para el botón "Cerrar sesión" nuevo */
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
            border: black;
            border-radius: 20px;
            font-size: 20px;
            cursor: pointer;
            transition: background 0.3s;
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
    <form action="#" method="get" style="display: flex; gap: 80px;">
        <div class="columna">
            <button type="submit" name="opcion" value="historial">Historial de abonos</button>
            <button type="submit" name="opcion" value="buscar">Buscar trabajo</button>
            <button type="submit" name="opcion" value="trabajos">Trabajos por aprobar</button>
        </div>
        <div class="columna">
            <button type="submit" name="opcion" value="registrar">Registrar cliente</button>
            <button type="submit" name="opcion" value="solicitar">Historial de pagos</button>
        </div>
    </form>
</section>

<!-- Nuevo botón "Cerrar sesión" centrado debajo -->
<div class="cerrar-sesion-contenedor">
    <form action="#" method="get" style="width: 100%; max-width: 700px;">
        <button type="submit" name="opcion" value="cerrar">Cerrar sesión</button>
    </form>
</div>

<footer>
    &copy; 2025 Taller de mecanizado. Todos los derechos reservados.
</footer>

</body>
</html>
"""

@app.route("/")  # Página principal
def admin():
    return render_template_string(html_admin)

if __name__ == "__main__":
    app.run(debug=True)




