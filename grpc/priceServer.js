var PROTO_PATH = __dirname + '/grpcService.proto';
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');
// Suggested options for similarity to existing grpc.load behavior
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
// The protoDescriptor object has the full package hierarchy
var exchange = protoDescriptor.salesExchange;

var data = [
    {name: "a", price: 101010},
    {name: "b", price: 102022},
    {name: "c", price: 300303}
];

function getPrice(call, callback){
    console.log("using getPrice: ", call.request.name);
    data.forEach(element => {
        if( element.name == call.request.name){
            console.log("found: ", element);
            callback(null, {name: call.request.name, price: element.price});
        }
    });
}

function getServer() {
    var server = new grpc.Server();
    server.addService(exchange.service, {
      GetPrice: getPrice
    });
    return server;
  }
var routeServer = getServer();
routeServer.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
routeServer.start();
console.log("started the server", data[0]);