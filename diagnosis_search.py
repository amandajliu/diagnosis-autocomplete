#!hd/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from Trie import Trie

app = Flask(__name__)
prefix_tree = Trie()

# Dummy database array
selected_diagnoses = []

# Autocomplete words, given prefix as query
@app.route('/api/search/<prefix>', methods = ['GET'])
def get_autocomplete_words(prefix):
    return jsonify({ 'words': prefix_tree.autocomplete(prefix) })       

# Update/store query with selected diagnosis
@app.route('/api/search', methods = ['PUT'])
def select_diagnosis():
    if not request.json:
        abort(400)
    diagnosis = {
        'query': request.json['query'],
        'selected': request.json['selected']
    }
    # Store new entry or find relevant query in db then update value
    matched_queries = [matched for matched in selected_diagnoses if matched['query'] == request.json['query']]
    if not matched_queries:
        selected_diagnoses.append(diagnosis)
    else:
        old_query = matched_queries[0]
        old_query['query'] = request.json['query']
        old_query['selected'] = request.json['selected']
    return jsonify({ 'selected_diagnosis': diagnosis }), 200

# Get database values of queries matched to selected diagnoses
@app.route('/api/search', methods = ['GET'])
def get_selected_diagnoses():
    return jsonify({ 'selected_diagnoses': selected_diagnoses })

if __name__ == '__main__':
    # Insert all sample diagnoses into prefix tree
    with open('short-diagnoses.txt', 'r') as word_sample_file:
        for line in word_sample_file:
            full_word = line.strip()
            # Also insert alternate names for diagnoses
            if full_word.find("(") != -1 and full_word.find(")") != -1:
                alternate_name = full_word[full_word.find("(")+1:full_word.find(")")]
                prefix_tree.addWord(alternate_name, line.strip())
            prefix_tree.addWord(line.strip())
    app.run(debug = True)
