# What this bot does
Whenever someone sends in a discord server the word bee in any context, 
it will send the entire bee movie script.

# How to set it up
clone the project and create a discord bot using the discord developer portal.
in your project, add a secrets.py file and write a function "get_token()" and make
it return your discord bot token.

now you can simply run bot.py and your bot will activate (remember to invite your bot
to your discord server too)

When it comes to hosting I'm using a remote Linode and docker but a heroku server should work just fine
I think.