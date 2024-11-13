from flask import Flask ,jsonify,request
from flight_crud_opr import create_table_flights ,create_flight,search_flight,list_flights,delete_flight,update_flight,Flight

create_table_flights()

app =Flask(__name__)
# restfull end points

#post- used for insert query rest full end points 
#get- to read and select command 
#get /id - 0 or 1 row
#put /id - update only one row 
#delete /id- to delete the row
# test backend thunder client and post man api 

@app.route('/flight',method=['POST'])
def flights_create():
    body = request.get_json()
    new_flight = Flight(body['airline'],body['source'],body['destination'],body['duration'],body['fare'])
    id=create_flight(new_flight)
    flight = search_flight(id)
    
