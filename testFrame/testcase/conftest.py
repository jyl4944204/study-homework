import os
import signal
import subprocess

import pytest


@pytest.fixture(scope='module',autouse=True)
def record_video():
    cmd = "scrpy --record file.mp4"
    p = subprocess.Popen(cmd,shell=True,stdout = subprocess.PIPE,stderr=subprocess.STDOUT)
    print(p)
    yield
