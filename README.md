# GROUP 43
Students: 
* Adrian-Gabriel Aduculesei - ec18123@qmul.ac.uk:
  Implemented account model, user authentication, article model, articles ajax like, email notification, and relevant templates

* Anton Petrov Nyagolov - ec18201@qmul.ac.uk:
  Implemented accoutn settings, categories and comments models, profile picture, post/edit/delete/new ajax coment, testing and relevant templates


Test users:
* Username: user Password: user - admin 
* Username: user1 Password: user1
* Username: user2 Password: user2
* Username: user3 Password: user3

Deployed on: https://mygroup43-mygroup43.apps.okd.eecs.qmul.ac.uk/

**Current Chromedriver is provided for Chrome - version 87.
Unless your chrome browser is different version (not 87), there is no need to download it as it is automatically picked for your OS  by the test scripts**


# Instructions: 

This project has been created under Conda virtual environment : https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

Assuming you have conda installed:

1) Create new conda env: ```conda create --name "environment name"``` (the name of the environment should be withough double quotes)

2) Activate the new conda environment: ```conda activate "environment name"```

3) Install pip package: ```conda install pip```

4) install all the modules from the requirements.txt file by:
 ``` pip install -r requirements.txt```
5) Run the server: ```./manage.py runserver```

