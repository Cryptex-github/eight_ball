"""
A very sophisticated 8-ball algorithm >:)
"""

import random as ball_algorithm_

from functools import wraps
from typing import Callable, List, TypeVar


__all__: Tuple[str] = (
    'ball_decorator',
)


choices: Tuple[str] = (
    "It is certain",
    "Without a doubt", 
    "You may rely on it",
    "Yes definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy try again",
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don’t count on it",
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no",
    "I'm not sure, but I do know that you are very sus",
)


PT = TypeVar('PT')
RT = TypeVar('RT')


def ball_decorator(func: Callable[PT, RT]) -> Callable[PT, RT]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> RT:
        kwargs['response'] = ball_algorithm_.choice(choices)
        return func(*args, **kwargs)
    
    return wrapper
