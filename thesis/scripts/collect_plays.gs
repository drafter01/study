/**
 * 커뮤니티 시뮬레이터 – 플레이 기록과 한마디 받기 (Google Apps Script 웹 앱)
 *
 * 설치 (한 번만)
 * 1. 구글 시트 "모임 설계자 – 플레이 기록 (전시)"를 열고 확장 프로그램 > Apps Script
 * 2. 이 파일 내용을 전부 붙여넣고 저장
 * 3. 배포 > 새 배포 > 유형: 웹 앱
 *    - 다음 사용자 인증 정보로 실행: 나
 *    - 액세스 권한이 있는 사용자: 모든 사용자
 * 4. 권한 승인 후 나오는 웹 앱 URL(https://script.google.com/macros/s/.../exec)을 복사해 Claude에게 전달
 *    → 게임 파일 안에 주소를 넣어 두면 아이맥·휴대폰 어디서 열어도 같은 시트로 모임
 *
 * 시트 두 개를 씀
 * - 첫 번째 시트: 플레이 기록 (한 판이 끝날 때마다 한 줄)
 * - "메시지" 시트: 한마디 (없으면 자동으로 만듦). 부적절한 글은 "숨김" 칸에 아무 글자나 적으면 화면에서 사라짐
 * 개인 정보는 받지 않음: 커뮤니티 종류, 스킬 배분, 결과 숫자, 익명 한마디만.
 */
const KEYS = ['open', 'welcome', 'rhythm', 'conn', 'roles'];
const MSG_SHEET = '메시지';
const MSG_HEAD = ['받은 시각', '기록 ID', '쓴 시각(ms)', '나는', '한마디', '결과 유형', '커뮤니티', '숨김'];

function playSheet_() { return SpreadsheetApp.getActiveSpreadsheet().getSheets()[0]; }
function msgSheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(MSG_SHEET);
  if (!sh) { sh = ss.insertSheet(MSG_SHEET); sh.appendRow(MSG_HEAD); sh.setFrozenRows(1); }
  return sh;
}
function hasId_(sh, id) {
  const last = sh.getLastRow() - 1;
  if (last < 1) return false;
  return sh.getRange(2, 2, last, 1).getValues().flat().indexOf(id) >= 0;
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const d = JSON.parse(e.postData.contents);
    if (d.kind === 'msg') {
      const sh = msgSheet_();
      if (hasId_(sh, d.id)) return out_({ ok: true, dup: true });
      sh.appendRow([new Date(), d.id, d.t, String(d.role || ''), String(d.text || '').slice(0, 140), d.verdict || '', d.type || '', '']);
      return out_({ ok: true });
    }
    const sh = playSheet_();
    if (hasId_(sh, d.id)) return out_({ ok: true, dup: true });
    const s = d.skills || {}, a = d.alloc1 || {};
    sh.appendRow([new Date(), d.id, d.t, d.type, d.verdict, d.total, d.rooted, d.leaders, d.links, d.rate, d.energy]
      .concat(KEYS.map(k => s[k] || 0), KEYS.map(k => a[k] || 0), [d.gain || 0, d.playSec || 0]));
    return out_({ ok: true });
  } finally {
    lock.releaseLock();
  }
}

function doGet(e) {
  const p = (e && e.parameter) || {};
  const n = Math.min(Number(p.n || 300), 1000);
  if (p.kind === 'msg') {
    const sh = msgSheet_();
    const last = sh.getLastRow() - 1;
    if (last < 1) return out_([]);
    const start = Math.max(2, sh.getLastRow() - n + 1);
    const rows = sh.getRange(start, 1, sh.getLastRow() - start + 1, MSG_HEAD.length).getValues();
    return out_(rows.filter(r => !r[7]).map(r => ({ id: r[1], t: Number(r[2]), role: r[3], text: r[4], verdict: r[5], type: r[6] })).reverse());
  }
  const sh = playSheet_();
  const last = sh.getLastRow() - 1;
  if (last < 1) return out_([]);
  const start = Math.max(2, sh.getLastRow() - n + 1);
  const rows = sh.getRange(start, 1, sh.getLastRow() - start + 1, 23).getValues();
  return out_(rows.map(r => ({
    id: r[1], t: Number(r[2]), type: r[3], verdict: r[4], total: r[5], rooted: r[6], leaders: r[7], links: r[8],
    rate: r[9], energy: r[10],
    skills: { open: r[11], welcome: r[12], rhythm: r[13], conn: r[14], roles: r[15] }
  })).reverse());
}

function out_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
