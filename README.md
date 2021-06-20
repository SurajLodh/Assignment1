# API
# Software Requirement

1. Python 3.6+
2. MongoDBCompass


# Follow Steps and Setup

https://github.com/SurajLodh/Assignment1

1. Copy or download the given repo

2. Open 'Assignment1' path into your Terminal(cmd)

3. Run this command 'pip install -r requirements.txt'
    - It will automatically download all the dependencies.
    
4. Open MonogoDBCompass and create new database.
    - Database name should be 'Assignment'

5. For database creation run this command 'python manage.py makemigrations' 
    After that, run this 'python manage.py migrate'
    - it will create all the tables into database.

6. Now we will Create Superuser for Admin panel Auth
   run this code 'python manage.py createsuperuser'
   - Enter Username what you want e.g. 'admin' same as enter password e.g. 'admin'

7. Now, Run the server 'python manage.py runserver'

done!!


# API Endpoints

## Inputs 
{‘type’:regular or square;‘size’:small or medium or large;‘toppings’:[‘onion’,’tomato','corn','capsicum','cheese','jalapeno']}

## Response Meaaseges
    
   Status                       Successful Message                    
1. HTTP_201_CREATED             {'Data Created !!'}                   
2. HTTP_400_BAD_REQUEST           -----------
3. HTTP_200_OK                   {Data updated !!'}
4. HTTP_206_PARTIAL_CONTENT     {'Data updated !!'}
5. HTTP_400_OK                   {'Data deleted'}
6. HTTP_204_NO_CONTENT             ------------


   Route                 Method                               Input                                                   Output                                   
1. /create                POST        {‘type’:regular;‘size’:medium;‘toppings’:[‘onion’,’tomato']}                    -----                                            
2. /alldata               GET                                -------                           {'id':1;‘type’:regular;‘size’:medium;‘toppings’:[‘onion’,’tomato']}
3. /searchdata            GET                        filter '/searchdata/?search=regular'                            ------
4. /crud/<int:pk>/    PUT,PATCH,DELETE      {‘type’:square;‘size’:small;‘toppings’:[‘onion’,’capsicum']}             ------




