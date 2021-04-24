import csv
from db import db

def create_list():
    sql = "SELECT COUNT(*) FROM continents"
    result = db.session.execute(sql)
    db.session.commit()

    if result.fetchone()[0] > 1:
        return False

    sql = "INSERT INTO continents (name) VALUES " \
    "('Africa'), ('Asia'), ('Europe'), ('North America'), ('South America'), ('Oceania')"
    db.session.execute(sql)
    db.session.commit()

    with open('data/countries.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            name = row[1]
            continent_id = ""
            if row[0] == "AF":
                continent_id = 1
            if row[0] == "AS":
                continent_id = 2
            if row[0] == "EU":
                continent_id = 3
            if row[0] == "NA":
                continent_id = 4
            if row[0] == "SA":
                continent_id = 5
            if row[0] == "OC":
                continent_id = 6
            sql = "INSERT INTO countries (name, continent_id) VALUES (:name, :continent_id)"
            db.session.execute(sql, {"name":name, "continent_id":continent_id})
        db.session.commit()

    return True
        
def get_list():
    sql = "SELECT id, name, continent_id FROM countries"
    result = db.session.execute(sql)
    return result.fetchall()