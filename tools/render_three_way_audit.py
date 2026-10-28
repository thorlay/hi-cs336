"""Render explicit human review records; rendering never implies semantic review."""
from pathlib import Path
import json,re
from urllib.parse import quote
from sync_gitbook_pages import CHAPTER_NAMES
ROOT=Path(__file__).resolve().parents[1]
REV='de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e'
PDFS={3:67,4:60,5:55,8:73,9:57,11:58,15:65,16:61}
CODE=[1,2,6,7,10,12,13,14,17]
def slug(s):
    return re.sub(r'[^\w\-\u4e00-\u9fff ]','',s.lower()).replace(' ','-')
def heading(chapter, sec):
    for prefix in ['逐页核验补充：','Transcript 对照补遗：']:
        if sec.startswith(prefix):sec=sec.split('：',1)[1]
    headers=re.findall(r'^#{2,4} (.+)$',chapter.read_text(),re.M)
    matches=[h for h in headers if h==sec or h.startswith(sec)]
    if not matches:raise ValueError((chapter,sec))
    return matches[0]
def main():
    out=ROOT/'sources/three-way';out.mkdir(exist_ok=True)
    index=['# 每页 Slides ↔ 完整 Transcript ↔ 教材','',
      '页码统一使用 PDF 物理页（从 1 开始）；字幕时间是近似定位，不是逐帧校时。视频文字稿是主线，课件帮助校正公式、图表与术语；编者补充均写入教材。', '',
      '每页单独列记录，包括封面、目录、重复构建页和总结。已复核记录由人工填写；提取、渲染、自动搜索均不计为语义复核。完整文字稿包含无时间戳续行；原文保留在本地，不上传公共仓库。尚未回听音频。','',
      '| 讲次 | 课件页数 | 三方复核记录 | 对照入口 |','| --- | --- | --- | --- |']
    total=0
    for n,count in PDFS.items():
        path=out/f'lecture-{n:02}.json'
        rows=json.loads(path.read_text()) if path.exists() else []
        bypage={r['page']:r for r in rows}
        assert len(bypage)==len(rows)
        assert all(1<=p<=count for p in bypage)
        chapter=ROOT/'textbook'/CHAPTER_NAMES[n]
        book=chapter.read_text()
        completed=sum(r.get('review','').startswith('已对照') for r in rows);total+=completed
        parts=[f'# L{n:02}｜逐页三方对照','',f'固定[官方 PDF](https://github.com/stanford-cs336/lectures/blob/{REV}/lecture_{n:02}.pdf)，共 {count} 页。教材：[L{n:02}](../../textbook/{chapter.name})。', '',
            'Transcript：用户原文件 `lecture-%02d.txt`，已用保留全部续行的解析器准备。下表时间为近似范围；“待核验”不表示该页已读或已覆盖。全文指原文件全部正文，不是只抽取带时间戳行。'%n,'',
            '| PDF 页 | 完整 Transcript 定位 | 教材去向 | 核验说明 |','| --- | --- | --- | --- |']
        for page in range(1,count+1):
            row=bypage.get(page)
            if row:
                # Resolve exact heading or an explicitly labeled prefix of an existing heading.
                sec=heading(chapter,row['section'])
                dest=f'../../textbook/{chapter.name}#{slug(sec)}'
                pdfurl=f'https://raw.githubusercontent.com/stanford-cs336/lectures/{REV}/lecture_{n:02}.pdf#page={page}'
                parts.append(f"| [{page}]({pdfurl}) | {row['transcript']} | [{sec}]({dest}) | {row['review']}；{row['note']} |")
            else:parts.append(f'| {page} | 待核验 | 待定位 | 尚未完成三方语义复核 |')
        (out/f'lecture-{n:02}.md').write_text('\n'.join(parts)+'\n')
        index.append(f'| L{n:02} | {count} | {completed}/{count} | [逐页表](three-way/lecture-{n:02}.md) |')
    index+=['',f'目前保存 **{total}/496 页**三方复核记录。完成数来自显式填写的页面记录，不能据提取或生成成功标为“无遗漏”。','',
      '## 没有独立 PDF 的讲次','',
      '以下讲次使用官方课堂代码作为讲义，按可讲授段落与固定版本代码行号建立映射。辅助函数和行政说明单列；代码里的外部链接、图像与排行榜没有全部重新抓取，不能视为外部网页逐项视觉验收。', '',
      '| 讲次 | 已记录段落组 | 对照入口 |','| --- | --- | --- |']
    code_total=0
    for n in CODE:
        rows=json.loads((out/f'lecture-{n:02}-code.json').read_text())
        chapter=ROOT/'textbook'/CHAPTER_NAMES[n]
        parts=[f'# L{n:02}｜代码讲义 ↔ 完整 Transcript ↔ 教材','',
          '这是可执行课堂讲义，使用代码行号而非虚构的 PDF 页码。字幕区间是近似主题定位，嵌套调用可能让文件顺序与讲授顺序不同。全文包含无时间戳续行；未回听音频，也未据此声称 GPU 运行验证。','',
          f'[固定版本完整讲义](https://github.com/stanford-cs336/lectures/blob/{REV}/lecture_{n:02}.py) · [教材](../../textbook/{chapter.name}) · [总入口](../three-way-audit.md)','',
          '| 代码行 | 完整 Transcript 定位 | 教材去向 | 核验说明 |','| --- | --- | --- | --- |']
        last=0
        for r in rows:
            assert r['start']>last and r['end']>=r['start'];last=r['end']
            sec=heading(chapter,r['section'])
            url=f'https://github.com/stanford-cs336/lectures/blob/{REV}/lecture_{n:02}.py#L{r["start"]}-L{r["end"]}'
            dest=f'../../textbook/{chapter.name}#{slug(sec)}'
            parts.append(f'| [{r["start"]}–{r["end"]}]({url}) | {r["transcript"]} | [{sec}]({dest}) | {r["review"]}；{r["note"]} |')
        (out/f'lecture-{n:02}-code.md').write_text('\n'.join(parts)+'\n')
        code_total+=len(rows)
        index.append(f'| L{n:02} | {len(rows)} | [代码段表](three-way/lecture-{n:02}-code.md) |')
    n=19;chapter=ROOT/'textbook'/CHAPTER_NAMES[n]
    rows=json.loads((out/'lecture-19-transcript.json').read_text())
    parts=['# L19｜完整 Transcript ↔ 教材','',
      'Dan Fu 嘉宾课目前没有独立官方 PDF/课堂代码，以下只记录全文与教材的两方对照，不冒充逐页 Slides 核验。时间为近似主题区间，完整文字稿包含原文件全部正文；未回听音频。','',
      '| Transcript 定位 | 教材去向 | 核验说明 |','| --- | --- | --- |']
    for r in rows:
        sec=heading(chapter,r['section'])
        dest=f'../../textbook/{chapter.name}#{slug(sec)}'
        parts.append(f'| {r["transcript"]} | [{sec}]({dest}) | {r["review"]}；{r["note"]} |')
    (out/'lecture-19-transcript.md').write_text('\n'.join(parts)+'\n')
    index+=['',f'9 讲共 **{code_total} 个代码段落组**；L19 另有 [11 个全文主题区间](three-way/lecture-19-transcript.md)。L18 缺原始文字稿与课件，保持未覆盖。','',
      '## 复核口径','',
      '“已对照”表示阅读该页图像/文字，联系完整字幕上下文，并检查教材实际去向；不等于逐字翻译、不保证所有图中数值已独立复算，也不等于音频准确性认证。时间跨度可能覆盖课堂追问或前后回指；课件与口述不一致时，教材记录疑点或给出可验证的校正。','',
      '[Transcript 提取更正与全文进度](transcript-audit.md) · [材料版本与编写说明](textbook-evidence.md)']
    (ROOT/'sources/three-way-audit.md').write_text('\n'.join(index)+'\n')
    print(f'Explicitly reviewed: {total}/496 pages; all 496 rows present.')
if __name__=='__main__':main()
