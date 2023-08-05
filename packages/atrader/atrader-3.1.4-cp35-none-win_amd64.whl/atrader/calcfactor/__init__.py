# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:39:04 2018

@author: kunlin.l
"""

import numpy as np
import pandas as pd

import atrader.enums as enums
from atrader.setting import get_setting, get_support, set_setting, get_version
# noinspection PyUnresolvedReferences
from atrader.tframe.sysclsbase import smm
# noinspection PyUnresolvedReferences
from atrader.tframe.sysclsbase import gv
# noinspection PyUnresolvedReferences
from atrader.tframe.utils.argchecker import apply_rule, verify_that
from atrader.tframe import clear_cache
from atrader.tframe.snapshot import ContextFactor

# noinspection PyUnresolvedReferences
from atrader.api.bpfactor import *
# noinspection PyUnresolvedReferences
from atrader.api.history import *
# noinspection PyUnresolvedReferences
from atrader.api.regfuncs import *
from atrader.api import bpfactor as factors_api, history as history_api, regfuncs as reg_api

__all__ = [
    'np',
    'pd',
    'enums',
    'set_setting',
    'get_setting',
    'get_support',
    'get_version',
    'clear_cache',
    'run_factor',
    'ContextFactor',
    'get_auto_value',
    *factors_api.__all__,
    *history_api.__all__,
    *reg_api.__all__,
    # *fundamental_api.__all__
]


@smm.force_mode(gv.RUNMODE_CONSOLE)
@smm.force_phase(gv.RUMMODE_PHASE_DEFAULT)
@apply_rule(verify_that('factor_name').is_instance_of(str),
            verify_that('file_path').is_exist_path(),
            verify_that('targets').is_instance_of(str),
            verify_that('begin_date').is_valid_date(),
            verify_that('end_date').is_valid_date(),
            verify_that('fq').is_in((enums.FQ_BACKWARD,
                                     enums.FQ_FORWARD,
                                     enums.FQ_NA)))
def run_factor(factor_name='', file_path='.', targets='', begin_date='', end_date='', fq=enums.FQ_NA):
    raise NotImplementedError('暂时不支持')
    config = {
        'entry': {
            'factor_name': factor_name,
            'file_path': file_path,
            'targets': targets,
            'begin_date': begin_date,
            'end_date': end_date,
            'fq': fq,
        }
    }

    from .main import main_run_factor
    return main_run_factor(config)


@smm.force_phase(gv.RUMMODE_PHASE_CALC_FACTOR)
@apply_rule(verify_that('length').is_instance_of(int))
def get_auto_value(length=1):
    from ._calcfactor import _get_auto_value
    return _get_auto_value(length)
