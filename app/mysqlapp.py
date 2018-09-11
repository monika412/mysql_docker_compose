from typing import List, Dict
from flask import Flask, jsonify
import mysql.connector
import json

app = Flask(__name__)


def all_users() -> Dict:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db-mysql',
        'port': '3306',
        'database': 'fresco_segment'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT party_id,fresco13_seg,fresco13_sseg,fresco13_mseg,match_flag FROM customer_segments')
    results_val = cursor.fetchall()
    
    cursor.close()
    connection.close()
    headers=['party_id','fresco13_seg','fresco13_sseg','fresco13_mseg','match_flag']
    results=[dict(zip(headers,val)) for val in results_val]
    
    print (results)
    return results


@app.route('/')
def index() -> str:
    return all_users()


if __name__ == '__main__':
    print ("in main")
    app.run(debug=True,host='0.0.0.0',port=80)
