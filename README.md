<h1>버킷리스트 - homework</h1>

1. 기능
   1. 버킷 리스트 남기기[POST] : 입력한 데이터(버킷)를 db에 저장.
      1. 클라이언트: 
         - data out : 버킷
         - data in : 메시지
      2. 서버 :
         - data in : 메시지
         - data out : 버킷 
   2. 버킷 리스트 보기[GET] : 페이지 로딩 후 db에서 버킷 리스트 가져오기.
      1. 클라이언트 
         - data out : x
         - data in : 버킷 리스트
      2. 서버 :
         - data in : x
         - data out : 버킷 리스트
   3. 버킷 상태 업데이트[POST] : 해당 번호의 버킷을 완료 처리로 업데이트
      1. 클라이언트 
         - data out : num
         - data in : 메시지
      2. 서버 :
         - data in : num
         - data out : 메시지
  
2. 기타 파일
   