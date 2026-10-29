# L14｜代码讲义 ↔ 完整 Transcript ↔ 教材

这是可执行课堂讲义，使用代码行号而非虚构的 PDF 页码。字幕区间是近似主题定位，嵌套调用可能让文件顺序与讲授顺序不同。全文包含无时间戳续行；未回听音频，也未据此声称 GPU 运行验证。

[固定版本完整讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py) · [教材](../../textbook/14-data-processing.md) · [总入口](../three-way-audit.md)

| 代码行 | 完整 Transcript 定位 | 教材去向 | 核验说明 |
| --- | --- | --- | --- |
| [1–36](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py#L1-L36) | 00:00–03:00；81:00–结束 | [1. 四个步骤分别改变什么](../../textbook/14-data-processing.md#1-四个步骤分别改变什么) | 已对照代码讲义、完整字幕与教材；主程序串联转换/过滤/去重/混合，入口非独立 slides |
| [39–57](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py#L39-L57) | 00:00–06:00 | [2. 转换首先是保真问题](../../textbook/14-data-processing.md#2-转换首先是保真问题) | 已对照代码讲义、完整字幕与教材；HTML 结构丢失、截断 PDF 重抓、OCR 成本 |
| [60–142](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py#L60-L142) | 06:00–22:00 | [3. 过滤是一个目标分布迁移问题](../../textbook/14-data-processing.md#3-过滤是一个目标分布迁移问题) | 已对照代码讲义、完整字幕与教材；目标分布、轻量分类、OpenWebMath 名称、Pareto 保留概率、尺度过滤 |
| [145–175](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py#L145-L175) | 21:00–30:00 | [4. 精确去重：先定义什么叫同一条](../../textbook/14-data-processing.md#4-精确去重先定义什么叫同一条) | 已对照代码讲义、完整字幕与教材；重复层级、匹配策略、删除策略和跨数据集去重 |
| [178–214](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py#L178-L214) | 27:00–33:00 | [4. 精确去重：先定义什么叫同一条](../../textbook/14-data-processing.md#4-精确去重先定义什么叫同一条) | 已对照代码讲义、完整字幕与教材；哈希冲突不能当精确相等；排序非线性时间；C4 删段破坏连贯性 |
| [217–265](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py#L217-L265) | 30:00–39:00 | [5. Jaccard 与 MinHash 的直觉](../../textbook/14-data-processing.md#5-jaccard-与-minhash-的直觉) | 已对照代码讲义、完整字幕与教材；Jaccard=3/5、MinHash 理想随机排列与有限哈希误差 |
| [268–321](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py#L268-L321) | 36:00–49:00 | [6. LSH 怎样避免两两比较](../../textbook/14-data-processing.md#6-lsh-怎样避免两两比较) | 已对照代码讲义、完整字幕与教材；AND/OR 概率、b/r 成本、0.9934 特征阈值不是硬阈值 |
| [324–406](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py#L324-L406) | 48:00–72:00 | [7. 混合权重必须换算成 epoch](../../textbook/14-data-processing.md#7-混合权重必须换算成-epoch) | 已对照代码讲义、完整字幕与教材；50 epoch、UniMax 修正单位、RegMix 外推、simulated epoching 与源内混合 |
| [409–464](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py#L409-L464) | 72:00–结束 | [9. 合成数据从任务设计开始](../../textbook/14-data-processing.md#9-合成数据从任务设计开始) | 已对照代码讲义、完整字幕与教材；OpenThoughts/SWE-smith/Zero/rebench/12M；任务、问题、轨迹分开 |
