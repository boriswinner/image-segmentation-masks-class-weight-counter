# Class percentage counter for image segmentation datasets

There are a lot of unbalanced image segmentation datasets. For example, 90% of a dataset can be forest, 9.5% water and only 0.5% - buildings.

To cope with such datasets, I've created this tool. It processes a folder with segmentation masks and outputs percentage and absolute values of pixel count for each class in the dataset.

You can use the output to weight your loss function or to balance the dataset manually.

## How to use

  * Download the binary (see ```Releases```) or clone this repo
  * Put your masks in ```images``` directory

```
SOME_FOLDER_ON_YOUR_COMPUTER
+-- images
|   +-- mask1.jpg
|   +-- mask2.png
    ...
+-- main.exe (or main.py)
```

* Run the ```main``` executable. Wait some time...
* Success! Now in ```output.txt``` you can see the results and a pie chart is shown on the screen.


## Dependencies
* cv2
* numpy as np
* matplotlib
* tqdm
