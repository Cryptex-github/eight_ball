# async8ball
Asynchronous 8ball response generator.
Example:
```py
import async8ball
async def your_function():
 response = await async_8ball.response()
```
Deco Example:
```py
from async8ball.decorators import ball_decorator
@ball_decorator
def my_function(**kwargs):
  return kwargs['response']
```
Discord.py command implement:
```py
from async8ball.decorators import ball_decorator
@ball_decorator
def my_func(question, **kwargs):
  return kwargs['response']
@bot.command()
async def my_command(ctx, *, question:str):
  await ctx.send(ball8(question))
```
or
```py
import async8ball
@bot.command(self, ctx, *, question:str):
 await ctx.send(await async8ball.response(question))
 ```
