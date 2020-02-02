import tensorflow as tf

######################################
# Gradient Descent
######################################

# the Graph

var = tf.Variable(2,                 # set the variable to 2
                  name='var',        # name the variable 'var'
                  dtype=tf.float32)  # set the datatype to float32


######################################


# the squared log of the node

logVar = tf.log(var)                 # get the nodes log
logVarSquared = tf.square(logVar)    # square the log


####################################


# the initializer

init = tf.initialize_all_variables()


#######################################


# the Session

with tf.Session() as sess:                        # create the session
    sess.run(init)                                # run the initializer
    print("\n\nthe log of x squared is: "
          "\n", logVarSquared.eval(), "\n")       # print the squared log


##################################################


# the gradient descent optimizer
optimizer = tf.train.GradientDescentOptimizer(0.5)  # set the GDO to 0.5
train = optimizer.minimize(logVarSquared)           # run minimize on squared log


# an optimizer method
def optimize():
    with tf.Session() as session:
        session.run(init)
        print("starting at", "var:", "\n",
              session.run(logVar),
              "log(var)^2:", "\n" ,
              session.run(logVarSquared))

        #################################

        # run the Gradient Descent
        for step in range(10):
            session.run(train)
            print("step: ",
                  step,
                  "var: ",
                  session.run(logVar),
                  "log(var)^2: ",
                  session.run(logVarSquared))


optimize()


########################################################
