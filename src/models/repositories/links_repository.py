from sqlite3 import Connection

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
        
    def create_link(self, links_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO links
                (id, trip_id, link, title)
            VALUES
                (?, ?, ?, ?);
            ''', (
                links_info['id'],
                links_info['trip_id'],
                links_info['link'],
                links_info['title']
            )
        )
        self.__conn.commit()
        
    def get_links_by_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM links
            WHERE 
                trip_id = ?;
            ''', (trip_id,)
        )
        link = cursor.fetchone()
        return link