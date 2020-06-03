from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient            
client = MongoClient('localhost', 27017)   
db = client.dbsparta                    

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    counts_receive = request.form['counts_give']
    addr_receive = request.form['addr_give']
    telno_receive = request.form['telno_give']

    orderlist = {
       'name': name_receive,
       'counts': counts_receive,
       'addr': addr_receive,
       'telno': telno_receive
    }
    
    db.bikeorders.insert_one(orderlist)
    return jsonify({'result':'success', 'msg': '주문이 잘 되었습니다!'})


@app.route('/orders', methods=['GET'])
def read_order():
    orders = list(db.bikeorders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'msg': orders})
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)