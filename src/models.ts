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
