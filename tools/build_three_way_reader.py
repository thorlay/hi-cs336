"""Build a local three-column reader; raw course materials never enter tracked output.
Requires Markdown (pip install Markdown), plus prepared local PDF page images.
"""
from pathlib import Path
import json,re,html,sys
from urllib.parse import quote, unquote
import markdown
from prepare_transcript_audit import parse
from render_three_way_audit import PDFS,heading,slug
from sync_gitbook_pages import CHAPTER_NAMES
ROOT=Path(__file__).resolve().parents[1]

def seconds(t):
    a=list(map(int,t.split(':')))
    return sum(v*60**i for i,v in enumerate(a[::-1]))

def main():
    chapters=[]
    for n in list(range(1,18))+[19]:
        chapter=ROOT/'textbook'/CHAPTER_NAMES[n]
        raw=ROOT/'sources/raw/transcripts-spring2026'/('guest-dan-fu.txt' if n==19 else f'lecture-{n:02}.txt')
        records=parse(raw.read_text())
        buckets={}
        for r in records:
            sec=seconds(r['time']);bucket=sec//180*180
            buckets.setdefault(bucket,[]).append(r['text'])
        transcript=[{'seconds':sec,'text':' '.join(body)} for sec,body in buckets.items()]
        assert ' '.join(' '.join(x['text'] for x in records).split())==' '.join(' '.join(x['text'] for x in transcript).split())
        kind='pdf' if n in PDFS else 'transcript' if n==19 else 'code'
        suffix='' if kind=='pdf' else '-transcript' if n==19 else '-code'
        rows=json.loads((ROOT/f'sources/three-way/lecture-{n:02}{suffix}.json').read_text())
        for row in rows:
            row['anchor']=slug(heading(chapter,row['section']))
            found=re.search(r'\d{1,2}:\d{2}(?::\d{2})?',row['transcript'])
            row['seconds']=seconds(found[0]) if found else None
        book_source=re.sub(r'\$\$(.*?)\$\$',lambda m:'<pre class="math">'+html.escape(m[0])+'</pre>',chapter.read_text(),flags=re.S)
        book=markdown.markdown(book_source,extensions=['tables','fenced_code','toc'],extension_configs={'toc':{'slugify':lambda s,sep:slug(s)}})
        def resolve_link(m):
            target=html.unescape(m[1])
            if '://' in target or target.startswith('#'):return m[0]
            raw,sep,anchor=target.partition('#')
            resolved=(chapter.parent/unquote(raw)).resolve()
            url='https://github.com/thorlay/hi-cs336/blob/main/'+quote(resolved.relative_to(ROOT).as_posix())+(sep+anchor if sep else '')
            return 'href="'+html.escape(url,quote=True)+'"'
        book=re.sub(r'href="([^"]+)"',resolve_link,book)
        ids=set(re.findall(r' id="([^"]+)"',book))
        assert all(row['anchor'] in ids for row in rows),(n,'missing rendered section')
        if kind=='pdf':
            assert all((ROOT/f'outputs/three-way-review/lecture_{n:02}/page-{row["page"]:02}.png').exists() for row in rows)
        source='' if kind!='code' else (ROOT/f'sources/raw/official-spring2026/lecture_{n:02}.py').read_text()
        chapters.append(dict(n=n,title=chapter.read_text().splitlines()[0].lstrip('# '),kind=kind,rows=rows,transcript=transcript,book=book,code=source))
    template=r'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>CS336 三方对照阅读器</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f5f4f0;color:#202a30;font:15px/1.65 system-ui,sans-serif}header{padding:14px 22px;background:#133b40;color:white}h1{font-size:20px;margin:0 0 8px}select,button{font:inherit;padding:5px 9px;border:1px solid #b5c6c2;border-radius:5px;background:white;color:#133b40}select{max-width:45vw}button{cursor:pointer}#status{font-size:12px;margin-top:7px;color:#d2e3df}main{display:grid;grid-template-columns:36% 29% 35%;height:calc(100vh - 144px)}section{min-height:0;min-width:0;display:flex;flex-direction:column;border-right:1px solid #d6dcd6}.label{padding:8px 15px;background:#e6ece6;font-weight:650;border-bottom:1px solid #c8d2cb}.pane{min-height:0;overflow:auto;padding:16px;flex:1;scroll-behavior:auto}#slide img{width:100%;background:white}#note{background:#e8f0ea;padding:12px;margin-top:12px;font-size:13px}#transcript p{margin:0 0 15px;padding:8px;border-left:3px solid transparent;font:14px/1.8 Georgia,serif}#transcript p.active{background:#fff0bd;border-color:#bc820b}time{font:600 12px system-ui;color:#316762;display:block}.pane h2{font-size:19px}.pane h3{font-size:16px}.pane a{color:#197069}.pane table{border-collapse:collapse;font-size:12px;max-width:100%;display:block;overflow:auto}th,td{border:1px solid #cdd5ce;padding:6px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px;background:#eaf0e9;padding:10px}blockquote{margin:8px 0;padding-left:12px;border-left:3px solid #a7bfb5}.code-line{display:block;white-space:pre-wrap;font:12px/1.7 ui-monospace,monospace}.code-line.active{background:#fff0bd}.ln{display:inline-block;color:#77867c;width:3.5em;user-select:none}#book .focus{background:#fff0bd}footer{height:28px;padding:3px 20px;font-size:11px;color:#5d7069}@media(max-width:900px){main{grid-template-columns:1fr;height:auto}section{height:65vh}select{max-width:80vw}}
</style><header><h1>CS336 · Slides ↔ 完整 Transcript ↔ 教材</h1><select id="chapter" aria-label="选择讲次"></select> <button id="prev">上一项</button> <select id="item" aria-label="选择页面或代码段"></select> <button id="next">下一项</button><div id="status"></div></header>
<main><section><div class="label" id="source-label">原始课件</div><div class="pane" id="slide"></div></section><section><div class="label">完整英文 Transcript · 含全部续行</div><div class="pane" id="transcript"></div></section><section><div class="label">详细中文教材 · 已定位对应小节</div><div class="pane" id="book"></div></section></main><footer>仅本地阅读；时间是近似主题定位，未回听音频。L18 缺材料；L19 无独立课件。公式保留 LaTeX，正式排版可在 GitBook 阅读。</footer>
<script id="data" type="application/json">__DATA__</script><script>
const DATA=JSON.parse(document.getElementById('data').textContent),$=s=>document.getElementById(s),esc=s=>s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));let current;
function time(s){return `${Math.floor(s/3600).toString().padStart(2,'0')}:${Math.floor(s%3600/60).toString().padStart(2,'0')}:${(s%60).toString().padStart(2,'0')}`}
function selectChapter(){current=DATA[+$('chapter').value];$('item').innerHTML=current.rows.map((r,i)=>`<option value="${i}">${current.kind==='pdf'?'PDF 第 '+r.page+' 页':current.kind==='code'?'代码 '+r.start+'–'+r.end+' 行':r.transcript}</option>`).join('');$('transcript').innerHTML=current.transcript.map(r=>`<p id="t${r.seconds}"><time>${time(r.seconds)}</time>${esc(r.text)}</p>`).join('');$('book').innerHTML=current.book;$('source-label').textContent=current.kind==='pdf'?'原始 Slides · PDF 物理页':current.kind==='code'?'原始可执行讲义 · 固定版本行号':'本讲暂无独立 Slides';selectItem()}
function selectItem(){const r=current.rows[+$('item').value];$('status').textContent=`L${current.n.toString().padStart(2,'0')} · ${r.transcript} · ${r.review}`;let source='';if(current.kind==='pdf')source=`<a target="_blank" href="../three-way-review/lecture_${current.n.toString().padStart(2,'0')}/page-${r.page.toString().padStart(2,'0')}.png"><img alt="L${current.n} PDF 第 ${r.page} 页" src="../three-way-review/lecture_${current.n.toString().padStart(2,'0')}/page-${r.page.toString().padStart(2,'0')}.png"></a>`;else if(current.kind==='code')source='<pre>'+current.code.split('\n').map((line,i)=>`<span class="code-line ${i+1>=r.start&&i+1<=r.end?'active':''}" id="c${i+1}"><span class="ln">${i+1}</span>${esc(line)}</span>`).join('')+'</pre>';else source='<p>仅有用户提供的完整文字稿，本轮不虚构课件页。</p>';$('slide').innerHTML=source+`<div id="note"><b>本项核验</b><br>${esc(r.note)}</div>`;if(current.kind==='code'){const el=$('c'+r.start);$('slide').scrollTop=el.offsetTop-$('slide').offsetTop-12}else $('slide').scrollTop=0;document.querySelectorAll('#transcript .active,#book .focus').forEach(el=>el.classList.remove('active','focus'));if(r.seconds!==null){const bucket=Math.floor(r.seconds/180)*180,el=$('t'+bucket);if(el){el.classList.add('active');$('transcript').scrollTop=el.offsetTop-$('transcript').offsetTop-8}}const target=$('book').querySelector('[id="'+CSS.escape(r.anchor)+'"]');if(target){target.classList.add('focus');$('book').scrollTop=target.offsetTop-$('book').offsetTop-8}else $('book').scrollTop=0;$('prev').disabled=+$('item').value===0;$('next').disabled=+$('item').value===current.rows.length-1;location.hash=`L${current.n}-${+$('item').value+1}`}
$('chapter').innerHTML=DATA.map((c,i)=>`<option value="${i}">${esc(c.title)}</option>`).join('');$('chapter').onchange=selectChapter;$('item').onchange=selectItem;$('prev').onclick=()=>{$('item').value=+$('item').value-1;selectItem()};$('next').onclick=()=>{$('item').value=+$('item').value+1;selectItem()};const match=location.hash.match(/^#L(\d+)-(\d+)/);if(match){const idx=DATA.findIndex(c=>c.n===+match[1]);if(idx>=0)$('chapter').value=idx}selectChapter();if(match&&+match[2]<=current.rows.length){$('item').value=+match[2]-1;selectItem()}
window.addEventListener('hashchange',()=>{const m=location.hash.match(/^#L(\d+)-(\d+)/);if(!m)return;const idx=DATA.findIndex(c=>c.n===+m[1]),item=+m[2]-1;if(idx<0||item<0||item>=DATA[idx].rows.length)return;if(current.n===+m[1]&&+$('item').value===item)return;if(current.n!==+m[1]){$('chapter').value=idx;selectChapter()}$('item').value=item;selectItem()});
</script></html>'''
    out=ROOT/'outputs/three-way-reader';out.mkdir(exist_ok=True)
    encoded=json.dumps(chapters,ensure_ascii=False).replace('<','\\u003c')
    (out/'index.html').write_text(template.replace('__DATA__',encoded))
    print(f'Local reader: {out/"index.html"}; {len(chapters)} complete transcripts, {sum(len(c["rows"]) for c in chapters)} correspondence entries')
if __name__=='__main__':main()
