import streamlit as st

# -------------------------
# 세션 상태 초기화
# -------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "step1_data" not in st.session_state:
    st.session_state.step1_data = {}

if "step2_data" not in st.session_state:
    st.session_state.step2_data = {}

# -------------------------
# 1단계
# -------------------------
if st.session_state.step == 1:
    st.title("🤖 로봇 제작 알고리즘")
    st.header("1단계: 기본 정보 입력")

    budget = st.text_input("예산", st.session_state.step1_data.get("budget", ""))
    purpose = st.text_input("사용 목적", st.session_state.step1_data.get("purpose", ""))
    feature = st.text_area("원하는 기능", st.session_state.step1_data.get("feature", ""))
    reference = st.text_input("참고 로봇", st.session_state.step1_data.get("reference", ""))

    if st.button("다음 단계로"):
        st.session_state.step1_data = {
            "budget": budget,
            "purpose": purpose,
            "feature": feature,
            "reference": reference,
        }
        st.session_state.step = 2
        st.rerun()

# -------------------------
# 2단계
# -------------------------
elif st.session_state.step == 2:
    st.title("🤖 로봇 제작 알고리즘")
    st.header("2단계: 로봇 개념 정의")

    st.subheader("🔹 1단계 요약")
    for k, v in st.session_state.step1_data.items():
        st.write(f"- {k}: {v}")

    st.divider()

    이동방식 = st.selectbox(
        "이동 방식",
        ["바퀴형", "다족 보행형", "무한궤도형", "고정형", "기타"],
        index=0
    )

    제어방식 = st.selectbox(
        "제어 방식",
        ["유선", "무선(리모컨)", "자율 제어", "혼합형"],
        index=0
    )

    역할 = st.multiselect(
        "주요 역할 (복수 선택 가능)",
        ["이동", "탐지", "작업 수행", "데이터 수집", "교육용", "기타"]
    )

    환경 = st.radio(
        "사용 환경",
        ["실내", "실외", "혼합"]
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("이전 단계"):
            st.session_state.step = 1
            st.rerun()

    with col2:
        if st.button("다음 단계"):
            st.session_state.step2_data = {
                "이동방식": 이동방식,
                "제어방식": 제어방식,
                "역할": 역할,
                "환경": 환경,
            }
            st.session_state.step = 3
            st.rerun()

# -------------------------
# 3단계 (임시)
# -------------------------
elif st.session_state.step == 3:
    st.title("🤖 로봇 제작 알고리즘")
    st.header("3단계: 기능 정의 (다음 단계)")

    st.subheader("2단계 결과")
    st.json(st.session_state.step2_data)

    if st.button("이전 단계"):
        st.session_state.step = 2
        st.rerun()
