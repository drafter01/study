/**
 * 디자이너 대상 예비 설문 구글 폼 자동 생성 스크립트
 * (thesis/21-designer-pilot-survey.md 기준, v2: 필수 서술형을 Q4 하나로 줄임)
 *
 * 사용 방법
 * 1. https://script.google.com 접속 → [새 프로젝트]
 * 2. 기본 코드를 모두 지우고 이 파일 내용을 전부 붙여넣기
 * 3. 상단 함수 선택에서 createPilotForm 선택 → [실행]
 * 4. 처음 실행하면 권한 요청 → 본인 계정 선택 → 허용
 * 5. 아래 [실행 로그]에 나오는 "편집 링크"로 폼을 열어 확인
 *
 * 실행 후 폼 편집 화면에서 직접 해야 할 것
 * - Q5 객관식의 [옵션 순서 섞기] 켜기 (스크립트로는 설정 불가)
 * - Q6 격자 문항의 [행 순서 섞기] 켜기 (스크립트로는 설정 불가)
 * - [설정] → 이메일 주소 수집: "수집하지 않음" 확인
 */
function createPilotForm() {
  var form = FormApp.create('커뮤니티·모임 운영에 관한 5분 설문 (졸업논문 예비 조사)');
  form.setDescription(
    '졸업논문 예비 조사로, 커뮤니티나 모임을 운영하는 상황을 어떻게 바라보는지 묻는 짧은 설문입니다.\n' +
    '약 5분이 걸리며, 정답은 없습니다.\n' +
    '익명으로 진행되며 개인을 알아볼 수 있는 정보는 수집하지 않습니다. 응답은 연구 목적으로만 사용합니다.\n' +
    '언제든 중단하셔도 됩니다.'
  );
  form.setCollectEmail(false);
  form.setProgressBar(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage('응답해 주셔서 감사합니다. 연구에 소중하게 쓰겠습니다.');

  // 0. 동의 (동의하지 않으면 바로 제출)
  var consent = form.addMultipleChoiceItem();
  consent.setTitle('위 안내를 확인했고 설문 참여에 동의하시나요?')
    .setChoices([
      consent.createChoice('네, 동의합니다', FormApp.PageNavigationType.CONTINUE),
      consent.createChoice('아니요, 참여하지 않겠습니다', FormApp.PageNavigationType.SUBMIT)
    ])
    .setRequired(true);

  // 1. 기본 정보
  form.addPageBreakItem().setTitle('1. 기본 정보');

  form.addMultipleChoiceItem()
    .setTitle('Q1. 현재 직무를 골라주세요.')
    .setChoiceValues(['UX/UI 디자이너', '프로덕트 디자이너', 'UX 리서처', '그 외 디자인 직무'])
    .showOtherOption(true)
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Q2. 실무 경력은 어느 정도인가요?')
    .setChoiceValues(['1년 미만', '1~3년', '3~7년', '7년 이상'])
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('Q3. 커뮤니티나 모임을 운영해 본 경험이 있나요? (해당하는 것을 모두 골라주세요)')
    .setChoiceValues(['없음', '일회성 모임을 주최해 봄', '정기 모임을 운영해 봄', '업무로 커뮤니티를 운영해 봄'])
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

  // 3. 평가 질문
  form.addPageBreakItem().setTitle('3. 평가 질문');

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
    .setChoiceValues(['디자인 업무 경험', '커뮤니티·모임 경험', '디자인이 아닌 다른 업무 경험', '일상생활 경험'])
    .showOtherOption(true)
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('Q8. 위의 일 중 가장 자신 없는 것은 무엇이고, 그 이유는 무엇인가요? (선택)')
    .setRequired(false);

  // 4. 마지막 질문 (앞 문항에 영향을 주지 않도록 맨 끝)
  form.addPageBreakItem().setTitle('4. 마지막 질문 (선택)');

  form.addScaleItem()
    .setTitle('Q9. 기회가 있다면 직접 커뮤니티나 모임을 만들어볼 생각이 있나요?')
    .setBounds(1, 5)
    .setLabels('전혀 없다', '매우 있다')
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle('Q9-1. 망설여진다면 가장 큰 이유는 무엇인가요?')
    .setRequired(false);

  Logger.log('편집 링크: ' + form.getEditUrl());
  Logger.log('응답 링크(공유용): ' + form.getPublishedUrl());
}
