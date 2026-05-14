from lib.film import Film

class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM films')
        films = []
        for row in rows:
            item = Film(row["title"], row["director"], row["id"])
            films.append(item)
        return films