def perceptron_input(inputs, weights):
    weighed_sum = sum(i * w for i, w in zip(inputs, weights))
    return weighed_sum

def perceptron_output(inputs, weights, thold):
    bias = thold * -1
    return bias + perceptron_input(inputs, weights)

inputs = [1, 1, 2]
weights = [1, 1, 2]
thold = 1.5

print(perceptron_output(inputs, weights, thold))