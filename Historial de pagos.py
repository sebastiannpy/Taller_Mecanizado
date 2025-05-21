from flask import Flask, request, redirect, url_for, render_template_string
from datetime import datetime

app = Flask(__name__)

# Datos temporales
historial_pagos = [
    {"nombre": "Ana López", "documento": "12345678", "fecha": "2024-05-01", "estado": "Pagado", "metodo": "Tarjeta"},
    {"nombre": "Carlos Pérez", "documento": "98765432", "fecha": "2024-05-02", "estado": "Pendiente", "metodo": "Efectivo"},
]

# Estilo CSS global
style_css = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
    }

    .barra-superior {
        background-color: #800080;
        padding: 50px;  /* Barra superior más grande */
        text-align: center;
        color: white;
        font-size: 32px;
        font-weight: bold;
    }

    .contenido {
        padding: 30px;
        text-align: center;
    }

    h1 {
        color: #000;
        margin-bottom: 40px;
    }

    form {
        display: inline-block;
        text-align: left;
        margin-top: 20px;
    }

    label {
        display: block;
        margin-top: 10px;
    }

    input, select {
        width: 100%;
        padding: 8px;
        margin-top: 5px;
    }

    button {
        margin-top: 15px;
        padding: 10px 20px;
        background-color: #b51fdf;
        color: white;
        border: none;
        cursor: pointer;
    }

    .boton {
        display: inline-block;
        margin: 15px;
        padding: 10px 15px;
        background-color: #b51fdf;
        color: white;
        text-decoration: none;
        border-radius: 5px;
    }

    .boton-negro {
        display: inline-block;
        margin: 15px;
        padding: 10px 15px;
        background-color: black; /* Botón de borrar en negro */
        color: white;
        text-decoration: none;
        border-radius: 5px;
    }

    table {
        width: 95%;
        margin: 60px auto 20px auto;
        border-collapse: collapse;
    }

    th {
        background-color: #800080;  /* Encabezado en morado */
        color: white;
    }

    th, td {
        border: 1px solid #ccc;
        padding: 10px;
        text-align: center;
    }

    .acciones a {
        margin: 0 5px;
        font-size: 14px;
    }

    .acciones .borrar {
        background-color: black;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        text-decoration: none;
    }

    .acciones .borrar:hover {
        background-color: #444;
    }

    /* Estilo del footer */
    .footer {
        background-color: #444242;
        color: white;
        text-align: center;
        padding: 15px 0;
        position: absolute;
        width: 100%;
        bottom: 0;
    }

    .footer a {
        color: #800080;
        text-decoration: none;
    }

    .footer a:hover {
        text-decoration: underline;
    }
</style>
"""

# Página principal con historial de pagos
historial_template = style_css + """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Historial de Pagos</title>
</head>
<body>
    <div class="barra-superior">Sistema de Pagos</div>
    <div class="contenido">
        <h1>Historial de Pagos</h1>
        <a class="boton" href="{{ url_for('agregar_pago') }}">Agregar Pago</a>
        <a class="boton" href="{{ url_for('historial') }}">Volver</a>  <!-- Botón Volver -->
        <table>
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Documento</th>
                    <th>Fecha</th>
                    <th>Estado</th>
                    <th>Método</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                {% for pago in pagos %}
                <tr>
                    <td>{{ pago.nombre }}</td>
                    <td>{{ pago.documento }}</td>
                    <td>{{ pago.fecha }}</td>
                    <td>{{ pago.estado }}</td>
                    <td>{{ pago.metodo }}</td>
                    <td class="acciones">
                        <a href="{{ url_for('editar_estado', id=loop.index0) }}">Editar estado</a> |
                        <a href="{{ url_for('borrar_pago', id=loop.index0) }}" class="borrar">Borrar</a> <!-- Botón Borrar -->
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    <div class="footer">
        <p>&copy; 2025 Taller de mecanizado. Todos los derechos reservados.</p>

    </div>
</body>
</html>
"""

# Formulario para agregar un pago
formulario_template = style_css + """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Agregar Pago</title>
</head>
<body>
    <div class="barra-superior">Sistema de Pagos</div>
    <div class="contenido">
        <h1>Agregar Nuevo Pago</h1>
        <form method="POST">
            <label for="nombre">Nombre:</label>
            <input type="text" name="nombre" required>

            <label for="documento">Documento:</label>
            <input type="text" name="documento" required>

            <label for="fecha">Fecha:</label>
            <input type="date" name="fecha" value="{{ hoy }}" required>

            <label for="estado">Estado:</label>
            <select name="estado" required>
                <option value="Pagado">Pagado</option>
                <option value="Pendiente">Pendiente</option>
                <option value="Fallido">Fallido</option>
            </select>

            <label for="metodo">Método:</label>
            <select name="metodo" required>
                <option value="Tarjeta">Tarjeta</option>
                <option value="Efectivo">Efectivo</option>
                <option value="Transferencia">Transferencia</option>
            </select>

            <button type="submit">Agregar</button>
        </form>
        <br>
        <a class="boton" href="{{ url_for('historial') }}">Volver</a>
    </div>
    <div class="footer">
        <p>&copy; 2025 Taller de mecanizado. Todos los derechos reservados.</p>

    </div>
</body>
</html>
"""

# Formulario para editar estado
editar_template = style_css + """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Editar Estado</title>
</head>
<body>
    <div class="barra-superior">Sistema de Pagos</div>
    <div class="contenido">
        <h1>Editar Estado de Pago</h1>
        <form method="POST">
            <p><strong>Nombre:</strong> {{ pago.nombre }}</p>
            <p><strong>Documento:</strong> {{ pago.documento }}</p>
            <p><strong>Fecha:</strong> {{ pago.fecha }}</p>
            <p><strong>Método:</strong> {{ pago.metodo }}</p>

            <label for="estado">Nuevo Estado:</label>
            <select name="estado" required>
                <option value="Pagado" {% if pago.estado == 'Pagado' %}selected{% endif %}>Pagado</option>
                <option value="Pendiente" {% if pago.estado == 'Pendiente' %}selected{% endif %}>Pendiente</option>
                <option value="Fallido" {% if pago.estado == 'Fallido' %}selected{% endif %}>Fallido</option>
            </select>

            <button type="submit">Actualizar</button>
        </form>
        <br>
        <a class="boton" href="{{ url_for('historial') }}">Volver</a>
    </div>
    <div class="footer">
        <p>&copy; 2025 Taller de mecanizado. Todos los derechos reservados.</p>
       
    </div>
</body>
</html>
"""

# Rutas Flask
@app.route('/')
def historial():
    return render_template_string(historial_template, pagos=historial_pagos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_pago():
    if request.method == 'POST':
        nombre = request.form['nombre']
        documento = request.form['documento']
        fecha = request.form['fecha']
        estado = request.form['estado']
        metodo = request.form['metodo']
        nuevo_pago = {
            "nombre": nombre,
            "documento": documento,
            "fecha": fecha,
            "estado": estado,
            "metodo": metodo
        }
        historial_pagos.append(nuevo_pago)
        return redirect(url_for('historial'))
    hoy = datetime.now().strftime("%Y-%m-%d")
    return render_template_string(formulario_template, hoy=hoy)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_estado(id):
    if id < 0 or id >= len(historial_pagos):
        return "Pago no encontrado", 404

    pago = historial_pagos[id]

    if request.method == 'POST':
        nuevo_estado = request.form['estado']
        pago['estado'] = nuevo_estado
        return redirect(url_for('historial'))

    return render_template_string(editar_template, pago=pago)

@app.route('/borrar/<int:id>', methods=['GET'])
def borrar_pago(id):
    if id < 0 or id >= len(historial_pagos):
        return "Pago no encontrado", 404
    
    historial_pagos.pop(id)  # Elimina el pago de la lista
    return redirect(url_for('historial'))  # Redirige a la página de historial

if __name__ == '__main__':
    app.run(debug=True)