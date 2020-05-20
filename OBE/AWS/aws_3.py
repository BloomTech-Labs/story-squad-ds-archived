import json, ndjson
import numpy as np
from matplotlib import pyplot as plt

file = "penis-simplified.ndjson"
dataset = ['penis-simplified']

labels, dataset_name = dataset, 'penises'


with open('penis_simplified.ndjson') as f:
    data = ndjson.load(f)
    print(len(data))
    print(data[1].keys())

drawing = data[0]['drawing']
print(drawing)

print('Shapes:', [np.array(stroke).shape for stroke in drawing])
print('Example stroke:', drawing[0])

for stroke in drawing:
  # Each array has X coordinates at [0, :] and Y coordinates at [1, :].
  plt.plot(np.array(stroke[0]), -np.array(stroke[1]))


def showimg(img):
  if isinstance(img, np.ndarray):
    img = Image.fromarray(img, 'L')
  b = io.BytesIO()
  img.convert('RGB').save(b, format='png')
  enc = base64.b64encode(b.getvalue()).decode('utf-8')
  display.display(display.HTML(
      '<img src="data:image/png;base64,%s">' % enc))


def dict_to_img(drawing, img_sz=512, lw=3, maximize=True):

  print(drawing)
  img = Image.new('L', (img_sz, img_sz))
  draw = ImageDraw.Draw(img)

  lines = np.array([
      stroke[0:2, i:i+2]
      for stroke in drawing['drawing']
      for i in range(stroke.shape[1] - 1)
  ], dtype=np.float32)
  print("Lines:", lines)
  if maximize:
    for i in range(2):
      min_, max_ = lines[:,i,:].min() * 0.95, lines[:,i,:].max() * 1.05
      lines[:,i,:] = (lines[:,i,:] - min_) / max(max_ - min_, 1)
  else:
    lines /= 1024
  for line in lines:
    print("Line:", line)
    draw.line(tuple(line.T.reshape((-1,)) * img_sz), fill='white', width=lw)

  showimg(img)
  return img
