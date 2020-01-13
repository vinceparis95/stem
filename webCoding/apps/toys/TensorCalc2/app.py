from flask import Flask, render_template, request
import numpy as np
import matrixMath.quantumComputing.bits.matrices.unitaries

app = Flask(__name__)

#######################################


# define the application
@app.route("/")
def home():
    return render_template("home.html")

########################################

@app.route("/send", methods=['POST'])
# define send message
def send():

    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        # separate and convert numbers to floats
        num1 = [float(i) for i in num1.split()]
        num2 = [float(i) for i in num2.split()]
        array1 = np.array([num1])
        print("array 1 (row, or bra) = \n", array1, "\n")
        array2 = np.array([num2])
        # transpose second array
        array2 = array2.transpose()
        print("array 2 (column, or ket) = \n", array2, "\n")
        operation = request.form['operation']
        if operation == 'unitarity':



######################################
if __name__ == "__main__":
    app.run(debug=True)
