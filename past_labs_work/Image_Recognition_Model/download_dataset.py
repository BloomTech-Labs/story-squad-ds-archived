# it downloads the full quickdraw dataset
from __future__ import absolute_import, division, print_function, unicode_literals
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

# tfds works in both Eager and Graph modes
tf.enable_v2_behavior()
tfds.disable_progress_bar()

# Construct a tf.data.Dataset
ds = tfds.load(
  'quickdraw_bitmap', split='train', shuffle_files=True, as_supervised=True)
for example in ds.take(1):
  image, label = example['image'], example['label']

## Reshape and normalize
def normalize_img(image, label):
  """Normalizes images: `uint8` -> `float32`."""
  return tf.cast(image, tf.float32) / 255., label

ds = ds.map(
    normalize_img, num_parallel_calls=tf.data.experimental.AUTOTUNE)
# Build your input pipeline
ds = ds.shuffle(1000).batch(32).prefetch(tf.data.experimental.AUTOTUNE)


#plt.imshow(image.numpy()[:, :, 0].astype(np.float32), cmap=plt.get_cmap("gray"))
#print("Label: %d" % label.numpy())
