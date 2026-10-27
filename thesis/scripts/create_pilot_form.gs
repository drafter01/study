/**
 * 디자이너 대상 예비 설문 구글 폼 자동 생성 스크립트
 * (thesis/21-designer-pilot-survey.md 기준, v3: 안내문 정리, 섹션 5개, 운영 경험 섹션·자유 의견 추가)
 *
 * 사용 방법
 * 1. https://script.google.com 접속 → [새 프로젝트]
 * 2. 기본 코드를 모두 지우고 이 파일 내용을 전부 붙여넣기
 * 3. 상단 함수 선택에서 createFollowupForm 선택 → [실행] → 실행 로그의 "응답 링크"를 복사
 * 4. 아래 FOLLOWUP_URL 따옴표 안에 그 링크를 붙여넣고 저장
 * 5. 함수 선택에서 createPilotForm 선택 → [실행]
 * 6. 처음 실행하면 권한 요청 → 본인 계정 선택 → 허용
 * 7. 실행 로그의 "편집 링크"로 폼을 열어 확인
 *
 * 실행 후 폼 편집 화면에서 직접 해야 할 것 (스크립트로는 설정 불가)
 * - Q5, Q9, Q10의 [옵션 순서 섞기] 켜기
 * - Q6 격자 문항의 [행 순서 섞기] 켜기
 * - [설정] → 이메일 주소 수집: "수집하지 않음" 확인
 * - 안내문의 기간(~날짜) 고치기
 */
var FOLLOWUP_URL = ''; // createFollowupForm 실행 후 응답 링크를 붙여넣기

function createPilotForm() {
  var form = FormApp.create('커뮤니티·모임을 어떻게 바라보는지 묻는 5분 설문 (졸업논문 예비 조사)');
  form.setDescription(
    '사람들이 모이는 커뮤니티와 모임은 어떻게 만들어지고 유지될까요? 이 설문은 디자인을 전공·실무하는 사람과 모임을 운영하는 사람이 커뮤니티의 과제를 어떻게 바라보는지 알아보기 위한 졸업논문 예비 조사입니다.\n\n' +
    '📌 참여 안내\n' +
    '- 대상: 디자이너(UX/UI·프로덕트·리서처 등), 커뮤니티·모임을 운영하거나 기획하는 분. 운영 경험이 없어도 참여할 수 있어요.\n' +
    '- 소요 시간: 약 5분 / 정답은 없어요.\n' +
    '- 기간: ~(날짜를 입력해 주세요)\n\n' +
    '💬 응답은 이렇게 쓰여요\n' +
    '① 커뮤니티 과제를 바라보는 관점 파악 ② 졸업논문의 커뮤니티 설계 프레임워크 근거 ③ 졸업 전시(커뮤니티 시뮬레이터) 내용 보완\n\n' +
    '익명으로 진행하며 이름·이메일 등 개인을 알아볼 수 있는 정보는 수집하지 않아요. 결과는 묶어서만 보고하고, 언제든 중단하셔도 돼요.'
  );
  form.setCollectEmail(false);
  form.setProgressBar(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    '응답해 주셔서 감사합니다. 연구에 소중하게 쓰겠습니다.' +
    (FOLLOWUP_URL ? '\n\n결과 요약을 받아보거나 졸업 전시 「Community Design Simulator」 플레이 테스트에 참여하고 싶으시면 아래 별도 폼에 연락처를 남겨주세요. 이 설문의 응답과는 연결되지 않아요.\n' + FOLLOWUP_URL : '')
  );

  // 0. 동의 (동의하지 않으면 바로 제출)
  var consent = form.addMultipleChoiceItem();
  consent.setTitle('위 안내를 확인했고 설문 참여에 동의하시나요?')
    .setChoices([
      consent.createChoice('네, 동의합니다', FormApp.PageNavigationType.CONTINUE),
      consent.createChoice('아니요, 참여하지 않겠습니다', FormApp.PageNavigationType.SUBMIT)
    ])
    .setRequired(true);

  // 1. 나에 대해
  form.addPageBreakItem().setTitle('1. 나에 대해');

  form.addMultipleChoiceItem()
    .setTitle('Q1. 지금 하는 일에 가장 가까운 것을 골라주세요.')
    .setChoiceValues(['UX/UI·프로덕트 디자이너', 'UX 리서처', '그 외 디자인 직무', '디자인 직무는 아니지만 커뮤니티·모임을 운영하거나 기획한다'])
    .showOtherOption(true)
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Q2. 그 일을 한 기간은 어느 정도인가요?')
    .setChoiceValues(['1년 미만', '1~3년', '3~7년', '7년 이상'])
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('Q3. 커뮤니티나 모임을 운영해 본 경험이 있나요? (해당하는 것을 모두 골라주세요)')
    .setChoiceValues(['없음', '일회성 모임을 주최해 봄', '정기 모임을 운영해 봄 (취미·동네 등)', '업무로 커뮤니티를 운영해 봄'])
    .setRequired(true);

  // 2. 상황 질문
  form.addPageBreakItem()
    .setTitle('2. 상황 질문')
    .setHelpText('정답은 없어요. 떠오르는 대로 답해주세요.');

  form.addParagraphTextItem()
    .setTitle('Q4. 동네에서 매주 모이는 15명 규모의 독서모임 운영을 맡게 되었습니다. 최근 석 달 동안 매번 3분의 1 정도가 말없이 빠집니다. 어떻게 하시겠어요?')
    .setHelpText('한두 줄, 키워드만 적어도 괜찮아요.')
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Q5. 모임에 처음 온 사람이 다음 모임에 다시 오는 경우가 적습니다. 가장 먼저 해볼 일 하나를 골라주세요.')
    .setChoiceValues([
      '다시 오지 않은 사람들에게 이유를 물어본다',
      '첫 모임의 진행 방식을 바꿔본다',
      '모임 소개와 신청·안내 과정을 다시 살펴본다',
      '처음 온 사람에게 개별 연락해 다시 와달라고 한다',
      '기존 멤버에게 새로 온 사람을 챙겨달라고 부탁한다',
      '뒤풀이나 친목 자리를 만든다',
      '출석 규칙이나 보증금을 만든다',
      '원래 그런 것이라 크게 신경 쓰지 않는다'
    ])
    .showOtherOption(true)
    .setRequired(true);

  // 3. 이런 일을 맡는다면
  form.addPageBreakItem().setTitle('3. 이런 일을 맡는다면');

  form.addGridItem()
    .setTitle('Q6. 아래 일을 맡는다면 어느 정도 자신 있게 해낼 수 있을 것 같나요?')
    .setRows([
      '처음 온 사람이 어색하지 않도록 첫 모임 진행 방식 정하기',
      '다시 오지 않는 사람들의 이유 알아내기',
      '모임 소개글과 신청 과정 만들기',
      '모임이 끝난 뒤 의견을 받아 다음 모임에 반영하기',
      '모임 방식을 조금씩 바꿔보고 반응 비교하기',
      '회비를 걷고 정산하기',
      '모임 장소를 찾고 예약하기',
      '멤버 사이의 말다툼 중재하기',
      '분위기를 해치는 멤버에게 주의 주기',
      '오래된 멤버와 새 멤버가 잘 섞이게 하기',
      '운영을 도와줄 사람을 찾고 일을 나누기'
    ])
    .setColumns(['1 전혀 자신 없다', '2', '3', '4', '5 매우 자신 있다', '잘 모르겠다'])
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('Q7. 위에서 자신 있다고 답한 일은 주로 어떤 경험 덕분인가요? (해당하는 것을 모두 골라주세요)')
    .setChoiceValues(['디자인 업무 경험', '커뮤니티·모임 경험', '디자인이 아닌 다른 업무 경험', '일상생활 경험', '자신 있다고 답한 일이 없음'])
    .showOtherOption(true)
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('Q8. 위의 일 중 가장 자신 없는 것은 무엇이고, 그 이유는 무엇인가요? (선택)')
    .setRequired(false);

  // 4. 직접 운영해 본 경험
  form.addPageBreakItem()
    .setTitle('4. 직접 운영해 본 경험')
    .setHelpText('운영해 본 커뮤니티나 모임 하나를 떠올리며 답해주세요. 경험이 없으면 "운영해 본 적 없음"을 고르고 넘어가세요.');

  var atMost3 = FormApp.createCheckboxValidation().requireSelectAtMost(3).setHelpText('최대 3개까지 골라주세요.').build();

  form.addCheckboxItem()
    .setTitle('Q9. 운영하면서 가장 어려웠던 점은 무엇인가요? (최대 3개)')
    .setChoiceValues([
      '처음 온 사람이 다시 오지 않음',
      '기존 멤버가 점점 빠짐',
      '모임을 알리고 사람을 모으기',
      '일정·장소·회비 관리',
      '멤버 사이의 갈등이나 불편한 분위기',
      '오래된 멤버와 새 멤버 사이의 벽',
      '운영을 혼자 떠맡아 지침',
      '모임이 무엇을 위한 것인지 흐려짐',
      '특별히 어려움이 없었음',
      '운영해 본 적 없음'
    ])
    .showOtherOption(true)
    .setValidation(atMost3)
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('Q10. 그 어려움을 주로 어떻게 풀었나요? (최대 3개)')
    .setChoiceValues([
      '멤버에게 직접 물어봤다',
      '진행 방식을 바꿔 보고 반응을 봤다',
      '다른 모임이나 자료를 참고했다',
      '운영을 도와줄 사람을 구하고 일을 나눴다',
      '규칙을 만들었다',
      '친목 자리를 늘렸다',
      '해결하지 못했다',
      '운영해 본 적 없음'
    ])
    .showOtherOption(true)
    .setValidation(atMost3)
    .setRequired(true);

  // 5. 마지막으로 (앞 문항에 영향을 주지 않도록 맨 끝)
  form.addPageBreakItem().setTitle('5. 마지막으로 (선택)');

  form.addScaleItem()
    .setTitle('Q11. 기회가 있다면 직접 커뮤니티나 모임을 만들어볼 생각이 있나요?')
    .setBounds(1, 5)
    .setLabels('전혀 없다', '매우 있다')
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle('Q11-1. 망설여진다면 가장 큰 이유는 무엇인가요?')
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle('Q12. 커뮤니티·모임과 관련해 기억에 남는 고민이나 사례가 있다면 자유롭게 들려주세요.')
    .setHelpText('어려웠던 경험뿐 아니라 도움이 되었던 방법도 좋아요. 특정 단체나 개인을 알아볼 수 있는 정보는 빼주세요.')
    .setRequired(false);

  Logger.log('편집 링크: ' + form.getEditUrl());
  Logger.log('응답 링크(공유용): ' + form.getPublishedUrl());
}

/**
 * 결과 공유·플레이 테스트 참여 의향을 받는 별도 폼 (본 설문과 응답이 연결되지 않음)
 */
function createFollowupForm() {
  var form = FormApp.create('결과 공유·플레이 테스트 참여 신청 (선택)');
  form.setDescription('본 설문과는 연결되지 않는 별도 폼이에요. 남겨주신 연락처는 아래 안내 목적으로만 쓰고, 연구가 끝나면 삭제합니다.');
  form.setCollectEmail(false);
  form.addCheckboxItem()
    .setTitle('받고 싶은 안내를 골라주세요.')
    .setChoiceValues(['설문 결과 요약', '졸업 전시 「Community Design Simulator」 플레이 테스트 참여', '프레임워크 서면 검토 참여'])
    .setRequired(true);
  form.addTextItem()
    .setTitle('연락받을 이메일')
    .setValidation(FormApp.createTextValidation().requireTextIsEmail().build())
    .setRequired(true);
  Logger.log('응답 링크(FOLLOWUP_URL에 붙여넣기): ' + form.getPublishedUrl());
}
