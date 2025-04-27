# modules/syllabus.py

import streamlit as st
# from gtts import gTTS  # Commented out: TTS dependency
# import tempfile         # Commented out: TTS dependency
# from utils.progress import add_score # Removed: No persistent progress

# --- Chapter Content Imports ---
# Assuming these files exist in ../chapters/ relative to this file
try:
    from chapters import ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13
    chapters_modules = {
        # Using simple keys for easier lookup if needed
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
    chapters_modules = {} # Use empty dict if import fails

# --- Translations for UI elements ---
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

# --- Function to display the module ---
def render(lang="en"):
    # Get translations for the current language
    t = texts.get(lang, texts["en"]) # Default to English

    # --- Chapter Selection ---
    # Use chapter titles directly for selection
    chapter_titles = [ch_data["title"] for ch_key, ch_data in chapters_modules.items()]
    if not chapter_titles:
        st.warning("No chapters available.")
        return

    # Selectbox to choose chapter
    # Use title for display, key persists across reruns if using session state approach
    # Using index=None allows default selection based on order if key is not in session_state
    selected_title = st.selectbox(
        t["select_chapter"],
        chapter_titles,
        key="syllabus_chapter_select", # Key to store selection in session state
        index=None # No default index, first item will be selected initially
    )

    # Find the corresponding module object based on the selected title
    selected_module = None
    if selected_title:
        for ch_key, ch_data in chapters_modules.items():
            if ch_data["title"] == selected_title:
                selected_module = ch_data["module"]
                break

    if not selected_module or not hasattr(selected_module, "get_content"):
        st.error(f"Could not load content for selected chapter: '{selected_title}'")
        return

    # --- Load and Display Chapter Content ---
    try:
        chapter = selected_module.get_content() # Call the function in the chapter file
    except Exception as e:
        st.error(f"Error getting content from chapter module: {e}")
        return

    st.title(f"🦷 {selected_title}") # Display selected chapter title

    # Display Paragraphs (with optional TTS)
    if "paragraphs" in chapter and isinstance(chapter["paragraphs"], list):
        for i, p in enumerate(chapter["paragraphs"]):
            st.write(p)
            # --- Optional TTS ---
            # Uncomment the following block if you want Text-to-Speech
            # Make sure you have gTTS installed: pip install gTTS
            # Also note: creates temporary files and needs internet connection at runtime
            # if st.button(f"{t['speak_button']} ({p[:25]}...)", key=f"tts_{selected_title}_{i}"):
            #     try:
            #         tts = gTTS(p, lang='nl') # Assuming content is always Dutch for TTS
            #         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            #             tts.save(tmp.name)
            #             st.audio(tmp.name, format='audio/mp3')
            #             # Consider deleting the temp file later if needed: os.unlink(tmp.name)
            #     except Exception as e_tts:
            #         st.error(f"Could not generate audio: {e_tts}")
            # --- End Optional TTS ---
    else:
        st.warning("No paragraphs found for this chapter.")


    # Display Vocabulary
    if "vocab" in chapter and isinstance(chapter["vocab"], dict):
        st.markdown("---")
        st.subheader(t["vocab_title"])
        for k, v in chapter["vocab"].items():
            st.markdown(f"**{k}** → {v}")

    # Display Reflection Questions
    if "questions" in chapter and isinstance(chapter["questions"], list):
        st.markdown("---")
        st.subheader(t["questions_title"])
        for q in chapter["questions"]:
            st.markdown(f"- {q}")

    # Display Mini-Quiz
    if "quiz" in chapter and isinstance(chapter["quiz"], dict):
        st.markdown("---")
        st.subheader(t["quiz_title"])
        quiz = chapter["quiz"]
        quiz_question = quiz.get("question")
        quiz_options = quiz.get("options")
        quiz_answer = quiz.get("answer")
        quiz_explanation = quiz.get("explanation", "")

        if quiz_question and quiz_options and quiz_answer:
            # Use a unique key for the radio button based on chapter and question
            quiz_key = f"quiz_{selected_title}_{quiz_question[:20]}"
            selected = st.radio(quiz_question, quiz_options, key=quiz_key, index=None) # index=None avoids default selection

            if st.button(t["submit_answer"]):
                if selected == quiz_answer:
                    # add_score("syllabus") # Removed progress tracking
                    st.success(t["correct"])
                else:
                    st.error(t["incorrect"])
                st.caption(f"{t['explanation_info']} {quiz_explanation}") # Show explanation on submit
        else:
            st.warning("Mini-quiz data is incomplete for this chapter.")