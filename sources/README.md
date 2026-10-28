# 官方来源与版本

## 主版本：Spring 2026

按用户指定，以 **Spring 2026 视频版本**为学习主线。官方入口：[2026 课程主页](https://cs336.stanford.edu/) · [官方录播播放列表](https://www.youtube.com/watch?v=JuoVZkPBiKk&list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV) · [用户提供的 Transcript 索引](transcripts.md)。

核验日期：2026-10-27。官方课表中的 L1–L17 主题与用户文字稿文件名对应；Dan Fu 对应 L19，L18 Daniel Selsam 的文字稿尚缺。尚未完成视频与文字稿逐句校对。

编写笔记时以视频讲次和用户文字稿组织内容，使用同年官方课件校对术语、公式与代码。文字稿中的转写错误应结合视频/课件处理；无法确认时保留待核验标记。2025 内容只作为明确注明年份的历史参考，不覆盖 2026 的顺序与要求。

## 逐讲导航

课题按 [2026 官方课表](https://cs336.stanford.edu/#schedule) 整理；材料链接为核验时官网所列入口，未来主分支内容仍可能变化。Transcript 的 L6 文件名另含 XLA，标题细节仍以实际视频内容核对。

| 讲次 | 主题 | 官方材料 | 本地 Transcript |
| --- | --- | --- | --- |
| L01 | 总览与分词 | [课件/代码](https://cs336.stanford.edu/lectures/?trace=lecture_01) | `lecture-01.txt` |
| L02 | PyTorch（einops）与资源核算 | [课件/代码](https://cs336.stanford.edu/lectures/?trace=lecture_02) | `lecture-02.txt` |
| L03 | 架构与超参数 | [课件/代码](https://github.com/stanford-cs336/lectures/blob/main/lecture_03.pdf) | `lecture-03.txt` |
| L04 | Attention 替代方案与 MoE | [课件/代码](https://github.com/stanford-cs336/lectures/blob/main/lecture_04.pdf) | `lecture-04.txt` |
| L05 | GPU 与 TPU | [课件/代码](https://github.com/stanford-cs336/lectures/blob/main/lecture_05.pdf) | `lecture-05.txt` |
| L06 | Kernel 与 Triton | [课件/代码](https://cs336.stanford.edu/lectures/?trace=lecture_06) | `lecture-06.txt` |
| L07 | 并行训练（一） | [课件/代码](https://cs336.stanford.edu/lectures/?trace=lecture_07) | `lecture-07.txt` |
| L08 | 并行训练（二） | [课件/代码](https://github.com/stanford-cs336/lectures/blob/main/lecture_08.pdf) | `lecture-08.txt` |
| L09 | Scaling laws（一） | [课件/代码](https://github.com/stanford-cs336/lectures/blob/main/lecture_09.pdf) | `lecture-09.txt` |
| L10 | 推理 | [课件/代码](https://cs336.stanford.edu/lectures/?trace=lecture_10) | `lecture-10.txt` |
| L11 | Scaling laws（二） | [课件/代码](https://github.com/stanford-cs336/lectures/blob/main/lecture_11.pdf) | `lecture-11.txt` |
| L12 | 评估 | [课件/代码](https://cs336.stanford.edu/lectures/?trace=lecture_12) | `lecture-12.txt` |
| L13 | 数据来源与数据集 | [课件/代码](https://cs336.stanford.edu/lectures/?trace=lecture_13) | `lecture-13.txt` |
| L14 | 数据过滤、去重、混合与合成数据 | [课件/代码](https://cs336.stanford.edu/lectures/?trace=lecture_14) | `lecture-14.txt` |
| L15 | Mid/post-training | [课件/代码](https://github.com/stanford-cs336/lectures/blob/main/lecture_15.pdf) | `lecture-15.txt` |
| L16 | Post-training：RLVR | [课件/代码](https://github.com/stanford-cs336/lectures/blob/main/lecture_16.pdf) | `lecture-16.txt` |
| L17 | 多模态 | [课件/代码](https://cs336.stanford.edu/lectures/?trace=lecture_17) | `lecture-17.txt` |
| L18 | 嘉宾：Daniel Selsam | 官网未列独立材料 | **未提供** |
| L19 | 嘉宾：Dan Fu | 官网未列独立材料 | `guest-dan-fu.txt` |

## 当前作业快照

下面固定了核验时 2026 官方课程页所链接仓库的默认分支提交，后续学习使用这些提交以保证可复现。它们是仓库快照，不是官方统一 release。

**A1 年份例外：** 2026 官网链接的 A1 README 标题仍为 “Spring 2025”；这里按 2026 官网的实际入口使用并注明标题差异，不把它说成已核验的独立 2026 发行版。A2–A5 的 README 标题均标注 Spring 2026。

| 作业 | 固定来源 | 提交 | README 年份 |
| --- | --- | --- | --- |
| A1 | [assignment1-basics](https://github.com/stanford-cs336/assignment1-basics/tree/a158843b20107949f1a8d7df1b05cd33b9166712) | `a158843b20107949f1a8d7df1b05cd33b9166712` | 2025（2026 官网链接） |
| A2 | [assignment2-systems](https://github.com/stanford-cs336/assignment2-systems/tree/ca8bc81a59b70516f7ebb2da4808daade877c736) | `ca8bc81a59b70516f7ebb2da4808daade877c736` | 2026 |
| A3 | [assignment3-scaling](https://github.com/stanford-cs336/assignment3-scaling/tree/03e9372992e913061b9e78b5cfcb62ad8a87de35) | `03e9372992e913061b9e78b5cfcb62ad8a87de35` | 2026 |
| A4 | [assignment4-data](https://github.com/stanford-cs336/assignment4-data/tree/0555bea66369872d912652debf10b115ca0688c8) | `0555bea66369872d912652debf10b115ca0688c8` | 2026 |
| A5 | [assignment5-alignment](https://github.com/stanford-cs336/assignment5-alignment/tree/c2734a26308710949fe13226960a1e8cece94b7e) | `c2734a26308710949fe13226960a1e8cece94b7e` | 2026 |

## 历史参考与内容状态

[Spring 2025 历史索引](spring2025-reference.md)保留原有提交，供比较版本差异使用。已有三篇笔记是通用概念初稿，尚未按 2026 各讲 Transcript 完整改写，不能视为已经完成的逐讲教材。

原始文字稿仅在本地 `sources/raw/transcripts-spring2026/` 保存；不将原始讲义、字幕或大型数据上传 GitHub。
