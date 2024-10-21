"""Get bitahub status."""

from typing import List, Literal
from urllib import request

import pandas as pd
from bs4 import BeautifulSoup, FeatureNotFound

RESOURCE = Literal["titanxp", "gtx1080ti", "rtx3090", "teslav100", "debug"]


def get_gpu_status(resource: RESOURCE = "gtx1080ti") -> str:
    """Get bitahub status.

    :param resource:
    :type resource: Literal["titanxp", "gtx1080ti", "rtx3090", "teslav100", "debug"]
    """
    with request.urlopen(  # nosec: B310
        "https://bitahub.ustc.edu.cn/resources/" + resource
    ) as f:
        html = f.read()
    return get_result(html)


def get_result(html: str, col: str = "GPU_Left") -> str:
    """Get result.

    :param html:
    :type html: str
    :param col:
    :type col: str
    """
    try:
        soup = BeautifulSoup(html, "lxml")
        flavor = "lxml"
    except FeatureNotFound:
        soup = BeautifulSoup(html, "html.parser")
        flavor = "bs4"
    df = pd.read_html(str(soup.find("table")), flavor=flavor)[0]
    ts = df.groupby(col).count().loc[:, "node_id"]
    s = ts.sum()
    number_gpu_max = 8
    num = number_gpu_max + 1
    keys = list(range(num))
    keys.reverse()
    status = dict(zip(keys, [0] * num))
    status.update(ts.to_dict())
    for k in list(status.keys()):
        if k <= 0:
            status.pop(k)
    results: List[str] = []
    for k, v in status.items():
        if v == 0:
            color = "red"
        elif v >= s / num:
            color = "green"
        else:
            color = "yellow"
        result = "#[fg=black]" + str(k) + ":#[fg=" + color + "]" + str(v)
        results += [result]
    return " ".join(results) + "#[fg=default]"
