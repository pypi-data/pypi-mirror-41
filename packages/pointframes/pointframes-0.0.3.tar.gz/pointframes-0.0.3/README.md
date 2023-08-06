# PointFrames - A Scalable Point Cloud Library

## 3D Point Cloud Processing

The pointframe library is primarily a 3D point cloud processing library, designed to work with point clouds as dataframes. The current features revolve around basic point cloud processing tasks. The library is designed to work natively with Pandas data frames and generally all functions take a dataframe as an input for processing. To allow this a strict column naming convention needs to be employed with your data frame. Each function initially asserts the required columns are present by comparing the data frame column names with a requirement list. This allows functions to be created for processes requiring a range of attributes. For more common functions a PointCloud() class can be used to directly access core functionality easily. There is no limit to what can be added to the class function list, although it makes sense to only add functions that are used frequently.

The scalability of the library comes from utilising the [dask](https://docs.dask.org/en/latest/) package. Dask is a "flexible library for parallel computing in Python". Dask is designed to work natively with pandas dataframes and as such all the functions in pointframes should be compatible with dask. Any functions should be tested with a dask multi-partition array to determine if it is compatible. If it isn't it should be clearly noted, or a work-around should be implemented using a `dask=True` function variable. Dask should allow for point clouds of arbitrary size to be loaded in and processed. When designing dask specific functions, it is a reasonable assumption that dataset has been indexed by the z-order as this provides very large performance improvements with respect to speed.

### Attribute naming convention

The following column headers should be adhered to. Any attribute names that are used in new functions should be agreed on and added here for future use.

```
pID, z_ord, X, Y, Z, R, G, B, nX, nY, nZ, cam_coord, inv_prob, eig1, eig2, eig3, class, sum_eigens, planarity, omnivariance, linearity, anisotropy, eigentropy, scattering, curvature, point_density
```

The order is not important for each data frame as the data is indexed from the header name.

### Current Functions

* Read and write pointcloud
* Visualisation
* Normal estimation
* Eigenvalue feature calculation
* Voxel down sampling
* Rotation and translation
* Horizontal scene parsing
* PointNet / PointNet ++ model training
* MCCNN model training
* View frustum bounding box
* Object to camera pixel
* Z-order indexing and selection

### Features to add

* Euclidean clustering
* Ground segmentation
* Dask machine learning

Visit the example section for basic functionality code.

## 2D Image Processing

Currently, no 2D image processing tools are present. This is mainly due to wealth of 2D image processing libraries. However, if we have a good reason to start adding some, we can also use this repository. A slight restructuring would be necessary, so this decision is best made sooner rather than later.

## General Rules

All code written should be compatible with both python 2.7 and 3.X. In general, try to make sure code is developed with up-to-date libraries and note versions when using less common libraries. Below are some standard library requirements.

* Open3D >= 0.4.0
* tensorflow (gpu) >= 1.7 (CUDA 9)
* OpenCV >= 4.0
* pytorch >= 1.0

The library should be designed to scale. If you ever feel we need to rearrange the folder structure always do this sooner rather than later.

Where possible always format the code in [PEP 8](https://www.python.org/dev/peps/pep-0008/) style.
