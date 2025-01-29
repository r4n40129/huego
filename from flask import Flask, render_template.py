from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>¿Quieres cerrar?</title>
    <style>
        body { text-align: center; font-family: Arial, sans-serif; }
        .btn { padding: 10px 20px; font-size: 18px; cursor: pointer; margin: 10px; }
        .no-btn { position: absolute; transition: 0.3s; }
    </style>
    <script>
        function moveButton() {
            let btn = document.getElementById("no");
            let x = Math.random() * (window.innerWidth - 100);
            let y = Math.random() * (window.innerHeight - 50);
            btn.style.left = x + "px";
            btn.style.top = y + "px";
        }
    </script>
</head>
<body>
    <h2>¿Quieres cerrar la página?</h2>
    <button class="btn" onclick="window.close()">Sí</button>
    <button class="btn no-btn" id="no" onmouseover="moveButton()">No</button>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
