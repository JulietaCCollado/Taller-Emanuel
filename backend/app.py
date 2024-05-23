from flask import Flask, send_file

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def index():
    # Specify the path to your HTML file
    html_file_path = 'C:\\Users\\julie\\OneDrive\\Escritorio\\Pagina papá\\template\\index.html'
    # Send the HTML file as a response
    return send_file(html_file_path)

if __name__ == '__main__':
    app.run(debug=True)
