from ansible_runner.runners import get_playbook_shell, run_playbook


fake_play_inputs = {'playbook': 'play.yml', 'limit': 'group:&subgroup', 'extra_vars': 'foo=bar foo2=bar2'}
fake_inputs_injested = [
    'ansible-playbook',
    '--limit',
    "'group:&subgroup'",
    '--extra-vars',
    "'foo=bar foo2=bar2'",
    'play.yml']


def test_command_construction():
    cmd = get_playbook_shell(**fake_play_inputs)
    assert cmd == fake_inputs_injested


def test_arg_passed_correctly():
    cp = run_playbook(**fake_play_inputs)
    assert cp.args == fake_inputs_injested
