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
  script: keyof Scripts,
  data: Scripts[typeof script]['input'],
  findResults: (out: string[]) => Scripts[typeof script]['output']
): Promise<ReturnType<typeof findResults>> => {
  const shell = new PythonShell(script, { stdio: 'pipe' });
  return new Promise((resolve, reject) => {
    shell.stdin.write(JSON.stringify(data));
    shell.stdin.end();

    let out: string[] = [];
    shell.stderr.on('error', (...err) => reject(...err));
    shell.stdout.on('data', (...data) => (out = [...out, ...data]));
    shell.stdout.on('close', () => resolve(findResults(out)));
  });
};
