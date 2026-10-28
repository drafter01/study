/**
 * 모임 설계자 – 플레이 기록 받기 (Google Apps Script 웹 앱)
 *
 * 설치 (한 번만)
 * 1. 구글 시트 "모임 설계자 – 플레이 기록 (전시)"를 열고 확장 프로그램 > Apps Script
 * 2. 이 파일 내용을 전부 붙여넣고 저장
 * 3. 배포 > 새 배포 > 유형: 웹 앱
 *    - 다음 사용자 인증 정보로 실행: 나
 *    - 액세스 권한이 있는 사용자: 모든 사용자
 * 4. 권한 승인 후 나오는 웹 앱 URL(https://script.google.com/macros/s/.../exec)을 복사
 * 5. 전시 컴퓨터에서 게임을 한 번만 moim.html?collect=웹앱URL 로 열면 그 컴퓨터에 주소가 기억됨
 *
 * 게임은 한 판이 끝날 때마다 기록을 POST로 보내고(doPost),
 * 첫 화면을 열 때 최근 기록을 GET으로 받아 원 그림에 그림(doGet).
 * 개인 정보는 받지 않음: 모임 종류, 스킬 배분, 결과 숫자만.
 */
const SHEET_NAME = ''; // 비워 두면 첫 번째 시트

function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  return SHEET_NAME ? ss.getSheetByName(SHEET_NAME) : ss.getSheets()[0];
}

const KEYS = ['open', 'welcome', 'rhythm', 'conn', 'roles'];

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const d = JSON.parse(e.postData.contents);
    const sh = sheet_();
    // 같은 기록이 두 번 오면 한 번만 남김
    const last = Math.max(sh.getLastRow() - 1, 0);
    if (last) {
      const ids = sh.getRange(2, 2, last, 1).getValues().flat();
      if (ids.indexOf(d.id) >= 0) return out_({ ok: true, dup: true });
    }
    const s = d.skills || {}, a = d.alloc1 || {};
    sh.appendRow([new Date(), d.id, d.t, d.type, d.verdict, d.total, d.rooted, d.leaders, d.links, d.rate, d.energy]
      .concat(KEYS.map(k => s[k] || 0), KEYS.map(k => a[k] || 0), [d.gain || 0, d.playSec || 0]));
    return out_({ ok: true });
  } finally {
    lock.releaseLock();
  }
}

function doGet(e) {
  const n = Math.min(Number((e && e.parameter && e.parameter.n) || 300), 1000);
  const sh = sheet_();
  const last = sh.getLastRow() - 1;
  if (last < 1) return out_([]);
  const start = Math.max(2, sh.getLastRow() - n + 1);
  const rows = sh.getRange(start, 1, sh.getLastRow() - start + 1, 23).getValues();
  const list = rows.map(r => ({
    id: r[1], t: Number(r[2]), type: r[3], verdict: r[4], total: r[5], rooted: r[6], leaders: r[7], links: r[8],
    rate: r[9], energy: r[10],
    skills: { open: r[11], welcome: r[12], rhythm: r[13], conn: r[14], roles: r[15] }
  })).reverse();
  return out_(list);
}

function out_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
