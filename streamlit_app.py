import streamlit as st

# -------------------------
# 세션 상태 초기화
# -------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "step1_data" not in st.session_state:
    st.session_state.step1_data = {}

# -------------------------
# 1단계 화면
# -------------------------
if st.session_state.step == 1:
    st.title("🤖 로봇 제작 알고리즘")
    st.header("1단계: 기본 정보 입력")

    budget = st.text_input(
        "예산을 입력하세요",
        value=st.session_state.step1_data.get("budget", "")
    )
    purpose = st.text_input(
        "로봇의 사용처를 입력하세요",
        value=st.session_state.step1_data.get("purpose", "")
    )
    feature = st.text_area(
        "특별히 넣고 싶은 기능",
        value=st.session_state.step1_data.get("feature", "")
    )
    reference = st.text_input(
        "참고하고 싶은 로봇",
        value=st.session_state.step1_data.get("reference", "")
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("다음 단계로"):
            st.session_state.step1_data = {
                "budget": budget,
                "purpose": purpose,
                "feature": feature,
                "reference": reference,
            }
            st.session_state.step = 2
            st.rerun()

    with col2:
        if st.button("초기화"):
            st.session_state.step1_data = {}
            st.rerun()

# -------------------------
# 2단계 (임시 화면)
# -------------------------
elif st.session_state.step == 2:
    st.title("🤖 로봇 제작 알고리즘")
    st.header("2단계: 개념 정리 (임시)")

    st.subheader("1단계에서 입력한 내용")
    for k, v in st.session_state.step1_data.items():
        st.write(f"- {k}: {v}")

    if st.button("이전 단계로"):
        st.session_state.step = 1
        st.rerun()
