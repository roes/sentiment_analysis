#Web server used to display data from sentiment analysis.

The application displays per company the reputation change over time using Google Charts. It requires you have files containing the data to be displayed.

## The data to be displayed

The data must be stored as csv files in `data/`

Each line of the csv files should be of the form:
`companyName;YYYY-MM-DD;reputationValue`

## Setting up the database

You need to have __sqlite__ installed.

Run `./db/setup_database.sh`

You only need to do this once or if you want to use new data files.

## Running the server

Requires __python__ and [pyramid](http://www.pylonsproject.org/projects/pyramid/download).
Also requires you to have created the database, see above. It should found here: `db/reputation.db`

Run `python display.py`
