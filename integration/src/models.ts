export interface Transcribable {
  images: string[];
}

export interface Transcription {
  images: string[];
  metadata: Metadata[];
}

export interface Metadata {
  [key: string]: string;
}

// An interface used to determine what scripts are valid for `runScripts()`
export interface Scripts {
  // Each script path should be used as a key here, the keys are used in the `keyof Scripts` param of `runScripts()`
  '../src/transcription.py': {
    input: Transcribable; // This is the data shape that the script is built for
    output: Transcription; // This is the data shape of the expected output of the script
  };
}
