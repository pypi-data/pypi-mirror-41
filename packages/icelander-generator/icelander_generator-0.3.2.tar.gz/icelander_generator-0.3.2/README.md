# Icelander generator
Icelander generator is a tool made to generate a bunch of icelanders.

## Details
Icelander generator uses a list of male and female names scraped from is.wikipedia.org and
the kennitala pypi package (https://pypi.org/project/kennitala/) to generate random people
with proper icelandic names and kennitala. It can be very useful for testing purposes where
a bunch of icelanders are required. Can also just be used for fun, I guess.

## Installation
Inside your virtualenv run
```
$ pip install icelander-generator
```

## Usage
### Icelander
```python
from icelander_generator import Icelander

icelander = Icelander()

# Generate a random person
icelander.get_random_person()
# Returns {
#   'ssn': '{random ssn}',
#   'gender': '{randomly selected gender},
#   'firstname': '{randomly selected first name based on gender}',
#   'lastname': '{randomly selected last name based on gender}',
# }

# Generate a woman born in 1981
icelander.get_random_person(gender='female', year=1981)
# Returns {
#   'ssn': '{random ssn from year 1981}',
#   'gender': 'female',
#   'firstname': '{randomly selected first name based on gender}',
#   'lastname': '{randomly selected last name based on gender}',
# }

# Return a list of randomly generated people of random age and gender
icelander.get_random_people(10)

# Return a list of randomly generated women born in 1981
icelander.get_random_people(10, gender='female', year=1981)

# Dump result from get_random_people to a json file
icelander.dump_random_people_to_file(filename='dump.json', num_people=10, gender='female', year='1981')
```

### Address
```python
from icelander_generator.address import Address

ad = Address()

# Get random address
ad.get_random_address()

# Get random address in Reykjavík
ad.get_random_address(place='Reykjavík')

# Get random address in 101 PO code
ad.get_random_address(po_code='101')

# Get random address, but only up to street number 23
ad.get_random_address(max_num=23)

```


## Future ideas
- More gender options?
- Middle names
- Company generator

I'm also open for suggestions and pull requests on https://github.com/7oi/IcelanderGenerator
