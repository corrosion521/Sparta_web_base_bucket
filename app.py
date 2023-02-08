from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 이하 3줄 db사용 위해
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.n0vryb2.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

# api 1 : 버킷 등록하기
@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
    # 버킷 번호도 들어가야 하는데, 이를 위해서 이전에 쌓여 있던 버킷 리스트 가져와야함.
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_list) + 1

    doc = {
        'num' : count, # 번호
        'bucket' : bucket_receive, #내용
        'done' : 0 # 최초에는 완료 당연히 안되어있음.
    }

    db.bucket.insert_one(doc) # 데이터 넣기

    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST(완료) 연결 완료!'})


# api 2 : 버킷 리스트 보여주기
@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({}, {'_id': False}))

    return jsonify({'buckets': bucket_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)