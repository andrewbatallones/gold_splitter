from gold_splitter import split
from decimal import Decimal


def test_with_just_party_size():
    assert split(5) == {'Per Person': {'Gold': Decimal('0'), 'Silver': Decimal('0'), 'Copper': Decimal(
        '0')}, 'Left over money': {'Gold': Decimal('0'), 'Silver': Decimal('0'), 'Copper': Decimal('0')}}

