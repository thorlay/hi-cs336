# L06｜代码讲义 ↔ 完整 Transcript ↔ 教材

这是可执行课堂讲义，使用代码行号而非虚构的 PDF 页码。字幕区间是近似主题定位，嵌套调用可能让文件顺序与讲授顺序不同。全文包含无时间戳续行；未回听音频，也未据此声称 GPU 运行验证。

[固定版本完整讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py) · [教材](../../textbook/06-kernels-triton.md) · [总入口](../three-way-audit.md)

| 代码行 | 完整 Transcript 定位 | 教材去向 | 核验说明 |
| --- | --- | --- | --- |
| [1–36](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L1-L36) | 00:00–03:00；总结末尾 | [1. 正确性模型与性能模型](../../textbook/06-kernels-triton.md#1-正确性模型与性能模型) | 已对照代码讲义、完整字幕与教材；引言、调用顺序、总结与辅助导入 |
| [39–142](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L39-L142) | 00:00–22:00 | [1. 正确性模型与性能模型](../../textbook/06-kernels-triton.md#1-正确性模型与性能模型) | 已对照代码讲义、完整字幕与教材；warp、占用率、bank/coalescing、wave；128线程算例与64线程文字不同 |
| [145–205](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L145-L205) | 约 22:00–30:00 | [2. Benchmark 和 profiler 各回答什么](../../textbook/06-kernels-triton.md#2-benchmark-和-profiler-各回答什么) | 已对照代码讲义、完整字幕与教材；warmup、CUDA event、测量单位 ms 与端到端边界 |
| [207–260](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L207-L260) | 约 27:00–36:00 | [2. Benchmark 和 profiler 各回答什么](../../textbook/06-kernels-triton.md#2-benchmark-和-profiler-各回答什么) | 已对照代码讲义、完整字幕与教材；kernel 表、shape/dtype 选择与采样开销 |
| [263–303](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L263-L303) | 约 30:00–42:00 | [4. 为什么融合 GELU 能省时间](../../textbook/06-kernels-triton.md#4-为什么融合-gelu-能省时间) | 已对照代码讲义、完整字幕与教材；naive/builtin/compiled 同 tanh 近似；融合减少中间流量 |
| [306–390](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L306-L390) | 约 36:00–57:00 | [3. 一个 Triton program 的生命周期](../../textbook/06-kernels-triton.md#3-一个-triton-program-的生命周期) | 已对照代码讲义、完整字幕与教材；Triton program/grid、元素块≠线程数、mask、exp形式tanh边界 |
| [393–485](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L393-L485) | 约 57:00–66:00 | [5. 从逐元素走到行 softmax](../../textbook/06-kernels-triton.md#5-从逐元素走到行-softmax) | 已对照代码讲义、完整字幕与教材；row softmax、-inf补齐、输入列stride限制与读写计数 |
| [488–536](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L488-L536) | 约 66:00–72:00 | [6. 行求和是分块的入门练习](../../textbook/06-kernels-triton.md#6-行求和是分块的入门练习) | 已对照代码讲义、完整字幕与教材；循环tile的向量累加和最后归约；要求行连续布局 |
| [539–677](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L539-L677) | 约 72:00–结束 | [7. 分块 matmul 与 epilogue 融合](../../textbook/06-kernels-triton.md#7-分块-matmul-与-epilogue-融合) | 已对照代码讲义、完整字幕与教材；二维grid、stride、K-loop、FP32累加、ReLU epilogue 与mask |
| [680–745](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py#L680-L745) | 贯穿上述演示；未独立讲授 | [8. 最小调优流程](../../textbook/06-kernels-triton.md#8-最小调优流程) | 已对照代码讲义、完整字幕与教材；输入生成、近似GELU参照、随机allclose与PTX输出工具；不代表已在本机GPU复跑 |
