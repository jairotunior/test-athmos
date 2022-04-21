# Test

This is the solution to the proposal test.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

1. Create a new virtual environment with your prefered tools
2. Copy the repositiory https://github.com/jairotunior/test-athmos.git
3. Install the dependencies

```
pip install -r requerimientos.txt
```

That's all for use.

### Exercise 1

You need to start the InfluxDB in Docker with the next script.

```
bash run_influxdb.sh
```

To achieve the purpose the problem is divided in two scripts. The exercise1_ws.py does a connection with the websocket and store the data in InfluxDB while exercise1_process
every minutes preprocess the information.

```
bash run_exercise1_ws.sh
```

Open another terminal

```
bash run_exercise1_process.sh
```


### Exercise 2

You could use the CLI with the requirements request with the next command.

```
python exercise2.py -h
```

If you want to test the CLI you should run the next script:

```
bash run_test.py -h
```


## Built With

* [Gym](https://gym.openai.com/) - Toolkit for developing and comparing reinforcement learning algorithms.
* [Numpy](http://www.numpy.org/) - Is the fundamental package for scientific computing with Python.
* [Python](https://www.python.org/) - Programming Language.
* [Docker](https://www.docker.com) - Container system.
* [InfluxDB](https://www.influxdata.com) - Time Series Database.

