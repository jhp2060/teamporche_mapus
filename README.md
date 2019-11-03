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

### URLS
- USE viewset
    : 