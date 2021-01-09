# API Test
This program uses openweathermap.org to display weather conditions in a user-inputted city.

It will only work on my machine since it deals with an APPID.  However if a local key is acquired, it will work.

The program runs on a while True loop to provide as many opportunities as the user would like.
From what I found, there is not a pretty way in python to prompt until success. This way is functional.

I could not find a module to directly convert epoch time to UTC datetime.  Since datetime.datetime.fromtimestamp
automatically converts to the local timezone, I negated that with time.timezone, then converted to the desired timezone
provided by the JSON.

I used pyinstaller to create an executable.  It can be found at apiTest/dist/apiTest/apiTest.exe
