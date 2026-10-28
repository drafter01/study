const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [,,file,dir]=process.argv;fs.rmSync(dir+'/f',{recursive:true,force:true});fs.mkdirSync(dir+'/f',{recursive:true});
const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1920,height:1080}});const p=await ctx.newPage();
p.on('pageerror',e=>console.log('ERR',e.message));
await p.addInitScript(sd=>{let a=sd>>>0;Math.random=()=>{a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};},+(process.env.SEED||1));
await p.addInitScript(()=>{try{localStorage.clear()}catch(e){};addEventListener('DOMContentLoaded',()=>{
  const c=document.createElement('div');c.id='fcur';c.style.cssText='position:fixed;left:0;top:0;width:28px;height:28px;margin:-14px 0 0 -14px;border-radius:50%;background:rgba(17,17,17,.28);border:2px solid rgba(255,255,255,.95);box-shadow:0 2px 8px rgba(0,0,0,.25);z-index:99999;pointer-events:none;transition:transform .12s,background .12s;transform:translate(960px,700px)';
  document.body.appendChild(c);let x=960,y=700,dn=false;const set=()=>c.style.transform=`translate(${x}px,${y}px) scale(${dn?.75:1})`;
  addEventListener('mousemove',e=>{x=e.clientX;y=e.clientY;set()},true);addEventListener('mousedown',()=>{dn=true;c.style.background='rgba(17,17,17,.55)';set()},true);addEventListener('mouseup',()=>{dn=false;c.style.background='rgba(17,17,17,.28)';set()},true);});});
const cdp=await ctx.newCDPSession(p);const frames=[];let n=0;
cdp.on('Page.screencastFrame',async f=>{const name=`${dir}/f/${String(n++).padStart(5,'0')}.jpg`;fs.writeFileSync(name,Buffer.from(f.data,'base64'));frames.push([name,f.metadata.timestamp]);try{await cdp.send('Page.screencastFrameAck',{sessionId:f.sessionId})}catch(e){}});
await p.goto('file://'+file);await p.waitForTimeout(500);
await cdp.send('Page.startScreencast',{format:'jpeg',quality:92,maxWidth:1920,maxHeight:1080,everyNthFrame:1});
const W=ms=>p.waitForTimeout(ms);
const moveTo=async(sel,steps=25)=>{const r=await p.locator(sel).first().boundingBox();await p.mouse.move(r.x+r.width/2,r.y+r.height/2,{steps});return r;};
const click=async(sel,pause=350)=>{await moveTo(sel);await W(pause);await p.mouse.down();await W(90);await p.mouse.up();};
const drag=async(k,to)=>{const L=p.locator('#r-'+k),r=await L.boundingBox(),y=r.y+r.height/2;const val=async()=>+(await L.inputValue());
  const cur=await val();let x=r.x+10+(r.width-20)*cur/5;await p.mouse.move(x,y,{steps:20});await W(200);await p.mouse.down();
  const dir=to>cur?1:-1;for(let i=0;i<200&&(await val())!==to;i++){x+=dir*4;await p.mouse.move(x,y);await W(8);}
  await p.mouse.move(x+dir*6,y,{steps:3});await W(80);await p.mouse.up();await W(350);console.log(k,await val());};
await W(2200);
await click('#start');await W(1600);
await moveTo('.ecard[data-t=book]',30);await W(500);await moveTo('.ecard[data-t=plog]',30);await W(500);
await click('.ecard[data-t=run] .btn, .ecard[data-t=run]');await W(4200);
await click('#help-ok');await W(900);
for(const [k,v] of [['open',2],['welcome',3],['rhythm',1],['conn',1],['roles',1]])await drag(k,v);
await W(600);await click('#go');
await p.waitForSelector('#lv-ok',{timeout:40000});await W(2600);await click('#lv-ok');await W(700);
{const pts=+(await p.locator('.pts3 b').innerText());await drag('conn',1+Math.ceil(pts/2));await drag('roles',1+Math.floor(pts/2));}await W(500);await click('#go');
await p.waitForSelector('.case3',{timeout:60000});console.log('verdict',await p.locator('h2.one').innerText());await W(1500);
await moveTo('.q2',30);await W(2500);await moveTo('.big2',30);await W(1800);
await click('#home');await W(1500);
const mine=await p.$('.comms circle[stroke-dasharray]');if(mine){const r=await mine.boundingBox();await p.mouse.move(r.x+r.width/2,r.y+r.height/2,{steps:30});}
await W(3500);
await cdp.send('Page.stopScreencast');await W(300);
const list=[];for(let i=0;i<frames.length;i++){const d=i<frames.length-1?frames[i+1][1]-frames[i][1]:0.5;list.push(`file '${frames[i][0]}'\nduration ${Math.max(d,0.001).toFixed(4)}`);}
list.push(`file '${frames[frames.length-1][0]}'`);fs.writeFileSync(dir+'/list.txt',list.join('\n'));
console.log('frames',frames.length,'secs',(frames[frames.length-1][1]-frames[0][1]).toFixed(1));await b.close();})();
