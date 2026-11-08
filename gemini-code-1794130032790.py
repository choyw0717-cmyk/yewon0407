import streamlit as st

st.set_page_config(page_title="Lyric2Poster Extension", page_icon="🎵")

st.title("🎵 Lyric2Poster (Extension Edition)")
st.write("가사를 입력하면 아트 브리프와 포스터 컨셉을 생성합니다.")

# 가사 입력 받기
song_title = st.text_input("곡 제목", value="예시 곡 제목")
artist = st.text_input("아티스트", value="예시 아티스트")
lyrics = st.text_area("가사 입력", value="여기에 가사를 입력하세요...", height=150)

if st.button("아트 브리프 및 포스터 생성"):
    st.subheader("1. Art Brief (Claude)")
    st.json({
        "summary": f"{song_title}의 가사를 바탕으로 한 아트 브리프 예시입니다.",
        "mood": ["wistful", "emotional"],
        "palette": ["#FF5733", "#C70039", "#900C3F"],
        "composition": "중앙 인물 배치 및 감성적인 분위기"
    })
    
    st.subheader("2. Generated Poster Concept")
    st.info(f"[{artist} - {song_title}] 포스터 생성 완료 (데모 버전)")