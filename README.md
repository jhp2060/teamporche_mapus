# teamporche_mapus

## ABOUT OUR SERVICE
location-based service providing information about a campus to users


## FUNCTION 1
- provide informations about many facilities in buildings in a campus
- classified as building and floor, or types of facilities


-----------------------------
## DEV ISSUES
### DATABASE
- before migration, should create 'database' first 
  <br>`mysql> CREATE DATABASE 'mapus';`
- to renew the password of 'root' account, use the command below (https://wickedmagic.tistory.com/315)
  <br>`GRANT ALL ON *.* TO 'root'@'localhost' IDENTIFIED BY '비밀번호' WITH GRANT OPTION;`

### RESTful API
- use 'serializer' and 
- nested serializer : 


### temporary web hosting : use AWS EC2 instance
- assume that we got the pem key of EC2 instance
- with WindowPowerSehll, access to AWS
    <br>`ssh ubuntu@[instance address:IPv4 public IP
] -i [.pem file name with directory address]`
- after accessing ubuntu instance, activate the virtual environment and install the packages
    <br>`pyenv activate [virtual environment name _ex.proudction]`
    <br>
- move directory to 'srv' and clone the codes from remote repository like github
    <br> `cd src`
    <br> `git clone [github repository address]`
- do runserver with port 8000
    <br> `python manage.py runserver 0.0.0.0:8000`


### others
- archive virtual environment : make requirements.txt file and update it
    <br>`pip freeze > requirements.txt`
    