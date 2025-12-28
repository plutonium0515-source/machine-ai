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
# 3단계: 기능 정의
# -------------------------
elif st.session_state.step == 3:
    st.title("🤖 로봇 제작 알고리즘")
    st.header("3단계: 기능 정의")

    # -------------------------
    # 2단계 요약
    # -------------------------
    st.subheader("🔹 2단계 요약")
    st.json(st.session_state.step2_data)
    st.divider()

    # -------------------------
    # 기본 기능 자동 생성 (최초 1회)
    # -------------------------
    if "functions" not in st.session_state:
        st.session_state.functions = [
            {"text": "직진할 수 있어야 한다", "enabled": True},
            {"text": "방향을 바꿀 수 있어야 한다", "enabled": True},
            {"text": "멈출 수 있어야 한다", "enabled": True},
        ]

    # -------------------------
    # 기능 목록 (활성 / 비활성)
    # -------------------------
    st.subheader("📌 기능 목록 (활성 / 비활성 가능)")

    for i, func in enumerate(st.session_state.functions):
        col1, col2 = st.columns([8, 1])

        with col1:
            if func["enabled"]:
                st.markdown(f"**{i+1}. {func['text']}**")
            else:
                st.markdown(
                    f"<span style='color:gray; text-decoration:line-through;'>"
                    f"{i+1}. {func['text']}</span>",
                    unsafe_allow_html=True
                )

        with col2:
            if func["enabled"]:
                if st.button("⛔", key=f"off_{i}"):
                    st.session_state.functions[i]["enabled"] = False
                    st.rerun()
            else:
                if st.button("✅", key=f"on_{i}"):
                    st.session_state.functions[i]["enabled"] = True
                    st.rerun()

    # -------------------------
    # 기능 추가
    # -------------------------
    st.divider()
    st.subheader("➕ 기능 추가")

    new_func = st.text_input(
        "추가할 기능을 동작 형태로 입력",
        placeholder="예: 원격 조종이 가능해야 한다"
    )

    if st.button("기능 추가"):
        if new_func.strip():
            st.session_state.functions.append({
                "text": new_func,
                "enabled": True
            })
            st.rerun()

    # -------------------------
    # 단계 이동
    # -------------------------
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("이전 단계"):
            st.session_state.step = 2
            st.rerun()

    with col2:
        if st.button("다음 단계"):
            # 활성 기능만 다음 단계로 전달
            st.session_state.step3_data = [
                f["text"] for f in st.session_state.functions if f["enabled"]
            ]
            st.session_state.step = 4
            st.rerun()
