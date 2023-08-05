[![Build Status](https://travis-ci.org/istommao/easyxlsx.svg?branch=master)](https://travis-ci.org/istommao/easyxlsx)
[![codecov](https://codecov.io/gh/istommao/easyxlsx/branch/master/graph/badge.svg)](https://codecov.io/gh/istommao/easyxlsx)
[![PyPI](https://img.shields.io/pypi/v/easyxlsx.svg)](https://pypi.python.org/pypi/easyxlsx)
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg?style=plastic)](https://pypi.python.org/pypi/easyxlsx)


# easyxlsx
easy way to use xlsxwriter

## Installation

```shell
pip install easyxlsx
```

## Usage

`Django`
```python
from django.http import HttpResponse

from easyxlsx import ModelWriter


class UserWriter(ModelWriter):
    model = User
    fields = ('username', 'gender', 'age', 'email', 'added_at')


def download_excel(request):
    data = UserWriter(queryset).export()

    response = HttpResponse(data, content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="download.xls"'
    return response

# use StreamingHttpResponse
from django.http.response import StreamingHttpResponse

from easyxlsx import StreamModelWriter

class StreamUserWriter(StreamModelWriter):
    model = User
    fields = ('username', 'gender', 'age', 'email', 'added_at')


def download_excel(request):
    data = StreamUserWriter(queryset).export()

    response = StreamingHttpResponse(data, content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="download.xls"'
    return response
```

`save excel`

```python
from easyxlsx import SimpleWriter


dataset = (
  [1, '无声', 25],
  [2, '星尘', 26],
  [3, '黎明', 27],
)

SimpleWriter(dataset, headers=('编号', '姓名', '年龄'), bookname='demo.xlsx').export()
```

![save excel](resources/screenshots.png)

