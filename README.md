# Face Matching Using DCT Coefficients

## Objective
To determine if a given face matches one of two stored reference faces using Discrete Cosine Transform (DCT) coefficients of the images.

## Methodology
- **Image Preprocessing:** The input image is loaded and converted to grayscale for easier manipulation. A binary mask is created to isolate the subject in the image, and contours are detected to determine the bounding box for the subject.
  
- **Feature Extraction:** The DCT coefficients of the input image are calculated and compared with those of the two reference images.

- **Classification:** The image is classified as "real" or "fake" based on the difference calculated using the sum of absolute differences from the reference coefficients. A predefined threshold is used to determine the classification outcome.

## Results
- The system classifies input images as either "real" or "fake" based on their similarity to two stored reference faces, achieving an accuracy of approximately 88%.

