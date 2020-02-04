import { PythonShell } from 'python-shell';
import * as express from 'express';
import * as dotenv from 'dotenv';

import { Transcribable, Transcription } from './models';
import { attemptJSONParse, onlyTranscription } from './utils';

dotenv.config();

const processImage = (data: Transcribable) => {
  const shell = new PythonShell('./ds/transcription.py', { stdio: 'pipe' });
  shell.stdin.write(JSON.stringify(data));
  shell.stdin.end();
  return new Promise<Transcription>((resolve, reject) => {
    let out: string[] = [];
    shell.stderr.on('error', (...err) => reject(...err));
    shell.stdout.on('data', (...data) => (out = [...out, ...data]));
    shell.stdout.on('close', () => resolve(out.map(attemptJSONParse).find(onlyTranscription)));
  });
};

const app = express();
app.use(express.json());

app.post('/upload', async (req, res) => {
  const data = req.body as Transcribable;
  const processed = await processImage(data);
  res.json({ processed });
});

const port = Number(process.env.PORT);
app.listen(port);
console.log(`Listening on port ${port}`);
