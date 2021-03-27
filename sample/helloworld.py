# -*- coding: utf-8 -*-
import bwiki


if __name__ == "__main__":
    bwiki.set_config_path('../config.json')
    token = bwiki.Token()
    token.get_token()
    print(bwiki.api.Checktoken(
        type='csrf'
    ).send())
