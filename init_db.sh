#!/bin/bash

DB_NAME="harward_university"
DB_USER="areg"
DB_PASSWORD="7125"

psql -U postgres <<EOF
CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
CREATE DATABASE $DB_NAME OWNER $DB_USER;
EOF

echo "Database $DB_NAME and user $DB_USER created."
