# 数据概览工具
当前支持的功能：基于`Pandas`的DataFrame，生成该DataFrame的表和字段粒度概览，HTML格式。

## 当前功能：
1. 数据表概览
    - 数据表行数，列数，内存大小
    - 各类型数据字段数量

2. 数据字段概览
    - 每个字段的类型，数量，去重后数量，缺失值数量，缺失率等

3. 数据字段详情
    - 每个字段的详细信息

## 在研功能：
1. 导出excel和csv
2. 其他

## 使用示例：
参考`data_overview/Usage.ipynb`文件
```python
import pandas as pd
import data_overview as do # 前提是先要执行：pip install data_overview进行安装

# 载入数据
df = pd.read_csv("./data/test_data.csv", encoding='gb18030')

# 用法：输入df，可导出数据概览
dfo = do.DataOverview(df)
dfo.to_html("./data/report.html") # 导出路径和命名自定义
```