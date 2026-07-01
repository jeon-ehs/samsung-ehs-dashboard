import streamlit as st

# 1. 페이지 기본 설정 (코딩의 가장 첫 줄에 위치해야 합니다)
st.set_page_config(
    page_title="협력사 안전보건 정보제공 시스템",
    page_icon="🛡️",
    layout="wide"  # 전체 화면 너비 사용
)

# 2. 커스텀 CSS 주입 (CLINE SR의 styles.css 디자인을 Streamlit에 강제 적용)
# 이 부분이 UI를 전문가 수준으로 바꾸는 핵심입니다.
def local_css():
    st.markdown("""
        <style>
            /* Google Font 임포트 */
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

            /* 기본 폰트 및 배경색 */
            html, body, [class*="st-"] {
                font-family: 'Noto Sans KR', sans-serif;
                background-color: #F0F4F8; /* 전체 배경 */
            }

            /* Streamlit 기본 헤더 및 여백 제거 */
            header {visibility: hidden;}
            .main .block-container {
                padding-top: 1.5rem;
                padding-bottom: 1rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }

            /* 카드 UI 스타일 */
            [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
                background-color: white;
                border-radius: 16px;
                padding: 20px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                border: 1px solid #E2E8F0;
            }

            /* 탭(Tab) UI 커스텀 */
            [data-testid="stTabs"] button {
                background-color: #F0F4F8;
                border-radius: 12px;
                color: #5A6478;
                font-weight: 500;
                padding: 10px 18px;
                margin-right: 8px;
            }
            [data-testid="stTabs"] button[aria-selected="true"] {
                background-color: #1565C0;
                color: white;
                font-weight: 700;
            }

            /* 체크박스 스타일 */
            .stCheckbox {
                background-color: #F1F8E9;
                padding: 10px;
                border-radius: 8px;
            }

            /* 주황색 주의사항 박스 */
            .caution-box {
                background-color: #FFF3E0;
                border-radius: 10px;
                padding: 14px;
                display: flex;
                align-items: center;
                gap: 10px;
                border-left: 5px solid #F57C00;
                font-size: 14px;
                font-weight: 600;
                color: #E65100;
            }

            /* 보라색 법령 박스 */
            .regulation-box {
                background-color: #E8EAF6;
                border-radius: 10px;
                padding: 12px;
                display: flex;
                align-items: center;
                gap: 10px;
                font-size: 13px;
                color: #283593;
            }
        </style>
    """, unsafe_allow_html=True)

local_css()

# --- 화면 UI 구성 시작 ---

# 3. 상단 대시보드 (날씨 및 안전포인트)
st.markdown("##### 오늘의 날씨 및 안전대책")
col1, col2 = st.columns(2)

with col1:
    with st.container(): # 카드 UI 적용을 위한 컨테이너
        st.error("🚨 **폭염 주의** : 시설관리 업종 기준") # st.error가 붉은색 박스를 만듭니다.
        st.info("💧 **수분 섭취** : 30분 간격 주기적 실시")
        st.info("🌬️ **그늘진 휴식공간** : 현장 내 휴식 공간 확보")

with col2:
    with st.container():
        st.success("✅ **오늘의 안전 핵심포인트**") # st.success가 녹색 박스를 만듭니다.
        st.write("1. 폭염특보 시 휴식시간 연장")
        st.write("2. 수분 섭취 30분 간격")
        st.write("3. 그늘진 휴식공간 확보")
        st.write("4. 장마로 인한 침수 주의")


st.write("---") # 구분선

# 4. 업종별 탭 메뉴 구성
tab_titles = ["🏗️ 시설관리", "🧹 청소", "📦 물류", "🍳 식당", "🤝 서비스", "♻️ 폐기물처리", "🏭 제조"]
tabs = st.tabs(tab_titles)

# '시설관리' 탭 내용 구현
with tabs[0]:
    st.markdown("#### **밀폐공간 작업**")
    st.write(":blue[#시설관리 업종]")

    # 핵심포인트 4개 카드
    kp_cols = st.columns(4)
    with kp_cols[0]:
        st.warning("🔺 **산소농도 측정**\n\n산소농도 측정 (18~23.5%)")
    with kp_cols[1]:
        st.info("😷 **가스농도 측정 및 환기**\n\n유해가스 측정 및 환기")
    with kp_cols[2]:
        st.success("👥 **구조대기자 배치**\n\n구조대기자 배치 완료")
    with kp_cols[3]:
        st.success("✅ **작업허가서 확인**\n\n작업허가서 발급 확인")

    st.write("") # 간격

    # 안전점검 체크리스트
    st.markdown("###### ✅ 오늘의 안전점검 체크리스트")
    cl_cols = st.columns(4)
    with cl_cols[0]:
        st.checkbox("산소농도 측정기 비치")
    with cl_cols[1]:
        st.checkbox("유해가스 측정 및 환기")
    with cl_cols[2]:
        st.checkbox("구조대기자 배치 완료")
    with cl_cols[3]:
        st.checkbox("작업허가서 발급 확인")
    st.checkbox("안전보호구 착용 상태", value=True) # 기본 체크된 상태

    st.write("") # 간격

    # 주의사항 및 법령
    st.markdown('<div class="caution-box">⚠️ 산소농도 18% 미만 시 즉시 작업 중지</div>', unsafe_allow_html=True)
    st.markdown('<div class="regulation-box">📜 산업안전보건법 제37조 (밀폐공간 작업)</div>', unsafe_allow_html=True)


# 다른 탭들은 여기에 내용을 채워넣을 수 있습니다.
with tabs[1]:
    st.write("청소 업종 관련 콘텐츠가 여기에 표시됩니다.")
