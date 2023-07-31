# Dune Analytics API

- Use this python script to retrieve data from Dune queries.
- User inputs the **QUERY ID** of the query they want the results for via in terminal prompts. A Dune query's ID can be found at the end of the query's URL. For example, the ID of the query with the URL https://dune.com/queries/4319/22558 is **22558**. When prompted, copy and paste **22558** into the terminal to retrieve results.
- File returned will look like the table of the query requested. For example, the CSV file returned from [this query](https://dune.com/queries/4319/22558) will have four columns (Rank, Project, 7 Days Volume, and 24 Hours Volume) and 47 rows (one row for each rank).

**User must input their API Key in the " " marks of line 15. This can be retrieved from the [settings](https://dune.com/settings/api) of your Dune account.**

_Reference [here](https://github.com/check-sked/dune_analytics_api) for the script in Node.JS._
