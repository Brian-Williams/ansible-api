import shlex
from subprocess import run, PIPE, CompletedProcess
from typing import List


PARAM_NAMES = {'limit': '--limit',
               'extra_vars': '--extra-vars'}


def get_playbook_shell(playbook: str, *, limit: str=None, extra_vars: str=None) -> List[str]:
    parameters = []
    for input in ['limit', 'extra_vars']:
        if locals()[input] is not None:
            parameters += [PARAM_NAMES[input]] + [shlex.quote(locals()[input])]
    return ['ansible-playbook'] + parameters + [playbook]


def run_playbook(playbook, *args, _cwd="/etc/ansible/", **kwargs) -> CompletedProcess:
    """Run a playbook and return a completed process"""
    execution_opts = get_playbook_shell(playbook, *args, **kwargs)
    cp = run(execution_opts, cwd=_cwd, stdout=PIPE, stderr=PIPE)
    return cp
