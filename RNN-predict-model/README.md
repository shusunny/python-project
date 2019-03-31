# RNN-prediction-model

This is a rnn model I build to predict bitcoin price trend for practise. This model will use the previous days of data (day's number depends on the timestep entered)to predict the following day's price. 

Here are some results images generated with this model. 

Figure for 3 LSTM layers and 100 timestep with minmax scaler 
![](https://raw.githubusercontent.com/shusunny/python-project/master/RNN-predict-model/Figure_with_3layer_100step.png)


Figure for 4 LSTM layers and 60 timestep with standard scaler
![](https://raw.githubusercontent.com/shusunny/python-project/master/RNN-predict-model/Figure_4layer_60step_stdscaler.png)

---

## How to use this model
To use it, you will need the following deps for python.

- [Theano](http://deeplearning.net/software/theano/install.html#install)
- [TensorFlow](https://www.tensorflow.org/install/)
- [keras](https://keras.io/#installation)

And then, fit in your own data. 

There are lots of params to play with, such as number of layers, dropout, optimizer, epochs. Still need time to find the best params. However, Due to high volatility of Bitcoin price, it's really hard to predict the exact price. Please just play it for fun.
