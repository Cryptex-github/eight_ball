# eight_ball
8ball response generator.
Example:
```py
import eight_ball
ball = eight_ball.ball()
print(ball.response("is eight_ball a good ball"))
```
Discord.py bot implement
"""
Put the ball object under the bot object
"""
```py
@bot.command()
async def ball(ctx, *, question):
 await ctx.send(bot.ball.response(question)
```
