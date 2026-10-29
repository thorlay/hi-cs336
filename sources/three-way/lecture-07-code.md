# L07｜代码讲义 ↔ 完整 Transcript ↔ 教材

这是可执行课堂讲义，使用代码行号而非虚构的 PDF 页码。字幕区间是近似主题定位，嵌套调用可能让文件顺序与讲授顺序不同。全文包含无时间戳续行；未回听音频，也未据此声称 GPU 运行验证。

[固定版本完整讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py) · [教材](../../textbook/07-distributed-primitives.md) · [总入口](../three-way-audit.md)

| 代码行 | 完整 Transcript 定位 | 教材去向 | 核验说明 |
| --- | --- | --- | --- |
| [1–74](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py#L1-L74) | 00:00–06:00；总结 72:00–结束 | [1. 多卡解决两个问题](../../textbook/07-distributed-primitives.md#1-多卡解决两个问题) | 已对照代码讲义、完整字幕与教材；层级与主程序；导入/入口是运行支撑，不伪造为幻灯片 |
| [75–206](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py#L75-L206) | 06:00–21:00 | [3. 用两个数组记住通信原语](../../textbook/07-distributed-primitives.md#3-用两个数组记住通信原语) | 已对照代码讲义、完整字幕与教材；逐项核对 broadcast/scatter/gather/reduce/AG/RS/AR/A2A；修正口述 inverse of scatter 重复词 |
| [209–236](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py#L209-L236) | 21:00–36:00 | [1. 多卡解决两个问题](../../textbook/07-distributed-primitives.md#1-多卡解决两个问题) | 已对照代码讲义、完整字幕与教材；硬件数字为具体配置；NVL72 tray 口径按官方资料更正 |
| [239–284](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py#L239-L284) | 36:00–46:00 | [2. Rank、进程组与通信顺序](../../textbook/07-distributed-primitives.md#2-rank进程组与通信顺序) | 已对照代码讲义、完整字幕与教材；后端、原地 AR、独立输出 RS、AG；empty 中数据未初始化 |
| [287–372](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py#L287-L372) | 45:00–55:00 | [4. 通信为什么有启动成本和带宽成本](../../textbook/07-distributed-primitives.md#4-通信为什么有启动成本和带宽成本) | 已对照代码讲义、完整字幕与教材；warmup、设备完成与进程同步；按相同输入字节数比较带宽 |
| [375–436](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py#L375-L436) | 54:00–63:00 | [5. 数据并行：复制模型，划分样本](../../textbook/07-distributed-primitives.md#5-数据并行复制模型划分样本) | 已对照代码讲义、完整字幕与教材；DDP 平均的是梯度；默认一步无 zero_grad 不适合照搬多步 |
| [439–481](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py#L439-L481) | 63:00–69:00 | [6. 张量并行：分一层的矩阵](../../textbook/07-distributed-primitives.md#6-张量并行分一层的矩阵) | 已对照代码讲义、完整字幕与教材；列切分、GELU 后 AG；反向没有实现，非完整训练器 |
| [484–536](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py#L484-L536) | 69:00–75:00 | [7. 流水并行：按深度拆模型](../../textbook/07-distributed-primitives.md#7-流水并行按深度拆模型) | 已对照代码讲义、完整字幕与教材；send/recv 与 microbatch；没有反向或显式通信计算重叠 |
| [540–619](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py#L540-L619) | 03:00–06:00；36:00–46:00 | [2. Rank、进程组与通信顺序](../../textbook/07-distributed-primitives.md#2-rank进程组与通信顺序) | 已对照代码讲义、完整字幕与教材；setup/cleanup、单进程展示替身、固定随机种子和工具函数；辅助代码按一组说明 |
