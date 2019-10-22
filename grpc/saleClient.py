import json
import grpc
import logging
from flask import Flask, request
import grpcService_pb2
import grpcService_pb2_grpc
app = Flask(__name__)
salesData = json.loads('{"a": 0.1,"b": 0.3,"c": 0.5}')

channel = grpc.insecure_channel('localhost:50051')
stub = grpcService_pb2_grpc.salesExchangeStub(channel)
@app.route('/discounts')
def discounts_c():
    resp = stub.GetPrice(grpcService_pb2.PriceRequest(name="a"))
    if not resp.price:
        return "bad response, no price"
    return "Item name: " + resp.name + " and its price with sale: " + str(resp.price - resp.price * salesData["a"])

if __name__ == '__main__':
    logging.basicConfig()
    app.run(debug=True, port=5000, host='0.0.0.0')
