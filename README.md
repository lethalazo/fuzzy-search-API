Description:<br/>
This fuzzy-search-api package is written using Python 3 and tested using Python 3.9 and Elasticsearch 7.14.1.<br/>
The REST API is written using Flask to perform CRUD operations on the provided data, which is imported as JSON and indexed using Elasticsearch.<br/>
<br/>
Files:<br/>
    - api.py: The main API app file. Creates an Elasticsearch index, imports and indexes the JSON data,<br/>
        and runs a Flask API with the following endpoints:<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;-> /data<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Request formats supported:<br/>
        <br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/data/&lt;document-id&gt;<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/data/?query=&lt;query-string&gt;<br/>
        <br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/data/&lt;document-id&gt;<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with JSON content-type.<br/>
    <br/>
    - config.py: Contains constants for Flask API and Elasticsearch indexer config.<br/>
    <br/>
    - es_indexer.py: A Python class to encapsulate the Elasticsearch operations and provide a high-level 'API' for the app to use.<br/>
    <br/>
    - data.json: The provided JSON data file.<br/>
<br/>
How to run:<br/>
    - Run a 'elasticsearch' node on http://localhost:9200 (preferably as a daemon).<br/>
    - Run the api.py file using Python 3.<br/>
    - Run example GET and POST operations on the /data endpoint using the run.sh file.<br/>
