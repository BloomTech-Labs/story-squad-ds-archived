import { PythonShell } from 'python-shell';

import { Transcribable, Transcription } from './models';
import { attemptJSONParse, onlyTranscription } from './utils';

const process = async (data: Transcribable) => {
  const shell = new PythonShell('../src/transcription.py', { stdio: 'pipe' });
  shell.stdin.write(JSON.stringify(data));
  shell.stdin.end();
  return await new Promise<Transcription>((resolve, reject) => {
    let out: string[] = [];
    shell.stderr.on('error', (...err) => reject(...err));
    shell.stdout.on('data', (...data) => (out = [...out, ...data]));
    shell.stdout.on('close', () => resolve(out.map(attemptJSONParse).find(onlyTranscription)));
  });
};

const data = require('./test.json');
process(data)
  .then(console.log)
  .catch(console.error);
