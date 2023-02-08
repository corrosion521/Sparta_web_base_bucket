from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 이하 3줄 db사용 위해
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.n0vryb2.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
    # 리스트 번호도 들어가야 하는데, 이를 위해서 이전에 쌓여 있던 리스트 가져와야함.
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_list) + 1

    doc = {
        'num' : count,
        'bucket' : bucket_receive,
        'done' : 0
    }

    db.bucket.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST(완료) 연결 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)