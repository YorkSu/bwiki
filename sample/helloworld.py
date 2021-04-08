# -*- coding: utf-8 -*-
import bwiki


if __name__ == "__main__":
    bwiki.init('../config.json')
    print(bwiki.api.Checktoken(
        type='csrf'
    ).send())
