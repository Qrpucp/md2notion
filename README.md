使用了 [*md2notion*](https://github.com/Cobertos/md2notion) 库，针对个人习惯和 *Typora* 格式做了一些处理。

主要用于公式的转换，图片能否成功上传和网络有关，可能会报 *429 Client Error*，该错误来自底层的 [*notion-py*](https://github.com/jamalex/notion-py) 库，详见 [*Issue #296*](https://github.com/jamalex/notion-py/issues/296)。



```shell
pip install notion md2notion
# fixbug
# [HTTPError - Invalid Input](https://github.com/Cobertos/md2notion/issues/40)
pip install notion-cobertos-fork
pip uninstall notion-cobertos-fork
pip install notion-cobertos-fork
```



上传失败可能由于：

- 使用全局代理
- 网络问题
- 图片名称中带有空格
- 使用了 *notion* 不支持的 *markdown* 格式，比如四级标题
