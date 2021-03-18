SURVIVED = """SELECT COUNT(*) FROM titanic WHERE survived = 1"""
DIED = """SELECT COUNT(*) FROM titanic WHERE survived = 0"""
FIRST_CLASS = """SELECT COUNT(pclass) FROM titanic WHERE pclass = 1 GROUP BY pclass"""
SECOND_CLASS = """SELECT COUNT(pclass) FROM titanic WHERE pclass = 2 GROUP BY pclass"""
THIRD_CLASS = """SELECT COUNT(pclass) FROM titanic WHERE pclass = 3 GROUP BY pclass"""
FIRST_CLASS_SURVIVED = """SELECT COUNT(*) FROM titanic WHERE pclass = 1 AND survived = 1"""
FIRST_CLASS_DIED = """SELECT COUNT(*) FROM titanic WHERE pclass = 1 AND survived = 0"""
SECOND_CLASS_SURVIVED = """SELECT COUNT(*) FROM titanic WHERE pclass = 2 AND survived = 1"""
SECOND_CLASS_DIED = """SELECT COUNT(*) FROM titanic WHERE pclass = 2 AND survived = 0"""
THIRD_CLASS_SURVIVED = """SELECT COUNT(*) FROM titanic WHERE pclass = 3 AND survived = 1"""
THIRD_CLASS_DIED = """SELECT COUNT(*) FROM titanic WHERE pclass = 3 AND survived = 0"""
AVG_AGE_SURVIVED = """SELECT AVG(age) FROM titanic WHERE survived = 1"""
AVG_AGE_DIED = """SELECT AVG(age) FROM titanic WHERE survived = 0"""
AVG_AGE_1ST = """SELECT AVG(age) FROM titanic WHERE pclass = 1"""
AVG_AGE_2ND = """SELECT AVG(age) FROM titanic WHERE pclass = 2"""
AVG_AGE_3RD = """SELECT AVG(age) FROM titanic WHERE pclass = 3"""
AVG_FARE_1ST = """SELECT AVG(fare) FROM titanic WHERE pclass = 1"""
AVG_FARE_2ND = """SELECT AVG(fare) FROM titanic WHERE pclass = 2"""
AVG_FARE_3RD = """SELECT AVG(fare) FROM titanic WHERE pclass = 3"""
AVG_FARE_SURVIVED = """SELECT AVG(fare) FROM titanic WHERE survived = 1"""
AVG_FARE_DIED = """SELECT AVG(fare) FROM titanic WHERE survived = 0"""
AVG_SIBSPOUS_1ST = """SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE pclass = 1"""
AVG_SIBSPOUS_2ND = """SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE pclass = 2"""
AVG_SIBSPOUS_3RD = """SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE pclass = 3"""
AVG_SIBSPOUS_SURVIVED = """SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE survived = 1"""
AVG_SIBSPOUS_DIED = """SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE survived = 0"""
AVG_PARCHILD_1ST = """SELECT AVG(parents_children_aboard) FROM titanic WHERE pclass = 1"""
AVG_PARCHILD_2ND = """SELECT AVG(parents_children_aboard) FROM titanic WHERE pclass = 2"""
AVG_PARCHILD_3RD = """SELECT AVG(parents_children_aboard) FROM titanic WHERE pclass = 3"""
AVG_PARCHILD_SURVIVED = "SELECT AVG(parents_children_aboard) FROM titanic WHERE survived = 1"
AVG_PARCHILD_DIED = "SELECT AVG(parents_children_aboard) FROM titanic WHERE survived = 0"

all_queries = [SURVIVED, DIED, FIRST_CLASS, SECOND_CLASS, THIRD_CLASS, FIRST_CLASS_SURVIVED,
               FIRST_CLASS_DIED, SECOND_CLASS_SURVIVED, SECOND_CLASS_DIED, THIRD_CLASS_SURVIVED,
               THIRD_CLASS_DIED, AVG_AGE_SURVIVED, AVG_AGE_DIED, AVG_AGE_1ST, AVG_AGE_2ND, AVG_AGE_3RD,
               AVG_FARE_1ST, AVG_FARE_2ND, AVG_FARE_3RD, AVG_FARE_SURVIVED, AVG_FARE_DIED,
               AVG_SIBSPOUS_1ST, AVG_SIBSPOUS_2ND, AVG_SIBSPOUS_3RD, AVG_SIBSPOUS_SURVIVED,
               AVG_SIBSPOUS_DIED, AVG_PARCHILD_1ST, AVG_PARCHILD_2ND, AVG_PARCHILD_3RD,
               AVG_PARCHILD_SURVIVED, AVG_PARCHILD_DIED]
