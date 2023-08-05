"""Collection of convenience functions for statistical work.
"""

# pylint: disable=E1101, C0103

from copy import copy
import math
import pickle

from numba import njit
import numpy
import pandas
import patsy
from scipy.stats import norm
from statsmodels.regression.linear_model import WLS
numpy.warnings.filterwarnings("ignore")
from statsmodels.api import GLM
numpy.warnings.resetwarnings()
from statsmodels.genmod.families import Binomial
from statsmodels.formula.api import mnlogit
from statsmodels.genmod.families.links import logit


@njit
def logit_transform(X, betas):
    """Performs a logistic transformation on data.

    Arguments:
        X {numpy.array} -- nxm numpy array.
        betas {numpy.array} -- mx1 numpy array with coefficients.

    Returns:
        numpy.array -- nx1 numpy array with logistic transformation applied.
    """

    return 1 / (1 + numpy.exp(-1 * X @ betas))


@njit
def linear_transform(X, betas):
    """Performs a linear transformation on data.

    Arguments:
        X {numpy.array} -- nxm numpy array.
        betas {numpy.array} -- mx1 numpy array with coefficients.

    Returns:
        numpy.array -- nx1 numpy array with linear transformation applied.
    """

    return X @ betas


def inverse_mills_ratio(x, mu=0, sigma=1, invert=False):
    """Computes the inverse mills ratio of some data.

    Arguments:
        x {numpy.array} -- nx1 numpy array of data.

    Keyword Arguments:
        mu {int} -- The mean of the normal distribution. (default: {0})
        sigma {int} -- The standard deviation of the normal distribution. (default: {1})
        invert {bool} -- Which of two sides to compute, defaults to <=. (default: {False})

    Returns:
        numpy.array -- nx1 numpy array of transformed data
    """

    if not invert:
        return norm.pdf((x - mu) / sigma) / (1 - norm.cdf((x - mu) / sigma))
    else:
        return -1 * norm.pdf((x - mu) / sigma) / (norm.cdf((x - mu) / sigma))


def weighted_quantile(values,
                      quantiles,
                      sample_weight=None,
                      values_sorted=False,
                      old_style=False):
    """ Very close to numpy.percentile, but supports weights.
    Source: https://stackoverflow.com/questions/21844024/weighted-percentile-using-numpy
    NOTE: quantiles should be in [0, 1]!
    :param values: numpy.array with data
    :param quantiles: array-like with many quantiles needed
    :param sample_weight: array-like of the same length as `array`
    :param values_sorted: bool, if True, then will avoid sorting of initial array
    :param old_style: if True, will correct output to be consistent with numpy.percentile.
    :return: numpy.array with computed quantiles.
    """
    values = numpy.array(values)
    quantiles = numpy.array(quantiles)
    if sample_weight is None:
        sample_weight = numpy.ones(len(values))
    sample_weight = numpy.array(sample_weight)
    assert numpy.all(quantiles >= 0) and numpy.all(
        quantiles <= 1), 'quantiles should be in [0, 1]'

    if not values_sorted:
        sorter = numpy.argsort(values)
        values = values[sorter]
        sample_weight = sample_weight[sorter]

    weighted_quantiles = numpy.cumsum(sample_weight) - 0.5 * sample_weight
    if old_style:
        # To be convenient with numpy.percentile
        weighted_quantiles -= weighted_quantiles[0]
        weighted_quantiles /= weighted_quantiles[-1]
    else:
        weighted_quantiles /= numpy.sum(sample_weight)
    return numpy.interp(quantiles, weighted_quantiles, values)


def weighted_std(values, weights):
    """Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.

    https://stackoverflow.com/questions/2413522/weighted-standard-deviation-in-numpy
    """
    average = numpy.average(values, weights=weights)
    # Fast and numerically precise:
    variance = numpy.average((values - average)**2, weights=weights)
    return math.sqrt(variance)


class LogitRegression(object):
    """Patsy wrapper for logit model estimation and prediction.

    Example usage:

    # construct and estimate model using patsy formula
    # uses the cps pickle file under dataset processor
    cps["EarnedWage"] = (cps.WageIncomeLastYear > 0).astype(int)
    model = LogitRegression(
        "EarnedWage ~ C(Race)",
        cps,
        freq_weights=cps.Weight
    )

    # print model summary
    print(model)

    # return predicted probability of working for blacks
    prob_works = model.predict(
        pandas.DataFrame({
            "Race": ["Black"]
        })
    )
    """

    def __init__(self, formula=None, data=None, link=logit, **kwargs):

        if formula:
            y, X = patsy.dmatrices(formula, data, 1)
            self._y_design_info = y.design_info
            self._X_design_info = X.design_info
            self._model = GLM(y, X, family=Binomial(link), **kwargs)
            self._fit = self._model.fit()
            self._betas = self._fit.params
            self._link = link
        else:
            self._y_design_info = None
            self._X_design_info = None
            self._model = None
            self._fit = None
            self._betas = None
            self._link = link

    def __repr__(self):
        return str(self._fit.summary()) if self._fit                           \
            else "Logistic regression"

    def predict(self, data, linear=False):

        if len(data) == 0:
            return []

        (X, ) = patsy.build_design_matrices([self._X_design_info], data)

        if not linear:
            return self._link.inverse(self._link(),
                                      linear_transform(
                                          numpy.asarray(X), self._betas))

        else:
            return linear_transform(numpy.asarray(X), self._betas)

    def draw(self, data, rand_engine):

        prediction = self.predict(data)

        return rand_engine.binomial(1, prediction)

    def to_pickle(self, filename):

        pickle.dump((self._y_design_info, self._X_design_info, self._betas,
                     self._link), open(filename, "wb"))

    @staticmethod
    def read_pickle(filename):
        y_design_info, X_design_info, betas, link = pickle.load(
            open(filename, "rb"))

        logit_regression = LogitRegression()
        logit_regression._y_design_info = y_design_info
        logit_regression._X_design_info = X_design_info
        logit_regression._betas = betas
        logit_regression._link = link

        return logit_regression

    def __add__(self, other):
        ret = copy(self)
        ret._betas = self._betas + other._betas
        return ret

    def __sub__(self, other):
        ret = copy(self)
        ret._betas = self._betas - other._betas
        return ret

    def __mul__(self, other):
        ret = copy(self)
        ret._betas = ret._betas * other
        return ret


class MultinomialRegression(object):
    """Patsy wrapper for logit model estimation and prediction.

    Example usage:

    # construct and estimate model using patsy formula
    # uses the cps pickle file under dataset processor
    cps["EarnedWage"] = (cps.WageIncomeLastYear > 0).astype(int)
    model = LogitRegression(
        "EarnedWage ~ C(Race)",
        cps,
        freq_weights=cps.Weight
    )

    # print model summary
    print(model)

    # return predicted probability of working for blacks
    prob_works = model.predict(
        pandas.DataFrame({
            "Race": ["Black"]
        })
    )
    """

    def __init__(self, formula=None, data=None, weights=None, **kwargs):

        if formula:
            y, X = patsy.dmatrices(formula, data, 1)
            self._y_design_info = y.design_info
            self._X_design_info = X.design_info
            self._model = mnlogit(formula, data, **kwargs)
            self._fit = self._model.fit(maxiter=10000)
            self._betas = self._fit.params
        else:
            self._y_design_info = None
            self._X_design_info = None
            self._model = None
            self._fit = None
            self._betas = None

    def __repr__(self):
        return str(self._fit.summary()) if self._fit                           \
            else "Multinomial regression"

    def predict(self, data, linear=False):

        if len(data) == 0:
            return []

        (X, ) = patsy.build_design_matrices([self._X_design_info], data)

        linear_transforms = numpy.asarray(X) @ self._betas

        linear_transforms = numpy.concatenate(
            [numpy.zeros((len(data), 1)), linear_transforms], axis=1)

        linear_transforms = numpy.exp(linear_transforms)

        columns = self._y_design_info.column_names
        is_true = ["True]" in i for i in columns]
        columns = [c for c in columns if "True]" in c]


        return pandas.DataFrame(
            linear_transforms[:,is_true] / numpy.sum(
                linear_transforms, axis=1, keepdims=True),
            columns=columns)

    def draw(self, data, rand_engine):

        prediction = self.predict(data).values.cumsum(axis=1)
        prediction = numpy.append(prediction, numpy.ones((prediction.shape[0], 1)), axis=1)
        random = rand_engine.uniform(size=(len(data), 1))
        return numpy.argmax(prediction > random, axis=1)

    def to_pickle(self, filename):

        pickle.dump((self._y_design_info, self._X_design_info, self._betas),
                    open(filename, "wb"))

    @staticmethod
    def read_pickle(filename):
        y_design_info, X_design_info, betas = pickle.load(open(filename, "rb"))

        multinomial_regression = MultinomialRegression()
        multinomial_regression._y_design_info = y_design_info
        multinomial_regression._X_design_info = X_design_info
        multinomial_regression._betas = betas

        return multinomial_regression

    def __add__(self, other):
        ret = copy(self)
        ret._betas = self._betas + other._betas
        return ret

    def __sub__(self, other):
        ret = copy(self)
        ret._betas = self._betas - other._betas
        return ret

    def __mul__(self, other):
        ret = copy(self)
        ret._betas = ret._betas * other
        return ret


class LinearRegression(object):
    """Patsy wrapper for linear estimation and prediction.
    """

    def __init__(self, formula=None, data=None, **kwargs):

        if formula:
            y, X = patsy.dmatrices(formula, data, 1)

            self._y_design_info = y.design_info
            self._X_design_info = X.design_info

            self._model = WLS(y, X, **kwargs)
            self._fit = self._model.fit()
            self._betas = self._fit.params
            self._std = numpy.std(data[self._model.data.ynames].values - self.predict(data))
        else:
            self._y_design_info = None
            self._X_design_info = None
            self._model = None
            self._fit = None
            self._betas = None
            self._std = None

    def __repr__(self):
        return str(self._fit.summary())

    def predict(self, data):

        if len(data) == 0:
            return []

        (X, ) = patsy.build_design_matrices([self._X_design_info], data)

        return linear_transform(numpy.asarray(X), self._betas)

    def draw(self, data, rand_engine):

        return self.predict(data) + rand_engine.normal(0, self._std, len(data))

    def to_pickle(self, filename):

        pickle.dump((self._y_design_info, self._X_design_info, self._betas, self._std),
                    open(filename, "wb"))

    @staticmethod
    def read_pickle(filename):
        y_design_info, X_design_info, betas, std = pickle.load(open(filename, "rb"))

        linear_regression = LinearRegression()
        linear_regression._y_design_info = y_design_info
        linear_regression._X_design_info = X_design_info
        linear_regression._betas = betas
        linear_regression._std = std

        return linear_regression

    def __add__(self, other):
        ret = copy(self)
        ret._betas = self._betas + other._betas
        return ret

    def __sub__(self, other):
        ret = copy(self)
        ret._betas = self._betas - other._betas
        return ret

    def __mul__(self, other):
        ret = copy(self)
        ret._betas = ret._betas * other
        return ret
