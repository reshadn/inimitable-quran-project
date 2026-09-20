const data = JSON.parse(document.getElementById('research-data').textContent);
const make = (tag, text, cls) => { const e=document.createElement(tag); if(text!==undefined)e.textContent=text; if(cls)e.className=cls; return e; };
function selectPanel(id, update=true) {
  if(!['book','dossier','lab','sources'].includes(id)) id='book';
  document.querySelectorAll('.panel').forEach(p=>p.hidden=p.id!==id);
  document.querySelectorAll('[data-panel]').forEach(b=>{ if(b.dataset.panel===id)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current'); });
  if(update){ history.replaceState(null,'','#'+id); document.getElementById('main').scrollIntoView({behavior:'auto'}); }
}
document.querySelectorAll('[data-panel]').forEach(b=>b.addEventListener('click',()=>selectPanel(b.dataset.panel)));
document.querySelectorAll('.prose p').forEach(p=>{
  const ar=(p.textContent.match(/[\u0600-\u06ff]/g)||[]).length;
  const latin=(p.textContent.match(/[A-Za-z]/g)||[]).length;
  if(ar>0 && ar>latin*2){p.setAttribute('lang','ar');p.setAttribute('dir','rtl');p.classList.add('arabicline');}
});
const select=document.getElementById('surah-select');
const known={1:'Al-Fatiha',12:'Yusuf',19:'Maryam',36:'Ya-Sin',55:'Al-Rahman',67:'Al-Mulk',75:'Al-Qiyama',93:'Al-Duha',103:'Al-Asr',108:'Al-Kawthar',112:'Al-Ikhlas',114:'Al-Nas'};
data.surahs.forEach(r=>{const o=make('option',r.surah+(known[r.surah]?' · '+known[r.surah]:''));o.value=r.surah;select.append(o);});
select.value='103';
function showSurah(){const r=data.surahs.find(x=>x.surah===select.value);document.getElementById('surah-details').textContent=`Surah ${r.surah}: ${Number(r.verses).toLocaleString()} verses · ${Number(r.lexical_tokens).toLocaleString()} written tokens · median ${r.median_tokens_per_verse} per verse`;}
select.addEventListener('change',showSurah);showSurah();
const statusNames={passage_inspected:'Passage inspected',catalog_confirmed:'Catalogue confirmed',discovery_lead:'Discovery lead'};
function external(url,label){const a=make('a',label);if(/^https?:\/\//.test(url)){a.href=url;a.rel='noopener';}return a;}
function showSources(){
  const query=document.getElementById('source-search').value.trim().toLowerCase();
  const status=document.getElementById('status-filter').value;
  const records=data.catalog.sources.filter(s=>(status==='all'||s.status===status)&&[s.author,s.title,s.domain,s.id].join(' ').toLowerCase().includes(query));
  document.getElementById('source-count').textContent=`${records.length} of ${data.catalog.sources.length} bibliography records. No full works claimed as read.`;
  const list=document.getElementById('source-list');list.replaceChildren();
  records.forEach(s=>{const c=make('div',undefined,'source-card');c.append(make('div',s.id+' · '+(statusNames[s.status]||s.status),'meta'),make('h3',s.title),make('p',[s.author,s.year,s.domain].filter(Boolean).join(' · ')),make('p',s.argument_role));
    if(s.url)c.append(external(s.url,'Open source record'));
    const d=make('details');d.append(make('summary','Inspection scope and limitations'),make('p',s.inspection),make('p',s.limitations));if(s.locator)d.append(make('p','Locator: '+s.locator));if(s.dependence)d.append(make('p','Dependence: '+s.dependence));c.append(d);list.append(c);});
}
document.getElementById('source-search').addEventListener('input',showSources);document.getElementById('status-filter').addEventListener('change',showSources);showSources();
data.evidence.forEach(s=>{const c=make('div',undefined,'source-card');c.append(make('div',s.id+' · '+(s.status||s.verification_status).replaceAll('_',' '),'meta'),make('h3',s.title),make('p',s.author||s.provider||''));const scope=s.inspected_scope||s.inspection||s.scope; if(scope)c.append(make('p',typeof scope==='string'?scope:JSON.stringify(scope)));let urls=s.urls||[s.url];urls.filter(Boolean).forEach((u,i)=>{c.append(external(u,'Source '+(i+1)),document.createTextNode(' '));});const gaps=s.gaps||s.limitations;if(gaps)c.append(make('p',Array.isArray(gaps)?gaps.join(' '):gaps));document.getElementById('evidence-list').append(c);});
(data.claims.claims||data.claims).forEach(s=>{const c=make('div',undefined,'claim-card');c.append(make('div',s.id+' · '+s.level+' · '+s.status,'meta'),make('h3',s.claim),make('p','Evidence: '+s.evidence.join('; ')),make('p','Limit: '+s.limit));document.getElementById('claim-list').append(c);});
const first=location.hash.slice(1);if(['book','dossier','lab','sources'].includes(first))selectPanel(first,false);
