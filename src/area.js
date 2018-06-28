const fs = require('fs');
const turf = require('@turf/turf');
module.exports = function (file) {
  var area = 0;
  var geojson = JSON.parse(fs.readFileSync(file).toString());
  geojson.features.forEach(function (feature) {
    area += turf.area(feature) / 1000000;
  });
  console.log(area + ' MK2');
};