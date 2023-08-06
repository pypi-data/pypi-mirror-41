#!/usr/bin/env python3

import sys

from pocketlint import FalsePositive, PocketLintConfig, PocketLinter

class PykickstartLintConfig(PocketLintConfig):
    def __init__(self):
        PocketLintConfig.__init__(self)

        self.falsePositives = [
            FalsePositive(r"^E1102.*: .*_TestCase.runTest: self.handler is not callable$"),
            FalsePositive(r"^W1113.*: Keyword argument before variable positional arguments list in the definition of __init__ function$"),
            FalsePositive(r"^W0107.*: Unnecessary pass statement$"),
        ]

    @property
    def ignoreNames(self):
        return {"translation-canary"}

if __name__ == "__main__":
    conf = PykickstartLintConfig()
    linter = PocketLinter(conf)
    rc = linter.run()
    sys.exit(rc)
