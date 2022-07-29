rm -rf dist build && python setup.py sdist bdist_wheel && unzip -l dist/*.whl && tar --list -f dist/*.tar.gz
