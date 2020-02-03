import { Transcription } from './models';

/**
 * @description Attempts to parse a data string into JSON, if it fails it returns the string instead
 * @param {*} data
 * @returns {data is Transcription} the parsed JSON or the input string
 */
export const attemptJSONParse = (data: string) => {
  try {
    return JSON.parse(data);
  } catch {
    return data;
  }
};

/**
 * @description Returns true if the data matches the transcription data shape
 * @param {*} data
 * @returns {data is Transcription} if the data is in the transcription data shape
 */
export const onlyTranscription = (data: any): data is Transcription => data.images && data.metadata;
