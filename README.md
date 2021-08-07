----------------list--------------
http://127.0.0.1:8000/list/

------------create---------------
http://127.0.0.1:8000/create/
  {
  	"first_name": "naresh",
  	"last_name": "patel",
  	"email": "naresh@gmail.com",
  	"phone_no": "+919090909090",
  	"password": "admin",
  	"is_active": true
  }

---------------put-update-------------------------
http://127.0.0.1:8000/user/7/
{
    "id": 7,
    "first_name": "nareshpatel",
    "last_name": "patel",
    "email": "naresh@gmail.com",
    "phone_no": "+919090909090",
    "is_active": true
}