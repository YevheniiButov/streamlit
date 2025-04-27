# modules/flashcards.py

import streamlit as st
import random

words = {
    "tandarts": "dentist",
    "wortelkanaal": "root canal",
    "kies": "molar",
    "tandvlees": "gum",
    "röntgenfoto": "X-ray",
    "verdoving": "anesthesia",
    "vulling": "filling",
    "extractie": "extraction"
}
word_keys = list(words.keys())

texts = {
    "en": {
        "title": "🧠 Flashcards for Dentists",
        "what_means": "👉 What does this word mean:",
        "show_translation": "Show Translation",
        "hide_translation": "Hide Translation",
        "translation_label": "✅ English:",
        "next_button": "Next Card"
    },
    "ru": {
        "title": "🧠 Карточки для Стоматологов",
        "what_means": "👉 Что означает это слово:",
        "show_translation": "Показать перевод",
        "hide_translation": "Скрыть перевод",
        "translation_label": "✅ Английский:",
        "next_button": "Следующая карточка"
    },
    "nl": {
        "title": "🧠 Flashcards voor Tandartsen",
        "what_means": "👉 Wat betekent het woord:",
        "show_translation": "Toon Vertaling",
        "hide_translation": "Verberg Vertaling",
        "translation_label": "✅ Engels:",
        "next_button": "Volgende Kaart"
    }
    # TODO: Add other languages uk, es, pt, tr, fa
}

def render(lang="en"):
    t = texts.get(lang, texts["en"])

    st.title(t["title"])

    if "flashcard_word_key" not in st.session_state:
        if word_keys: # Ensure word_keys is not empty before choosing
             st.session_state.flashcard_word_key = random.choice(word_keys)
        else:
             st.session_state.flashcard_word_key = None

    if "show_translation_flashcard" not in st.session_state:
        st.session_state.show_translation_flashcard = False

    # Handle case where words dictionary might be empty initially
    if st.session_state.flashcard_word_key is None and not word_keys:
        # Provide translations for the warning message
        warning_texts = {
            "en": "No words available for flashcards.",
            "ru": "Нет слов для карточек.",
            "nl": "Geen woorden beschikbaar voor flashcards.",
            "uk": "Немає слів для карток.",
            "es": "No hay palabras disponibles para las tarjetas.",
            "tr": "Bilgi kartları için kelime mevcut değil.",
            "fa": "کلمه ای برای فلش کارت موجود نیست.",
            "pt": "Nenhuma palavra disponível para flashcards."
        }
        st.warning(warning_texts.get(lang, warning_texts["en"]))
        return # Exit the function if no words

    current_key = st.session_state.flashcard_word_key
    # Ensure current_key is not None before accessing words dict
    if current_key:
        english_translation = words.get(current_key, "Translation not found")
    else:
        # Fallback if something went wrong with state initialization
        st.error("Error: Could not load a word.")
        return

    st.write(t["what_means"])
    st.header(f"📘 {current_key}")

    st.session_state.show_translation_flashcard = st.toggle(
        t["show_translation"] if not st.session_state.show_translation_flashcard else t["hide_translation"],
        key="show_translation_flashcard_toggle"
    )

    if st.session_state.show_translation_flashcard:
        st.success(f"{t['translation_label']} {english_translation}")

    st.divider() # Use st.divider() instead of st.markdown("---")

    if st.button(t["next_button"]):
        if len(word_keys) > 1:
            new_key = current_key
            while new_key == current_key:
                new_key = random.choice(word_keys)
            st.session_state.flashcard_word_key = new_key
        elif len(word_keys) == 1:
             st.session_state.flashcard_word_key = word_keys[0]
        else:
             st.session_state.flashcard_word_key = None

        st.session_state.show_translation_flashcard = False
        st.rerun()