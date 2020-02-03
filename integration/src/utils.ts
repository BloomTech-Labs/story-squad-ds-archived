import { Transcription } from './models';

export const attemptJSONParse = (data: string) => {
  try {
    return JSON.parse(data);
  } catch {
    return data;
  }
};

export const onlyTranscription = (data: any): data is Transcription =>
  data?.images && data.metadata;
