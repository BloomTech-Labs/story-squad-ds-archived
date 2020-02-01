import { Transcribed } from './models';

export const attemptJSONParse = (data: string) => {
  try {
    return JSON.parse(data);
  } catch {
    return data;
  }
};

export const onlyTranscribed = (data: any): data is Transcribed => data?.images && data.metadata;
