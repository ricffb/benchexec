# This file is part of BenchExec, a framework for reliable benchmarking:
# https://github.com/sosy-lab/benchexec
#
# SPDX-FileCopyrightText: 2007-2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import benchexec.result as result
import benchexec.tools.template


class Tool(benchexec.tools.template.BaseTool2):
    """
    Tool info for the witness checker (witnesslint)
    (https://github.com/sosy-lab/sv-witnesses)
    """

    def executable(self, tool_locator):
        return tool_locator.find_executable("witnesslint.py")

    def name(self):
        return "witnesslint"

    def determine_result(self, run):
        if run.exit_code.value == 0:
            return result.RESULT_TRUE_PROP
        else:
            return result.RESULT_FALSE_PROP
