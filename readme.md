# Class Bot

## installation 

1. go to main.py file. Search for variable meetMap, and add links of all your classes.
First dictionary in the array is Monday, similarly second one is Tuesday, and so on.

2. Create a new file 'creds.py' and add the following lines:

        email = 'your institute mail'
        pword = 'your password'

3. open a terminal and type the following command:

        pip install selenium

4. run 'python main.py' in a terminal to start the bot.


### Note:
>Chrome driver present in chrome-driver folder is for v87 only.
>You need to download the same version of chrome driver and place it in the 
>'chrome-driver' folder, as the version of google chrome installed on your machine. 
>
>The bot can also mark your attendance.
>Have a look at the mark attendace function.
>It will type 47 in the chat, when any of the strings present in alertWords,
>is typed in the chat by other people.
>You can come up with your own mark attendance function, by learning a little 
>web scraping. 

## have a nice day!



