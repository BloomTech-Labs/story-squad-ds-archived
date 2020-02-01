import { PythonShell } from 'python-shell';
import { from } from 'rxjs';
import { map, filter } from 'rxjs/operators';
import { attemptJSONParse, onlyParsedData } from './utils';

const testData = require('./test.json');
const args = [JSON.stringify(testData)];
PythonShell.run('../src/app.py', { args }, (err, data: string[]) => {
  if (err) throw err;
  from(data)
    .pipe(map(attemptJSONParse), filter(onlyParsedData))
    .subscribe(console.log);
});
