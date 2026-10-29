# Stanford CS336｜从零构建语言模型 · 中文学习笔记

以用户提供的 **Spring 2026 视频及 Transcript** 为主线，面向有后端、系统或 CS149 基础，希望理解大模型训练与 AI Infrastructure 的自学者。这里记录原创概念解释、作业路线与可复现实验。

## 逐讲详细教材

[GitBook 在线阅读](https://niuniu.gitbook.io/cs336-cong-ling-gou-jian-yu-yan-mo-xing/00-cs336-spring-2026-zhu-jiang-zhong-wen-jiao-cai) · [GitHub 教材目录](textbook/README.md)

已生成 [Spring 2026 中文教材](textbook/README.md)：覆盖现有文字稿的 18 讲，按课程推进顺序直接讲解，章内解释必要背景、符号、推导和完整算例，附自测与逐题推理。L18 缺原始材料，单独标记待补；正文不是逐字稿，尚未逐句对照视频。

## 逐页三方对照

[Slides ↔ 完整 Transcript ↔ 教材总入口](sources/three-way-audit.md)：8 份 PDF 的 496 页、9 讲代码讲义的 110 个段落组、L19 的 11 个文字稿主题区间均有教材去向。18 份文字稿包含全部续行；时间为近似定位，未回听音频。

本地另有三栏阅读器：左侧原始页面/代码，中间完整英文文字稿，右侧中文教材，选择页面会联动定位。需准备本地原材料与页面图，再安装 Python `Markdown` 并运行 `python3 tools/build_three_way_reader.py`；生成文件位于被忽略的 `outputs/three-way-reader/index.html`。原文与页面图留在本地，不进入公共仓库。公式保留 LaTeX，正式阅读可使用 GitBook。

## 从这里开始

1. [8 个阶段的学习路线](study-plan.md)：按产出推进，不强行按周追进度。
2. [课程与官方材料索引](sources/README.md)：核对课程年份和作业版本。
3. [语言模型训练全景](notes/01-training-overview.md)：先理解数据、模型、优化器和评估的关系。
4. [Tokenization 与 BPE](notes/02-tokenization.md)：从文本到 token IDs。
5. [Transformer 与资源核算](notes/03-transformer-accounting.md)：建立形状、参数量与显存的直觉。
6. [五次作业的实践路线](assignments/README.md)。
7. [本地小实验](labs/README.md)与[实验记录模板](templates/experiment-log.md)。

## 学到什么程度算完成

- 能解释并实现 tokenizer、因果语言模型和训练循环。
- 能用参数量、FLOPs、显存与通信量说明训练成本。
- 能通过测量定位瓶颈，并验证 kernel 或分布式训练优化。
- 能设计数据与规模实验，区分训练损失、泛化和下游评估。
- 能解释预训练、SFT、偏好优化与奖励驱动训练之间的联系。

## 主线文字稿与课件

已收到用户提供的 [Spring 2026 Transcript（18 份）](sources/transcripts.md)：L1–L17 与 Dan Fu 嘉宾讲座。已与 [2026 官方课表](https://cs336.stanford.edu/#schedule)核对讲次：Dan Fu 为 L19，L18 Daniel Selsam 的文字稿尚缺。原文保存在本地，已按主题整理为中文教材初版，尚未逐句校对录音。作业已切换为 2026 官网所链接仓库的固定快照；A1 README 仍标 2025 的例外见来源索引。

## 内容状态

| 内容 | 当前状态 |
| --- | --- |
| 学习路线与来源索引 | 已建立 |
| 全景、分词、Transformer 资源核算 | 通用入门初稿，待按 2026 Transcript 扩写 |
| A1–A5 | 已建立实践入口，尚未完成作业 |
| 本地资源核算实验 | 已提供，可用 Python 标准库运行 |
| 逐讲详细教材 | 18 讲中文初版 + L18 材料缺口说明 |

教材覆盖已有 18 讲材料，详细状态与核验边界见[教材说明](sources/textbook-evidence.md)。尚未完成课程作业或 GPU 训练实验。

## 和 CS149 怎样衔接

[CS149 学习仓库](https://github.com/thorlay/cs149)帮助理解并行、局部性、GPU 与通信；CS336 把这些基础放进语言模型训练中。学习 systems 部分时，可以回看 CS149 的 GPU、调度与内存局部性章节。

## 仓库结构

```text
textbook/     逐讲中文详细教材
notes/        入门速读笔记
assignments/  作业路线与完成记录
labs/         独立的小实验
sources/      官方来源、年份与版本
templates/   笔记和实验记录模板
```

[SUMMARY.md](SUMMARY.md) 是阅读目录，`.gitbook.yaml` 已配置好。[GitBook 站点](https://niuniu.gitbook.io/cs336-cong-ling-gou-jian-yu-yan-mo-xing/)已发布当前教材初版；已连接 GitHub 同步。原创教材维护在下列逐讲文件；发布前运行 `python3 tools/sync_gitbook_pages.py` 更新 GitBook 已有页面，保留公开网址。

官方入口：[Spring 2026 课程主页](https://cs336.stanford.edu/)。官方资料归原作者所有；本仓库只链接资料，不批量转载讲义、字幕或数据。课程要求和作业接口以固定版本的官方材料为准。
