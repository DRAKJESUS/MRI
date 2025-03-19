from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    image_names = ["imagen_1.png", "imagen_2.png", "imagen_3.png", "imagen_4.png", "imagen_5.png"]
    return render_template('index.html', image_names=image_names)

# Ruta para servir imágenes desde la carpeta static
@app.route('/static/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/img', filename)

if __name__ == '__main__':
    app.run(debug=True)
