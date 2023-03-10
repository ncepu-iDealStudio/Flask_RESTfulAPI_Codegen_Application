#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:main.py
# author:Itsuka
# datetime:2021/8/26 14:33
# software: PyCharm

"""
    this is function description
"""

import os

from .codegenerator import CodeGenerator


def generate_controller_layer(table_dict, settings, session_id, ip):
    """
    Generate Controller layer code
    :return: None
    """

    project_dir = settings.PROJECT_DIR

    # create the controller file
    os.makedirs(controller_dir := os.path.join(project_dir, 'controller'), exist_ok=True)

    generator = CodeGenerator(table_dict)
    generator.controller_codegen(
        controller_dir=controller_dir,
        session_id=session_id,
        ip=ip
    )
    return
