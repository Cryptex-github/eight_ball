import random
import asyncio
import aiofile

responses_list=["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]

__all__ = ("__version__", "ball")
__version__ = "2.0"
"""
Here we start the ball you can pass in your own asyncio event loop if you wish
"""
class ball:
 def __init_(self, loop=None):
  self.loop = asyncio.get_event_loop() if loop is None else loop
  
async def response(question) -> str:
  return random.choice(responses_list)
