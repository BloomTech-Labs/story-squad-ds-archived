import { Transcription } from './models';

/**
 * @description Attempts to parse a data string into JSON, if it fails it returns the string instead
 * @param {string} data a string that may or may not be JSON data
 * @returns {Object | string} the parsed JSON or the input string
 */
export const attemptJSONParse = (data: string): Object | string => {
  try {
    return JSON.parse(data);
  } catch {
    return data;
  }
};

/**
 * @description Returns true if the data matches the Transcription data shape
 * @param {Object | string} data a string or a parsed JSON that may or may not be in the Transcription data shape
 * @returns {data is Transcription} if the data is in the Transcription data shape
 */
export const onlyTranscription = (data: Object | string): data is Transcription =>
  data['images'] && data['metadata'];
