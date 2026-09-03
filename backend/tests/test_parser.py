from app.core.curl_parser import curl_parser

str_curl = """curl -X 'POST' \
  'https://musical-enigma-x59v7x55pxr53pxgp-8000.app.github.dev/auth/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "string",
  "email": "user@example.com",
  "password": "string"
}'"""

result = curl_parser(str_curl)

print(result)