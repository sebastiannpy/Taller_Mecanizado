from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

pedidos = [
    {'id': 1, 'cliente': 'Ana Torres', 'documento': 'DOC001', 'fecha': '2025-05-10', 'estado': 'Pendiente'},
    {'id': 2, 'cliente': 'Luis Díaz', 'documento': 'DOC002', 'fecha': '2025-05-11', 'estado': 'Pendiente'},
    {'id': 3, 'cliente': 'María Gómez', 'documento': 'DOC003', 'fecha': '2025-05-12', 'estado': 'Pendiente'},
]

html_buscar = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Buscar Pedido</title>
    <style>
        body {
            background: #f3ecff;
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            color: #333;
        }

        header {
            background: linear-gradient(135deg, #5a00b3, #a54cf2);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .container {
            padding: 40px 20px;
            text-align: center;
        }

        input[type="text"], button {
            padding: 12px 20px;
            margin: 10px;
            border-radius: 10px;
            border: none;
            font-size: 16px;
        }

        input[type="text"] {
            width: 300px;
            background: #fdfbff;
            border: 1px solid #ccc;
        }

        button {
            background-color: #8e24aa;
            color: white;
            cursor: pointer;
            transition: background 0.3s;
        }

        button:hover {
            background-color: #6a1b9a;
        }

        .resultado {
            margin-top: 30px;
            background: white;
            padding: 20px;
            display: inline-block;
            border-radius: 15px;
            box-shadow: 0 0 10px rgba(138, 43, 226, 0.2);
        }

        .cancelar {
            background-color: #e53935;
            margin-top: 15px;
        }

        .volver {
            background-color: #512da8;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<header>
    <h1>Buscar Cliente o Pedido</h1>
</header>

<div class="container">
    <form method="POST">
        <input type="text" name="query" placeholder="Nombre del cliente o número de pedido" required>
        <button type="submit">Buscar</button>
    </form>

    {% if pedido %}
        <div class="resultado">
            <p><strong>Cliente:</strong> {{ pedido.cliente }}</p>
            <p><strong>Documento:</strong> {{ pedido.documento }}</p>
            <p><strong>Fecha:</strong> {{ pedido.fecha }}</p>
            <p><strong>Estado:</strong> {{ pedido.estado }}</p>
            {% if pedido.estado != 'Cancelado' %}
            <form method="POST" action="{{ url_for('cancelar_pedido') }}">
                <input type="hidden" name="pedido_id" value="{{ pedido.id }}">
                <button type="submit" class="cancelar">Cancelar Pedido</button>
            </form>
            {% endif %}
        </div>
    {% elif pedido is not none %}
        <p>No se encontró ningún pedido.</p>
    {% endif %}

    <form action="/" method="get">
        <button class="volver">Volver al Inicio</button>
    </form>
</div>

</body>
</html>
"""

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    pedido = None
    if request.method == 'POST':
        query = request.form['query'].lower()
        for p in pedidos:
            if query in p['cliente'].lower() or query == str(p['id']):
                pedido = p
                break
    return render_template_string(html_buscar, pedido=pedido)

@app.route('/cancelar_pedido', methods=['POST'])
def cancelar_pedido():
    id_cancelar = int(request.form['pedido_id'])
    for p in pedidos:
        if p['id'] == id_cancelar:
            p['estado'] = 'Cancelado'
            break
    return redirect(url_for('buscar'))

@app.route('/')
def inicio():
    return '<h2 style="text-align:center; padding: 40px;">Página Principal - <a href="/buscar">Buscar Pedido</a></h2>'

if __name__ == '__main__':
    app.run(debug=True)