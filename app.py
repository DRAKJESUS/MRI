from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    image_names = ["imagen_3.png", "imagen_4.png", "imagen_5.png"]
    return render_template('index.html', image_names=image_names)

# Servir imágenes desde la carpeta static/img
@app.route('/static/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/img', filename)

# Servir el archivo CSV
@app.route('/data_mask.csv')
def serve_csv():
    return send_from_directory('.', 'data_mask.csv')

if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
