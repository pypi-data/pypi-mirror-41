# firelane
A Pytorch training and visualisation library.

## [Dataset](https://github.com/krinj/torch-raptor/blob/master/docs/dataset.md)

A Dataset is a wrapper for a collection of `Samples`. It comes with functionality to help with understanding and balancing the data for training:

* Easily visualize the class distribution into a graph.
* Can be split into evenly balanced (label wise) k-folds.
* Can be resampled to achieve a more even class distribution.
* Can be shuffled so that batching will produced balanced distributions of classes.

| Original Data                                            | Oversampled                                                  | Undersampled                                                 |
| -------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![starting_samples](images/dataset/starting_samples.png) | ![oversampled_gallery](images/dataset/oversampled_gallery.png) | ![undersampled_gallery](images/dataset/undersampled_gallery.png) |

| Batching + Unbalanced Shuffle               | Batching + Balanced Shuffle               |
| ------------------------------------------- | ----------------------------------------- |
| ![img](images/dataset/unbalanced_batch.png) | ![img](images/dataset/balanced_batch.png) |

## Problems

* There's a lot of boilerplate code that I need to re-write every time I begin a new Pytorch project (e.g. training loop, logging the progress, saving the checkpoints).
* Depending on the epochs, the logging could be too slow or too fast. I want a time-based tracking system.
* There's no easy way to queue up multiple configurations or parameters of a model to be trained. I need to wait for one to finish before trying something else.
* There's no easy system for versioning and logging the things that work well.
* I want a clear way to visualize my progress.
* Will train on GPU when available.

## Stretch Goals

* I want a way to access and train my models while I'm out and about.
* I want a system that can search and tune for its own parameters.
* I want my system to be adaptable to different data types.





