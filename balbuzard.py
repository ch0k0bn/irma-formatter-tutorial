#
# Copyright (c) 2013-2014 QuarksLab.
# This file is part of IRMA project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the top-level directory
# of this distribution and at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# No part of the project, including this file, may be copied,
# modified, propagated, or distributed except according to the
# terms contained in the LICENSE file.

from lib.plugins import PluginBase
from lib.irma.common.utils import IrmaProbeType


class BalbuzardFormatterPlugin(PluginBase):

    # =================
    #  plugin metadata
    # =================

    _plugin_name_ = "Balbuzard"
    _plugin_author_ = "Your Name"
    _plugin_version_ = "0.1"
    _plugin_category_ = IrmaProbeType.metadata
    _plugin_description_ = "Balbuzard results Formatter"
    _plugin_dependencies_ = []

    # ===========
    #  Formatter
    # ===========

    @staticmethod
    def can_handle_results(raw_result):
        expected_name = BalbuzardFormatterPlugin.plugin_name
        expected_category = BalbuzardFormatterPlugin.plugin_category
        return raw_result.get('type', None) == expected_category and \
            raw_result.get('name', None) == expected_name

    @staticmethod
    def format(raw_result):
        try:
	    formatted_res = ""
            for (category, value_list) in raw_result['results'].items():
                formatted_res += "{0}:\n".format(category)
                for item in value_list:
                    try:
                        formatted_res += "    {0} ({1})\n".format(item[1], item[0])
                    except UnicodeEncodeError:
                        formatted_res += "    {0} ({1})\n".format(repr(item[1]), item[0])
            raw_result['results'] = formatted_res
            return raw_result
        except Exception as e:
            raw_result['results'] = "Formatter error: {0}".format(e)
            return raw_result
