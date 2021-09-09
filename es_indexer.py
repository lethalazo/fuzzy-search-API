'''
Author: Arsalan Azmi
Description: Elasticsearch indexer.
Package: fuzzy-search-api
Python Version: 3.9
Year: 2021
Version: 1
'''
# ---- IMPORTS ----
import config as _config
import elasticsearch as _es

class ESIndexer:
    '''
    Class for Elasticsearch indexer.
    '''
    def __init__(self):
        es    = _es.Elasticsearch(host= _config.ES_HOST, port= _config.ES_PORT)
        es    = _es.Elasticsearch()

        index = _config.ES_INDEX

        # Create an elasticsearch index.
        es.indices.create(index=index, ignore=400)

        self.__es    = es
        self.__index = index

    # Public API
    def upsert(self, id, data):
        '''
        Insert data for provided ID or update with an incremented revision if data exists.

        Parameters
        ----------
        id : str
            Document ID.
        data : dict
            Document data.

        Returns
        -------
        response : any
        '''
        return self.__insertData(id, data)

    def get(self, id):
        '''
        Get document by ID.

        Parameters
        ----------
        id : str
            Document ID.

        Returns
        -------
        response : any
        '''
        return self.__getById(id)
    
    def search(self, query, attribute):
        '''
        Query based on the provided attribute and get a list of documents sorted by their decreasing similarity score.

        Parameters
        ----------
        query : str
            Query string to search.
        attribute : str
            Attribute to query.

        Returns
        -------
        documents : list
        '''
        res  = self.__fuzzySearch(query, attribute)
        docs = sorted(res['hits']['hits'], key=lambda x: -x['_score'])
        return docs

    # Private API
    def __fuzzySearch(self, query, attribute):
        es    = self.__es
        index = self.__index
        # construct dict for elasticsearch fuzzy query.
        fuzzyQuery = {
            attribute: {
                'query': query,
                'fuzziness': 'AUTO'
            }
        }
        # Search query to match exact occurences, similar keywords and similar prefixes.
        return es.search(index=index, body={
            'query': {
                'bool': {
                    'should': [ 
                        {'match': fuzzyQuery}, 
                        {'match_bool_prefix': fuzzyQuery} 
                    ]
                }
            }
        })
        
    def __getById(self, id):
        es    = self.__es
        index = self.__index
        return es.get(index=index, id=id)

    def __insertData(self, id, data):
        es    = self.__es
        index = self.__index
        return es.index(index=index, id=id, body=data)
    