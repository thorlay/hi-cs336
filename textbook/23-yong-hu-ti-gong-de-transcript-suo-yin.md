# 23 用户提供的 Transcript 索引

导入日期：2026-10-27。来源：用户提供的 `transcripts.zip`，共 18 份 UTF-8 文本。

## 年份与核验状态

本仓库按用户指定，以这批 **Spring 2026 视频/Transcript 为主版本**。已核对 [2026 官方课表](https://cs336.stanford.edu/#schedule)：L1–L17 的主题对应，Dan Fu 为 L19；官方 L18 Daniel Selsam 的文字稿尚未提供。课程年份和讲次对应已核验，字幕准确性和各讲覆盖完整性尚未逐句校验。L1 中课程编号已出现转写错误，使用时需要结合上下文与课件纠正。

[2026 主线来源与作业快照](22-guan-fang-lai-yuan-yu-ban-ben.md)是当前入口；[2025 历史参考](24-spring-2025-li-shi-can-kao.md)保留用于对比。后续教材按 2026 视频顺序组织。

现已据这 18 份文字稿与官方材料生成[逐讲中文教材初版](00-cs336-spring-2026-zhu-jiang-zhong-wen-jiao-cai.md)，采用主题扫描、重点段落抽核与材料交叉检查；**尚未逐句对照录音，也不声称覆盖全部课堂问答**。L18 仍缺材料。

## 文件清单

原文位于本地 `sources/raw/transcripts-spring2026/`，已由 `.gitignore` 排除，不上传 GitHub。末尾时间戳仅用于初步检查，不代表已核验的视频时长。

| 讲次 | 文件名中的主题                   | 本地文件               | 末尾时间戳 |
| -- | ------------------------- | ------------------ | ----- |
| 1  | Overview, Tokenization    | `lecture-01.txt`   | 79:16 |
| 2  | PyTorch (einops)          | `lecture-02.txt`   | 77:19 |
| 3  | Architectures             | `lecture-03.txt`   | 89:07 |
| 4  | Attention Alternatives    | `lecture-04.txt`   | 86:14 |
| 5  | GPUs, TPUs                | `lecture-05.txt`   | 78:31 |
| 6  | Kernels, Triton, XLA      | `lecture-06.txt`   | 86:34 |
| 7  | Parallelism               | `lecture-07.txt`   | 80:54 |
| 8  | Parallelism               | `lecture-08.txt`   | 80:02 |
| 9  | Scaling Laws              | `lecture-09.txt`   | 77:47 |
| 10 | Inference                 | `lecture-10.txt`   | 85:23 |
| 11 | Scaling Laws              | `lecture-11.txt`   | 76:55 |
| 12 | Evaluation                | `lecture-12.txt`   | 78:28 |
| 13 | Data (Sources, Datasets)  | `lecture-13.txt`   | 81:52 |
| 14 | Data                      | `lecture-14.txt`   | 84:37 |
| 15 | MidPost-Training          | `lecture-15.txt`   | 79:46 |
| 16 | Post-Training - RLVR      | `lecture-16.txt`   | 75:42 |
| 17 | Alignment - Multimodality | `lecture-17.txt`   | 77:29 |
| 19 | Guest Lecture — Dan Fu    | `guest-dan-fu.txt` | 71:33 |

缺少 L18（Daniel Selsam）；不得标为已获取或已学习。

## 完整性校验

保存原始文件字节，只将本地文件名规范化。以下 SHA-256 可用于确认后续使用的是同一份文字稿。

```
e1b6160e52e7165ce46a17b1ae474fb472ceda433d192ca40b8d0ce41c1f80d2  lecture-01.txt
6359d1b3e7ae7c71a1b8e5c3c94ac0e24840d41c03291a893a00de7ef2a3b331  lecture-02.txt
59a0952dfcd001d3ca4a1ebec327d341ea879ff0421e9857a415a46eaac52b43  lecture-03.txt
fdc6c42a31618ff2ca664dea6fe75dffb02f99eed10738944d2bb7fbf8c04f30  lecture-04.txt
b47b2a54cc44fee7ee79ac14613fb5469d761422554f0edd8d04800506773c3a  lecture-05.txt
cb55e88a428138b6d9d1ab747499b8e27e84879ccd99579cefcdb4ea1b42655c  lecture-06.txt
3c567fac20dee6d9b55230fa60a20986bdcff957c9681e71256f056eb1f1a34d  lecture-07.txt
dbb12afce75a12ed4b0e425eae64d7c3df461f62a55d18caea3b3a4f74885439  lecture-08.txt
d319ad2200f6c6b827978e8afffacfb8296e882f41e18ad523a46e318dea89d6  lecture-09.txt
5ed7c1fe048f6ee4ed9a42223ba1412e95fe3ee6e189af9689962745972fb047  lecture-10.txt
8964cff53ed7131f8595daf6dafea7fc43c84e8b976a8bb2e48e2b68954d5a3f  lecture-11.txt
438178120fd39db24a585773cbf35984a1c7765fefaf088cbe590687829ec5ed  lecture-12.txt
1a631222ee7f93c65114c4570ad0c09555110b91906dc8e45fa78e635eac623e  lecture-13.txt
ca2943d123c7890719d42c1568a1252034273832a16553c2d425b03786b0cba3  lecture-14.txt
caf70d11a3e3bb17ae8f86415d8bca6f2248588f3149b6b75d51f1f578ea36bc  lecture-15.txt
e60c4e339cd4a71d6a657a016b875c6b5b8d469c538eb4efcd5fb0ae646a994b  lecture-16.txt
daa29793588a7b61883683f4d4d93c4e623865dfe82523de9e1cb2a18068512e  lecture-17.txt
fd11b00cc3d66dff80cae7d159c72a902257ec1bb5a61cfc798a87d07f1f8f05  guest-dan-fu.txt
```
