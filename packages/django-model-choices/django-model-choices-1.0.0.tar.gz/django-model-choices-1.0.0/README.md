# Django Model Choices

Django Model Choices (DMC) provides a readable and DRY way to specify choices for Django models and forms. Although there are many similar projects available, Django Model Choices is willing to offer the most neat and DRY syntax.

## Features

A classic choices class in Django looks like this:

```py
class CharityType(models.Model):
    SOCIAL = 'SOC'
    ENVIRONMENTAL = 'ENV'
    EDUCATIONAL = 'EDU'
    CHOICES = (
        (SOCIAL, 'Social'),
        (ENVIRONMENTAL, 'Environmental'),
        (EDUCATIONAL, 'Educational'),
    )
```

This is far from being DRY and is also prone to typos and other mistakes. Using Django Model Choices you could do:

```py
from modelchoices import Choices


class CharityType(Choices):
    SOCIAL = ('SOC', 'Social')
    ENVIRONMENTAL = ('ENV', 'Environmental')
    EDUCATIONAL = ('EDU', 'Educational')
```

The value of each choice must be a tuple containing a value for the database and a user readable value, which could also be translation object as in this example.

The `CHOICES` field will be generated magically by the metaclass, so you can use it in the model like this:

```py
class Charity(models.Model):
    charity_type = models.CharField(max_length=1, choices=CharityType.CHOICES)
```

The variables `SOCIAL`, `ENVIRONMENTAL` and `EDUCATIONAL` can be used to programmatically represent the choice values. Once the class is created, their values are no longer a tuples, but only the database fields (so `CharityType.ENVIRONMENTAL` is equal to `'ENV'`). So you can do:

```py
charity = Charity()
charity.charity_type = CharityType.ENVIRONMENTAL
charity.save()
```

Another field generated magically is `VALUE_MAPPER`. It is a dictionary, where the keys represent the database values and the dictionary values represent the variable name used to declare the options. In our example `VALUE_MAPPER` look like this:

```py
>>> CharityType.VALUE_MAPPER
{
    'SOC': 'SOCIAL',
    'ENV': 'ENVIRONMENTAL',
    'EDU': 'EDUCATIONAL'

}
```

This is useful if you need to use the variable names a codes (for a REST API for instance), because the user readable values might be subjects of translation.
