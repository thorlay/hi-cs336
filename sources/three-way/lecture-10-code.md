# L10｜代码讲义 ↔ 完整 Transcript ↔ 教材

这是可执行课堂讲义，使用代码行号而非虚构的 PDF 页码。字幕区间是近似主题定位，嵌套调用可能让文件顺序与讲授顺序不同。全文包含无时间戳续行；未回听音频，也未据此声称 GPU 运行验证。

[固定版本完整讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py) · [教材](../../textbook/10-inference.md) · [总入口](../three-way-audit.md)

| 代码行 | 完整 Transcript 定位 | 教材去向 | 核验说明 |
| --- | --- | --- | --- |
| [1–60](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L1-L60) | 00:00–06:00；总结末尾 | [1. 先把“快”说清楚](../../textbook/10-inference.md#1-先把快说清楚) | 已对照代码讲义、完整字幕与教材；主程序、符号与路线；有损/无损/动态调度分开 |
| [63–97](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L63-L97) | 00:00–12:00 | [1. 先把“快”说清楚](../../textbook/10-inference.md#1-先把快说清楚) | 已对照代码讲义、完整字幕与教材；使用、评估、RL；TTFT、每请求token延迟、总吞吐 |
| [100–115](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L100-L115) | 约 09:00–15:00 | [3. KV cache 容量手算](../../textbook/10-inference.md#3-kv-cache-容量手算) | 已对照代码讲义、完整字幕与教材；B/S/T/D/N/K/H/L 记号与张量收缩 |
| [118–159](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L118-L159) | 约 12:00–24:00 | [4. 为什么 batch 有帮助，但不能解决一切](../../textbook/10-inference.md#4-为什么-batch-有帮助但不能解决一切) | 已对照代码讲义、完整字幕与教材；bf16 GEMM 强度趋向B；295为特定峰值理想阈值 |
| [162–260](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L162-L260) | 约 21:00–36:00 | [2. Prefill 与 decode 的工作不同](../../textbook/10-inference.md#2-prefill-与-decode-的工作不同) | 已对照代码讲义、完整字幕与教材；无缓存立方主项、KV两阶段、MLP与MHA注意力IO模型限定 |
| [263–329](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L263-L329) | 约 30:00–45:00 | [3. KV cache 容量手算](../../textbook/10-inference.md#3-kv-cache-容量手算) | 已对照代码讲义、完整字幕与教材；参数元素数、权重字节、KV字节、理想延迟与Llama配置 |
| [332–368](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L332-L368) | 约 30:00–45:00 | [4. 为什么 batch 有帮助，但不能解决一切](../../textbook/10-inference.md#4-为什么-batch-有帮助但不能解决一切) | 已对照代码讲义、完整字幕与教材；容量、延迟吞吐权衡；最小延迟而非maximum latency |
| [371–446](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L371-L446) | 约 45:00–65:00 | [5. 两类有损节省](../../textbook/10-inference.md#5-两类有损节省) | 已对照代码讲义、完整字幕与教材；GQA/MLA/CLA/local/hybrid/压缩注意力；同batch GQA文字标签错误 |
| [449–487](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L449-L487) | 约 63:00–70:00 | [5. 两类有损节省](../../textbook/10-inference.md#5-两类有损节省) | 已对照代码讲义、完整字幕与教材；量化单位、QAT/PTQ/GPTQ/AWQ；缩放不等于保留全部FP16重要通道 |
| [490–502](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L490-L502) | 约 69:00–72:00 | [5. 两类有损节省](../../textbook/10-inference.md#5-两类有损节省) | 已对照代码讲义、完整字幕与教材；剪枝校准、结构变小与蒸馏修复 |
| [507–550](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L507-L550) | 约 72:00–78:00 | [6. 推测采样为何可以保留目标分布](../../textbook/10-inference.md#6-推测采样为何可以保留目标分布) | 已对照代码讲义、完整字幕与教材；accept min(1,q/p)、归一化残差、全接受时额外采样与变体条件 |
| [553–573](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L553-L573) | 约 78:00–81:00 | [7. Continuous batching 与分页](../../textbook/10-inference.md#7-continuous-batching-与分页) | 已对照代码讲义、完整字幕与教材；iteration调度、attention各序列处理与非attention拼接 |
| [576–611](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_10.py#L576-L611) | 约 81:00–结束 | [7. Continuous batching 与分页](../../textbook/10-inference.md#7-continuous-batching-与分页) | 已对照代码讲义、完整字幕与教材；内/外碎片、逻辑块、精确前缀共享与copy-on-write；入口支撑 |
