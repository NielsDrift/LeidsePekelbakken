from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_the_map():
    return render_template('the_map.html')

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    