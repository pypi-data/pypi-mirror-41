import pytest
import numpy as np

from utils import *

import qcelemental


@pytest.mark.parametrize("inp,expected", [
    (['AAAABBBCCDAABBB'], 'ABCD'),
    (['ABBCcAD', str.lower], 'ABCD'),
])
def test_unique_everseen(inp, expected):
    ue = qcelemental.util.unique_everseen(*inp)
    assert list(ue) == list(expected)

@pytest.mark.parametrize("inp,expected", [

(({1:{"a":"A"},2:{"b":"B"}}, {2:{"c":"C"},3:{"d":"D"}}), {1:{"a":"A"},2:{"b":"B","c":"C"},3:{"d":"D"}}),
(({1:{"a":"A"},2:{"b":"B","c":None}}, {2:{"c":"C"},3:{"d":"D"}}), {1:{"a":"A"},2:{"b":"B","c":"C"},3:{"d":"D"}}),
(({1: [None, 1]}, {1: [2, 1],3:{"d":"D"}}), {1:[2, 1], 3:{"d":"D"}})
])
def test_updatewitherror(inp, expected):
    print('ans', qcelemental.util.update_with_error(inp[0], inp[1]))
    print('exp', expected)
    assert compare_dicts(expected, qcelemental.util.update_with_error(inp[0], inp[1]), 4, tnm())

@pytest.mark.parametrize("inp", [
({1:{"a":"A"},2:{"b":"B"}}, {1:{"a":"A"},2:{"b":"C"}}),
({1:{"a":"A"},2:{"b":"B"}}, {1:{"a":"A"},2:{"b":None}}),
({1: [None, 1]}, {1: [2, 2],3:{"d":"D"}}),
])
def test_updatewitherror_error(inp):
    with pytest.raises(KeyError):
        qcelemental.util.update_with_error(inp[0], inp[1])

@pytest.mark.parametrize("inp,expected", [
    ({'dicary': {"a":"A", "b":"B"}}, {"a":"A", "b":"B"}),
    ({'dicary': {"a":np.arange(2), "b":[1, 2]}}, {"a":[0, 1], "b":[1, 2]}),
    ({'dicary': {"c":{"a":np.arange(2), "b":[1, 2]}}}, {"c":{"a":[0, 1], "b":[1, 2]}}),
    ({'dicary': {"c":{"a":np.arange(2), "b":[1, 2]}}, 'flat': True}, {"c":{"a":[0, 1], "b":[1, 2]}}),
    ({'dicary': {"c":{"a":np.arange(2), "b":[1, 2]}, "d":np.arange(6).reshape((2, 3))}}, {"c":{"a":[0, 1], "b":[1, 2]}, "d":[[0, 1, 2], [3, 4, 5]]}),
    ({'dicary': {"c":{"a":np.arange(2), "b":[1, 2]}, "d":np.arange(6).reshape((2, 3))}, 'flat': True}, {"c":{"a":[0, 1], "b":[1, 2]}, "d":[0, 1, 2, 3, 4, 5]}),
    ({'dicary': {"a": np.arange(2), "e": ["mouse", np.arange(4).reshape(2, 2)]}}, {"a": [0, 1], "e": ["mouse", [[0, 1], [2, 3]]]}),
    ({'dicary': {"a": np.arange(2), "e": ["mouse", {"f": np.arange(4).reshape(2, 2)}]}}, {"a": [0, 1], "e": ["mouse", {"f": [[0, 1], [2, 3]]}]}),
    ({'dicary': {"a": np.arange(2), "e": ["mouse", [np.arange(4).reshape(2, 2), {"f": np.arange(6).reshape(2, 3), "g": [[11], [12]]}]]}}, {"a": [0, 1], "e": ["mouse", [[[0, 1], [2, 3]], {"f": [[0, 1, 2], [3, 4, 5]], "g": [[11], [12]]}]]}),
    ({'dicary': {"a": np.arange(2), "e": ["mouse", np.arange(4).reshape(2, 2)]}, 'flat': True}, {"a": [0, 1], "e": ["mouse", [0, 1, 2, 3]]}),
    ({'dicary': {"a": np.arange(2), "e": ["mouse", {"f": np.arange(4).reshape(2, 2)}]}, 'flat': True}, {"a": [0, 1], "e": ["mouse", {"f": [0, 1, 2, 3]}]}),
    ({'dicary': {"a": np.arange(2), "e": ["mouse", [np.arange(4).reshape(2, 2), {"f": np.arange(6).reshape(2, 3), "g": [[11], [12]]}]]}, 'flat': True}, {"a": [0, 1], "e": ["mouse", [[0, 1, 2, 3], {"f": [0, 1, 2, 3, 4, 5], "g": [[11], [12]]}]]}),
])
def test_unnp(inp, expected):
    assert compare_dicts(expected, qcelemental.util.unnp(**inp), 4, tnm())
