import lit.formats
import shutil
import os

config.name = "Test suite"
config.test_format = lit.formats.ShTest(True)

config.suffixes = ['.cs', '.test', '.il']

config.test_source_root = os.path.dirname(__file__)
config.test_build_root = os.path.join(config.my_obj_root, 'integration-test')

config.substitutions.append(('%mono', config.mono_bin))
config.substitutions.append(('%mcs', config.mcs_bin))
config.substitutions.append(('%ilasm', config.ilasm_bin))
config.substitutions.append(('%FileCheck', os.path.join(config.llvm_bin_dir, "FileCheck")))

# This is required for testing the nuget package, which happens in the CI.
# If the directory is not found, fallback to the output of "dotnet build"
nuget_tool_installation = os.path.join(config.cilver_src_dir, "local-installation/cilver-cli")
if os.path.isfile(nuget_tool_installation):
    cilver_cli_path = nuget_tool_installation
else:
    cilver_cli_path = os.path.join(config.cilver_bin_dir, "cilver-cli")

config.substitutions.append(('%cilver-cli', cilver_cli_path))

# This is useful if a custom dotnet installation is used.
if os.environ.get('DOTNET_ROOT') is not None:
    config.environment['DOTNET_ROOT'] = os.environ.get('DOTNET_ROOT')

def _clean_test_directory(directory):
    for entry in os.scandir(directory):
        basename = os.path.basename(entry.path)
        if basename == "lit.site.cfg.py":
            continue
        if entry.is_dir():
            shutil.rmtree(entry.path)
        else:
            os.remove(entry.path)

_clean_test_directory(config.test_build_root)

