# modules/bi_toets.py

import streamlit as st

texts = {
    "en": {
        "title": "🧪 BI-toets Preparation",
        "question_header": "Question {q_num} of {total}",
        "choose_answer": "Choose the correct answer:",
        "confirm_button": "Confirm",
        "correct_feedback": "✅ Correct!",
        "incorrect_feedback": "❌ Incorrect.",
        "explanation_info": "ℹ️ Explanation:",
        "your_answer_label": "**Your answer:**",
        "next_button": "Next Question",
        "result_button": "View Result",
        "final_score_message": "You answered {score} out of {total} correctly!",
        "restart_button": "🔁 Start Over"
    },
    "ru": {
        "title": "🧪 Подготовка к BI-toets",
        "question_header": "Вопрос {q_num} из {total}",
        "choose_answer": "Выберите правильный ответ:",
        "confirm_button": "Подтвердить",
        "correct_feedback": "✅ Верно!",
        "incorrect_feedback": "❌ Неверно.",
        "explanation_info": "ℹ️ Пояснение:",
        "your_answer_label": "**Ваш ответ:**",
        "next_button": "Следующий вопрос",
        "result_button": "Посмотреть результат",
        "final_score_message": "Вы правильно ответили на {score} из {total}!",
        "restart_button": "🔁 Начать сначала"
    },
    "nl": {
        "title": "🧪 BI-toets voorbereiding",
        "question_header": "Vraag {q_num} van {total}",
        "choose_answer": "Kies het juiste antwoord:",
        "confirm_button": "Bevestigen",
        "correct_feedback": "✅ Correct!",
        "incorrect_feedback": "❌ Onjuist.",
        "explanation_info": "ℹ️ Uitleg:",
        "your_answer_label": "**Je antwoord:**",
        "next_button": "Volgende vraag",
        "result_button": "Bekijk resultaat",
        "final_score_message": "Je hebt {score} van {total} goed beantwoord!",
        "restart_button": "🔁 Opnieuw beginnen"
    }
}

questions = [
    {
        "question": "Wat is de aanbevolen manier om instrumenten te steriliseren?",
        "options": ["In water met zeep", "Met alcohol", "Met een autoclaaf"],
        "answer": "Met een autoclaaf",
        "explanation": "Een autoclaaf doodt bacteriën, virussen en schimmels onder hoge druk en temperatuur."
    },
    {
        "question": "Wat hoort bij goede handhygiëne?",
        "options": ["Handschoenen hergebruiken", "Sieraden dragen", "Handen wassen voor en na contact"],
        "answer": "Handen wassen voor en na contact",
        "explanation": "Handen wassen voorkomt verspreiding van infecties."
    },
    {
        "question": "Wat betekent informed consent?",
        "options": ["De patiënt beslist na uitleg", "De arts beslist", "De verzekering beslist"],
        "answer": "De patiënt beslist na uitleg",
        "explanation": "De patiënt moet weten wat er gaat gebeuren en akkoord gaan."
    },
    {
        "question": "Wat is een mogelijk gevolg van onvoldoende sterilisatie?",
        "options": ["Verlies van instrumenten", "Verspreiding van infecties", "Geen effect"],
        "answer": "Verspreiding van infecties",
        "explanation": "Onvoldoende sterilisatie verhoogt het risico op kruisbesmetting."
    },
    {
        "question": "Wat is de functie van een medisch dossier?",
        "options": ["Voor administratie", "Voor onderzoek", "Voor communicatie en continuïteit van zorg"],
        "answer": "Voor communicatie en continuïteit van zorg",
        "explanation": "Een dossier helpt zorgverleners samen te werken en het verloop te volgen."
    }
]

def initialize_state():
    if "bi_q_index" not in st.session_state:
        st.session_state.bi_q_index = 0
    if "bi_score" not in st.session_state:
        st.session_state.bi_score = 0
    if "bi_confirmed" not in st.session_state:
        st.session_state.bi_confirmed = False
    if "bi_done" not in st.session_state:
        st.session_state.bi_done = False
    for i in range(len(questions)):
        if f"selected_{i}" not in st.session_state:
            st.session_state[f"selected_{i}"] = None

def render(lang="en"):
    t = texts.get(lang, texts["en"])

    st.title(t["title"])

    initialize_state()

    if st.session_state.bi_done:
        st.success(t["final_score_message"].format(score=st.session_state.bi_score, total=len(questions)))

        if st.session_state.bi_score == len(questions):
             st.balloons()
        elif st.session_state.bi_score >= len(questions) // 2: 
             pass 

        if st.button(t["restart_button"]):
            st.session_state.bi_q_index = 0
            st.session_state.bi_score = 0
            st.session_state.bi_confirmed = False
            st.session_state.bi_done = False
            for i in range(len(questions)):
                st.session_state[f"selected_{i}"] = None
            st.rerun()
        return

    current_index = st.session_state.bi_q_index
    q = questions[current_index]

    st.metric(label="Прогресс", value=f"{current_index + 1}/{len(questions)}")
    st.progress((current_index + 1) / len(questions))
    st.divider()


    st.markdown(f"### {t['question_header'].format(q_num=current_index + 1, total=len(questions))}")
    st.write(f"**{q['question']}**")

    radio_key = f"q_{current_index}"

    if not st.session_state.bi_confirmed:
        selected_option = st.radio(
            t["choose_answer"],
            q['options'],
            key=radio_key,
            index=q['options'].index(st.session_state[f"selected_{current_index}"]) if st.session_state[f"selected_{current_index}"] in q['options'] else None
        )
        st.session_state[f"selected_{current_index}"] = selected_option

        if st.button(t["confirm_button"]):
            if selected_option is None:
                 # Переводим сообщение об ошибке
                warning_texts = {
                    "en": "Please select an answer.",
                    "ru": "Пожалуйста, выберите ответ.",
                    "nl": "Selecteer alstublieft een antwoord.",
                    "uk": "Будь ласка, оберіть відповідь.",
                    "es": "Por favor, seleccione una respuesta.",
                    "tr": "Lütfen bir cevap seçin.",
                    "fa": "لطفا یک پاسخ انتخاب کنید.",
                    "pt": "Por favor, selecione uma resposta."
                }
                st.warning(warning_texts.get(lang, warning_texts["en"]))
            else:
                if selected_option == q['answer']:
                    st.session_state.bi_score += 1
                st.session_state.bi_confirmed = True
                st.rerun()

    else:
        st.markdown(f"{t['your_answer_label']} {st.session_state[f'selected_{current_index}']}")

        if st.session_state[f"selected_{current_index}"] == q['answer']:
            st.success(t["correct_feedback"])
        else:
            st.error(t["incorrect_feedback"])

    
        if q.get("explanation"):
            with st.expander(t["explanation_info"]):
                 st.write(q['explanation'])


        if current_index + 1 < len(questions):
            if st.button(t["next_button"]):
                st.session_state.bi_q_index += 1
                st.session_state.bi_confirmed = False
                st.rerun()
        else:
            if st.button(t["result_button"]):
                st.session_state.bi_done = True
                st.rerun()