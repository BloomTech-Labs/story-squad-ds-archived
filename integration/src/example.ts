import { PythonShell } from 'python-shell';

import { Transcribable, Transcription } from './models';
import { attemptJSONParse, onlyTranscription } from './utils';

// Function that takes in data in the Transcribable data format then outputs
// the transcribed data as a promise
const process = (data: Transcribable) => {
  // Calls the Python script using `spwan` from node's built in `child_process` (Wrapped in helpful abstraction library)
  const shell = new PythonShell('../src/transcription.py', { stdio: 'pipe' });

  // Writes the input data to the `stdin` of the python shell
  shell.stdin.write(JSON.stringify(data));
  shell.stdin.end();

  // Creates a new promise of output
  return new Promise<Transcription>((resolve, reject) => {
    // An array of the terminal outputs
    let out: string[] = [];

    // Rejects the promise if an error occurs
    shell.stderr.on('error', (...err) => reject(...err));

    // Each time data is outputted to stdout, save it to the terminal outputs array
    shell.stdout.on('data', (...data) => (out = [...out, ...data]));

    // When the script is over, map over the outputs, attempt to parse them into json then resolve
    // the promise with the first found output that matches the Transcription data shape
    shell.stdout.on('close', () => resolve(out.map(attemptJSONParse).find(onlyTranscription)));
  });
};

// Loads the test.json file
const data = require('./test.json');

// Runs the processing on that data then console.logs the result, if errors occurs it console.errors the errors
process(data)
  .then(console.log)
  .catch(console.error);
