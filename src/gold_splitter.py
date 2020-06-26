from decimal import Decimal


def split(party_size, platinum=Decimal(0), gold=Decimal(0), silver=Decimal(0), copper=Decimal(0)):
	copper = (platinum * 1000) + (gold * 100) + (silver * 10) + copper
	each_copper = copper // party_size
	left_over_copper = copper % party_size

	return {"Per Person": convert_to_currency(each_copper), "Left over money": convert_to_currency(left_over_copper)}

def convert_to_currency(copper):
	return {
		"Gold": copper // 100,
		"Silver": (copper % 100) // 10,
		"Copper": copper % 10
	}
