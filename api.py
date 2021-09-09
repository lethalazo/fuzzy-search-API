'''
Author: Arsalan Azmi
Description: Fuzzy Search Flask REST API. 
Package: fuzzy-search-api
Python Version: 3.9
Year: 2021
Version: 1
'''
# ---- IMPORTS ----
import config as _config
from es_indexer import ESIndexer
import flask as _flask
import json as _json

# ---- PRIVATE HELPERS ----
def _loadAndBulkUpdateJSONData(fileName, indexer):
    with open(fileName) as f:
        JSONData = _json.load(f)
        for doc in JSONData:
            indexer.upsert(doc['uid'], doc)

# Initialize app.
_app = _flask.Flask(__name__)

# Create an index and update/insert JSON data.
try:
    _indexer = ESIndexer()
    _loadAndBulkUpdateJSONData(_config.DATA_FILE, _indexer)
except ConnectionError:
    print('Please make sure an Elasticsearch node is running on host: {} port {}'.format(_config.ES_HOST, _config.ES_PORT))
    exit(-1)
except Exception as e:
    print(e)
    exit(-1)

# ---- API ROUTES ----
@_app.route('/data/<id>', methods=['GET'])
def api_get_data(id):
    return _json.dumps(_indexer.get(id))

@_app.route('/data/<id>', methods=['POST'])
def api_update_data(id):
    data = _flask.request.json
    return _json.dumps(_indexer.upsert(id, data))

@_app.route('/data/', methods=['GET'])
def api_search_data_by_name():
    args = _flask.request.args
    key = 'name'
    value = args.get('query')
    return _json.dumps(_indexer.search(value, key))

# ---- RUNNER ----
if __name__ == '__main__':
    _app.run()