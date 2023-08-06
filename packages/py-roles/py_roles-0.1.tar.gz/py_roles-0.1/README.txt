Library for Role based development.

The big difference with mixins is that this role is applied only to the subject instance, not to the subject class (alas, a new class is constructed).

Roles can be assigned and revoked. Multiple roles can be applied to an instance. Revocation can happen in any particular order.

Using Roles
As a basic example, consider a domain class:

>>> class Person:
...     def __init__(self, name):
...         self.name = name
>>> person = Person("John")
The instance should participate in a collaboration in which it fulfills a particular role:

>>> from roles import RoleType
>>> class Carpenter(metaclass=RoleType):
...     def chop(self):
...          return "chop, chop"
Assign the role to the person:

>>> Carpenter(person)                           # doctest: +ELLIPSIS
<Person+Carpenter object at 0x...>
>>> person                                      # doctest: +ELLIPSIS
<Person+Carpenter object at 0x...>
The person is still a Person:

>>> isinstance(person, Person)
True
… and can do carpenter things:

>>> person.chop()
'chop, chop'
Context
Roles make a lot of sense when used in a context. A classic example is the money transfer example. Here two accounts are used and an amount of money is transfered from one account to the other. So, one account playes the role of source account and the other plays the role of target account.