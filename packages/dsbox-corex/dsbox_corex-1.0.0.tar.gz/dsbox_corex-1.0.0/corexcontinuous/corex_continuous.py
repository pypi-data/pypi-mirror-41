from sklearn import preprocessing
#import primitive
import sys
import os
import corexcontinuous.linearcorex.linearcorex.linearcorex as corex_cont
#import LinearCorex.linearcorex as corex_cont
from collections import defaultdict, OrderedDict
from scipy import sparse
import pandas as pd
import numpy as np
import git

from d3m import utils
import d3m.container as container
import d3m.metadata.hyperparams as hyperparams
import d3m.metadata.params as params
from d3m.metadata.base import PrimitiveMetadata

from d3m.primitive_interfaces.unsupervised_learning import UnsupervisedLearnerPrimitiveBase
from d3m.primitive_interfaces.base import CallResult
#from d3m.primitive_interfaces.params import Params
from d3m.metadata.hyperparams import Uniform, UniformInt, Union, Enumeration

from typing import NamedTuple, Optional, Sequence, Any
import typing

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#from .. import config

Input = container.DataFrame
Output = container.ndarray

class CorexContinuous_Params(params.Params):
    model:typing.Union[corex_cont.Corex, None]
    #fitted: bool
    #training_inputs: Input

    # add support for resuming training / storing model information


class CorexContinuous_Hyperparams(hyperparams.Hyperparams):
    n_hidden = Union(OrderedDict([('n_hidden int' , hyperparams.Uniform(lower = 1, upper = 50, default = 2, q = 1, description = 'number of hidden factors learned')),
        ('n_hidden pct' , hyperparams.Uniform(lower = 0, upper = .50, default = .2, q = .05, description = 'number of hidden factors as percentage of # input columns'))]), 
        default = 'n_hidden pct')


class CorexContinuous(UnsupervisedLearnerPrimitiveBase[Input, Output, CorexContinuous_Params, CorexContinuous_Hyperparams]):  #(Primitive):
    
    """
    Return components/latent factors that explain the most multivariate mutual information in the data under Linear Gaussian model. For comparison, PCA returns components explaining the most variance in the data.  Serves as DSBox 'wrapper' for https://github.com/gregversteeg/linearcorex"
    """
    metadata = PrimitiveMetadata({
      "schema": "v0",
      "id": "d2d4fefc-0859-3522-91df-7e445f61a69b",
      "version": "1.0.0",
      "name": "CorexContinuous",
      "description": "Return components/latent factors that explain the most multivariate mutual information in the data under Linear Gaussian model. For comparison, PCA returns components explaining the most variance in the data.",
      "python_path": "d3m.primitives.dsbox.CorexContinuous",
      "original_python_path": "corexcontinuous.corex_continuous.CorexContinuous",
      "source": {
            "name": "ISI",
            "contact": 'mailto:brekelma@usc.edu',
            "uris": [ 'https://github.com/brekelma/dsbox_corex' ]
            },
      "installation":
            {
             'type': 'PIP', 
             'package_uri': 'git+https://github.com/brekelma/dsbox_corex.git@7381c3ed2d41a8dbe96bbf267a915a0ec48ee397#egg=dsbox-corex'#+ str(git.Repo(search_parent_directories = True).head.object.hexsha) + '#egg=dsbox-corex'
            }
        ,
      "algorithm_types": ["EXPECTATION_MAXIMIZATION_ALGORITHM"],
      "primitive_family": "FEATURE_CONSTRUCTION",
      "preconditions": ["NO_MISSING_VALUES", "NO_CATEGORICAL_VALUES"],
      "hyperparams_to_tune": ["n_hidden"]
    })
    #  "effects": [],

    #def __init__(self, n_hidden : Any = None, max_iter : int = 10000, 
    def __init__(self, *, hyperparams : CorexContinuous_Hyperparams) -> None: #, random_seed : int =  0, docker_containers: typing.Dict[str, DockerContainer] = None
        # Additional Corex Parameters set to defaults:  see github.com/gregversteeg/LinearCorex
        
        #tol : float = 1e-5, anneal : bool = True, discourage_overlap : bool = True, gaussianize : str = 'standard',  
        #gpu : bool = False, verbose : bool = False, seed : int = None, **kwargs) -> None:
        
        super().__init__(hyperparams = hyperparams)# random_seed = random_seed, docker_containers = docker_containers)
        


    def fit(self, *, timeout: float = None, iterations : int = None) -> CallResult[None]:
        if self.fitted:
            return
        if not hasattr(self, 'training_inputs'):
            raise ValueError("Missing training data.")

        self._fit_transform(self.training_inputs, timeout, iterations)
        self.fitted = True
        # add support for max_iter / incomplete
        return CallResult(None, True, self.max_iter)

    def produce(self, *, inputs : Input, timeout : float = None, iterations : int = None) -> CallResult[Output]: 

        self.columns = list(inputs)
        X_ = inputs[self.columns].values 
    	
        if iterations is not None:
            self.max_iter = iterations
        else:
            self.max_iter = 10000

        if not self.fitted:
            raise ValueError('Please fit before calling produce')

        self.latent_factors = self.model.transform(X_)

        return CallResult(self.latent_factors, True, self.max_iter)

    def _fit_transform(self, inputs : Input, timeout: float = None, iterations : int = None) -> Sequence[Output]:
        
        self.columns = list(inputs)
        X_ = inputs[self.columns].values

        if iterations is not None:
            self.max_iter = iterations
        else:
            self.max_iter = 10000

        if isinstance(self.hyperparams['n_hidden'], int):
            self.n_hidden = self.hyperparams['n_hidden']
        elif isinstance(self.hyperparams['n_hidden'], float):
            self.n_hidden = max(1,int(self.hyperparams['n_hidden']*len(self.columns)))

        if not hasattr(self, 'model') or self.model is None:
            _stdout = sys.stdout
            null = open(os.devnull,'wb')
            sys.stdout = null
            self.model = corex_cont.Corex(n_hidden= self.n_hidden, max_iter = self.max_iter)
            sys.stdout = _stdout

        self.latent_factors = self.model.fit_transform(X_)
        self.fitted = True
        return self.latent_factors

    def set_training_data(self, *, inputs : Input, outputs : Output) -> None:
        self.training_inputs = inputs
        self.fitted = False

    def get_params(self) -> CorexContinuous_Params:
        return CorexContinuous_Params(model = self.model)

    def set_params(self, *, params: CorexContinuous_Params) -> None:
        self.model = params['model']
        #self.fitted = params.fitted
        #self.training_inputs = params.training_inputs


    def _annotation(self):
        if self._annotation is not None:
            return self._annotation
        self._annotation = Primitive()
        self._annotation.name = 'CorexContinuous'
        self._annotation.task = 'FeatureExtraction'
        self._annotation.learning_type = 'UnsupervisedLearning'
        self._annotation.ml_algorithm = ['Dimension Reduction']
        self._annotation.tags = ['feature_extraction', 'continuous']
        return self._annotation

    def _get_feature_names(self):
    	return ['CorexContinuous_'+ str(i) for i in range(self.hyperparams['n_hidden'])]

