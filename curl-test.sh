curl -X POST http://localhost:5000/api/timeline_post -d 'name=Lauren&email=fake@email.com&content=test'
if [ $? -eq 0 ]; then
  echo "POST request had no errors"
fi

curl http://localhost:5000/api/timeline_post
if [ $? -eq 0 ]; then
  echo "GET request had no errors"
fi

curl --request DELETE http://localhost:5000/api/timeline_post
