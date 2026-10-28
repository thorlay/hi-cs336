# Transcript 逐章覆盖核验

核验日期：2026-10-27。当前为补遗版：8 讲完成本轮全文阅读；10 讲需补查无时间戳续行，整体校验尚未完成。L18 没有材料。

## 进度更正

此前提取只保留带时间戳的行，漏掉了 10 份文件的续行，共 12,134 行。这是提取错误，不是原始字幕必然缺词。已修正提取工具并验证所有正文行都被保留，但重新提取不等于已完成语义复核。

全文阅读的 8 讲为 L01、L02、L03、L04、L06、L09、L10、L19；其余 10 讲在下表明确标待补查。所有现有章节均已加入本轮发现的内容补遗。

寒暄、重复口述、现场操作和临时排行榜不逐字转载；历史例子概括教学作用。补遗含编者的数学澄清与工程边界，不等于讲者原话。未回听录音，不承诺视频信息零遗漏，也不声称 PDF 全页事实审校或完成独立实验。

## 逐章结果

| 讲次 | 本次补充/修正 | 状态 |
| --- | --- | --- |
| [L01](../textbook/01-overview-tokenization.md) | 课程背景、规模迁移限制、五单元/作业目标与自适应计算 | 文字稿已对照；音频未复核 |
| [L02](../textbook/02-pytorch-resource-accounting.md) | 低精度位分配、课堂成本算例、算术强度表、AdaGrad 与检查点边界 | 文字稿已对照；音频未复核 |
| [L03](../textbook/03-architectures.md) | 并行残差、超参数范围、位置方案、z-loss 与 KV 口误 | 文字稿已对照；音频未复核 |
| [L04](../textbook/04-linear-attention-moe.md) | 递推等价条件、DSA 索引成本、路由设计空间、均衡与系统细节 | 文字稿已对照；音频未复核 |
| [L05](../textbook/05-gpu-flashattention.md) | 硬件层级、低精度转换、tile/wave 效应与 FlashAttention 边界 | 续行待补查，完整核验进行中 |
| [L06](../textbook/06-kernels-triton.md) | occupancy 算例、bank conflict、编译与逻辑块/线程区别 | 文字稿已对照；音频未复核 |
| [L07](../textbook/07-distributed-primitives.md) | 拓扑/RDMA、通信带宽口径、autograd 与异步依赖 | 续行待补查，完整核验进行中 |
| [L08](../textbook/08-zero-hybrid-parallelism.md) | ZeRO 生命周期、激活账本、EP 组合与实际配方 | 续行待补查，完整核验进行中 |
| [L09](../textbook/09-scaling-laws.md) | 混合/重复、critical batch、上下游差异与 Chinchilla 拟合分歧 | 文字稿已对照；音频未复核 |
| [L10](../textbook/10-inference.md) | 完整成本模型、跨层 KV、量化/剪枝与分页细节 | 文字稿已对照；音频未复核 |
| [L11](../textbook/11-scaling-practice.md) | 公开 scaling 配方、优化器证据边界、μP 假设 | 续行待补查，完整核验进行中 |
| [L12](../textbook/12-evaluation.md) | 各类基准的目的、裁判偏差、污染路线与基准本身的错误 | 续行待补查，完整核验进行中 |
| [L13](../textbook/13-data-sources.md) | 抓取/格式、数据集演化、来源链与法律口述边界 | 续行待补查，完整核验进行中 |
| [L14](../textbook/14-data-processing.md) | 过滤实例、去重条件、混合外推和合成代码任务 | 续行待补查，完整核验进行中 |
| [L15](../textbook/15-sft-rlhf-dpo.md) | SFT 数据演化、知识/风格纠缠、人工/模型标注与 PPO 桥梁 | 续行待补查，完整核验进行中 |
| [L16](../textbook/16-rlvr-grpo.md) | 组均值/标准差偏差、各家后训练路线与环境漏洞 | 续行待补查，完整核验进行中 |
| [L17](../textbook/17-multimodality.md) | CLIP/SigLIP、各代 VLM、视频与离散生成路线 | 续行待补查，完整核验进行中 |
| L18 | 无原始材料 | 待补 |
| [L19](../textbook/19-dan-fu-inference-codesign.md) | 请求全生命周期、缓存分层、异常行为、megakernel 成本与 Parcae 问答 | 文字稿已对照；音频未复核 |

## 后续核验

逐章读取包含续行的完整文本，复查新增补遗的表述、数字与问答，记录具体时间段；只对真正听不清或有歧义的片段列出回听需求，不能笼统称原材料损坏。

原始文件与校验值见 [Transcript 索引](transcripts.md)，材料范围见 [编写说明](textbook-evidence.md)。
