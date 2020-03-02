import sqlite3

connection = sqlite3.connect('comics.db')


def connect_to_DB():
    cursor = connection.cursor()
    return cursor


# def create_table():
#     with connection:
#         cursor = connect_to_DB()
#         cursor.execute(
#             """CREATE TABLE dilbert_comics (id text, publish_date text, comics_name text, comics_url text)""")


def insert_values(values):
    with connection:
        cursor = connect_to_DB()
        cursor.execute("""INSERT INTO dilbert_comics VALUES (?,?,?,?)""", values)
        connection.commit()


def get_last_added_record():
    with connection:
        cursor = connect_to_DB()
        cursor.execute(
            """SELECT * FROM dilbert_comics ORDER BY publish_date DESC LIMIT 1""")
        results = cursor.fetchone()
        return results

# def select_values(id):
#     with connection:
#         cursor = connect_to_DB()
#         cursor.execute(
#             """SELECT * FROM dilbert_comics WHERE id='""" + id + """'""")
#         results = cursor.fetchall()
#         return results
#
#
# def update_values(date, title, image_url):
#     with connection:
#         cursor = connect_to_DB()
#         cursor.execute(
#             """UPDATE dilbert_comics SET publish_date='""" + date + """', comics_name='""" + title
#             + """', comics_url='""" + image_url + """' WHERE comics_url='""" + image_url + """'""")
#         connection.commit()
#
#
# def delete_values(id):
#     with connection:
#         cursor = connect_to_DB()
#         cursor.execute(
#             """DELETE FROM dilbert_comics WHERE id='""" + id + """'""")
#         connection.commit()
