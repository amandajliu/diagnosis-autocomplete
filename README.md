Files:
- Trie.py: Implementation of Trie data structure for prefix tree
- diagnosis_search.py: Flask app with API for autocomplete and updating/storing query with selected hypothesis 

How to run:
Create a new virtualenv named 'hd', activate it, and install requirements:
`virtualenv hd`
`. hd/bin/activate`
`pip install -r requirements.txt`

Run diagnosis_search.py to start web service:
`chmod a+x diagnosis_search.py`
`./diagnosis_search.py`
Now the webservice is running on localhost:5000/

You may use `curl` command to make API calls:
Ex:
Autocomplete GET request:
`curl -i http://localhost:5000/api/search/ar`

POST match query with selected diagnosis:
`curl -i -H "Content-Type: application/json" -X POST -d '{"query":"ar", "selected":"arthritis"}' http://localhost:5000/api/search`

PUT update query with selected diagnosis:
`curl -i -H "Content-Type: application/json" -X PUT -d '{"query":"he", "selected":"heart disease"}' http://localhost:5000/api/search`

GET current database entries for selected diagnoses matched with queries:
`curl -i http://localhost:5000/api/search`

