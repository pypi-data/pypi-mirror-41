sassy
-----

A simple but powerful templating language for text interpolation inspired by sas macros.

How it works
------------

Sassy is a command-line program that interprets input macro tags.

**Macros**
::

    
   %let var1 = some value;
   %let var2 = some other value;

   %macro testMacro(param1);
       this text will show whenever the macro is called.
       variables can be referenced like this: &var1.
       we can reference macro parameters just like variables: &param1.
   %mend;

   here's how you call a macro:
   %exec testMacro(1);

   here's a call to the same macro with a different parameter:
   %exec testMacro(2);

Running **sassy** on the above text file will output the following...
::

    
   $ sassy test.txt
   here's how you call a macro:
       this text will show whenever the macro is called.
       variables can be referenced like this: somevalue
       we can reference macro parameters just like variables: 1

   here's a call to the same macro with a different parameter:
       this text will show whenever the macro is called.
       variables can be referenced like this: somevalue
       we can reference macro parameters just like variables: 2


**Nested variable resolution**
::

    
   %let var1 = some value;
   %let var2 = some other value;
   %let varNum = 1;

   %macro testMacro(param1);
       variables can be nested to form references to other variables: &var&varNum..
       ...and also nest parameters as with variables: &var&param1..
   %mend;

   here's how you call a macro:
   %exec testMacro(1);

   here's a call to the same macro with a different parameter:
   %exec testMacro(2);

Running **sassy** on the above text file will output the following...
::

    
   $ sassy test.txt
   here's how you call a macro:
       variables can be nested to form references to other variables: somevalue
       ...and also nest parameters as with variables: somevalue

   here's a call to the same macro with a different parameter:
       variables can be nested to form references to other variables: somevalue
       ...and also nest parameters as with variables: someothervalue


**Loops**
::

    
   this is how you execute a loop:
   %procloop (3) loopCounter;
       this loop will execute &loopCounter. times.
   %pend;

   ...you can also use a variable to set the number of iterations:
   %let loopVar0 = first loop;
   %let loopVar1 = second loop;
   %let loopVar2 = third loop;
   %let loopVar3 = fourth loop;
   %let numLoops = 4;
   %procloop (&numLoops.) counterVar;
       this other loop will execute &counterVar. times, and references a different variable each time: &loopVar&counterVar..
   %pend;

Running **sassy** on the above text file will output the following...
::

    
   $ sassy test.txt
   this is how you execute a loop:
       this loop will execute 0 times.
       this loop will execute 1 times.
       this loop will execute 2 times.

   ...you can also use a variable to set the number of iterations:
       this other loop will execute 0 times, and references a different variable each time: firstloop
       this other loop will execute 1 times, and references a different variable each time: secondloop
       this other loop will execute 2 times, and references a different variable each time: thirdloop
       this other loop will execute 3 times, and references a different variable each time: fourthloop


Installation
------------

Here's what you need to do to install sassy:

Python 3.6
~~~~~~~~~~

Sassy is compatible with **Python 3.6 and later**.

On Unix systems, install Python 3.6 (or later) via your package manager (apt, rpm, yum, brew).
Alternatively, you can download an installation package from the `official
Python downloads page <https://www.python.org/downloads/>`__.

Virtual Environment
~~~~~~~~~~~~~~~~~~~

It is recommended to put all project dependencies into its own virtual
environment - this way we don't pollute the global Python installation.
For this we recommend you use **virtualenvwrapper**. Follow the instructions
`here <http://virtualenvwrapper.readthedocs.io/en/latest/install.html>`__
to get this installed. Once you have virtualenvwrapper install, create
a new virtual environment with:

::

    
    mkvirtualenv sassy
    workon sassy


Now let's install sassy:

::

    pip install sassylang


Get help or give help
~~~~~~~~~~~~~~~~~~~~~

-  Open a new
   `issue <https://github.com/jmsmistral/sassy/issues/new>`__ if
   you encounter a problem.
-  Pull requests welcome. You can help with language features!

--------------

License
-------

-  sassy is Free Software and licensed under the 
   `GPLv3 <https://github.com/jmsmistral/macrosql/blob/master/LICENSE.txt>`__.
-  Main author is `@jmsmistral <https://github.com/jmsmistral>`__

