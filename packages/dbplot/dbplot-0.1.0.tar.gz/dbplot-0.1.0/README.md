# dbplot

dbplot allows you to make calculations for plots inside databases.

dbplot is powered by [ibis](https://github.com/ibis-project/ibis) so its possible to target multiple databases that include:
Postgres, MySQL, Apache Impala, Apache Kudu, BigQuery [and more](https://docs.ibis-project.org/), also everything that ibis will support
in the future such as Apache Spark.

## Install

```
pip install dbplot
```

Development version:

```
pip install git+git://github.com/danielfrg/dbplot.git
```

## Usage

See [notebooks]() for examples.

```python
import os
import ibis
import dbplot

# Connect to DB
host = os.environ.get("DBPLOT_TEST_POSTGRES_HOST", "localhost")
user = os.environ.get("DBPLOT_TEST_POSTGRES_USER", "postgres")
password = os.environ.get("DBPLOT_TEST_POSTGRES_PASSWORD")
database = os.environ.get("DBPLOT_TEST_POSTGRES_DATABASE", "nycflights13")
con = ibis.postgres.connect(host=host, database=database, user=user, password=password)

# Get a table
flights = con.table("flights")

# Plot stuff
dbplot.hist(flights, flights.dep_time, nbins=20)
```

## Roadmap

- Automated tests
- More plots such as raster plots, line charts and more :)

## Notes

Based on [dbplot for R](https://github.com/edgararuiz/dbplot).
