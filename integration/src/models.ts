export interface ProcessedData {
  images: string[];
  metadata: Metadata[];
}

export interface Metadata {
  [key: string]: string;
}
