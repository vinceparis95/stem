from flask import Flask, render_template, request


#####################


app = Flask(__name__)


############################################


# App routes for SciCode path


@app.route('/la')
def la():
    return render_template('sciCode/la.html')


@app.route('/ml')
def mL():
    return render_template('sciCode/ml.html')


@app.route("/qi")
# test channel
def qi():
    return render_template('sciCode/qi.html')


#############################################



if __name__ == "__main__":

    app.run(debug=True)


###########################


import numpy as np
from sciCode.qi.qubit.qubity import isUnitary
from sciCode.qi.qubit.qubity import isEigen

# define the app

# @app.route("/", methods=['POST'])
# # define send message
# def calc():
#
#     if request.method == 'POST':
#         num1 = request.form['num1']
#         # separate and convert numbers to floats
#         num1 = [float(i) for i in num1.split()]
#         array1 = np.array([num1])
#         array1 = array1.reshape(2, 2)
#         operation = request.form['operation']
#         if operation == 'unitarity':
#             unitary = isUnitary(array1)
#             print(unitary)
#             return render_template('ml.html', sum=unitary)
#         elif operation == 'eigenvalue':
#             eigen = isEigen(array1)
#             print(eigen)
#             return render_template('ml.html', sum=eigen)
#