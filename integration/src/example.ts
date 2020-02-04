import { runScript } from './scripting';
import { attemptJSONParse, onlyTranscription } from './utils';

// Wrapper function that runs a specific script
// Parameters<typeof runScript>[1] is used to specify the second parameter type of `runScript`
function transcribe(data: Parameters<typeof runScript>[1]) {
  return runScript(
    '../src/transcription.py', // Specifies the script to use, the path is relative to the directory the application is started from
    data, // The data to pass into stdin of the script
    (out) => out.map(attemptJSONParse).find(onlyTranscription) // A function to take the stdout of the script and find the result
  );
}

// Loads the test.json file
const data = require('./test.json');

// Runs the processing on that data then console.logs the result, if errors occurs it console.errors the errors
transcribe(data)
  .then(console.log)
  .catch(console.error);
