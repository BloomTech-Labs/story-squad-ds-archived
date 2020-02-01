export interface Transcribed {
  images: string[];
  metadata: Metadata[];
}

export interface Metadata {
  [key: string]: string;
}
