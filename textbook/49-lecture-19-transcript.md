# L19｜完整 Transcript ↔ 教材

Dan Fu 嘉宾课目前没有独立官方 PDF/课堂代码，以下只记录全文与教材的两方对照，不冒充逐页 Slides 核验。时间为近似主题区间，完整文字稿包含原文件全部正文；未回听音频。

| Transcript 定位 | 教材去向 | 核验说明 |
| --- | --- | --- |
| 00:00–09:00 | [1. 从训练完成那一刻开始思考](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#id-1.-cong-xun-lian-wan-cheng-na-yi-ke-kai-shi-si-kao) | 已对照完整文字稿与教材；无独立课件；由服务成本反推研究问题；汽车/马匹等类比保留教学作用，不复述商业传言 |
| 09:00–18:00 | [2. 真实流量是一种分布](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#id-2.-zhen-shi-liu-liang-shi-yi-zhong-fen-bu) | 已对照完整文字稿与教材；无独立课件；请求入口、路由、TTFT/TPOT、prefill/decode、agent 与多轮会话需求 |
| 18:00–24:00 | [请求、缓存与正确性](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#) | 已对照完整文字稿与教材；无独立课件；KV 命中、分离部署与模型输出之外的系统行为 |
| 24:00–30:00 | [请求、缓存与正确性](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#) | 已对照完整文字稿与教材；无独立课件；异常循环、未初始化内容、GPU/DRAM/SSD 缓存层与预取 |
| 30:00–36:00 | [3. Prefill/decode 分离的收益与成本](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#id-3.-prefilldecode-fen-li-de-shou-yi-yu-cheng-ben) | 已对照完整文字稿与教材；无独立课件；大互联域、长请求、命中率感知分流，收益限定实验设置 |
| 36:00–42:00 | [4. 独立 kernel 的边界可能造成浪费](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#id-4.-du-li-kernel-de-bian-jie-ke-neng-zao-cheng-lang-fei) | 已对照完整文字稿与教材；无独立课件；kernel 空隙、任务依赖、预取 KV/输出权重与融合执行 |
| 42:00–48:00 | [6. 参数复用：用循环增加计算深度](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#id-6.-can-shu-fu-yong-yong-xun-huan-zeng-jia-ji-suan-shen-du) | 已对照完整文字稿与教材；无独立课件；Parcae 名称、循环参数共享、敏感性和研究动机；未公开结构猜测不作事实 |
| 48:00–54:00 | [7. 稳定性：谱半径不是“另一种范数”](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#id-7.-wen-ding-xing-pu-ban-jing-bu-shi-ling-yi-zhong-fan-shu) | 已对照完整文字稿与教材；无独立课件；递推分析、非线性简化、谱范数/谱半径与离散稳定性的编者澄清 |
| 54:00–60:00 | [8. 给 scaling 多加一个维度](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#id-8.-gei-scaling-duo-jia-yi-ge-wei-du) | 已对照完整文字稿与教材；无独立课件；固定参数/FLOPs 的比较与参数/数据/循环联合 scaling |
| 60:00–66:00 | [Megakernel 的收益与工程代价](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#) | 已对照完整文字稿与教材；无独立课件；片上循环块是设想；形状/硬件/多GPU/部分融合的工程代价与问答 |
| 66:00–结束 | [Parcae：实验、简化与未知](20-l19dan-fu-tui-li-yue-shu-ru-he-fan-guo-lai-su-zao-jia-gou.md#) | 已对照完整文字稿与教材；无独立课件；量化、workflow、batch表示提取 vs 自回归；初步循环观察和未知解释 |
