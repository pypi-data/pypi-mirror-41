# AIoT Studio 

AIoT Studio is the official library to develop datasources and dependency sets for [mnubo's AIoT Studio.](https://smartobjects.mnubo.com/documentation/aiotStudio.html)

## Installation

### Requirements
* Python 2.7 or Python 3.4 and up
* `requests`
* `pandas` ≥ 0.20
* `numpy`

`$ pip install aiot-studio`

## Simple datasource usage

```python
from aiotstudio.datasource import search_df, log

def execute(parameters):
    log.info("Hello aiot-studio")
             
    result = search_df({
        "from": "event",
        "select": [{"count": "*"}]
    })
    return result
```

## Configuration

The library needs to be configured with your [mnubo API credentials](https://smartobjects.mnubo.com/documentation/api_security.html). 
The credentials can be shared as follows (by decreasing order of priority):

- Environment variables: `MNUBO_CLIENT_ID`, `MNUBO_CLIENT_SECRET`, `MNUBO_API_URL`
- Local config file: `application.conf` at the root of the project or anywhere indicated by the `MNUBO_CONFIG_FILE` environment variable
- Global config file: `~/.settings/mnubo/application.conf` (or `C:\Users\<username>\.settings\mnubo\application.conf` on Windows)

For the last two options, the configuration file should look like this:

```
[DEFAULT]
mnubo_client_id = {API_CLIENT_ID}
mnubo_client_secret = {API_CLIENT_SECRET}
mnubo_api_url = https://prod.api.mnubo.com
``` 


## Available methods

  - `search(query)`: returns the search result as a JSON
  - `search_df(query)`: returns the search result as a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)
  - `log`: [Python logger](https://docs.python.org/3/library/logging.html): will appear in the "Logs" app, use `log.info`, `log.warning` or `log.error` instead of `print`
  - `blob_store_bucket_names()`: returns the bucket names available
  - `blob_store_fetch(bucket_name, object_name)`: grabs the object from the bucket
  
_Notes_:
  - All "search" methods expect a MQL query as described in the [search API](https://smartobjects.mnubo.com/documentation/api_search.html) documentation 
  - Blob store methods are only available when the code runs inside mnubo's architecture, using it locally would throw a `FeatureUnavailableError`