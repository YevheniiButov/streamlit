# modules/syllabus.py

import streamlit as st

try:
    from chapters import ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13
    chapters_modules = {
        "ch1": {"title": "1 — Wat doet de tandarts?", "module": ch1},
        "ch2": {"title": "2 — Wie werken er in de tandartspraktijk?", "module": ch2},
        "ch3": {"title": "3 — De mond", "module": ch3},
        "ch4": {"title": "4 — De kies", "module": ch4},
        "ch5": {"title": "5 — Mondverzorging / Preventie", "module": ch5},
        "ch6": {"title": "6 — Angst voor de tandarts", "module": ch6},
        "ch7": {"title": "7 — Röntgenfoto’s", "module": ch7},
        "ch8": {"title": "8 — Tandartsbehandelingen", "module": ch8},
        "ch9": {"title": "9 — Aandoeningen in de mond", "module": ch9},
        "ch10": {"title": "10 — Woordenlijst", "module": ch10},
        "ch11": {"title": "11 — De tandartspraktijk", "module": ch11},
        "ch12": {"title": "12 — Hygiëne in de tandartspraktijk", "module": ch12},
        "ch13": {"title": "13 — Communicatie met patiënten", "module": ch13}
    }
except ImportError as e:
    st.error(f"Could not import chapter modules: {e}")
    chapters_modules = {}

texts = {
    "en": {
        "select_chapter": "📖 Choose a chapter:",
        "vocab_title": "📘 Vocabulary",
        "questions_title": "🧠 Questions to consider",
        "quiz_title": "🎯 Mini-Quiz",
        "submit_answer": "Confirm Answer",
        "correct": "Correct! Well done.",
        "incorrect": "Sorry, that's incorrect.",
        "explanation_info": "💡 Explanation:",
        "speak_button": "🔊 Speak"
    },
    "ru": {
        "select_chapter": "📖 Выберите главу:",
        "vocab_title": "📘 Словарь",
        "questions_title": "🧠 Вопросы для размышления",
        "quiz_title": "🎯 Мини-Квиз",
        "submit_answer": "Подтвердить ответ",
        "correct": "Верно! Отлично.",
        "incorrect": "К сожалению, неверно.",
        "explanation_info": "💡 Пояснение:",
        "speak_button": "🔊 Озвучить"
    },
    "nl": {
        "select_chapter": "📖 Kies een hoofdstuk:",
        "vocab_title": "📘 Woordenlijst",
        "questions_title": "🧠 Vragen om over na te denken",
        "quiz_title": "🎯 Mini-quiz",
        "submit_answer": "Bevestig je antwoord",
        "correct": "Correct! Goed gedaan.",
        "incorrect": "Helaas, dat is niet correct.",
        "explanation_info": "💡 Uitleg:",
        "speak_button": "🔊 Voorlezen"
    }
    # TODO: Add other languages uk, es, pt, tr, fa
}

def render(lang="en"):
    t = texts.get(lang, texts["en"])

    chapter_titles = [ch_data["title"] for ch_key, ch_data in chapters_modules.items()]
    if not chapter_titles:
        # Add translations for this warning
        warning_texts = {
            "en": "No chapters available.",
            "ru": "Нет доступных глав.",
            "nl": "Geen hoofdstukken beschikbaar.",
            "uk": "Немає доступних глав.",
            "es": "No hay capítulos disponibles.",
            "tr": "Kullanılabilir bölüm yok.",
            "fa": "هیچ فصلی در دسترس نیست.",
            "pt": "Nenhum capítulo disponível."
        }
        st.warning(warning_texts.get(lang, warning_texts["en"]))
        return

    selected_title = st.selectbox(
        t["select_chapter"],
        chapter_titles,
        key="syllabus_chapter_select",
        index=None
    )

    selected_module = None
    if selected_title:
        for ch_key, ch_data in chapters_modules.items():
            if ch_data["title"] == selected_title:
                selected_module = ch_data["module"]
                break

    if not selected_module or not hasattr(selected_module, "get_content"):
        # Add translations for this error
        error_texts = {
            "en": f"Could not load content for selected chapter: '{selected_title}'",
            "ru": f"Не удалось загрузить содержимое для выбранной главы: '{selected_title}'",
            "nl": f"Kon inhoud niet laden voor geselecteerd hoofdstuk: '{selected_title}'",
            "uk": f"Не вдалося завантажити вміст для вибраної глави: '{selected_title}'",
            "es": f"No se pudo cargar el contenido del capítulo seleccionado: '{selected_title}'",
            "tr": f"Seçilen bölüm için içerik yüklenemedi: '{selected_title}'",
            "fa": f"محتوای فصل انتخاب شده بارگیری نشد: '{selected_title}'",
            "pt": f"Não foi possível carregar o conteúdo do capítulo selecionado: '{selected_title}'"
        }
        st.error(error_texts.get(lang, error_texts["en"]))
        return

    try:
        chapter = selected_module.get_content()
    except Exception as e:
         # Add translations for this error
        error_texts = {
            "en": f"Error getting content from chapter module: {e}",
            "ru": f"Ошибка получения содержимого из модуля главы: {e}",
            "nl": f"Fout bij het ophalen van inhoud uit hoofdstukmodule: {e}",
            "uk": f"Помилка отримання вмісту з модуля глави: {e}",
            "es": f"Error al obtener el contenido del módulo del capítulo: {e}",
            "tr": f"Bölüm modülünden içerik alınırken hata oluştu: {e}",
            "fa": f"خطا در دریافت محتوا از ماژول فصل: {e}",
            "pt": f"Erro ao obter conteúdo do módulo do capítulo: {e}"
        }
        st.error(error_texts.get(lang, error_texts["en"]))
        return

    st.title(f"🦷 {selected_title}")

    # Using tabs for better organization
    tab_titles = {
        "en": ["📖 Text", "📘 Vocabulary", "🧠 Questions", "🎯 Quiz"],
        "ru": ["📖 Текст", "📘 Словарь", "🧠 Вопросы", "🎯 Квиз"],
        "nl": ["📖 Tekst", "📘 Woordenlijst", "🧠 Vragen", "🎯 Quiz"],
        "uk": ["📖 Текст", "📘 Словник", "🧠 Питання", "🎯 Квіз"],
        "es": ["📖 Texto", "📘 Vocabulario", "🧠 Preguntas", "🎯 Cuestionario"],
        "tr": ["📖 Metin", "📘 Kelime Bilgisi", "🧠 Sorular", "🎯 Test"],
        "fa": ["📖 متن", "📘 واژگان", "🧠 سوالات", "🎯 آزمون"],
        "pt": ["📖 Texto", "📘 Vocabulário", "🧠 Perguntas", "🎯 Quiz"]
    }
    current_tab_titles = tab_titles.get(lang, tab_titles["en"])
    tab1, tab2, tab3, tab4 = st.tabs(current_tab_titles)


    with tab1: # Text Tab
        if "paragraphs" in chapter and isinstance(chapter["paragraphs"], list):
            for i, p in enumerate(chapter["paragraphs"]):
                st.write(p)
        else:
             # Add translations for this warning
            warning_texts = {
                "en": "No paragraphs found for this chapter.",
                "ru": "Параграфы для этой главы не найдены.",
                "nl": "Geen paragrafen gevonden voor dit hoofdstuk.",
                "uk": "Параграфів для цієї глави не знайдено.",
                "es": "No se encontraron párrafos para este capítulo.",
                "tr": "Bu bölüm için paragraf bulunamadı.",
                "fa": "هیچ پاراگرافی برای این فصل یافت نشد.",
                "pt": "Nenhum parágrafo encontrado para este capítulo."
            }
            st.warning(warning_texts.get(lang, warning_texts["en"]))

    with tab2: # Vocabulary Tab
        if "vocab" in chapter and isinstance(chapter["vocab"], dict):
            st.subheader(t["vocab_title"])
            for k, v in chapter["vocab"].items():
                st.markdown(f"**{k}** → {v}")
        else:
            # Add translations for this warning (optional, could just be empty)
            st.info("No vocabulary listed for this chapter.")

    with tab3: # Questions Tab
        if "questions" in chapter and isinstance(chapter["questions"], list):
            st.subheader(t["questions_title"])
            for q in chapter["questions"]:
                st.markdown(f"- {q}")
        else:
             # Add translations for this warning (optional)
             st.info("No reflection questions listed for this chapter.")

    with tab4: # Quiz Tab
        if "quiz" in chapter and isinstance(chapter["quiz"], dict):
            st.subheader(t["quiz_title"])
            quiz = chapter["quiz"]
            quiz_question = quiz.get("question")
            quiz_options = quiz.get("options")
            quiz_answer = quiz.get("answer")
            quiz_explanation = quiz.get("explanation", "")

            if quiz_question and quiz_options and quiz_answer:
                quiz_key = f"quiz_{selected_title}_{quiz_question[:20]}"
                selected = st.radio(quiz_question, quiz_options, key=quiz_key, index=None)

                if st.button(t["submit_answer"], key=f"submit_{quiz_key}"): # Unique key for submit button
                    if selected is None:
                         # Add translations for this warning
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
                    elif selected == quiz_answer:
                        st.success(t["correct"])
                    else:
                        st.error(t["incorrect"])

                    # Show explanation in an expander after submission
                    if quiz_explanation:
                        with st.expander(t["explanation_info"]):
                            st.write(quiz_explanation)

            else:
                 # Add translations for this warning
                warning_texts = {
                    "en": "Mini-quiz data is incomplete for this chapter.",
                    "ru": "Данные мини-квиза для этой главы неполные.",
                    "nl": "Mini-quiz gegevens zijn onvolledig voor dit hoofdstuk.",
                    "uk": "Дані міні-квізу для цієї глави неповні.",
                    "es": "Los datos del mini-cuestionario están incompletos para este capítulo.",
                    "tr": "Bu bölüm için mini test verileri eksik.",
                    "fa": "داده های آزمون کوتاه برای این فصل ناقص است.",
                    "pt": "Os dados do mini-quiz estão incompletos para este capítulo."
                }
                st.warning(warning_texts.get(lang, warning_texts["en"]))
        else:
             # Add translations for this info (optional)
             st.info("No quiz available for this chapter.")