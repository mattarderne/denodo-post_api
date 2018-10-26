echo ####
echo start
date
echo ####

#txt='{"serverName": "localhost","type": "view","priority": "local"
params='{"language" : "TEEEST","framework" : "Flask","website" : "Scotch","version_info" : {"python" : 3.4,"flask" : 0.12},"examples" : ["query", "form", "json"],"boolean_test" : true}'

#curl -i -H "Content-Type:application/json" -X POST -d "$txt" "http://127.0.0.1:5000/json-example"

#curl --include --header "Content-Type:application/json" -X POST --data "$params" "http://127.0.0.1:5000/json-example"

curl --include --header "Content-Type:application/json" -X POST --data '{"language" : "TEEEST","framework" : "Flask","website" : "Scotch","version_info" : {"python" : 3.4,"flask" : 0.12},"examples" : ["query", "form", "json"],"boolean_test" : true}' "http://127.0.0.1:5000/json-example"



#curl -i -H "Content-Type:application/json" -X POST -d "{"language" : "TEEEST","framework" : "WHAT","website" : "Scotch","version_info" : {"python" : 3.4,"flask" : 0.12},"examples" : ["query", "form", "json"],"boolean_test" : true}" "http://127.0.0.1:5000/json-example"


#curl --include --header "Authorization: Basic YWRtaW46YWRtaW4=" --header "Accept: application/json" --header "Content-Type:application/json" -X POST --data "{"serverName": "127.0.0.1","type": "view","priority": "local"}" "http://127.0.0.1:9090/denodo-data-catalog/apirest/synchronize"

#curl -i -H "Authorization: Basic YWRtaW46YWRtaW4=" -H "Accept: application/json" -H "Content-Type:application/json" -X POST -d "$txt" "http://127.0.0.1:9090/denodo-data-catalog/"
