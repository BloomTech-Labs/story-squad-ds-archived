import * as express from 'express';
import * as dotenv from 'dotenv';

import { Transcribable } from './models';
import { attemptJSONParse, onlyTranscription } from './utils';
import { runScript } from './scripting';

dotenv.config();

function transcribe(data: Transcribable) {
  return runScript('./ds/transcription.py', data, (out) =>
    out.map(attemptJSONParse).find(onlyTranscription)
  );
}

const app = express();
app.use(express.json());

app.post('/upload', async (req, res) => {
  const data = req.body as Transcribable;
  const processed = await transcribe(data);
  res.json({ processed });
});

const port = Number(process.env.PORT);
app.listen(port);
console.log(`Listening on port ${port}`);
