var ipp = require("ipp");
var fs = require("fs");

var Printer = ipp.Printer("ipp://192.168.0.27");
var filename = "output.ps";
var filetype = "application/postscript";

var filedata = fs.readFileSync(filename);

const letter = "na_letter_8.5x11in";
const A4 = "iso_a4_210x297mm";
const A5 = "iso_a5_148x210mm";

console.log(filedata);

var msg = {
  "operation-attributes-tag": {
    "requesting-user-name": "John Doe",
	"document-format": "application/octet-stream",
  },
  "job-attributes-tag": {
    "media": A4,
	"sides": "two-sided-short-edge",
  },
  data: filedata
};

Printer.execute("Print-Job", msg, function(err, res) {
        console.log(err);
        console.log(res);
});
