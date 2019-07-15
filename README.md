This is an application that browse directories and shows simple html pages. Created from tutorial pages in web
and the purpose is to learn and develop apps with Flask and test them with Jenkins.

To run the app we need to have install:

Python 2.7+ 
pip
the modules from requirements.txt file

There are many pages in web that say how to install Python and Pip.
Supose that the above are installed then we can install the modules from requirements.txt file
using pip with this command in linux terminal: (it may needs to change directory to the folder that our app files are)

>  pip install -r requirements.txt

or the command in windows Power Shell.

If we are not facing any issue then we can see our app in a web broswer at:

http://localhost:5000/

If you want to use the Dockerfile and build a docker image then don not forget to change the flask's IP from 127.0.0.1 to 0.0.0.0 (all). To do that, open main.py and change the last line, app.run(debug=True), with app.run(host='0.0.0.0').

