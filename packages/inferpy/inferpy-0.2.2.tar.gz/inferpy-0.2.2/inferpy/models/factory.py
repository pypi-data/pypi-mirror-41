# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

""" This module implements all the methods for definition of each type of random variable.
 For further details about all the supported distributions,
 see `Guide to Building Probabilistic Models <../notes/guidemodels.html#supported-probability-distributions>`_ .

"""


from inferpy.util import tf_run_wrapper

from inferpy.models.params import *

import six

import inspect

from inferpy.models import RandomVariable





######

CLASS_NAME = "class_name"
PARAMS = "params"
BASE_CLASS_NAME = "base_class_name"
NDIM = "ndim"
IS_SIMPLE="is_simple"
PROPS="properties"


def __add_property(cls, name, call_name = None, from_dist=False, private=True):

    call_name = name if call_name == None else call_name
    call_name = "__"+call_name if private and not from_dist else call_name

    if from_dist:
        @tf_run_wrapper
        def param(self):
            """Distribution parameter for the mean."""

            out = self.dist
            for m in call_name.split("."):
                out = getattr(out, m)

            return out


    else:
        def param(self):
            """Distribution parameter for the mean."""

            return getattr(self, call_name)


    cls.__perinstance = True
    param.__doc__ = "property for " + name
    param.__name__ = name

    setattr(cls, param.__name__, property(param))



def __add_constructor(cls, class_name, base_class_name, params, is_simple):

    def constructor(self,*args, **kwargs):

        param_dist = {}
        args_list = list(args)
        dist = None
        observed = kwargs.get("observed") if kwargs.get("observed") != None else False


        if len(args)+len(kwargs)>0:


            param_dim = kwargs.get("dim")
            param_batch = kwargs.get("batches")

            rep = None

            if param_batch != None:
                rep = inf.replicate(size=np.prod(param_batch))
                rep.__enter__()


            param_list = ParamList(params,args_list,kwargs,is_simple,param_dim=param_dim)

            if not param_list.is_empty():

                param_list.check_params()
                param_dist = param_list.get_reshaped_param_dict()

                ## Build the underliying tf object

                validate_args = kwargs.get("validate_args") if  kwargs.get("validate_args") != None else False
                allow_nan_stats = kwargs.get("allow_nan_stats") if  kwargs.get("allow_nan_stats") != None else True
                name = kwargs.get("name") if kwargs.get("name") != None else "inf/"+class_name


                dist = getattr(ed.models, class_name)(name=name, validate_args= validate_args, allow_nan_stats=allow_nan_stats, **param_dist)


            if rep != None:
                rep.exit()


        super(self.__class__, self).__init__(dist, observed=observed)




    constructor.__doc__ = "constructor for "+class_name
    constructor.__name__ = "__init__"
    setattr(cls, constructor.__name__, constructor)

def __add_repr(cls, class_name, params):

    def repr(self):

        if self.base_object != None:
            s = ", ".join([p+"="+inf.util.np_str(getattr(self,p)) for p in params])


            return "<inferpy.models."+class_name+" "+self.name+", "+s+", shape="+str(self.shape)+" >"
        else:
            return ""


    repr.__doc__ = "__repr__ for "+class_name
    repr.__name__ = "__repr__"
    setattr(cls, repr.__name__, repr)


### general method for defining a random variable class ###
def def_random_variable(var):

    # only the class_name is indicated
    if isinstance(var, six.string_types):
        v = {CLASS_NAME: var}
    else:
        v = var


    # check the name of the encapsulated Edward class
    if not BASE_CLASS_NAME in v:
        v.update({BASE_CLASS_NAME : v.get(CLASS_NAME)})

    # if the parameters (e.g., loc, scale, rate, etc.) are not indicated
    # these are obtained from tf.contrib.distributions
    if not PARAMS in v:

        lst = tf.distributions._allowed_symbols

        if v.get(BASE_CLASS_NAME) in lst:
            init_f = getattr(getattr(tf.contrib.distributions, v.get(BASE_CLASS_NAME)), "__init__")
        else:
            init_f = getattr(getattr(ed.models, v.get(BASE_CLASS_NAME)), "__init__")

        sig = inspect.getargspec(init_f)
        v.update({PARAMS: [x for x in sig.args ]})


    # remove non-specific parameters of the random variable
    v.update({PARAMS: [x for x in v.get(PARAMS) if x not in ['self', 'validate_args', 'allow_nan_stats', 'name', 'dtype']]})


    if not IS_SIMPLE in v:
        v.update({IS_SIMPLE : {}})


    # starts the definition of the new class
    newclass = type(v.get(CLASS_NAME), (RandomVariable,),{})


    # Add the properties
    if not PROPS in v:
        props = {}
        for p in v.get(PARAMS):
            if p not in ['self', 'validate_args', 'allow_nan_stats', 'name', 'dtype']:
                props.update({p:p})

        v.update({PROPS:props})
    for p, prop_call in six.iteritems(v.get(PROPS)):
        __add_property(newclass,p, call_name=prop_call, from_dist=True)


    # Add the constructor
    __add_constructor(newclass, v.get(CLASS_NAME), v.get(BASE_CLASS_NAME), v.get(PARAMS), v.get(IS_SIMPLE))
    __add_repr(newclass, v.get(CLASS_NAME), v.get(PARAMS))

    # set a static list with the name of its parameters
    newclass.PARAMS = v.get(PARAMS)


    globals()[newclass.__name__] = newclass



####

class Normal(RandomVariable):
    def __init__(self, loc=0, scale=1,
                 validate_args=False,
                 allow_nan_stats=True,
                 dim=None, batches=None, observed=False, name="Normal"):
        self.loc = loc
        self.scale = scale


class Beta(RandomVariable):
    def __init__(
            self,
            concentration1=None,
            concentration0=None,
            validate_args=False,
            allow_nan_stats=True,
            observed=False,
            dim=None, batches=None,
            name='Beta'):
        self.concentration1 = concentration1
        self.concentration0 = concentration0



class Exponential(RandomVariable):
    def __init__(
            self,
            rate,
            validate_args=False,
            allow_nan_stats=True,
            observed = False,
            dim = None,
            name='Exponential'):
        self.rate = rate

class Uniform(RandomVariable):
    def __init__(
            self,
            low=None,
            high=None,
            validate_args=False,
            allow_nan_stats=True,
            name='Uniform',
            observed=False,
            dim=None, batches=None):
        self.low = low

class Poisson(RandomVariable):
    def __init__(
            self,
            rate,
            validate_args=False,
            allow_nan_stats=True,
            name='Poisson',
            observed=False,
            dim=None, batches=None):
        self.rate = rate

class Categorical(RandomVariable):
    def __init__(
            self,
            logits=None,
            probs=None,
            validate_args=False,
            allow_nan_stats=True,
            name='Categorical',
            observed=False,
            dim=None, batches=None):
        self.default_logits = logits
        self.default_probs = probs

class Multinomial(RandomVariable):
    def __init__(
            self,
            total_count=None,
            logits=None,
            probs=None,
            validate_args=False,
            allow_nan_stats=True,
            name='Categorical',
            observed=False,
            dim=None, batches=None):
        self.logits = logits
        self.probs = probs
        self.total_count = None

class Dirichlet(RandomVariable):
    def __init__(self,
            concentration,
            validate_args=False,
            allow_nan_stats=True,
            name='Dirichlet',
            observed=False,
            dim=None, batches=None):
        self.concentration=concentration

class Gamma(RandomVariable):
    def __init__(
            self,
            alpha, beta,
            validate_args=False,
            allow_nan_stats=True,
            observed=False,
            dim=None, batches=None,
            name='Gamma'):
        self.alpha = alpha
        self.beta = beta

class InverseGamma(RandomVariable):
    def __init__(
            self,
            alpha, beta,
            validate_args=False,
            allow_nan_stats=True,
            observed=False,
            dim=None, batches=None,
            name='InverseGamma'):
        self.alpha = alpha
        self.beta = beta

class Bernoulli(RandomVariable):
    def __init__(
            self,
            logits=None,
            probs=None,
            validate_args=False,
            allow_nan_stats=True,
            name='Bernoulli',
            observed=False,
            dim=None, batches=None):
        self.default_logits = logits
        self.default_probs = probs

class Laplace(RandomVariable):
    def __init__(self, loc, scale,
                 validate_args=False,
                 allow_nan_stats=True,
                 dim=None, batches=None, observed=False, name="Laplace"):
        self.loc = loc
        self.scale = scale

class MultivariateNormalDiag(RandomVariable):
    def __init__(self,
                 loc=None,
                 scale_diag=None,
                 validate_args=False,
                 allow_nan_stats=True,
                 name="MultivariateNormalDiag"):
        self.loc = loc
        self.scale_diag = scale_diag


####### run-time definition of random variables #########

SIMPLE_VARS = ["Normal","Beta", "Exponential","Uniform", "Gamma", "Laplace",
               {CLASS_NAME : "InverseGamma",
                PARAMS : ['concentration', 'rate', 'self', 'validate_args', 'allow_nan_stats', 'name', 'dtype']},
               {CLASS_NAME : "Poisson",
                PARAMS : ['rate', 'self', 'validate_args', 'allow_nan_stats', 'name', 'dtype']},
               ]


for v in SIMPLE_VARS:
    def_random_variable(v)
    g = globals()



NON_SIMPLE_VARS = [{CLASS_NAME : "Categorical", IS_SIMPLE : {"probs" : False, "logits": False}},
                   {CLASS_NAME: "Multinomial", IS_SIMPLE: {"total_count":True,"probs": False, "logits": False}},
                   {CLASS_NAME: "Dirichlet", IS_SIMPLE: {"concentration": False}},
                   {CLASS_NAME : "Bernoulli", IS_SIMPLE : {"probs" : True, "logits": True}},
                   {CLASS_NAME: "MultivariateNormalDiag",
                    IS_SIMPLE: {"loc": False, "scale_diag": False},
                    PARAMS: ['loc', 'scale_diag'],
                    PROPS:{'loc': 'loc', 'scale_diag': 'scale.diag'}
                    }

                   ]

for v in NON_SIMPLE_VARS:
    def_random_variable(v)


#####

