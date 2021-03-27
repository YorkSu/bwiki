# BWIKI

B站 MediaWiki API, [BWIKI](https://wiki.biligame.com/)

## 版本

Version 0.1.0

## 安装

```cmd
pip install -r requirements.txt
```

## 配置

修改根目录下的 `./config.json`

```json
{
	"host": "wiki.biligame.com",
	"host2": ".biligame.com",
	"site": "xxxx",  // 这里改成你需要编辑的wiki站点
	"browser": "Edge",  // 获取Cookies的浏览器
    "Cookies": {
        "SESSDATA": ""  // 如果不通过浏览器获取Cookies，需要手动填入该值
    }
}
```

- 本API可自动获取浏览器的 Cookies，目前支持的浏览器有
    - Edge
    - Chrome
- 如果不使用浏览器获取 Cookies，请自行获取 `SESSDATA`，并填到 `./config.json`
