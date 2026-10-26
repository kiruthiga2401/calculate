from flask import Flask

app = Flask(__name__)

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Cannot divide by zero"

@app.route('/')
def home():
    return f"""
    <h1>Simple Calculator App</h1>
    <p>Addition (5 + 3): {add(5, 3)}</p>
    <p>Subtraction (5 - 3): {sub(5, 3)}</p>
    <p>Multiplication (5 * 3): {mul(5, 3)}</p>
    <p>Division (6 / 2): {div(6, 2)}</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
