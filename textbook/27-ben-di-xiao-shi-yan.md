# 本地小实验

## 实验 0：Transformer 参数与权重核算

只依赖 Python 3 标准库，无需下载模型或数据：

```bash
python3 labs/resource_accounting.py
python3 labs/resource_accounting.py --vocab-size 32000 --layers 12 --d-model 768 --d-ff 3072 --tokens 100000000 --tied
```

模型假设是无 bias、标准多头注意力、普通两层 MLP；忽略 norm 与位置参数。输出参数估算、BF16 权重容量与粗略训练 FLOPs。权重容量不等于训练峰值显存；`6ND` 也不是长上下文场景的精确成本。

建议手算 `V=100, L=2, d=8, f=32`。不共享权重时结果应为 3136 个参数，共享后为 2336。

## 下一步实验（待实现）

- BPE 小语料统计与编码往返。
- 因果 attention 的形状与掩码检查。
- 小数据集过拟合和学习率曲线。
- CUDA 环境下的 attention 基线、profiling 与优化。

所有测量使用[实验模板](28-shi-yan-ji-lu.md)，不要把估算值填成实际测量值。
