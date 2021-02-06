import random
import functools
choices = ["It is certain","Without a doubt", "\
You may rely on it","\
Yes definitely","\
It is decidedly so","\
As I see it, yes","\
Most likely","\
Yes","\
Outlook good","\
Signs point to yes","\
Reply hazy try again","\
Better not tell you now","\
Ask again later","\
Cannot predict now","\
Concentrate and ask again","\
Don’t count on it","\
Outlook not so good","\
My sources say no","\
Very doubtful","\
My reply is no"]

def ball_decorator(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    kwargs['response'] = random.choice(choices)
    return await func(*args, **kwargs)
  return wrapper