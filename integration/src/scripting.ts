import { PythonShell } from 'python-shell';

import { Scripts } from './models';

/**
 * @description
 * @param {keyof Scripts} script The relative path from root to the script to run
 * @param {Scripts[typeof script]['input']} data input data to the script matching the dataType defined in the
 * `Scripts` interface
 * @param {(out: string[]) => Scripts[typeof script]['output']} findResults a callback function that will go
 * through the array of all outputs of the stdout outputs of the script and find the result value.
 *
 * Note: Some Scripts may stdout when printing out status messages
 * @returns {Promise<ReturnType<typeof findResults>>} A promise of the resulting data after being found with
 * the `findResult()` callback
 */
export const runScript = (
  script: keyof Scripts, // Matches a key of the `Scripts` interface which is a path to the script being used
  data: Scripts[typeof script]['input'], // Uses the `input` type for the selected Script
  findResults: (out: string[]) => Scripts[typeof script]['output'] // Uses the output data type of the selected Script
): Promise<ReturnType<typeof findResults>> => {
  const shell = new PythonShell(script, { stdio: 'pipe' }); // Starts script in the background and opens up stdin for piping data
  return new Promise((resolve, reject) => {
    // Creates a new promise for the result, since the script is async a promise makes most since
    shell.stdin.write(JSON.stringify(data)); // Writes the data to stdin
    shell.stdin.end(); // Closes stdin to the script can start

    let out: string[] = []; // An array of all the terminal outputs
    shell.stderr.on('error', (...err) => reject(...err)); // Rejects the promise if an error is thrown in the script
    shell.stdout.on('data', (...data) => (out = [...out, ...data])); // Adds every stdout (including `print()` calls) to the out array
    shell.stdout.on('close', () => resolve(findResults(out))); // Resolves the promise by calling the `findResult()` callback function
  });
};
