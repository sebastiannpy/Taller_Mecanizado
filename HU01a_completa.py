from flask import Flask, render_template_string, request

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def home():
    mensaje = ""
    if request.method == "POST":
        usuario_correcto = "123456789"
        contrasena_correcta = "admin123"

        usuario = request.form.get("documento")
        contrasena = request.form.get("contrasena")

        if usuario != usuario_correcto or contrasena != contrasena_correcta:
         mensaje = "Usuario o contraseña incorrectos"
        else:
         mensaje = ""


    return render_template_string(HTML, mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)


    #Solo usaremos el framework flask porque es mas accesible y facil de usar para nuestro caso. 
    #Linea 19 controla el color y etc.. del encabezado 
    #Linea 39 controla el color y etc.. del fondo la parte del medio
    #Linea 46 controla el color y etc.. del texto adentro de la parte del medio
    #Linea 70 controla el color y etc.. del boton de "iniciar sesion"
    #Linea 99 controla el color del mensaje de "error"
    #Linea 102 controla el color y etc.. de la parte de abajo 
    #Linea  149 y 150 controlan el usuario y la contraseña que se digita 
    
    

