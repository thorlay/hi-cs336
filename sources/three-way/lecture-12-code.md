# L12｜代码讲义 ↔ 完整 Transcript ↔ 教材

这是可执行课堂讲义，使用代码行号而非虚构的 PDF 页码。字幕区间是近似主题定位，嵌套调用可能让文件顺序与讲授顺序不同。全文包含无时间戳续行；未回听音频，也未据此声称 GPU 运行验证。

[固定版本完整讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py) · [教材](../../textbook/12-evaluation.md) · [总入口](../three-way-audit.md)

| 代码行 | 完整 Transcript 定位 | 教材去向 | 核验说明 |
| --- | --- | --- | --- |
| [1–30](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L1-L30) | 00:00–03:00；75:00–结束 | [1. 从抽象能力到可测指标](../../textbook/12-evaluation.md#1-从抽象能力到可测指标) | 已对照代码讲义、完整字幕与教材；主程序与总结，不把调用语句当 slides 页 |
| [33–57](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L33-L57) | 00:00–06:00 | [1. 从抽象能力到可测指标](../../textbook/12-evaluation.md#1-从抽象能力到可测指标) | 已对照代码讲义、完整字幕与教材；能力、成本、偏好、使用量对应不同目标 |
| [60–105](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L60-L105) | 03:00–18:00 | [2. 交叉熵与 perplexity 要分清](../../textbook/12-evaluation.md#2-交叉熵与-perplexity-要分清) | 已对照代码讲义、完整字幕与教材；PPL/熵与条件 PPL 公式更正；自报概率须有效 |
| [108–152](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L108-L152) | 18:00–33:00 | [3. 考试题有清晰答案，也有边界](../../textbook/12-evaluation.md#3-考试题有清晰答案也有边界) | 已对照代码讲义、完整字幕与教材；MMLU/Pro、GPQA、HLE；Diamond 判据按原论文校正 |
| [155–205](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L155-L205) | 30:00–45:00 | [4. 开放回答怎么比较](../../textbook/12-evaluation.md#4-开放回答怎么比较) | 已对照代码讲义、完整字幕与教材；Arena 比较图、AlpacaEval 长度控制、WildBench rubric |
| [208–254](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L208-L254) | 45:00–54:00 | [5. Agent 分数评估的是整个系统](../../textbook/12-evaluation.md#5-agent-分数评估的是整个系统) | 已对照代码讲义、完整字幕与教材；四类 agent benchmark 与 scaffold；训练材料中的委派不是本任务指令 |
| [257–283](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L257-L283) | 54:00–60:00 | [6. 推理、安全与现实任务](../../textbook/12-evaluation.md#6-推理安全与现实任务) | 已对照代码讲义、完整字幕与教材；ARC-1/2/3 与知识/推理分离的限制 |
| [286–311](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L286-L311) | 60:00–66:00 | [6. 推理、安全与现实任务](../../textbook/12-evaluation.md#6-推理安全与现实任务) | 已对照代码讲义、完整字幕与教材；HarmBench/AIR-Bench、对抗鲁棒性与双重用途背景 |
| [314–335](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L314-L335) | 63:00–69:00 | [6. 推理、安全与现实任务](../../textbook/12-evaluation.md#6-推理安全与现实任务) | 已对照代码讲义、完整字幕与教材；GDPVal/MedHELM/Clio；真实用途与隐私 |
| [338–368](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L338-L368) | 66:00–75:00 | [7. 数据污染会怎样误导判断](../../textbook/12-evaluation.md#7-数据污染会怎样误导判断) | 已对照代码讲义、完整字幕与教材；顺序检测、报告重叠、fresh/private、数据质量与空响应基线 |
| [371–394](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py#L371-L394) | 75:00–结束 | [9. 自测与评估卡片](../../textbook/12-evaluation.md#9-自测与评估卡片) | 已对照代码讲义、完整字幕与教材；评方法、模型或系统须先定义规则；入口为运行支撑 |
