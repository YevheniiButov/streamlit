# modules/bi_toets.py

import streamlit as st
# from utils.progress import add_score # <-- УДАЛЕНО: Больше не сохраняем прогресс

# --- Тексты для Перевода ---
# Добавляем словари для разных языков
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
    # TODO: Добавить переводы для других языков (uk, es, pt, tr, fa)
}

# --- Вопросы (остаются здесь для простоты) ---
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

# === Инициализация состояния сессии Streamlit ===
def initialize_state():
    if "bi_q_index" not in st.session_state:
        st.session_state.bi_q_index = 0
    if "bi_score" not in st.session_state:
        st.session_state.bi_score = 0
    if "bi_confirmed" not in st.session_state:
        st.session_state.bi_confirmed = False
    if "bi_done" not in st.session_state:
        st.session_state.bi_done = False
    # Инициализация для хранения выбранных ответов (чтобы они не сбрасывались)
    for i in range(len(questions)):
        if f"selected_{i}" not in st.session_state:
            st.session_state[f"selected_{i}"] = None

# === Функция отображения ===
def render(lang="en"): # Принимаем lang, по умолчанию 'en'
    # Получаем тексты для текущего языка
    t = texts.get(lang, texts["en"]) # Используем английский, если перевод не найден

    st.title(t["title"])

    # Инициализируем состояние, если еще не сделано
    initialize_state()

    # --- Отображение финального результата ---
    if st.session_state.bi_done:
        st.success(t["final_score_message"].format(score=st.session_state.bi_score, total=len(questions)))
        if st.button(t["restart_button"]):
            # Сброс состояния для начала нового теста
            st.session_state.bi_q_index = 0
            st.session_state.bi_score = 0
            st.session_state.bi_confirmed = False
            st.session_state.bi_done = False
            # Сброс выбранных ответов
            for i in range(len(questions)):
                st.session_state[f"selected_{i}"] = None
            st.rerun() # Перезапускаем скрипт для отображения первого вопроса
        return # Завершаем выполнение функции render

    # --- Отображение текущего вопроса ---
    current_index = st.session_state.bi_q_index
    q = questions[current_index]

    st.markdown(f"### {t['question_header'].format(q_num=current_index + 1, total=len(questions))}")
    st.write(f"**{q['question']}**")

    # Ключ для виджета radio должен быть уникальным для каждого вопроса
    radio_key = f"q_{current_index}"

    # Если ответ еще не подтвержден (st.session_state.bi_confirmed == False)
    if not st.session_state.bi_confirmed:
        # Отображаем радио-кнопки
        selected_option = st.radio(
            t["choose_answer"],
            q['options'],
            key=radio_key,
            # Устанавливаем значение по умолчанию из session_state, если оно там уже есть
            index=q['options'].index(st.session_state[f"selected_{current_index}"]) if st.session_state[f"selected_{current_index}"] in q['options'] else None
        )
        # Сохраняем выбор пользователя в session_state СРАЗУ при изменении radio
        st.session_state[f"selected_{current_index}"] = selected_option

        # Кнопка подтверждения
        if st.button(t["confirm_button"]):
            if selected_option is None:
                st.warning("Пожалуйста, выберите ответ.") # TODO: Translate
            else:
                # Проверяем ответ
                if selected_option == q['answer']:
                    st.session_state.bi_score += 1 # Увеличиваем счет только при правильном ответе
                    # add_score("bi_toets") # <-- УДАЛЕНО
                # Показываем результат и объяснение
                st.session_state.bi_confirmed = True # Ставим флаг, что ответ подтвержден
                st.rerun() # Перезапускаем скрипт, чтобы перейти к отображению подтвержденного состояния

    # Если ответ уже подтвержден (st.session_state.bi_confirmed == True)
    else:
        # Показываем выбранный ответ пользователя
        st.markdown(f"{t['your_answer_label']} {st.session_state[f'selected_{current_index}']}")

        # Показываем результат (верно/неверно) и объяснение
        if st.session_state[f"selected_{current_index}"] == q['answer']:
            st.success(t["correct_feedback"])
        else:
            st.error(t["incorrect_feedback"])
        if q.get("explanation"): # Показываем объяснение, если оно есть
             st.info(f"{t['explanation_info']} {q['explanation']}")

        # Показываем кнопку "Следующий вопрос" или "Посмотреть результат"
        if current_index + 1 < len(questions):
            if st.button(t["next_button"]):
                st.session_state.bi_q_index += 1 # Переходим к следующему вопросу
                st.session_state.bi_confirmed = False # Сбрасываем флаг подтверждения для нового вопроса
                st.rerun() # Перезапускаем для отображения нового вопроса
        else: # Это был последний вопрос
            if st.button(t["result_button"]):
                st.session_state.bi_done = True # Ставим флаг, что тест завершен
                st.rerun() # Перезапускаем для отображения финального результата