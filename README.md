# IDKScript

Just a little programming language I've been working on for a couple of weeks
open .ks files with KaneScript.exe
to have a better experience, load as custom language on Notepad++ Notepad++Language.xml

Sintax

HelloWorld:
    
        put-0-'Hello, World!'
        log-0

put stores a value in a variable

    put-'foo'-'Hello!'
    put-0-'Hello!'

log prints the value of a variable

    log-0
    log-'foo'

get stores user's input in a variable

    get-0-'what's your name? '
    get-'name'-'Gimme yr name: '

read copies the value of a variable on another
  
    read-'two0s'-0
    read-1-'message'

jump jumps to a specific line

    jump-4

int converts a variable to integer

    int-'output variable'-'input variable'

add sums or concatenates two variables

    add-'firs'-'second'
