from flask import Flask, render_template, jsonify, request
from neo4j import GraphDatabase
import json

app = Flask(__name__)

uri = "bolt://ec2-54-200-13-63.us-west-2.compute.amazonaws.com:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "wangda10"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/echo")
def print_paperID():
    with driver.session() as session:
        with session.begin_transaction() as tx:
            results = (tx.run("MATCH (n:paper_id) where n.name is not null RETURN n.name"))
          # results = (tx.run("MATCH p=()-[r:`is cited by`]->() RETURN p"))
        session.close()
        records = []
        for record in results:
            records.append({"paper_id": record["n.name"]})
        return jsonify(records)

#@app.route('/cool_form', methods=['GET', 'POST'])
app.route('/cool_form')
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')
#app.config['DEBUG'] = True

if __name__ == "__main__":
    app.run()

