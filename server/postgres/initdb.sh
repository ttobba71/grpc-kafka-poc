#!/usr/bin/env bash
set -e

function create_postgres_db() {
    db_name=$1
    echo "Creating database '$db_name'"
    psql -v ON_ERROR_STOP=0 --username "$POSTGRES_USER" <<-EOSQL
        CREATE DATABASE $db_name;
        CREATE DATABASE ${db_name}_test;
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
EOSQL
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
        CREATE ROLE ${db_name}_rw;
        CREATE ROLE ${db_name}_ro;
        GRANT ALL PRIVILEGES ON ALL TABLES    IN SCHEMA public TO ${db_name}_rw;
        GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ${db_name}_rw;
        CREATE USER ${db_name}_rw_app WITH IN ROLE ${db_name}_rw ENCRYPTED PASSWORD '$POSTGRES_PASSWORD';
        CREATE USER ${db_name}_ro_app WITH IN ROLE ${db_name}_ro ENCRYPTED PASSWORD '$POSTGRES_PASSWORD';
        GRANT ${db_name}_rw TO $POSTGRES_USER;
        GRANT ${db_name}_ro TO $POSTGRES_USER;
EOSQL
}

if [ -n "$POSTGRES_DATABASES" ]; then
    echo "Creating multiple databases: $POSTGRES_DATABASES"
    for db in $(echo "$POSTGRES_DATABASES" | tr ',' ' '); do
        create_postgres_db "$db"
    done
else
    create_postgres_db "$POSTGRES_NAME"
fi
