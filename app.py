#배송 조회 API - GET
from flask import Flask, request, jsonify
import pymysql

db = pymysql.connect(host='localhost',user='root',password='rkdekgus0813',database='TRAFFIC')

app = Flask(__name__)

@app.route("/api/external/data/tracking", methods=['GET'])
def tracking():
    params = request.args.get('shipment_number')
    cursor = db.cursor()

    sql = f"SELECT RESULT FROM delivery WHERE SHIPMENT_NUMBER={params}"
    
    cursor.execute(sql)
    status = cursor.fetchone()
    
    if status:
        response = {
            "송장번호":params,
            "배송상태":status #0 : 배송중, 1: 배송완료
        }
    else: #bad request
        return "해당 송장번호는 존재하지 않습니다."

    cursor.close()

    return jsonify(response) #json 형태로 반환

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
    db.close()

#예외처리 필요 부분(딱히 하진 않음)
# - 같은 송장번호에 대한 배송 상태가 2개 이상인 경우
   # - 즉, 하나의 송장번호가 db에 2개 이상 다른 row로 저장 되어 있을 경우
      # - 이 경우는 db 단에서 그냥 최신 상태 기준으로 처리 결과 정하는 걸로..

#의문점
#배송상태라는게 처리결과를 의미하는지.. 보여줄거면 메세지 보여주는게 낫지 않은지
#db 스키마 : shipment_number(pk), result, message
#mysql은 일단 도커로 띄워서 진행 함
#swagger 여부 : https://givemethesocks.tistory.com/116