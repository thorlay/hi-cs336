# CS336 Spring 2026｜逐讲中文教材

这本教材带你从分词与张量计算出发，逐步理解语言模型的结构、训练系统、数据、评估与后训练。每章从问题进入机制，用公式、手算和工程例子建立理解，再通过自测检查能否独立运用。

现有内容包括 L01–L17 和 L19，共 18 讲；L18 的原始材料尚缺，单独保留待补说明。教材以视频文字稿为主线，结合 Spring 2026 官方 slides 与代码编写；引用与校验记录放在参考资料中。

## 建议怎样读

各章遵循课程的推进顺序，必要术语与符号在章内解释。只预设基本 Python、矩阵运算和概率/求导知识，可以独立选读。第一次抓问题和机制，第二次做完整算例与自测，再进入作业；[符号与先修知识](00-prerequisites-and-notation.md)供需要时查阅。类比帮助建立直觉，推导则会说明成立条件；遇到工程结论时，还要结合具体配置理解。

- 系统基础较强：L1–L3 → L5–L8 → L10 → L19，再补 scaling、数据与后训练。
- 模型基础较强：按官方顺序阅读，重点补 L2、L5–L8 的成本与执行模型。
- 完整自学：每章至少完成一个手算和一个失败案例分析，实验记录使用[模板](../templates/experiment-log.md)。

## 逐讲目录

| 讲次 | 教材 | 核心产出 |
| --- | --- | --- |
| L01 | [从“会用模型”到“会造模型”：总览与分词](01-overview-tokenization.md) | 手算 BPE，解释分词的成本 |
| L02 | [把张量、显存和 FLOPs 算明白](02-pytorch-resource-accounting.md) | 核算张量容量、FLOPs 与带宽 |
| L03 | [现代 Transformer：从结构到训练稳定性](03-architectures.md) | 画出 decoder block 与位置旋转 |
| L04 | [长上下文与 MoE：改变计算的组织方式](04-linear-attention-moe.md) | 区分状态压缩与条件计算 |
| L05 | [GPU 怎样工作，FlashAttention 为什么更快](05-gpu-flashattention.md) | 推导在线 softmax 与分块复用 |
| L06 | [从 PyTorch 到 Triton：测量、融合与分块](06-kernels-triton.md) | 设计正确性检查和性能实验 |
| L07 | [多 GPU 的语言：集合通信与三种基本并行](07-distributed-primitives.md) | 理解 collective 与梯度等价性 |
| L08 | [ZeRO、流水线与组合并行：让大模型装得下、跑得快](08-zero-hybrid-parallelism.md) | 制定分片和组合并行方案 |
| L09 | [Scaling laws：把小实验变成大模型决策](09-scaling-laws.md) | 推导预算中的模型/数据折中 |
| L10 | [推理系统：KV cache、量化、推测采样与动态批处理](10-inference.md) | 核算 cache，解释采样与调度 |
| L11 | [规模化训练的细节：WSD、优化器与 μP](11-scaling-practice.md) | 识别超参数迁移的适用范围 |
| L12 | [评估：分数究竟说明模型会做什么](12-evaluation.md) | 为目标任务写评估规则 |
| L13 | [数据从哪里来：从网页到可训练语料](13-data-sources.md) | 追踪来源与处理造成的分布变化 |
| L14 | [数据管线：过滤、MinHash 去重、混合与合成](14-data-processing.md) | 核算去重概率与混合重复率 |
| L15 | [后训练：从模仿示范到优化偏好](15-sft-rlhf-dpo.md) | 理解 SFT、奖励与 DPO |
| L16 | [RLVR 与 GRPO：怎样从可验证结果中学习](16-rlvr-grpo.md) | 分析 GRPO 与可验证奖励的偏差 |
| L17 | [多模态：怎样让语言模型看见图像与视频](17-multimodality.md) | 核算视觉 token 并解释融合 |
| L18 | [Daniel Selsam 嘉宾课：材料待补](18-daniel-selsam-material-gap.md) | 缺原始材料，尚未编写 |
| L19 | [Dan Fu：推理约束如何反过来塑造架构](19-dan-fu-inference-codesign.md) | 连接真实推理、调度与循环架构 |

## 内容与验证边界

公式和算例使用简化模型，正文会注明条件；PyTorch/Triton 部分的伪代码用于解释机制，不声称已经在 GPU 上运行。数值示例使用独立的小检查核算；没有租用算力或执行完整作业。

原始字幕、PDF 与课堂代码保存在本地被忽略的目录，仓库发布原创正文与可追溯索引。[材料快照、转写校正与核验说明](../sources/textbook-evidence.md)记录引用来源和未完成项。
