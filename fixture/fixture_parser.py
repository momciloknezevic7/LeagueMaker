from fixtures_lib import parse_unread_fixtures, print_standings
from db.db_init import connect_to_database, disconnect_from_database

# Run this file for parsing unread fixtures and latest standings
if __name__ == '__main__':
    connect_to_database()

    parse_unread_fixtures()
    print_standings()

    disconnect_from_database()
