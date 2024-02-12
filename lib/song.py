from config import CONN, CURSOR
# from config import  CURSOR

class Song:
    
    """
    Initialize the object with the given name and album.
    Parameters:
        name (str): The name of the object.
        album (str): The album of the object.
    """
    def __init__(self, name, album):
        self.id = None  
        self.name = name
        self.album = album

    """
    Create a table if it does not already exist in the database. No parameters or return types.
    """
    @classmethod
    def create_table(cls):
        sql = """
                CREATE TABLE IF NOT EXISTS songs(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    album TEXT
                )
            """
        CURSOR.execute(sql)

    """
    Save the current object to the database.
    """
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
        CONN.commit()

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song


# hello = Song("Hello", "25")     
# hello.save()

# despacito = Song("Despacito", "Vida")
# despacito.save()
