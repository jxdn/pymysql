import pymysql,json

#membuat koneksi
db = pymysql.connect("localhost","root","" )
cursor = db.cursor()





sql = "CREATE DATABASE IF NOT EXISTS swapi"
cursor.execute(sql)



sql = "CREATE TABLE IF NOT EXISTS `swapi`.`people` ( `name` VARCHAR(20) NOT NULL , `gender` VARCHAR(20) NOT NULL , `homeworld` VARCHAR(20) NOT NULL ) ENGINE = InnoDB"
cursor.execute(sql)



#membuka list file json
list = [line.rstrip('\n') for line in open('list')]


#membaca file json
for li in list:
    with open(li) as json_data:
        d = json.load(json_data)
        for i in range(len(d['results'])):
            sql = "INSERT INTO `swapi`.`people` (`name`, `gender`, `homeworld`) VALUES ('" + d['results'][i][
                'name'] + "', '" + d['results'][i]['gender'] + "', '" + d['results'][i]['homeworld']+"');"
            print(sql);
         
            cursor.execute(sql)

db.commit()

db.close()