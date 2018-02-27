#!/usr/bin/env node

const argv = require('minimist')(process.argv.slice(2));
const area = require('./src/area');
const bbox2fc = require('./src/bbox2fc');
const buffer = require('./src/buffer');
const clip = require('./src/clip');
var action = argv._[0];
var file = argv._[1];
switch (action) {
	case 'area':
		area(file);
		break;
	case 'bbox2fc':
		bbox2fc(argv.bbox);
		break;
	case 'buffer':
		buffer(file, argv.unit, argv.radius);
		break;
	case 'clip':
		clip(file, argv._[2]);
		break;
	default:
		console.log('unknown command');
}