# EventMailer

## To send the mail call below API.

```
curl --location 'http://127.0.0.1:8000/send-event-emails/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "kunal",
    "mobile_number": "2354656",
    "gender": "Male"
}'
```
