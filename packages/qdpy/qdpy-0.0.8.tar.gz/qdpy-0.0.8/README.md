# qdpy - A Quality-Diversity framework for Python 3.6+

`qdpy` is a framework providing Python implementations of recent [Quality-Diversity](https://www.frontiersin.org/articles/10.3389/frobt.2016.00040/full) methodologies: [MAP-Elites](https://arxiv.org/abs/1504.04909), [CVT-MAP-Elites](https://arxiv.org/pdf/1610.05729.pdf), [NSLC](https://arxiv.org/pdf/1610.05729.pdf), [SAIL](https://arxiv.org/pdf/1702.03713.pdf), etc.
QD algorithms can be accessed directly, but `qdpy` also includes building blocks that can be easily assembled together to build your own QD algorithms. It can be used with parallelism mechanisms and in distributed environments.

`qdpy` includes the following features:
 * Generic support for diverse Containers: Grids, Novelty-Archives, Populations, etc
 * Optimisation algorithms for QD: random search methods, quasi-random methods, evolutionary algorithms
 * Support for multi-objective optimisation methods
 * Possible to use optimisation methods not designed for QD, such as [CMA-ES](https://arxiv.org/pdf/1604.00772.pdf)
 * Parallelisation of evaluations, using parallelism libraries, such as multiprocessing, concurrent.futures or [SCOOP](https://github.com/soravux/scoop)
 * Easy integration with the popular [DEAP](https://github.com/DEAP/deap) evolutionary computation framework 


## Installation
`qdpy` requires Python 3.6+. It can be installed with:
```bash
pip install qdpy
```

`qdpy` includes optional features that need extra packages to be installed:
 * `cma` for CMA-ES support
 * `deap` to integrate with the DEAP library
 * `tables` to output results files in the HDF5 format
 * `tqdm` to display a progress bar showing optimisation progress
 * `colorama` to add colours to pretty-printed outputs
You can install `qdpy` and all of these optional dependencies with:
```
pip install qdpy[all]
```

The latest version can be installed from the GitLab repository:
```bash
pip install git+https://gitlab.com/leo.cazenille/qdpy.git@master
```

To build `qdpy` from source:
```bash
git clone https://gitlab.com/leo.cazenille/qdpy.git
cd qdpy
./setup.py develop
```


## Usage

### Quickstart

The following code presents how to use MAP-Elites to explore the feature space of a target function (also available in `examples/rastrigin_short.py`):

```python
from qdpy import algorithms, collections, benchmarks, plots

# Create container and algorithm. Here we use MAP-Elites, by illuminating a Grid container by evolution.
grid = collections.Grid(shape=(64,64), items_per_bin=1,
        fitness_domain=((0., 1.),), features_domain=((0., 1.), (0., 1.)))
algo = algorithms.RandomSearchMutPolyBounded(grid, budget=60000, batch_size=500,
        optimisation_task="maximisation", dimension=3,
        ind_domain=(0., 1.), sel_pb=0.5, init_pb=0.5, mut_pb=0.2, eta=20.)

# Create a logger to pretty-print everything and generate output data files
logger = algorithms.TQDMAlgorithmLogger(algo)

# Define evaluation function
eval_fn = algorithms.partial(benchmarks.illumination_rastrigin_normalised,
        nb_features = len(grid.shape))

# Run illumination process !
best = algo.optimise(eval_fn)

# Print results info
print(algo.summary())

# Plot the results
plots.default_plots_grid(logger)

print("All results are available in the '%s' pickle file." % logger.final_filename)
```


`qdpy` separates Containers (here a Grid) from search algorithms, in a design inspired by [Cully2018](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7959075).
As such, to implement a MAP-Elites-style algorithm, we need to explicitly create 1) a Grid container, and 2) an evolutionary algorithm.
This algorithm will make use of this container in a similar way a classical evolutionary algorithm would use a population, and iteratively fill it with new solutions
obtained from mutation of previously explored individuals.

The target function explored in this example corresponds to the [Rastrigin function](https://en.wikipedia.org/wiki/Rastrigin_function), a classical benchmark problem for optimisation algorithms.
We translate this optimisation problem into a Quality-Diversity benchmark by defining `k` features corresponding to the first `k` parameters of the genomes of the evaluated individuals.

Here is a plot of the resulting grid of elites:
![Example of result](.description/performancesGrid.png)


### Examples
A number of examples are provided in the `examples` directory [here](https://gitlab.com/leo.cazenille/qdpy/tree/master/examples).
For now, most of these examples pertain to the illumination of the Rastrigin function in a way similar as to what was described in the previous sections, but using a collection of different techniques.




## Documentation
A complete documentation will be available on readthedocs.org.



## Citing

```bibtex
@misc{qdpy
    title = {QDPY: A Python framework for Quality-Diversity},
    author = {Cazenille, L.},
    year = {2019},
    publisher = {GitLab},
    journal = {GitLab repository},
    howpublished = {\url{https://gitlab.com/leo.cazenille/qdpy}},
}
```


## License

`qdpy` is distributed under the LGPLv3 license. See [LICENSE](LICENSE) for details.

