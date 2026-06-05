import os
import sys

import pynvim

_PIPE_PATH = "/tmp/hotmic.pipe"


def send_command(cmd: str):
    if not os.path.exists(_PIPE_PATH):
        print("hotmic is not running. Start it with: hotmic listen", file=sys.stderr)
        sys.exit(1)
    with open(_PIPE_PATH, "w") as f:
        f.write(cmd + "\n")


@pynvim.plugin
class HotmicPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.commands_map = {
            "save_duration": "save {} --name {}",
            "save_between_marks": "save --between-marks",
            "mark": "mark {}",
            "transcribe": "transcribe {}",
            "summarize": "summarize {}",
        }

    @pynvim.command("HotmicSaveDuration", nargs="+")
    def save_duration(self, args):
        send_command(self.commands_map["save_duration"].format(*args))

    @pynvim.command("HotmicSaveBetweenMarks", nargs="0")
    def save_between_marks(self, args):
        send_command(self.commands_map["save_between_marks"])

    @pynvim.command("HotmicMark", nargs="1")
    def mark(self, args):
        send_command(self.commands_map["mark"].format(*args))

    @pynvim.command("HotmicTranscribe", nargs="1")
    def transcribe(self, args):
        send_command(self.commands_map["transcribe"].format(*args))

    @pynvim.command("HotmicSummarize", nargs="1")
    def summarize(self, args):
        send_command(self.commands_map["summarize"].format(*args))

