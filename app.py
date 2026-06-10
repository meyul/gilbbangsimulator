import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="안전지대 예측 & 방어 게임", page_icon="🛡️", layout="centered")

# 세션 상태 초기화 (2페이지 게임용)
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'player_hp' not in st.session_state:
    st.session_state.player_hp = 100
if 'enemy_hp' not in st.session_state:
    st.session_state.enemy_hp = 100
if 'enemy_type' not in st.session_state:
    st.session_state.enemy_type = ""
if 'game_log' not in st.session_state:
    st.session_state.game_log = []

# 사이드바 메뉴 구성
st.sidebar.title("📌 메뉴 선택")
page = st.sidebar.radio("이동할 페이지", ["1P: 범죄 확률 & 결말 예측", "2P: 범죄자 퇴치 턴제 게임"])

# ------------------------------------------------------------------
# 1 페이지: 범죄 확률 및 결말 예측
# ------------------------------------------------------------------
if page == "1P: 범죄 확률 & 결말 예측":
    st.title("🛡️ 나의 범죄 노출 확률 & 결말 예측 시뮬레이터")
    st.write("재미로 보는 통계 기반 시뮬레이션입니다. 정보를 입력해 보세요!")
    
    st.markdown("---")
    
    # 사용자 입력 폼
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("성별", ["선택하세요", "남자", "여자"])
    with col2:
        age = st.number_input("나이 (만)", min_value=0, max_value=120, value=25)
    with col3:
        place = st.selectbox("현재(또는 자주 있는) 장소", ["선택하세요", "집/주거지", "길거리/노상", "직장/사무실", "온라인/SNS"])

    if st.button("🔮 결말 예측하기"):
        if gender == "선택하세요" or place == "선택하세요":
            st.error("🚨 성별과 장소를 올바르게 선택해 주세요!")
        else:
            with st.spinner('📊 대검찰청 범죄통계 데이터를 분석 중...'):
                time.sleep(1.5) # 감성적인 연출을 위한 딜레이
                
            st.success("🎯 분석이 완료되었습니다!")
            
            # --- 통계 기반 로직 연출 ---
            # 실제 통계 경향 반영: 사기/절도가 전반적으로 가장 높음. 여성이면 데이트폭력/강력범죄 비율 반영 등
            if place == "온라인/SNS":
                crime_type = "사기 범죄 (보이스피싱 및 중고거래 사기)"
                probability = random.randint(35, 55)
                suspect_desc = "당신의 신뢰를 이용해 지갑을 털어 가려는 '전혀 모르는 온라인 사기꾼'"
                ending = "돈을 송금하기 직전, 금융감독원 경고 알림이 울려 극적으로 자산을 지켜내고 사기꾼은 경찰에 잡힙니다!"
            elif place == "집/주거지":
                crime_type = "절도 또는 면식범에 의한 폭행"
                probability = random.randint(15, 28)
                suspect_desc = "당신의 동선을 은밀히 파악하고 있던 '이웃 또는 안면이 있는 인물'"
                ending = "집 비밀번호를 바꾸고 홈CCTV를 설치한 당신의 철저함에 범인은 문 앞에서 발을 돌려 도망칩니다."
            elif place == "직장/사무실":
                crime_type = "직장 내 괴롭힘 및 지능범죄(배임/횡령 부류)"
                probability = random.randint(20, 35)
                suspect_desc = "겉으로는 웃으면서 뒤로 책임을 떠넘기려는 '직장 상사 또는 동료'"
                ending = "당신이 차곡차곡 모아둔 메신저 캡처와 녹음 파일 앞의 무릎을 꿇고, 고용노동부의 매콤한 맛을 보게 됩니다."
            else: # 길거리/노상
                if gender == "여자":
                    crime_type = "강제추행 또는 폭력 범죄"
                    probability = random.randint(25, 40)
                else:
                    crime_type = "절도 또는 폭행 범죄"
                    probability = random.randint(20, 35)
                suspect_desc = "술에 취했거나 욱하는 성질을 참지 못하는 '길거리의 무법자'"
                ending = "당신의 엄청난 호신술(또는 112 빠른 신고 및 대피)로 위기를 모면하고, 범인은 CCTV 투성이인 대한민국 길거리에서 30분 만에 검거됩니다."

            # 결과 화면 출력
            st.markdown("### 📊 당신의 예측 결과")
            
            # 메트릭 레이아웃
            st.metric(label="⚠️ 범죄 노출 위험도", value=f"{probability}%")
            
            st.markdown(f"> **예측 죄종:** `{crime_type}`")
            st.markdown(f"> **예측 피의자 성향:** {suspect_desc}")
            
            st.markdown("### 🎬 피해자-피의자 최종 결말")
            st.info(f"🔮 **시나리오:** {ending}")
            
            st.caption("※ 본 결과는 제공된 2024년 범죄통계 자료의 비율적 경향성을 기반으로 각색한 재미용 시뮬레이터입니다.")

# ------------------------------------------------------------------
# 2 페이지: 턴제 범죄자 상대 게임 및 퇴치법
# ------------------------------------------------------------------
elif page == "2P: 범죄자 퇴치 턴제 게임":
    st.title("⚔️ 만난 범죄자를 상대하라! 턴제 방어 게임")
    st.write("일촉즉발의 상황! 올바른 대처법을 골라 범죄자를 무력화하고 안전하게 탈출하세요.")
    
    st.markdown("---")
    
    # 게임 시작 버튼
    if not st.session_state.game_started:
        if st.button("🎮 게임 시작하기"):
            st.session_state.game_started = True
            st.session_state.player_hp = 100
            st.session_state.enemy_hp = 100
            st.session_state.enemy_type = random.choice(["보이스피싱 사기꾼", "골목길 미행범", "중고거래 빌런"])
            st.session_state.game_log = [f"🚨 무시무시한 [{st.session_state.enemy_type}]이(가) 나타났다!"]
            st.rerun()

    # 게임 진행 화면
    if st.session_state.game_started:
        # HP 상태 바 표현
        st.subheader(" 체력 상황")
        col_p, col_e = st.columns(2)
        with col_p:
            st.write(f"🧑‍💼 **나의 멘탈/체력:** {st.session_state.player_hp} / 100")
            st.progress(max(0, st.session_state.player_hp))
        with col_e:
            st.write(f"🦹 **{st.session_state.enemy_type}의 전의:** {st.session_state.enemy_hp} / 100")
            st.progress(max(0, st.session_state.enemy_hp))
            
        st.markdown("---")
        st.subheader(" ACTIONS: 어떻게 대처하시겠습니까?")
        
        # 범죄자 유형별 맞춤형 선택지 제공
        act_col1, act_col2, act_col3 = st.columns(3)
        
        if st.session_state.enemy_type == "보이스피싱 사기꾼":
            with act_col1:
                if st.button("📞 '링크 보내주세요' 하고 누르기"):
                    st.session_state.player_hp -= 30
                    st.session_state.game_log.append("❌ 악성 앱이 설치되어 멘탈에 치명타를 입었습니다! (-30 HP)")
                    st.rerun()
            with act_col2:
                if st.button("🛑 일단 끊고 해당 기관 공식 번호로 재확인"):
                    st.session_state.enemy_hp -= 50
                    st.session_state.game_log.append("🏽 올바른 대처! 사기꾼이 당황하여 말을 더듬습니다. (-50 Damage)")
                    st.rerun()
            with act_col3:
                if st.button(" 대포통장 명의 대여해주기"):
                    st.session_state.player_hp -= 50
                    st.session_state.game_log.append("💥 공범으로 연루될 위기! 경찰서 뷰를 보게 생겼습니다. (-50 HP)")
                    st.rerun()
                    
        elif st.session_state.enemy_type == "골목길 미행범":
            with act_col1:
                if st.button("🏃 편의점이나 사람이 많은 밝은 곳으로 뛰기"):
                    st.session_state.enemy_hp -= 60
                    st.session_state.game_log.append("🏽 훌륭합니다! 미행범이 CCTV와 사람들을 의식해 접근을 포기합니다. (-60 Damage)")
                    st.rerun()
            with act_col2:
                if st.button("📱 이어폰 끼고 스마트폰 보면서 유유히 걷기"):
                    st.session_state.player_hp -= 40
                    st.session_state.game_log.append("❌ 표적이 되기 가장 좋은 행동입니다! 미행범이 거리를 좁힙니다. (-40 HP)")
                    st.rerun()
            with act_col3:
                if st.button("🚨 '112 긴급신고 앱' 원터치 신고 발동"):
                    st.session_state.enemy_hp -= 40
                    st.session_state.game_log.append("🏽 경찰 두 명이 근처 지구대에서 출동 대기 상태에 들어갑니다! (-40 Damage)")
                    st.rerun()

        elif st.session_state.enemy_type == "중고거래 빌런":
            with act_col1:
                if st.button("🤝 '안전결재'라며 보내준 외부 링크로 결제"):
                    st.session_state.player_hp -= 40
                    st.session_state.game_log.append("❌ 가짜 피싱 사이트였습니다! 돈만 날아갔습니다. (-40 HP)")
                    st.rerun()
            with act_col2:
                if st.button("📍 낮 시간에 사람 많은 지하철역 개찰구에서 직거래"):
                    st.session_state.enemy_hp -= 70
                    st.session_state.game_log.append("🏽 사기꾼이 발붙일 곳이 없습니다. 완벽한 방어! (-70 Damage)")
                    st.rerun()
            with act_col3:
                if st.button("💸 '선입금 시 할인' 유혹에 바로 송금"):
                    st.session_state.player_hp -= 50
                    st.session_state.game_log.append("💥 송금하자마자 상대방이 탈퇴했습니다. 혈압 상승! (-50 HP)")
                    st.rerun()

        # 게임 로그 출력
        st.markdown("---")
        st.subheader("📜 전투 기록")
        for log in reversed(st.session_state.game_log):
            st.write(log)
            
        # 승리 / 패배 조건 판단
        if st.session_state.enemy_hp <= 0:
            st.balloons()
            st.success("🎉 승리! 올바른 대처법으로 범죄자를 성공적으로 격퇴하고 안전을 확보했습니다!")
            st.session_state.game_started = False
            
            # 퇴치 교육용 요약 정보 제공
            st.markdown("""
            ### 💡 필수 범죄자 퇴치법 요약
            1. **지능형 사기범:** 의심스러운 외부 링크(URL)는 절대 누르지 말고, 공식 고객센터 번호로 직접 전화해 확인하세요[cite: 3].
            2. **대인 범죄(미행/폭행):** 이어폰을 낀 채 주변 경계를 게을리하는 행동은 금물입니다. 위기 시 주변 편의점(아동안전지킴이집 등)이나 밝은 곳으로 즉시 대피하세요.
            3. **중고거래:** 가급적 대낮에 사람이 많은 곳에서 직거래를 하거나, 플랫폼 내 공식 안전결제 시스템만 이용하세요.
            """)
            
        elif st.session_state.player_hp <= 0:
            st.error("💀 패배... 잘못된 대처로 인해 범죄자에게 취약점을 노출당했습니다. 대처법을 다시 숙지해 보세요!")
            st.session_state.game_started = False
