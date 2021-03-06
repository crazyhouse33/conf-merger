import pytest
import pathlib
import os
import sys
root_dir = pathlib.Path(__file__).parent.parent.absolute()
sys.path.append(root_dir / 'src')

test_dir = pathlib.Path(__file__).parent.absolute()
output = test_dir / 'products/result.conf'

exec_cmd = 'python3 {}/src/conf-merger -p {} -b {} -o {} '.format(root_dir, test_dir / 'test-confs/1/linux-kernel', test_dir / 'test-build', output )


config1= 'CONFIG_DQL=y'
config1bis= '# CONFIG_DQL is not set'
config2= 'CONFIG_GLOB=y'
config3= 'CONFIG_LRU_CACHE=y'
comboAll= 'CONFIG_DEBUG_KERNEL=y'
combo13 = 'CONFIG_XZ_DEC_SPARC=y'
combo13bis = '# CONFIG_XZ_DEC_SPARC is not set'

def assert_run(cmd, expected_status):
    print("TEST",cmd)
    ret = os.system(cmd)
    assert os.WEXITSTATUS(ret) == expected_status

def assert_file_match_configs(path, configs):
    with open(path) as f:
        file_confs = map(str.strip,f.readlines())
        file_confs=filter(None,file_confs) # Trashing empty lines
        assert sorted(file_confs) == sorted(configs)

def test_invalid_conf():
    assert_run(exec_cmd + 'bla1 bla2 bla314', 1)

def test_overide_conf():
    assert_run(exec_cmd + 'bla1 bla1bis', 0)
    assert_file_match_configs(output, [config1bis])

    assert_run(exec_cmd + 'bla1bis bla1', 0)
    assert_file_match_configs(output, [config1])

def test_overide_path():
    # 2 overwrite bla1 and bla1-bla3 combo
    exec_cmd2 = 'python3 {}/src/conf-merger -p {} -p {} -b {} -o {} '.format(root_dir, test_dir / 'test-confs/2/linux-kernel', test_dir / 'test-confs/1/linux-kernel', test_dir / 'test-build', output )
    assert_run(exec_cmd2 + 'bla1 bla3', 0)
    assert_file_match_configs(output, [config1bis, config3, combo13bis])

def test_all():
    assert_run(exec_cmd + 'bla1 bla2 bla3', 0)
    assert_file_match_configs(output, [config1, config2, config3,comboAll, combo13])
    
def test_2_simple():
    assert_run(exec_cmd + 'bla1 bla2', 0)
    assert_file_match_configs(output, [config1, config2])

def test_3_combo():
    assert_run(exec_cmd + 'bla1 bla3', 0)
    assert_file_match_configs(output, [config1, config3, combo13])

def test_conf_folder():
    conf_cmd = 'python3 {}/src/conf-merger -p {} -b {} --check '.format(root_dir, root_dir / 'default-confs/linux-kernel', test_dir / 'test-build' )
    assert_run(conf_cmd, 0)

def test_group():
    assert_run(exec_cmd + 'toto', 0)
    assert_file_match_configs(output, [config1, config2])

 
