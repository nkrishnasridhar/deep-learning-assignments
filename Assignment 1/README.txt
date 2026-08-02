# Answer the conceptual questions here
Q1: Is there anything we need to know to get your code to work? If you did not get your code working or handed in an incomplete solution please let us know what you did complete (0-4 sentences)
The code expects the four MNIST .gz files to be in a folder named MNIST_data next to assignment.py (or whatever path is passed in). It needs NumPy and Matplotlib installed. The solution is complete and reaches over 80% test accuracy after one training epoch.

Q2: Why do we normalize our pixel values between 0-1? (1-3 sentences)
Raw MNIST pixels are grayscale values from 0 to 255, so unscaled inputs can make the weighted sums in the forward pass very large. Dividing by 255 maps them into the 0-1 range helping avoid numerical overflow. Keeping features on a similar scale also makes the learning updates more stable.

Q3: Why do we use a bias vector in our forward pass? (1-3 sentences)
The bias acts like the intercept in y = mx + b, so each class perceptron can shift its decision boundary and is not forced through the origin. It can also capture a prior preference for a class, and it lets the model produce a non-zero score even when all input pixels are zero. Without bias, some digit patterns would be much harder to separate correctly.

Q4: Why do we separate the functions for the gradient descent update from the calculation of the gradient in back propagation? (2-4 sentences)
Backpropagation computes how wrong the model is and what gradient update each example suggests, while gradient descent applies those updates to the weights. Gradients are accumulated or averaged over a batch first and only then update the parameters, instead of changing the model after every single example. Separating these steps makes that process clearer, avoids the model “only remembering the last example,” and allows to test or change the update rule without rewriting the gradient calculation.

Q5: What are some qualities of MNIST that make it a “good” dataset for a classification problem? (2-3 sentences)
MNIST is a large labelled supervised dataset with about 70,000 fixed-size 28x28 digit images and 10 clear classes. It has a standard train/test split and has long been used as a vision benchmark, so results are easy to compare. It is also simple enough that a basic model can learn useful patterns from the data, which makes it a good classification problem.

Q6: Suppose you are an administrator of the NZ Health Service (CDHB or similar). What positive and/or negative effects would result from deploying an MNIST-trained neural network to recognize numerical codes on forms that are completed by hand by a patient when arriving for a health service appointment? (2-4 sentences)
A positive effect could be faster automatic reading of handwritten numbers on intake forms, reducing manual data entry. A major negative is domain mismatch beacuse the model was trained on MNIST digits, not real clinic forms, so its accuracy may not transfer and it could fail an external clinical test. Misread codes could affect patient routing or records, creating safety and privacy risks. For healthcare use, in-domain labelled data, careful validation, and human oversight is ideally needed before trusting such a system.
