import tensorflow as tf

x = tf.Variable(2, name='x', dtype=tf.float32)

logx = tf.log(x)
logxsquared = tf.square(logx)

print(logxsquared)

optimizer = tf.train.GradientDescentOptimizer(0.5)

print(optimizer)

init = tf.initialize_all_variables()
train = optimizer.minimize(logxsquared)


def optimize():
    with tf.Session() as session:
        session.run(init)
        print("starting at", "x:", session.run(x), "log(x)^2:", session.run(logxsquared))

        for step in range(10):
            session.run(train)
            print("step", step, "x:", session.run(x), "log(x)^2:", session.run(logxsquared))


optimize()