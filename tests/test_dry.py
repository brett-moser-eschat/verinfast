import os
from unittest.mock import patch
from pathlib import Path
import shutil

from verinfast.agent import Agent
from verinfast.config import Config
from verinfast.utils.utils import DebugLog

file_path = Path(__file__)
test_folder = file_path.parent.absolute()
results_dir = test_folder.joinpath("results").absolute()


@patch('verinfast.user.__get_input__', return_value='y')
def test_no_config(self):
    try:
        shutil.rmtree(results_dir)
    except Exception as e:
        print(e)
        pass
    os.makedirs(results_dir, exist_ok=True)
    agent = Agent()
    config = Config('./str_conf.yaml')
    config.output_dir = results_dir
    print(agent.config.output_dir)
    agent.config = config
    agent.config.dry = True
    agent.config.shouldUpload = False
    agent.debug = DebugLog(path=agent.config.output_dir, debug=False)
    agent.log = agent.debug.log
    print(agent.debug.logFile)
    agent.scan()
    with open(agent.debug.logFile) as f:
        logText = f.read()
        assert "Error" not in logText
