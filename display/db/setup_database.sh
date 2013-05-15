#!/bin/bash
rm db/reputation.db
sqlite3 db/reputation.db < db/schema.sql
for file in data/*.csv; do
  sqlite3 -separator ';' db/reputation.db ".import $file reputation"
done
