from fixtures_lib import generate_fixtures, create_fixture_file
from db.db_init import connect_to_database, get_names, disconnect_from_database

if __name__ == "__main__":

    connect_to_database()

    # Query for getting name of each team
    names = get_names()

    # True for two-leg fixtures, False for single
    fixtures = generate_fixtures(names, False)

    # Create file for each fixture with blank fields for result
    for game_week in range(len(fixtures)):
        create_fixture_file(game_week+1, fixtures[game_week])

    disconnect_from_database()
