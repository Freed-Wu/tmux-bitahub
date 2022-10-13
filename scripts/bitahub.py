#!/usr/bin/env python
"""Get bitahub status."""
import sys
from urllib import request

import pandas as pd
from bs4 import BeautifulSoup, FeatureNotFound


def main(resource: str = "", col: str = "GPU_Left"):
    """Get bitahub status.

    :param resource:
    :type resource: str
    :param col:
    :type col: str
    """
    if resource == "":
        try:
            resource = sys.argv[1]
        except IndexError:
            resource = "gtx1080ti"
    with request.urlopen("https://www.bitahub.com/resources/" + resource) as f:
        html = f.read()

    try:
        soup = BeautifulSoup(html, "lxml")
    except FeatureNotFound:
        soup = BeautifulSoup(html, "html.parser")

    df = pd.read_html(str(soup.find("table")))[0]
    ts = df.groupby(col).count().loc[:, "node_id"]
    keys = list(range(8))
    keys.reverse()
    status = dict(zip(keys, [0] * 8))
    status.update(ts.to_dict())
    status.pop(0)
    ret = " ".join([str(k) + ":" + str(v) for k, v in status.items()])
    print(ret)


if __name__ == "__main__":
    main()
