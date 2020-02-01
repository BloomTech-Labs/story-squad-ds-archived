const spawn = require('child_process').spawn;

const testData = require('./test.json');
const process = spawn('pipenv', ['run', 'python3', './app.py', JSON.stringify(testData)]);
process.stdout.on('data', (data) => console.log(data.toString()));
