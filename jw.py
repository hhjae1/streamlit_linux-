import streamlit as st

st.title("퀴즈 테스트 🎯")

st.subheader("문제 1. (객관식)")
st.write("파이썬에서 리스트의 길이를 구할 때 사용하는 함수는?")
mcq_answer = st.radio(
    "정답을 선택하세요:",
    ("len()", "size()", "length()", "count()")
)

st.subheader("문제 2. (주관식)")
st.write("자바에서 클래스를 실행할 수 있는 메서드 이름은 무엇인가요?")
subjective_answer = st.text_input("정답을 입력하세요:")

if st.button("제출"):
    # 정답 비교
    correct_mcq = mcq_answer == "len()"
    correct_subjective = subjective_answer.strip().lower() == "main"

    st.subheader("결과 ✅")
    st.write(f"문제 1 (객관식): {'정답입니다!' if correct_mcq else '오답입니다!'}")
    st.write(f"문제 2 (주관식): {'정답입니다!' if correct_subjective else '오답입니다!'}")
