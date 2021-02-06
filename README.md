# async_8ball
Asynchronous 8ball response generator.
Example:
```py
import async_8ball
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
