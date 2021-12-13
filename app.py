from flask import Flask, render_template, request
import kaiseki
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('layout.html')

@app.route('/',methods=["POST"])
def generate():
    ru = request.form['input_russian']
    new_ru = kaiseki.gen_ruword(ru)
    return render_template('res.html',russian=new_ru)

if __name__ == "__main__":
    app.run(debug=True)