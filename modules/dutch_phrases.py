import streamlit as st
import random

phrases = [
    {"nl": "Open je mond alsjeblieft", "en": "Please open your mouth"},
    {"nl": "Bijt alstublieft niet", "en": "Please don’t bite"},
    {"nl": "Iets meer openen", "en": "Open a little more"},
    {"nl": "Hoofd stilhouden, alstublieft", "en": "Keep your head still, please"},
    {"nl": "Gaat het?", "en": "Are you okay?"},
    {"nl": "Spoel uw mond alstublieft", "en": "Please rinse your mouth"},
    {"nl": "Voelt u pijn?", "en": "Do you feel pain?"},
    {"nl": "Ik ga nu verdoven", "en": "I am going to numb now"},
]

texts = {
    "en": {
        "title": "💬 Dutch Phrases for Dentists",
        "dutch_phrase": "Dutch Phrase:",
        "show_translation": "Show Translation",
        "hide_translation": "Hide Translation",
        "translation_label": "💡 English:",
        "next_button": "Next Phrase"
    },
    "ru": {
        "title": "💬 Голландские фразы для стоматологов",
        "dutch_phrase": "Фраза на голландском:",
        "show_translation": "Показать перевод",
        "hide_translation": "Скрыть перевод",
        "translation_label": "💡 Английский:",
        "next_button": "Следующая фраза"
    },
    "nl": {
        "title": "💬 Nederlandse Zinnen voor Tandartsen",
        "dutch_phrase": "Nederlandse Zin:",
        "show_translation": "Toon Vertaling",
        "hide_translation": "Verberg Vertaling",
        "translation_label": "💡 Engels:",
        "next_button": "Volgende Zin"
    },
    "uk": {
        "title": "💬 Голландські фрази для стоматологів",
        "dutch_phrase": "Фраза голландською:",
        "show_translation": "Показати переклад",
        "hide_translation": "Сховати переклад",
        "translation_label": "💡 Англійська:",
        "next_button": "Наступна фраза"
    },
    "es": {
        "title": "💬 Frases en neerlandés para dentistas",
        "dutch_phrase": "Frase en neerlandés:",
        "show_translation": "Mostrar traducción",
        "hide_translation": "Ocultar traducción",
        "translation_label": "💡 Inglés:",
        "next_button": "Siguiente frase"
    },
    "tr": {
        "title": "💬 Diş Hekimleri için Hollandaca İfadeler",
        "dutch_phrase": "Hollandaca İfade:",
        "show_translation": "Çeviriyi Göster",
        "hide_translation": "Çeviriyi Gizle",
        "translation_label": "💡 İngilizce:",
        "next_button": "Sonraki İfade"
    },
    "fa": {
        "title": "💬 عبارات هلندی برای دندانپزشکان",
        "dutch_phrase": "عبارت هلندی:",
        "show_translation": "نمایش ترجمه",
        "hide_translation": "پنهان کردن ترجمه",
        "translation_label": "💡 انگلیسی:",
        "next_button": "عبارت بعدی"
    },
    "pt": {
        "title": "💬 Frases em holandês para dentistas",
        "dutch_phrase": "Frase em holandês:",
        "show_translation": "Mostrar tradução",
        "hide_translation": "Ocultar tradução",
        "translation_label": "💡 Inglês:",
        "next_button": "Próxima frase"
    }
}

def render(lang="en"):
    t = texts.get(lang, texts["en"])

    st.title(t["title"])

    if "dutch_phrase_index" not in st.session_state:
        st.session_state.dutch_phrase_index = random.randrange(len(phrases))
    if "show_translation" not in st.session_state:
        st.session_state.show_translation = False

    current_index = st.session_state.dutch_phrase_index
    phrase = phrases[current_index]

    st.write(t["dutch_phrase"])
    st.header(f"🦷 {phrase['nl']}")

    st.session_state.show_translation = st.toggle(
        t["show_translation"] if not st.session_state.show_translation else t["hide_translation"],
        key="show_translation_toggle"
    )

    if st.session_state.show_translation:
        st.info(f"{t['translation_label']} {phrase['en']}")

    st.markdown("---")

    if st.button(t["next_button"]):
        if len(phrases) > 1:
            new_index = current_index
            while new_index == current_index:
                new_index = random.randrange(len(phrases))
            st.session_state.dutch_phrase_index = new_index
        else:
             st.session_state.dutch_phrase_index = 0

        st.session_state.show_translation = False
        st.rerun()