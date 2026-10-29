# 教材材料与编写说明

核验与编写日期：2026-10-27 至 2026-10-28。主版本为 Spring 2026。

## 本轮实际使用的材料

- 用户提供的 18 份 Transcript：[原文件清单与校验值](transcripts.md)。
- 官方 `stanford-cs336/lectures` 固定快照：`de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e`。
- 8 份 PDF，合计 496 页：L3、L4、L5、L8、L9、L11、L15、L16。
- 9 份课堂代码：L1、L2、L6、L7、L10、L12、L13、L14、L17。
- Dan Fu 嘉宾课以 Transcript 为主，补充作者团队关于 ThunderMLA 与 Parcae 的一手资料。

## 本轮逐页与全文复核

[三方对照总入口](three-way-audit.md)包含 8 份 PDF 的 **496/496 页**独立记录，以及 9 份课堂代码的段落/行号映射。现有 18 份文字稿已通读全部正文，包含此前解析漏掉的 12,134 行无时间戳续行。提取错误与修复经过见[全文核验记录](transcript-audit.md)。L19 仅做文字稿↔教材对照，L18 缺材料。

## 阅读与核验方式

PDF 按物理页从 1 开始，逐页读取文本并查看渲染图，联系完整字幕上下文检查公式、图表与教材去向；不是只靠关键词命中计覆盖。每页手工保存核验记录，含封面、重复构建页、总结和课上略过页。代码讲义按可讲授段落阅读，运行辅助与行政内容单列；外链网页与每个嵌入图像没有全部重新抓取，不能称外部页面逐项视觉验收。

核验记录中的时间范围用于回到原文查阅，是近似主题区间，不是逐帧换页时间。教材按知识逻辑重组，段落可能综合多页；表中链接指向实际小节。原始全文保留本地，公共仓库不上传原始字幕与 PDF。本文没有回听全部音频、不宣称逐字零遗漏，也未独立复算每个图表数值或运行所有论文/GPU 实验。

正文中的教学数字、小例子、类比与补充推导为编者解释。课件与口述不一致时，能验证的给出推导或一手来源；其余明确保留疑点。历史模型排名和某个配置的加速比不写成永久、普遍结论。补充的一手资料链接保留在相应概念的正文中。

“教材已形成”和“文字材料已对照”都不表示完成课程作业、跑通 GPU 实验或达到出版级逐句事实审校。

2026-10-28，L02 根据用户再次提供的完整字幕重写为可独立阅读的一章；该副本文字正文与此前 L02 原文件一致。必要训练概念、符号、einops、矩阵反向、资源账本和算例已合入正文，不再依靠核验补遗补齐关键解释。7 段 Python 代码分别在 CPU 上执行通过（PyTorch 2.15.0、einops 0.8.2）；另外检查了矩阵求导、不等大小 microbatch 加权、checkpoint 前后输出/梯度及数值答案。没有进行 GPU 性能测量；随后其余可用讲次也完成了按课堂顺序的独立阅读改写；L02 的代码执行记录只代表该章示例。

## 课堂顺序与独立阅读改写

现有 L01–L17、L19 共 18 讲已按各自 transcript 的问题展开顺序改写；L18 继续保留材料缺口。必要背景、术语和符号在正文首次使用处补充，原来集中在核验补遗中的实质解释移回相应主题。L02 也将前向计算量、计时/MFU、带宽模型放在反向传播之前；L09 先数据学习曲线后预算最优，L13 先获取/使用条件后来源，L15 先数据后目标与算法。

每章只预设基本 Python、矩阵运算和概率/求导知识，增加完整小算例与逐题推理。新增 BPE 示例及 L02 的 7 段完整 Python 示例分别运行通过；新增数值算例、反例与文内目标均已检查，未测 GPU 性能。保留课堂追问、实验条件、课件疑点及不能独立确认的边界；附加基础解释和例子是编者教学内容，不伪装成教师原话。这里的独立阅读不表示从零教授全部数学、跑通完整作业，或给出音频级零遗漏保证。

## 已处理的易错点

| 位置 | 风险 | 本文处理 |
| --- | --- | --- |
| L1 | 课程编号与专有名词转写错误 | 使用官方课程与代码名称 |
| L2 | 将 8 卡总容量误套为完整复制式训练容量 | 明确 53B 是 12 bytes/参数且理想分片的静态上限，另算完整复制与 16 bytes 账本 |
| L3 | RMSNorm 公式提取不完整 | 明确写出均方根中的 1/d |
| L5 | 硬件口述数字与不同型号混用 | 以机制为主，不把 SM 数当通用规格 |
| L9 | 口头交换模型/数据 scaling 指数 | 按课件确认 N、D 的方向；保留近似条件 |
| L12 | 熵、交叉熵与 perplexity 混说 | 明确 PPL=exp(平均负对数似然) |
| L13 | 对使用权限与法律情形的过度概括 | 只保留来源、许可与访问的区分，不作普遍法律判断 |
| L14 | 混合 epoch 上限的单位省略 | 写为 D·p_i ≤ E_max·U_i |
| L16 | 把 std 归一化当无偏 baseline | 分开讨论中心化、缩放与零方差组 |
| L19 | Parcae 被转成多个拼法 | 按作者项目与论文校正 |
| L19 | 谱半径/谱范数、连续/离散稳定性混淆 | 给出明确区分与 −2 的反例 |

## 官方文件快照

| 文件 | 固定来源 | SHA-256 |
| --- | --- | --- |
| `lecture_01.py` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_01.py) | `a7d47339eab889679010e926db8beb79f475a0596243f19bb15dbd69223f67e6` |
| `lecture_02.py` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_02.py) | `f731b3849afc970a062f1fe692d7d80f5952cf82c2a4f6f2803a8fb9a9dabfd6` |
| `lecture_03.pdf` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_03.pdf) | `20a953541b41a099bc69b8d809139a4ccdb2aefedaa13e50c766245fe4b5167e` |
| `lecture_04.pdf` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_04.pdf) | `922da01cee70ed9dc9eef13d8116f1d6f45d663c12e632b3e80954c783bd3ce5` |
| `lecture_05.pdf` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_05.pdf) | `a2d5664a3b5a1f246df2fe58b43189215f29931ec05bde4d8a6af4664f55cafe` |
| `lecture_06.py` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py) | `4be1200d93d1f38963d40d7c46a5be72dd67a230ebf8a48d446f018d5e8fa788` |
| `lecture_07.py` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py) | `7cdec6c6e2b78afd667c98e2826efea637bb076cd926c45b4f404b0528c42e60` |
| `lecture_08.pdf` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_08.pdf) | `4c4d7674b333693f20f328935d84dd8a073362c9725c5e05302b6650751ad4d1` |
| `lecture_09.pdf` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_09.pdf) | `92a5d9e26e65bb0a9d8c79b12ed7ea26d14530bf960dcf44f9ed5fd372f519fa` |
| `lecture_10.py` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py) | `e79acd9115d75f0b8bf4902d97dc41c1f6b5016778321f19c2dc241a90cfe9b9` |
| `lecture_11.pdf` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_11.pdf) | `b2148e683b4020f3fa95f5c95f37be55ebf6b2f57382f4c148517e84bf1df890` |
| `lecture_12.py` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_12.py) | `93e4049c9ee2665a7e5c883fee2c213e2eaa45aa5d452e447b5a15a5f353fd09` |
| `lecture_13.py` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_13.py) | `321fbab635378c275f65c41487119f3b9b171fc0ddef1454a4c607c9db72163b` |
| `lecture_14.py` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_14.py) | `8e0e17f868002f2e8f73afed018b2dd787c0a1b371eec599c44d8dbfe555ae9b` |
| `lecture_15.pdf` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_15.pdf) | `42a4bc02408a96e0b414f789f32780ae1d8461000f872d93aa38c94fe369e862` |
| `lecture_16.pdf` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_16.pdf) | `1a2bea825499f226b1c3fe990606253ad1b4fdbdf2ae90b4d12d7d0c07f2c8b3` |
| `lecture_17.py` | [官方文件](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_17.py) | `d8c3054ecce42fda3d92b4f21677a83d65cb525e8b3fbd4361c079f3cd20da52` |

## 嘉宾课补充来源

- [ThunderMLA：作者团队的融合执行说明](https://hazyresearch.stanford.edu/blog/2025-03-04-thundermla)。
- [Parcae 作者项目页](https://sandyresearch.github.io/parcae/)。
- [Parcae 论文](https://arxiv.org/abs/2604.12946)。

## 尚缺什么

L18 Daniel Selsam 未取得对应文字稿或独立课件，只有材料缺口页，不算已完成教材。现有 18 讲已完成课堂顺序改写，材料复核进度见核验记录；尚未回听视频、逐句双语对齐或执行 GPU 实验。

[返回教材目录](../textbook/README.md)

## 直接教学口吻修订

现有 18 讲正文已改为直接面向读者的讲解。字幕口误、页码导航与逐页核验过程由本目录保留；正文呈现正确概念、完整算例和适用条件，来源入口移至章末。研究报告中的实验结果仍保留配置与不确定性，不改写为作者亲测结果。代码块与独立公式块逐项对比，均保持不变。
