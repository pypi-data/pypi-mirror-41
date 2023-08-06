# Factory-Man

Factory-Man provides extensions for [Factory Boy](https://factoryboy.readthedocs.io/en/latest/introduction.html).

## Features

`ModelFieldSequence` extends `factory.Sequence` to provide a little more DRY syntax. It takes in a `string` parameter and uses it to create a unique value for each object by adding `-n` to the string, where `n` is the count of objects created.

When working with Django, `ModelFieldSequence` can also accept a `model` parameter instead of `string`. The `model` should be a Django model. The name of the model and the field to which `ModelFieldSequence` is signed to are used to automatically create the `string`. `model` can also be used as a positional argument.

Example:

```py
from factory.django import DjangoModelFactory as ModelFactory
from factoryman import ModelFieldSequence


class CharityFactory(ModelFactory):
    class Meta:
        model = Charity

    name = ModelFieldSequence(Charity)  # Will be `Charity__name-n`, where n is the object count
    email = ModelFieldSequence(string='hello@charity.ee')  # Will be `hello@charity.ee-n`, where n is the object count
```
