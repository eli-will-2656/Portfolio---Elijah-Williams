
# Part 1
* Loss is the error function (a measure of error from desired output)


# Part 2
- Takes a long time to train convolutional network (5 +- 2 minutes)


# Background

*Inferior Temporal cortex*
The inferior temporal cortex (IT) region of brain is thought represent high-order representations of objects in vision.

Recording electrical activity with electrodes is like fishing
* Some leeds splitting off an electrode are next to a neuron
* Some of those neurons are responsive to stimulus


*PCA*
Gabor Filtering - Breaking a picture down into orientations (end up with looking for patterns)
This replicates the visual system in which 40x number of neurons in V1 than in retina cells

*Visual System*

Something that realizes the autoassociator function is visual system
* input neurons project to lower-dimensional representation
* hidden layer proejct to higher-dimensional representation
* higher-dimensional representation projects back to input neurons (as an inhibitor)

ex. Dreaming - you can have activity propogate top-down from concept of vision to 
* Hallucinating networks (CMU)

*PCA* = Principal Component Analysis
* Nonlinear generalizaiton of PCA

*AlexNet*
* One of the first image classifiers


# Tensorflow
* one-hot: instead of just having model produce a 7, have model produce [0 0 0 0 0 0 1 0 0] (7 represented by activation at 7th index)
* The reason why the shape of a one-dimensional array is `(1,)` (why is there an ending comma), is so that the 1 is interpreted as a
tuple, not an integer. a.k.a `(1) == 1`
* When fitting a network, we are always fitting it to a dataset, trying to get the model to associatiate an input `x` with an output `y`. The syntax for fitting a model is `model.fit(x, y, batch_size, verbose, epochs, validation_split)


*Questions*
* What is the difference between PCA and ICA?
* What is max-pooling?
