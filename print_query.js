var ipp = require("ipp");
var Printer = ipp.Printer("ipp://192.168.0.27");

var msg = {
  "operation-attributes-tag": {
    "requesting-user-name": "John Doe",
	"job-id": 78,
  }
};

Printer.execute("Get-Job-Attributes", msg, function(err, res) {
        console.log(err);
        console.log(res);
});
