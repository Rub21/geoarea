/*const test = require('tape');
const logInterceptor = require('log-interceptor');
const cmdAreaF = require('../src/featurearea.js');
const FeatureCollection = {"type":"FeatureCollection","generator":"JOSM","features":[{"type":"Feature","properties":{"@id":"597911424","area":"218ha","landuse":"industrial","source":"http://vidgroup.com.vn/en/project/Tan-Truong-Industrial-Park/Technical-infrastructure-53/"},"geometry":{"type":"Polygon","coordinates":[[[106.2169254,20.9374026],[106.2156293,20.9345595],[106.2173691,20.9295566],[106.2217212,20.9297768],[106.2217533,20.9245157],[106.2217265,20.9215744],[106.2218124,20.921359],[106.2224829,20.9200462],[106.223132,20.919044],[106.2248701,20.9194348],[106.232686,20.9283112],[106.2327853,20.9287021],[106.2327397,20.9309543],[106.232729,20.9355137],[106.2278033,20.9361024],[106.2169254,20.9374026]]]}},{"type":"Feature","properties":{"@id":"597896810","area":"129ha","landuse":"industrial","source":"http://daianvietnam.com/dai-an-industrial-zone.html?lang=en"},"geometry":{"type":"Polygon","coordinates":[[[106.2700009,20.9228021],[106.2725758,20.9230727],[106.2747645,20.923233],[106.2768137,20.9234034],[106.275301,20.9340707],[106.2646043,20.9328833],[106.2649906,20.9292156],[106.2651355,20.9283704],[106.2628861,20.9274995],[106.2630916,20.9247863],[106.2695771,20.9256682],[106.2700009,20.9228021]]]}}]};
test('AreaF', function (t) {
  t.plan(1);
  logInterceptor();
  cmdAreaF(file);
  const fc = JSON.parse(logs[0]);
  t.deepEqual(fc, FeatureCollection, 'ok FeatureCollection');
  t.end();
});*/