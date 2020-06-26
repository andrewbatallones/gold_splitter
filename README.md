# Gold Splitter Package

Simple package that divides out the gold per player.

## Installation

```bash
$ pip install gold_splitter
```

## Use

```python
from gold_splitter import split

# This will return a dictionary of how much gold people get.
split(5, gold=3, silver=4, copper=5)
# Will output: {'Per Person': {'Gold': Decimal('0'), 'Silver': Decimal('6'), 'Copper': Decimal('9')}, 'Left over money': {'Gold': Decimal('0'), 'Silver': Decimal('0'), 'Copper': Decimal('0')}}
```

## Testing
To test the package, run the following

```bash
$ pip install -e .[dev]
```

Other notes
look into check-manifest package