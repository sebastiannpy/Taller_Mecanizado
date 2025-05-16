from flask import Flask, render_template_string

app = Flask(__name__)

# HTML para el historial de pagos
html_historial_pago = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Historial de Pago</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f0fa;
            color: #333;
        }

        header {
            background-color: #5a00b3;
            color: white;
            padding: 20px;
            text-align: center;
        }

        h2 {
            text-align: center;
            color: #5a00b3;
            margin: 30px 0;
        }

        table {
            width: 80%;
            margin: auto;
            border-collapse: collapse;
            background-color: white;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            border-radius: 10px;
            overflow: hidden;
        }

        th, td {
            padding: 15px;
            text-align: left;
        }

        th {
            background-color: #b51fdf;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f3e6ff;
        }

        tr:hover {
            background-color: #ebd4ff;
        }

        .botones {
            display: flex;
            justify-content: center;
            margin: 40px 0;
        }

        .boton {
            background-color: #b51fdf;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
        }

        .boton:hover {
            background-color: #9316b8;
        }
    </style>
</head>
<body>

<header>
    <h1>Historial de Pago</h1>
</header>

<h2>Pagos Realizados</h2>

<table>
    <tr>
        <th>Nombre</th>
        <th>Método</th>
        <th>Estado</th>
    </tr>
    <tr>
        <td>Valeria Gómez</td>
        <td>Transferencia</td>
        <td>Pagado</td>
    </tr>
    <tr>
        <td>Martín Ríos</td>
        <td>Efectivo</td>
        <td>Pendiente</td>
    </tr>
    <tr>
        <td>Ana Pérez</td>
        <td>Tarjeta</td>
        <td>Pagado</td>
    </tr>
</table>

<div class="botones">
    <a href="/cerrar_sesion" class="boton">Cerrar Sesión</a>
</div>

</body>
</html>
"""

@app.route("/historial_pago")
def historial_pago():
    return render_template_string(html_historial_pago)

@app.route("/cerrar_sesion")
def cerrar_sesion():
    return "<h2>Has cerrado sesión. ¡Gracias por usar el sistema!</h2>"

if __name__ == "__main__":
    app.run(debug=True)