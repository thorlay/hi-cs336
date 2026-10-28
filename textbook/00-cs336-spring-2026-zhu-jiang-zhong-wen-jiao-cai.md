# CS336 Spring 2026｜逐讲中文教材

以用户提供的视频文字稿为主线，结合同年官方 PDF 与课堂代码，按“问题 → 机制 → 公式 → 算例 → 工程联系 → 自测”的方式重写。适合会写 Python、愿意从张量形状和小例子建立理解的读者。

**范围：18 讲教材初版，另有 L18 的材料缺口说明。** 现有材料为 L1–L17 和 Dan Fu 嘉宾课；这里沿官方课程表将 Dan Fu 编为 L19。正文不是完整逐字翻译，也不声称覆盖全部课堂问答，未逐句对照视频录音。

编写时已通读现有 18 份完整文字稿，结合官方 PDF 和课堂代码检查概念、公式、图表与例子；发现的转写错误、口述与课件分歧，以及容易误读的适用条件，均写入对应章节。阅读时以教材讲解为主，无需先阅读核验表。

## 建议怎样读

第一次读时，先抓每章的问题和机制；第二次亲手做算例与自测，再进入对应作业。遇到公式，先读[符号与先修知识](00-prerequisites-and-notation.md)，对照维度、单位与近似假设。标记为“补充理解”的类比、推导和实验建议是作者解释，不作为讲者原话。

- 系统基础较强：L1–L3 → L5–L8 → L10 → L19，再补 scaling、数据与后训练。
- 模型基础较强：按官方顺序阅读，重点补 L2、L5–L8 的成本与执行模型。
- 完整自学：每章至少完成一个手算和一个失败案例分析，实验记录使用[模板](28-shi-yan-ji-lu.md)。

## 逐讲目录

| 讲次 | 教材 | 核心产出 |
| --- | --- | --- |
| L01 | [从“会用模型”到“会造模型”：总览与分词](02-l01-cong-hui-yong-mo-xing-dao-hui-zao-mo-xing-zong-lan-yu-fen-ci.md) | 手算 BPE，解释分词的成本 |
| L02 | [把张量、显存和 FLOPs 算明白](03-l02-ba-zhang-liang-xian-cun-he-flops-suan-ming-bai.md) | 核算张量容量、FLOPs 与带宽 |
| L03 | [现代 Transformer：从结构到训练稳定性](04-l03-xian-dai-transformer-cong-jie-gou-dao-xun-lian-wen-ding-xing.md) | 画出 decoder block 与位置旋转 |
| L04 | [长上下文与 MoE：改变计算的组织方式](05-l04-zhang-shang-xia-wen-yu-moe-gai-bian-ji-suan-de-zu-zhi-fang-shi.md) | 区分状态压缩与条件计算 |
| L05 | [GPU 怎样工作，FlashAttention 为什么更快](06-l05gpu-zen-yang-gong-zuo-flashattention-wei-shen-me-geng-kuai.md) | 推导在线 softmax 与分块复用 |
| L06 | [从 PyTorch 到 Triton：测量、融合与分块](07-l06-cong-pytorch-dao-triton-ce-liang-rong-he-yu-fen-kuai.md) | 设计正确性检查和性能实验 |
| L07 | [多 GPU 的语言：集合通信与三种基本并行](08-l07-duo-gpu-de-yu-yan-ji-he-tong-xin-yu-san-zhong-ji-ben-bing-xing.md) | 理解 collective 与梯度等价性 |
| L08 | [ZeRO、流水线与组合并行：让大模型装得下、跑得快](09-l08zero-liu-shui-xian-yu-zu-he-bing-xing-rang-da-mo-xing-zhuang-de-xia-pao-de-kuai.md) | 制定分片和组合并行方案 |
| L09 | [Scaling laws：把小实验变成大模型决策](10-l09scaling-laws-ba-xiao-shi-yan-bian-cheng-da-mo-xing-jue-ce.md) | 推导预算中的模型/数据折中 |
| L10 | [推理系统：KV cache、量化、推测采样与动态批处理](11-l10-tui-li-xi-tong-kv-cache-liang-hua-tui-ce-cai-yang-yu-dong-tai-pi-chu-li.md) | 核算 cache，解释采样与调度 |
| L11 | [规模化训练的细节：WSD、优化器与 μP](12-l11-gui-mo-hua-xun-lian-de-xi-jie-wsd-you-hua-qi-yu-p.md) | 识别超参数迁移的适用范围 |
| L12 | [评估：分数究竟说明模型会做什么](13-l12-ping-gu-fen-shu-jiu-jing-shuo-ming-mo-xing-hui-zuo-shen-me.md) | 为目标任务写评估规则 |
| L13 | [数据从哪里来：从网页到可训练语料](14-l13-shu-ju-cong-na-li-lai-cong-wang-ye-dao-ke-xun-lian-yu-liao.md) | 追踪来源与处理造成的分布变化 |
| L14 | [数据管线：过滤、MinHash 去重、混合与合成](15-l14-shu-ju-guan-xian-guolminhash-qu-zhong-hun-he-yu-he-cheng.md) | 核算去重概率与混合重复率 |
| L15 | [后训练：从模仿示范到优化偏好](16-l15-hou-xun-lian-cong-mo-fang-shi-fan-dao-you-hua-pian-hao.md) | 理解 SFT、奖励与 DPO |
| L16 | [RLVR 与 GRPO：怎样从可验证结果中学习](17-l16rlvr-yu-grpo-zen-yang-cong-ke-yan-zheng-jie-guo-zhong-xue-xi.md) | 分析 GRPO 与可验证奖励的偏差 |
| L17 | [多模态：怎样让语言模型看见图像与视频](18-l17-duo-mo-tai-zen-yang-rang-yu-yan-mo-xing-kan-jian-tu-xiang-yu-shi-pin.md) | 核算视觉 token 并解释融合 |
| L18 | [Daniel Selsam 嘉宾课：材料待补](19-l18daniel-selsam-jia-bin-ke-cai-liao-dai-bu.md) | 缺原始材料，尚未编写 |
| L19 | [Dan Fu：推理约束如何反过来塑造架构](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md) | 连接真实推理、调度与循环架构 |

## 内容与验证边界

公式和算例使用简化模型，正文会注明条件；PyTorch/Triton 部分的伪代码用于解释机制，不声称已经在 GPU 上运行。数值示例使用独立的小检查核算；没有租用算力或执行完整作业。

原始字幕、PDF 与课堂代码保存在本地被忽略的目录，仓库发布原创正文与可追溯索引。[材料快照、转写校正与核验说明](21-jiao-cai-cai-liao-yu-bian-xie-shuo-ming.md)记录引用来源和未完成项。
