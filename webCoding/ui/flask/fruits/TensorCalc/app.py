from flask import Flask, render_template, request
import numpy as np

#########################


# declare the application

app = Flask(__name__)


##########################


# the app route

@app.route('/')
# declare the main function
def main():
    # return a render of app.html
    return render_template('app.html')


######################################


# the form submission route

@app.route("/send", methods=['POST'])
# define send message
def send():

    if request.method =='POST':
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
        if operation == 'dot':
            sum = np.dot(array1, array2)
            print("shape: \n", sum.shape)
            return render_template('app.html', sum=sum)
        elif operation == "tensor":
            sum = np.kron(array1, array2)
            print("shape: \n ", sum.shape)
            return render_template('app.html', sum=sum)


#######################################################


if __name__ == '__main__':
    app.run(debug=True)