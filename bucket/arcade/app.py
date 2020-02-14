from flask import Flask, render_template, request
import numpy as np
from sciCode.qi.qubit.qubity import isUnitary
from sciCode.qi.qubit.qubity import isEigen
app = Flask(__name__)

#######################################
@app.route("/")
def home():
    return render_template('portal.html')



###################################################


@app.route("/qi")
# test channel
def qi():
    return render_template('qi.html')

###################################################


@app.route('/ml')
def mL():
    return render_template('ml.html')

######################################

if __name__ == "__main__":
    app.run(debug=True)



######################################################


# define the uiux

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