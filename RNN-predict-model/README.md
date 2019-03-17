# RNN-prediction-model

This is a rnn model I build to predict bitcoin price trend for practise. This model will use the previous timestep number of data to predict the following day's price. 

Here is some results img from this model. 

![](https://github.com/shusunny/python-project/RNN-predict-model\Figure_with_3layer_100step.png)
![](https://github.com/shusunny/python-project/RNN-predict-model\Figure_4layer_60step_stdscaler.png)

---

## How to use this model
To use it, you will need the following deps for python.

- [Theano](http://deeplearning.net/software/theano/install.html#install)
- [TensorFlow](https://www.tensorflow.org/install/)
- [keras](https://keras.io/#installation)

And then, fit in your own data. 

There are lots of params to play with, such as number of layers, dropout, optimizer, epochs. Still need time to find the best params. However, Due to high volatility of Bitcoin price, it's really hard to predict the exact price. Please just play it for fun.
