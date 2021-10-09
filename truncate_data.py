#!/usr/bin/env python3
import os

IMG_DIR = 'concrete-cracks'
IMG_CLASSES = ['negative', 'positive']
limit =  '05000.jpg'

for img_class in IMG_CLASSES:
  for root, dirs, files in os.walk(f'{IMG_DIR}/{img_class}'):
    for name in files:
      if name > limit:
        print(f'removing {name}!') 
        os.remove(os.path.join(root, name))
