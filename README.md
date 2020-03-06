Title:Based on binocular stereo vision system for comparing each function

This system includes the following modules: camera calibration, feature extraction, feature matching ,stereo matching, calculation of depth information and getting the depth image.
The purpose of this design: For binocular stereo vision system, I adopt different algorithms to compare the advantages and disadvantages of different modules.

Camera calibration: comparing the openCV built-in camera calibration function and Matlab camera calibration function.Result: openCV camera calibration is a bit of tedious, but Matlab has easy access to the internal and external parameters matrix and distortion coefficient.

Feature extraction: using SIFT (Scale Invariant Feature Transform) and SURF (Speeded Up Robust Features) algorithm to do feature extraction. SURF algorithm is about 3 times faster than SIFT in operation speed, and could extract more feature points.SURF borrows from the idea of reduced approximation in SIFT and uses the Hessian matrix instead of constructing DOG pyramid of SIFT, which can save time.In addition, SURF uses box blur to approximate the gaussian blur, so that the template only needs a few simple addition and subtraction operations to filter the image.

Feature matching: feature matching algorithm uses BF (Brute force) algorithm to compare with FLANN algorithm.FLANN algorithm has an internal mechanism, which can select the appropriate algorithm to process the data set according to the data itself, and the processing speed is fast.Although BF is a kind of violent matching algorithm, the operation time is shorter than FLANN algorithm in the processing of general photos,.However, BM algorithm is prone to mismatching regions.

Stereo matching: using BM algorithm to realize 3D reconstruction and obtain the image depth map.BM algorithm is more commonly used. It is a block stereo matching method and adopts the SAD algorithm,the calculation is simple and fast.


Prospect: BM stereo matching algorithm still has many shortcomings. For example, it is easy to appear more multi-point cloud. However, the stereo matching algorithm based on fully CNN(connected neural network) and edge perception parallax propagation has better performance.The algorithm first obtains the initial matching cost through the fully connected neural network, and generates the initial parallax graph after the cost aggregation.Then it carry out left and right consistency detection, filter out the inconsistent pixels, gets the parallax map;Then the parallax is filled by the method of edge perception parallax propagation.Finally, the packed parallax map is optimized with sub-pixel enhancement.The algorithm can effectively reduce the matching rate error, reduce noise interference and improve the accuracy of the parallax map.

Result:
main window:

![image](https://github.com/polya-xue/Based-on-binocular-stereo-vision-system-for-comparing-each-function/blob/master/screenshots/1.png)

SIFT algorithm

![image](https://github.com/polya-xue/Based-on-binocular-stereo-vision-system-for-comparing-each-function/blob/master/screenshots/2.png)

SURF algorithm

![image](https://github.com/polya-xue/Based-on-binocular-stereo-vision-system-for-comparing-each-function/blob/master/screenshots/3.png)

SURF+BF

![image](https://github.com/polya-xue/Based-on-binocular-stereo-vision-system-for-comparing-each-function/blob/master/screenshots/5.png)

SURF+FLANN

![image](https://github.com/polya-xue/Based-on-binocular-stereo-vision-system-for-comparing-each-function/blob/master/screenshots/6.png)

BM and get the 3D point coordinates in the camera coordinate system

![image](https://github.com/polya-xue/Based-on-binocular-stereo-vision-system-for-comparing-each-function/blob/master/screenshots/7.png)
