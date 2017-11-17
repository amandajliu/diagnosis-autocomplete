# Web service to autocomplete diagnoses
Files:
- `Trie.py`: Implementation of Trie data structure for prefix tree
- `diagnosis_search.py`: Flask app with API for autocomplete and updating/storing query with selected diagnosis

## Setup

Create a new virtualenv named 'hd', activate it, and install requirements:

`virtualenv hd`

`. hd/bin/activate`

`pip install -r requirements.txt`

Run `diagnosis_search.py` to start web service:

`chmod a+x diagnosis_search.py`

`./diagnosis_search.py`

Now the webservice is running on localhost:5000/

## API
- GET `api/search/<prefix>`: return autocompleted words for `<prefix>`
- PUT `api/search`: create or update a `{query: <string>, selected: <string>}` object in database
- GET `api/search`: return all query-diagnosis pairs in database
  
You may use `curl` command to make API calls:

### Example usage:

- GET request for autocompleted words with prefix "ar":

`curl -i http://localhost:5000/api/search/ar`

- PUT request to update or create an entry for query "he" with selected diagnosis "heart disease":

`curl -i -H "Content-Type: application/json" -X PUT -d '{"query":"he", "selected":"heart disease"}' http://localhost:5000/api/search`

- GET current database entries for selected diagnoses matched with queries:

`curl -i http://localhost:5000/api/search`

