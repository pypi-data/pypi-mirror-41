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


"""Module with useful definitions to be used in runtime
"""


import tensorflow as tf
from inferpy.util.wrappers import singleton
import edward as ed




@singleton
class Runtime():
    #def __init__(self):
    tf_run_default = True

    compact_param_str = True


    tf_sess = ed.get_session()
    init_g = tf.global_variables_initializer()
    init_l = tf.local_variables_initializer()
    tf_sess.run(init_g)
    tf_sess.run(init_l)


def get_session():
    """ Get the default tensorflow session """

    return Runtime.tf_sess















