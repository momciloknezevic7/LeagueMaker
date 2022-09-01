import psycopg2


conn = None
cur = None


def delete_table():
    command = """
            DROP TABLE IF EXISTS Team CASCADE;
        """

    cur.execute(command)


def create_table():
    command = """
            CREATE TABLE IF NOT EXISTS Team (
                team_id         SERIAL PRIMARY KEY,
                name            VARCHAR(50) NOT NULL,
                members         VARCHAR(255) NOT NULL,
                won             INT DEFAULT 0,
                drawn           INT DEFAULT 0,
                lost            INT DEFAULT 0,
                goal_diff       INT DEFAULT 0,
                points          INT DEFAULT 0
            );
        """

    cur.execute(command)


def load_teams():
    pass


def add_new_team(name, members):
    command = """
            INSERT INTO Team(name, members) 
            VALUES(%s, %s);
            """

    # cur.executemany(command, team_list)
    # team list [(name1,members1), (name2,members2)...]
    cur.execute(command, (name, members))


if __name__ == '__main__':
    print("Creating database...")
    try:
        # connect to the Postgresql server
        conn = psycopg2.connect(
            dbname='IbisLeague',
            user='postgres',
            password='momcilo',
            port='5433'
        )
        cur = conn.cursor()

        delete_table()
        create_table()

        # close communication with the Postgresql database server
        cur.close()

        # commit the changes
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print("DONE!")
