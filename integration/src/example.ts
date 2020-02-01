import { PythonShell } from 'python-shell';
import { Observable } from 'rxjs';
import { map, filter, shareReplay } from 'rxjs/operators';
import { attemptJSONParse, onlyTranscribed } from './utils';

const { stdin, stdout, stderr } = new PythonShell('../src/transcription.py', { stdio: 'pipe' });

const testData = require('./test.json');
stdin.write(JSON.stringify(testData));
stdin.end();

const $out = new Observable((observer) => {
  stdout.on('data', (...data) => observer.next(...data));
  stderr.on('error', (...err) => observer.error(err));
  stdout.on('close', () => observer.complete());
});

const $parsed = $out.pipe(map(attemptJSONParse), filter(onlyTranscribed), shareReplay(1));
$parsed.subscribe(console.log);
