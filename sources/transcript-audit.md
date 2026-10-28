# Transcript 逐章覆盖核验

核验日期：2026-10-27。当前是中间同步版，L01–L17 已逐段阅读可用文字稿并补遗；L19 最后一段仍在核验，L18 没有材料。

## 怎样理解“校验”

- 依时间轴顺序阅读文字稿的全部非空字幕，将概念、推导、实例、限制和实质问答与教材对照。连续字幕仅合并排版，不通过关键词摘要代替阅读。
- 初版确有实质遗漏；在每章新增“Transcript 对照补遗”，保留大致时间范围，并解释口误和有条件的经验结论。
- 寒暄、重复语气词、课堂现场操作和临时排行榜不逐字转载。历史研究/产品例子概括其教学作用，不承诺保存每个数字、每次措辞。
- 文字稿自身存在断句、缺词、听不清与转写错误，尤其 L05、L07、L08、L11–L17；阅读字幕不能恢复原本缺失的信息。未回听录音，不能声称视频信息零遗漏。
- “已对照”表示可读知识主线及本次发现的遗漏已检查/补充，不是逐句翻译、逐页 PDF 事实审校或独立复现实验。补遗中的数学澄清与实现边界属于编者解释。

## 逐章结果

| 讲次 | 本次补充/修正 | 状态 |
| --- | --- | --- |
| [L01](../textbook/01-overview-tokenization.md#transcript-对照补遗) | 课程背景、规模迁移限制、五单元/作业目标与自适应计算 | 文字稿已对照；音频未复核 |
| [L02](../textbook/02-pytorch-resource-accounting.md#transcript-对照补遗) | 低精度位分配、课堂成本算例、算术强度表、AdaGrad 与检查点边界 | 文字稿已对照；音频未复核 |
| [L03](../textbook/03-architectures.md#transcript-对照补遗) | 并行残差、超参数范围、位置方案、z-loss 与 KV 口误 | 文字稿已对照；音频未复核 |
| [L04](../textbook/04-linear-attention-moe.md#transcript-对照补遗) | 递推等价条件、DSA 索引成本、路由设计空间、均衡与系统细节 | 文字稿已对照；音频未复核 |
| [L05](../textbook/05-gpu-flashattention.md#transcript-对照补遗) | 硬件层级、低精度转换、tile/wave 效应与 FlashAttention 边界 | 文字稿已对照；音频未复核 |
| [L06](../textbook/06-kernels-triton.md#transcript-对照补遗) | occupancy 算例、bank conflict、编译与逻辑块/线程区别 | 文字稿已对照；音频未复核 |
| [L07](../textbook/07-distributed-primitives.md#transcript-对照补遗) | 拓扑/RDMA、通信带宽口径、autograd 与异步依赖 | 文字稿已对照；音频未复核 |
| [L08](../textbook/08-zero-hybrid-parallelism.md#transcript-对照补遗) | ZeRO 生命周期、激活账本、EP 组合与实际配方 | 文字稿已对照；音频未复核 |
| [L09](../textbook/09-scaling-laws.md#transcript-对照补遗) | 混合/重复、critical batch、上下游差异与 Chinchilla 拟合分歧 | 文字稿已对照；音频未复核 |
| [L10](../textbook/10-inference.md#transcript-对照补遗) | 完整成本模型、跨层 KV、量化/剪枝与分页细节 | 文字稿已对照；音频未复核 |
| [L11](../textbook/11-scaling-practice.md#transcript-对照补遗) | 公开 scaling 配方、优化器证据边界、μP 假设 | 文字稿已对照；音频未复核 |
| [L12](../textbook/12-evaluation.md#transcript-对照补遗) | 各类基准的目的、裁判偏差、污染路线与基准本身的错误 | 文字稿已对照；音频未复核 |
| [L13](../textbook/13-data-sources.md#transcript-对照补遗) | 抓取/格式、数据集演化、来源链与法律口述边界 | 文字稿已对照；音频未复核 |
| [L14](../textbook/14-data-processing.md#transcript-对照补遗) | 过滤实例、去重条件、混合外推和合成代码任务 | 文字稿已对照；音频未复核 |
| [L15](../textbook/15-sft-rlhf-dpo.md#transcript-对照补遗) | SFT 数据演化、知识/风格纠缠、人工/模型标注与 PPO 桥梁 | 文字稿已对照；音频未复核 |
| [L16](../textbook/16-rlvr-grpo.md#transcript-对照补遗) | 组均值/标准差偏差、各家后训练路线与环境漏洞 | 文字稿已对照；音频未复核 |
| [L17](../textbook/17-multimodality.md#transcript-对照补遗) | CLIP/SigLIP、各代 VLM、视频与离散生成路线 | 文字稿已对照；音频未复核 |
| L18 | 无原始材料 | 待补 |
| L19 | 已读至约 69 分钟；末段待查，尚未加入本轮补遗 | 进行中 |

## 仍需回听的具体风险

- L05：大量连续缺词，硬件型号、精度名称、数值与问答不能完整恢复。
- L07–L08：拓扑、规格和部分问答缺词；不按残句推测配置。
- L11：μP 量级推导多处公式只被部分口述，不能凭字幕还原全部乘数。
- L12–L14：基准、数据集名称/数量和法律背景存在残句；不作为今天的排名或法律结论。
- L15–L17：数据例子、版本规格和问答残缺；保留可核对机制，未恢复每一处细节。

原始文件与校验值见 [Transcript 索引](transcripts.md)，初版与本轮的材料范围见 [编写说明](textbook-evidence.md)。
