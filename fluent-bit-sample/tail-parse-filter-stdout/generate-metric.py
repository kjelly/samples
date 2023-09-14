#!/usr/bin/env python3
import json
import logging

logging.basicConfig(
    filename="a.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

logger.info("workspace cat-image 100")
logger.info(
    json.dumps({"metric": "cat-image", "value": 100, "workspace": "first_workspace"})
)
logger.info(
    json.dumps({"metric": "cat-image", "value": -10, "workspace": "first_workspace"})
)
logger.info(
    json.dumps(
        {
            "bad_metric": "cat-image",
            "value": "not good",
            "workspace": "first_workspace",
        }
    )
)
