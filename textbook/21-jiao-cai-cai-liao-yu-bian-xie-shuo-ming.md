# 教材材料与编写说明

核验与编写日期：2026-10-27。主版本为 Spring 2026。

## 本轮实际使用的材料

- 用户提供的 18 份 Transcript：[原文件清单与校验值](23-yong-hu-ti-gong-de-transcript-suo-yin.md)。
- 官方 `stanford-cs336/lectures` 固定快照：`de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e`。
- 8 份 PDF，合计 496 页：L3、L4、L5、L8、L9、L11、L15、L16。
- 9 份课堂代码：L1、L2、L6、L7、L10、L12、L13、L14、L17。
- Dan Fu 嘉宾课以 Transcript 为主，补充作者团队关于 ThunderMLA 与 Parcae 的一手资料。

## 本轮逐章复核进度

2026-10-27 已补充 [Transcript 逐章核验记录](30-transcript-audit.md)。8 讲完成本轮全文阅读，10 讲因提取时未合并无时间戳续行，需要补查；现有补遗已同步，但不代表全量核验完成。提取已修正，未回听录音。下方方式描述初版编写。

## 阅读与核验方式

本轮对每份文字稿作时间轴主题扫描与重点段落抽核，结合 PDF 提取文本或课堂代码的主题和机制重写；不是对所有字幕逐句翻译或视频逐秒校对。PDF 的公式提取可能丢失上下标，在线 softmax 与 DPO 等重点公式另作页面视觉核验。未对全部 496 页逐页截图验收，也未声称覆盖全部课堂问答。

每章时间范围用于回到原文查阅，带“约”的边界不是精确章节切点。正文中的教学数字、小例子、类比与补充推导为作者解释。引用课堂经验时保留条件，不把历史排行榜或某个配置的加速倍数写成普遍保证。

所有“已形成初版”均表示已有可阅读正文，不表示完成课程作业、跑通 GPU 实验或达到出版级逐句事实审校。

## 已处理的易错点

| 位置 | 风险 | 本文处理 |
| --- | --- | --- |
| L1 | 课程编号与专有名词转写错误 | 使用官方课程与代码名称 |
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

L18 Daniel Selsam 未取得对应文字稿或独立课件，只有材料缺口页，不算已完成教材。其余章节已有本轮补遗，完整复核进度见核验记录；尚未回听视频、逐句双语对齐或执行 GPU 实验。

[返回教材目录](README.md)
