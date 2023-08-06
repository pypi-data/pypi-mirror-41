# Dict extension - get_fuzzy
Get element by fuzzy key from dict.

## Introduction

The library is extension for buildin type `dict`. After import you can use `get_fuzzy` and `get_fuzzy_stats` like `get` method.

## Installing
This library can be install from pip:


```bash
pip install dict-extend-fuzzy
```

## Usage
Simple example
```python
from dictextendfuzzy import get_fuzzy

data = {
	'aaaa' : 1,
	'bbbb' : 2
}

data.get_fuzzy('aaab')  # 1

```

Get some more information

```python
from dictextendfuzzy import get_fuzzy_stats

data = {
	'aaaa' : 1,
	'bbbb' : 2
}

obj = data.get_fuzzy_stats('aaab')
obj.key     # 'aaaa'
obj.value   # 1
obj.ratio   # 0.75


```

With optional parameters
```python 
data.get_fuzzy('kei', 'default_object', level=0.5)
data.get_fuzzy_stats('kay', {}, level=0.25)
```