import random
import redis
from pyhive import hive

db = redis.StrictRedis(host='localhost', port=6379, db=0)
cursor = hive.connect(host='localhost', port='10000').cursor()

MONTH = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
         "September": 9, "October": 10, "November": 11, "December": 12}

GENRES = ['Action', 'War', 'Fiction', 'Disaster', 'Comedy', 'Documentary']


def date_parser(date):
    if date == "None":
        return "1800-1-1-T00:00:00Z"
    sp = date.split()
    month = str(MONTH[sp[0]])
    day = sp[1].replace(",", "")
    year = sp[2]
    return year+"-"+month+"-"+day+"-T00:00:00Z"

num = 0
fail = 0
for key in db.keys():
    real_key = key.decode()
    movie_id = real_key[-10:]

    # Not A Real Key
    if movie_id == "w_movie_id" or key == "useful_proxy".encode() or key == "raw_proxy".encode():
        continue

    movie = db.hgetall(key)

    genre = random.choice(GENRES)
    raw_date = movie["date".encode()].decode()
    utcdate = date_parser(raw_date)
    movie_id = movie["id".encode()].decode()
    actor = movie["actor".encode()].decode().strip('[]').split(',')[0].strip('\'')
    title = movie["title".encode()].decode()
    review_number = int(movie["review".encode()].decode())
    director = movie["director".encode()].decode().strip('[]').split(',')[0].strip('\'')
    price = float(random.randint(0, 39) + random.choice([0.99, 0.00]))

    num += 1
    try:
        cursor.execute('INSERT INTO movies VALUES ("%s", "%s", "%s", "%s", "%s", %.2f, "%s", %d)' % (movie_id, title, actor, director, utcdate, price, genre, review_number))
    except Exception:
        fail += 1
        print(movie_id, actor, director, genre, title, review_number, price, utcdate)
        print('Failure Numer: ' + str(fail) + '\n\n')

    if num%100 == 0:
        print('Success Number: ' + str(num) + '\n\n')
