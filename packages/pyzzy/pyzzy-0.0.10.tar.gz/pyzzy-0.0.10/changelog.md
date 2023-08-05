### v0.0.10

- Fix bad configuration for packaging
- Fix a bad escaped regexp in `tests/test_logs.py`
- Add python 3.4 test for Travis
- Update year in `LICENSE`


### v0.0.9

**Reformat some files (black)**


### v0.0.8

**Add support for travis and codecov**

**Added**
- Support for travis and codecov
- Some docstrings/comments in `pyzzy/data/core.py`

**Modified**
- Test in `tests/test_logs.py`
- Requirements in `tests-requirements.txt`
- Badges in `README.md`


### v0.0.7

**Add minor changes**


### v0.0.6

**Add more tests and enhance coverage**

**Added**
- Several tests functions in all `tests/*.py` files
- Better coverage of code (100%)
- `changelog.md` and `pytest.ini` in project directory

**Modified**
- Handling of `config` argument type is extracted from `pyzzy.logs.init_logging` and added in new function `pyzzy.logs._get_config`
- Predicate matching is extracted from `pyzzy.utils.dispatchers.predicate_dispatch.dispatch` and added in new function `pyzzy.utils.dispatchers.predicate_match`
- Configuration files in `tests/configuration` are now all converted to json
- Variables in `tests/test_data.py` starting with `datas_***` are replaced with `data_***`
- `for/else` codes are more explicit
- `pyzzy.utils.templates.xget` is now called `pyzzy.utils.templates.traverse`
- `tests\test_search_files.py` is renamed to `tests\test_utils.py` and contains more tests

**Fixed**
- Handling of default section inside `pyzzy.data.io_conf.conf2dict`
- Checking if `optionxform` is callable inside `pyzzy.data.io_conf._conf_factory`
- `filename` and `module` extraction in `pyzzy.logs.PzWarningsFormatter.update_record_from_warning`
- Dispatch handling in `pyzzy.utils.dispatchers.predicate_dispatch.dispatch_match`

**Removed**
- `init_logging` and `load_config` from `pyzzy.logs`
- `_in_defaults` from `pyzzy.data.io_conf`
- `exc` variable in `pyzzy.utils.templates.attr` and `pyzzy.utils.templates.item`
- Instance handling in `pyzzy.utils.predicate_dispatch`
- `ncopy` function from `pyzzy.utils.nested`. Redundant with `copy.deepcopy`
- `tests/commons.py`
