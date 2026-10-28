# L02｜代码讲义 ↔ 完整 Transcript ↔ 教材

这是可执行课堂讲义，使用代码行号而非虚构的 PDF 页码。字幕区间是近似主题定位，嵌套调用可能让文件顺序与讲授顺序不同。全文包含无时间戳续行；未回听音频，也未据此声称 GPU 运行验证。

[固定版本完整讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py) · [教材](../../textbook/02-pytorch-resource-accounting.md) · [总入口](../three-way-audit.md)

| 代码行 | 完整 Transcript 定位 | 教材去向 | 核验说明 |
| --- | --- | --- | --- |
| [1–68](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L1-L68) | 00:00–06:00；总结末尾 | [1. 先建立“物理账本”](../../textbook/02-pytorch-resource-accounting.md#1-先建立物理账本) | 已对照代码讲义、完整字幕与教材；行政公告、主程序和学习目标；不是额外任务指令 |
| [71–86](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L71-L86) | 00:00–06:00 | [保留课堂的两个端到端估算（00:00–约 04:00）](../../textbook/02-pytorch-resource-accounting.md#保留课堂的两个端到端估算0000约-0400) | 已对照代码讲义、完整字幕与教材；70B/15T/1024 H100 与 12 bytes 静态上限 |
| [89–181](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L89-L181) | 约 04:00–18:00 | [代码讲义核验补充](../../textbook/02-pytorch-resource-accounting.md#代码讲义核验补充) | 已对照代码讲义、完整字幕与教材；tensor rank、精度、AMP 与 NVFP4；名义内存与实际dtype分开 |
| [184–199](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L184-L199) | 约 17:00–21:00 | [1. 先建立“物理账本”](../../textbook/02-pytorch-resource-accounting.md#1-先建立物理账本) | 已对照代码讲义、完整字幕与教材；CPU/GPU 驻留和传输 |
| [202–276](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L202-L276) | 约 18:00–30:00 | [3. 形状是程序的类型说明](../../textbook/02-pytorch-resource-accounting.md#3-形状是程序的类型说明) | 已对照代码讲义、完整字幕与教材；einsum/reduce/rearrange 的维度语义 |
| [279–335](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L279-L335) | 约 28:00–39:00 | [4. 为什么一次矩阵乘法约为 2mnk FLOPs](../../textbook/02-pytorch-resource-accounting.md#4-为什么一次矩阵乘法约为-2mnk-flops) | 已对照代码讲义、完整字幕与教材；FLOPs vs FLOP/s、稠密/稀疏峰值与 MFU |
| [338–431](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L338-L431) | 约 36:00–49:00 | [5. Roofline：算得慢，还是搬得慢](../../textbook/02-pytorch-resource-accounting.md#5-roofline算得慢还是搬得慢) | 已对照代码讲义、完整字幕与教材；ReLU/GELU/点积逐项字节和计算，重叠为理想假设 |
| [434–481](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L434-L481) | 约 45:00–57:00 | [代码讲义核验补充](../../textbook/02-pytorch-resource-accounting.md#代码讲义核验补充) | 已对照代码讲义、完整字幕与教材；GEMV/GEMM、精度与 roofline 上界 |
| [484–556](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L484-L556) | 约 57:00–69:00 | [深入算例与补充理解](../../textbook/02-pytorch-resource-accounting.md#深入算例与补充理解) | 已对照代码讲义、完整字幕与教材；标量梯度、两矩阵反向与 6ND 近似条件 |
| [559–599](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L559-L599) | 约 57:00–69:00，深网络演示回指 | [3. 形状是程序的类型说明](../../textbook/02-pytorch-resource-accounting.md#3-形状是程序的类型说明) | 已对照代码讲义、完整字幕与教材；参数注册与 L 个 D×D 矩阵，实际运行在梯度章节前 |
| [602–715](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L602-L715) | 约 66:00–72:00；训练循环被口头略过 | [代码讲义核验补充](../../textbook/02-pytorch-resource-accounting.md#代码讲义核验补充) | 已对照代码讲义、完整字幕与教材；AdaGrad 状态、参数更新与演示训练循环的标量广播 |
| [718–787](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L718-L787) | 约 72:00–结束 | [7. 显存不足时，两种不同的交换](../../textbook/02-pytorch-resource-accounting.md#7-显存不足时两种不同的交换) | 已对照代码讲义、完整字幕与教材；累积与重计算；L/s+s 空间模型与特定逐层示例分开 |
| [791–856](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py#L791-L856) | 贯穿计时与内存示例，未单独讲授 | [代码讲义核验补充](../../textbook/02-pytorch-resource-accounting.md#代码讲义核验补充) | 已对照代码讲义、完整字幕与教材；工具函数：逻辑字节数不是allocator峰值；GPU峰值表和同步计时 |
