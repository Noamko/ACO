# Ant Colony Optimization

### Prerequisites:

#### Python >= 3.7 installed

#### required modules:

1.  NumPy
2.  PyPlot matplotlib

- to install:

```
pip3 install numpy
pip3 install matplotlib
```

---

## Running the tests:

Running test 1: In test 1 we compare an ACO variant with SM

Examples:

### Run test 1 with ACS variant

```
Python3 main.py test1 acs
```

### With Elitist:

```
Python3 main.py test1 elitist
```

### With Minmax:

```
Python3 main.py test1 minmax
```

Running test 2:

In test 2 we compare how adding ants effects the overall result

Again we can provide any function we want:

```
Python3 main.py test2 acs

Python3 main.py test2 elitist

Python3 main.py test2 minmax
```
