from db_init import connect_to_database, delete_table, create_table, disconnect_from_database

if __name__ == '__main__':
    connect_to_database()

    print("Deleting old version if exists...")
    delete_table()

    print("Creating tables...")
    create_table()

    disconnect_from_database()

    print("DATABASE HAS BEEN RESET!")
