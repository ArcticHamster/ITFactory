"""
Chain of responsibility,
Command,
Interpreter,

Iterator = este un design pattern care ne permite sa iteram pete anumite cloectii / range-uri (for si while)
ideea de baza este de a putea accesa in ordine secventiala elementele unei colectii fara a cunoaste detalii
despre implementare acestora
In Python iteratorii sunt implementati folosind interfata Iterable

Mediator,
Memento,
Null Object = folosit pentru a avea un element comun care sa semnifice absenta unei valori
Observer =
State,
Strategy,
Template method,
Visitor.
"""

class Blog:

    def __int__(self):
        self.observers = []

    def add_observer(self, obs, name):
        self.observers.append(obs)
        self.name = name

    def remove_observer(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.notify(self.neame)

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def notify(self, blog_name):
        print(f'Notifying {self.name} about blog post in {blog_name}')


blog = Blog('IT Factory Blog')
user1 = User('Ion', 'ion@ceva.com')
user2 = User('Gheo', 'celmaibun@ceva.com')


