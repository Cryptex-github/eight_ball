import random
import functools
choices = ['Yes', 'No', 'Yes']

def ball_decorator(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    kwargs['response'] = random.choice(choices)
    return func(*args, **kwargs)
  return wrapper
