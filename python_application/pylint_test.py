import os
import pathlib
import subprocess
import unittest
import sys

from python.runfiles import runfiles


class ExampleTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.maxDiff = None

        super().__init__(*args, **kwargs)

    def test_pylint_entry_point(self):
        rlocation_path = os.environ.get("ENTRY_POINT")
        assert (
            rlocation_path is not None
        ), "expected 'ENTRY_POINT' env variable to be set to rlocation of the tool"

        entry_point = pathlib.Path(runfiles.Create().Rlocation(rlocation_path))
        self.assertTrue(entry_point.exists(), f"'{entry_point}' does not exist")

        proc = subprocess.run(
            [str(entry_point), "./"],
            # check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out_str = proc.stdout.decode("utf-8")
        err_str = proc.stderr.decode("utf-8")
        print(f"OUT: {out_str}")
        print(f"ERR: {err_str}")


if __name__ == "__main__":
    unittest.main()
