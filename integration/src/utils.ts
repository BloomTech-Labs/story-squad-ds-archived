import { ProcessedData } from './models';

export const attemptJSONParse = (data: string) => {
  try {
    return JSON.parse(data);
  } catch {
    return data;
  }
};

export const onlyParsedData = (data: any): data is ProcessedData => data?.images && data.metadata;
