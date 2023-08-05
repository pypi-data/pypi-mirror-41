[//]: # ( [![PyPI package](https://img.shields.io/pypi/v/test_history_server.svg)](https://pypi.python.org/pypi/test_history_server) )
[//]: # ( [![Test results](https://circleci.com/gh/KarrLab/test_history_server.svg?style=shield)](https://circleci.com/gh/KarrLab/test_history_server) )
[//]: # ( [![Test coverage](https://coveralls.io/repos/github/KarrLab/test_history_server/badge.svg)](https://coveralls.io/github/KarrLab/test_history_server) )
[![Documentation](https://readthedocs.org/projects/test-history-server/badge/?version=latest)](http://docs.karrlab.org/test_history_server)
[![Code analysis](https://api.codeclimate.com/v1/badges/4123f20b28d181e733de/maintainability)](https://codeclimate.com/github/KarrLab/test_history_server)
[![License](https://img.shields.io/github/license/KarrLab/test_history_server.svg)](LICENSE)

# test_history_server
Unit test history report server

## Installation
1. Create a database
2. Install package
  ```
  pip install -e git+https://github.com/KarrLab/test_history_server -t /path/to/web-server/test_history_server
  ```
3. Edit site and database configuration in `/path/to/web-server/test_history_server/test_history_server/site/settings.py`
4. Setup database
  ```
  cd /path/to/web-server/test_history_server/test_history_server/site
  python manage.py makemigrations core
  python manage.py migrate
  ```
5. Edit server configuration in `/path/to/web-server/test_history_server/test_history_server/site/wsgi.py`

## Usage

### Browsing test histories
To browse test histories, open the URL specified by `BASE_URL` in `/path/to/web-server/test_history_server/test_history_server/site/settings.py`.

### Uploading test reports
The following example illustrates how to add test reports to the database:
```
import requests

r = requests.post('<settings.BASE_URL>/rest/submit_report',
      data={
          'token': <test_server_token>,
          'repo_name': <repo_name>,
          'repo_owner': <repo_owner>,
          'repo_branch': <repo_branch>,
          'repo_revision': <repo_revision>,
          'build_num': <build_num>,
          'report_name': <extra textual label for individual reports within build, such as to indicate results from different versions of Python>,
      },
      files={
          'report': </path/to/junit-style-XML-test-report.xml>,
      })

r_json = r.json()

if not r_json['success']:
    raise BuildHelperError('Error uploading report to test history server: {}'.format(r_json['message']))
```

## Documentation

### Python API
Please see the [API documentation](http://docs.karrlab.org/test_history_server).

### REST API
* Endpoint: `<settings.BASE_URL>/rest/submit_report`
* Method: POST
* Arguments:
  * `token` (string): secret token used to authenticate with server
  * `repo_owner` (string): user or organization which owns the GitHub repository
  * `repo_name` (string): the name of the GitHub repository
  * `repo_branch` (string):  the name of the branch of the repository that was tested
  * `repo_revision` (string): the SHA1 key of the revision that was tested
  * `build_num` (integer): the build number that was tested
  * `report_name` (string, optional): textual label for individual reports within build, such as to indicate results from different versions of Python
  * `report` (file): JUnit-style XML test report

## License
The build utilities are released under the [MIT license](LICENSE).

## Development team
This package was developed by [Jonathan Karr](http://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York, USA.

## Questions and comments
Please contact the [Jonathan Karr](http://www.karrlab.org) with any questions or comments.
