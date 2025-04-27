# modules/flashcards.py

import streamlit as st
import random
# from utils.progress import add_score # Removed: No persistent progress

# --- Word Data ---
# Dictionary mapping Dutch words to English translation
words = {
    "tandarts": "dentist",
    "wortelkanaal": "root canal",
    "kies": "molar",
    "tandvlees": "gum",
    "röntgenfoto": "X-ray",
    "verdoving": "anesthesia",
    "vulling": "filling", # Added example
    "extractie": "extraction" # Added example
}
# Convert keys to a list for indexing
word_keys = list(words.keys())

# --- Translations for UI elements ---
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

# --- Function to display the module ---
def render(lang="en"):
    # Get translations for the current language
    t = texts.get(lang, texts["en"]) # Default to English

    st.title(t["title"])

    # --- State Initialization ---
    if "flashcard_word_key" not in st.session_state:
        # Select a random starting word key
        st.session_state.flashcard_word_key = random.choice(word_keys)
    if "show_translation_flashcard" not in st.session_state:
        # Track if the translation should be shown
        st.session_state.show_translation_flashcard = False

    # --- Display Current Flashcard ---
    current_key = st.session_state.flashcard_word_key
    english_translation = words.get(current_key, "Translation not found")

    st.write(t["what_means"])
    st.header(f"📘 {current_key}") # Display the Dutch word

    # --- Show/Hide Translation Toggle ---
    # The toggle directly controls the session state variable
    st.session_state.show_translation_flashcard = st.toggle(
        t["show_translation"] if not st.session_state.show_translation_flashcard else t["hide_translation"],
        key="show_translation_flashcard_toggle" # Unique key for this toggle
    )

    # Conditionally display the translation
    if st.session_state.show_translation_flashcard:
        st.success(f"{t['translation_label']} {english_translation}")

    st.markdown("---") # Separator

    # --- Next Card Button ---
    if st.button(t["next_button"]):
        # Pick a new random key, different from the current one
        if len(word_keys) > 1:
            new_key = current_key
            while new_key == current_key:
                new_key = random.choice(word_keys)
            st.session_state.flashcard_word_key = new_key
        elif len(word_keys) == 1:
             st.session_state.flashcard_word_key = word_keys[0]
        else: # Handle empty words dictionary
             st.session_state.flashcard_word_key = None

        st.session_state.show_translation_flashcard = False # Reset translation visibility
        st.rerun() # Rerun script to display the new card

    # Handle case where words dictionary might be empty
    if st.session_state.flashcard_word_key is None and len(word_keys) == 0:
        st.warning("No words available for flashcards.")