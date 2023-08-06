# RADNFIT

to install

```
$ sudo pip install radnfit
```

## Usage

to load the library type from a python shell

```
import radnfit
```

then to execute the fit:

```
Qt, Rt, gamma = radnfit.Fit_Pattern(W,T,M)
```
With Qt the community strength matrix multiplied by lambda, and R the backbone matrix multiplied by (1-lambda), as shown in eq.(13) of the original articale. Gamma is the list of community belief parameter for the nodes of the network. 

The input parameters are W, that is the numpy asymettric adiacence matrix integrated of the considered time-window T, and M is the target matrix, that is a binary matrix of the same shape of Qt, with the zeros in the same position of Qt.


