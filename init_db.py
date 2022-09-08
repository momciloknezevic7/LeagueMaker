import psycopg2
import itertools
import pandas as pd

conn = None
cur = None


def connect_to_database():
    global conn
    global cur

    print("Connecting to database...")
    try:
        # connect to the Postgresql server
        conn = psycopg2.connect(
            dbname='IbisLeague',
            user='postgres',
            password='momcilo',
            port='5433'
        )
        cur = conn.cursor()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    print("Connected to database!")


def disconnect_from_database():
    print("Disconnecting from database...")
    try:
        # close communication with the Postgresql database server
        cur.close()

        # commit the changes
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    print("Disconnected from database!")


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
                played          INT DEFAULT 0,
                won             INT DEFAULT 0,
                drawn           INT DEFAULT 0,
                lost            INT DEFAULT 0,
                goal_diff       INT DEFAULT 0,
                points          INT DEFAULT 0
            );
    """

    cur.execute(command)


def load_teams():
    df = pd.read_csv("DataInput/formResult.csv")
    teams = []
    '''
    Google Form Format (saved as .csv file):
        Timestamp, TeamName, Player1Name, Player2Name, ...
    
        NOTE: For this use, team has only 2 players.
              If necessary, there can be more players. Their names will be placed after Team name.
    '''
    for row in range(len(df)):
        team_name = df.iloc[row][1]
        team_members = ", ".join(df.iloc[row][2:])  # Player1, Player2, Player3...
        teams.append((team_name, team_members))

    print("Teams are loaded from csv file!")
    add_teams_in_database(teams)


def add_teams_in_database(teams):
    command = """
            INSERT INTO Team(name, members) 
            VALUES(%s, %s);
    """

    # teams = [(name1,members1), (name2,members2)...]
    cur.executemany(command, teams)
    print("Teams are added to database!")


def get_names():
    command = """
        SELECT name
        FROM team;
    """

    cur.execute(command)
    teams = cur.fetchall()

    return list(itertools.chain(*teams))


if __name__ == '__main__':

    try:
        connect_to_database()

        delete_table()
        create_table()

        # Get data from Google Form and put it in database
        load_teams()
        get_names()

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
