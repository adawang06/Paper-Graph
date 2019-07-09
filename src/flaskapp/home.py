from flask import Flask, render_template, jsonify, request
from neo4j import GraphDatabase
import json
import psycopg2
import psycopg2.extras

app = Flask(__name__)

uri = "bolt://ec2-54-200-13-63.us-west-2.compute.amazonaws.com:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "wangda10"))

connection = psycopg2.connect(user="postgres",
                                  password="wangda10",
                                  host="54.245.145.134",
                                  port="5432",
                                  database="citation_pairs")
cur = connection.cursor()

@app.route('/')
def index():
    return render_template('home.html')


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


@app.route("/getdata", methods=["GET", "POST"])
def getdata():
    repoid = request.form['paper_id']
    cur.execute("SELECT * FROM citation_pairs_schema.table1 where id = (%s)", (repoid,))
    print("repoid",repoid)
    #cur.execute("select * from citation_pairs_schema.table1")
    results = cur.fetchall()
    return render_template('view.html', results=results)

if __name__ == "__main__":
    app.run()
