import streamlit as st
import unicodedata

# THE LAST COMMIT – 12A
# Стартиране локално:
#   pip install streamlit
#   streamlit run app.py
#
# За споделяне с класната: публикувайте проекта в Streamlit Community Cloud
# и ѝ изпратете получения линк.

st.set_page_config(
    page_title="THE LAST COMMIT | 12А",
    page_icon="🔐",
    layout="centered"
)

# ---------- ДИЗАЙН ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(145deg, #100d18 0%, #21152b 55%, #120f19 100%);
        color: #f7f0ff;
    }
    h1, h2, h3, p, label, div {
        color: #f7f0ff;
    }
    .hero {
        padding: 28px 20px;
        border: 1px solid #76548f;
        border-radius: 18px;
        background: rgba(35, 24, 47, .88);
        text-align: center;
        margin-bottom: 20px;
    }
    .eyebrow {
        color: #c9a5e8;
        letter-spacing: 4px;
        font-size: 12px;
        font-weight: 700;
    }
    .hero h1 {
        font-size: 36px;
        margin: 12px 0 4px 0;
        color: #ead8ff;
    }
    .hero p {
        color: #d8c8e6;
        margin-bottom: 0;
    }
    .panel {
        padding: 22px;
        border: 1px solid #59406e;
        border-radius: 16px;
        background: rgba(28, 21, 38, .92);
        margin: 12px 0;
    }
    .level {
        color: #c9a5e8;
        font-size: 12px;
        letter-spacing: 2px;
        font-weight: 700;
    }
    .location {
        color: #d9b8f5;
        font-weight: 700;
    }
    .small {
        color: #c8b8d5;
        font-size: 13px;
    }
    .success {
        padding: 14px;
        border-radius: 12px;
        background: #183528;
        border: 1px solid #3d8b65;
        color: #e0ffed;
    }
    .stTextInput input {
        background: #f7f0ff;
        color: #21152b;
        border-radius: 10px;
    }
    .stButton button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid #b58bd8;
        background: #79519b;
        color: white;
        font-weight: 700;
        min-height: 46px;
    }
    .stButton button:hover {
        background: #9468b8;
        color: white;
        border-color: #d9b8f5;
    }
    hr {
        border-color: #59406e;
    }
</style>
""", unsafe_allow_html=True)

# ---------- ЗАГАДКИ ----------
# При нужда редактирайте текстовете, местата и отговорите.
# Може да добавяте няколко допустими начина на изписване.

levels = [
    {
        "title": "Ниво 1 – Началото",
        "place": "Релефната карта на България при училището",
        "type": "C++ Challenge",
        "story": "Първата следа е скрита в един кратък програмен код.",
        "question": """Какво ще изведе програмата?

```cpp
int a = 17;
int b = 78;
cout << a * 100 + b;
```""",
        "hint": "Първо умножете 17 по 100, а след това прибавете 78.",
        "answers": ["1778"],
        "success": "Правилно! Получихте 1778. Следващата следа ви очаква при часовниковата кула.",
        "next": "Отидете до Часовниковата кула в Дряново."
    },
    {
        "title": "Ниво 2 – Времето",
        "place": "Часовниковата кула",
        "type": "Logic Challenge",
        "story": "Времето пази следващия ключ. Решете задачата, за да продължите.",
        "question": """Какъв е резултатът?

```cpp
int x = 18;
int y = 59;
cout << x * 100 + y;
```""",
        "hint": "Изчислете 18 × 100 + 59.",
        "answers": ["1859"],
        "success": "Кодът е приет. 1859 е годината, която ви насочва към следващия дом.",
        "next": "Следващата локация е Икономовата къща."
    },
    {
        "title": "Ниво 3 – Езикът на машините",
        "place": "Икономовата къща",
        "type": "Binary / ASCII Challenge",
        "story": "Компютърът говори с нули и единици. Превърнете двоичния код в текст.",
        "question": """Разчетете шестте ASCII байта:

```text
01001110 01001001 01001011
01001111 01001100 01000001
```

Въведете получената дума.""",
        "hint": "Всеки осембитов блок е един ASCII символ.",
        "answers": ["NIKOLA", "НИКОЛА"],
        "success": "Отлично! Разчетохте името NIKOLA.",
        "next": "Потърсете църквата „Св. Никола“."
    },
    {
        "title": "Ниво 4 – Следата на майстора",
        "place": "Църквата „Св. Никола“",
        "type": "Riddle Challenge",
        "story": "Следващата следа не е скрита в код, а в една забележителност на Дряново.",
        "question": """Аз свързвам два бряга,
над река стоя,
а името на голям майстор
завинаги нося.

Какво съм аз?""",
        "hint": "Помислете за съоръжение, по което хората преминават над река.",
        "answers": ["МОСТ", "МОСТЪТ", "МОСТА", "МОСТЪТ НА КОЛЮ ФИЧЕТО",
                    "МОСТ НА КОЛЮ ФИЧЕТО"],
        "success": "Точно така! Намерихте следата на майстора.",
        "next": "Отидете до моста на Колю Фичето."
    },
    {
        "title": "Ниво 5 – Къщата без пирони",
        "place": "Мостът на Колю Фичето",
        "type": "History Challenge",
        "story": "Време е за загадка, в която историята среща наблюдателността.",
        "question": """В Дряново има възрожденска къща,
известна с прозвището „Къщата без пирони“.

Как се нарича тя?""",
        "hint": "Името ѝ започва с „Л“.",
        "answers": ["ЛАФЧИЕВАТА КЪЩА", "ЛАФЧИЕВА КЪЩА",
                    "КЪЩАТА БЕЗ ПИРОНИ"],
        "success": "Поздравления! Разпознахте Лафчиевата къща.",
        "next": "Следващата следа ви очаква при Лафчиевата къща."
    },
    {
        "title": "Ниво 6 – Последният код",
        "place": "Лафчиевата къща",
        "type": "Alphabet Cipher",
        "story": "Последният код ще ви покаже къде приключва мисията.",
        "question": """Използвайте българската азбука:
А = 1, Б = 2, В = 3 и така нататък.

Разчетете:

```text
16 – 12 – 15 – 26 – 1 – 5
```""",
        "hint": "Потърсете думата, която означава открито обществено пространство в града.",
        "answers": ["ПЛОЩАД"],
        "success": "Последният код е отключен!",
        "next": "Отидете до паметника „Майка България“ на площад „Освобождение“."
    }
]

# ---------- ПОМОЩНИ ФУНКЦИИ ----------
def normalize(value):
    value = unicodedata.normalize("NFKC", value).strip().upper()
    value = " ".join(value.split())
    return value

if "unlocked" not in st.session_state:
    st.session_state.unlocked = 0

if "mission_started" not in st.session_state:
    st.session_state.mission_started = False

if "hints" not in st.session_state:
    st.session_state.hints = set()

if "finished" not in st.session_state:
    st.session_state.finished = False

# ---------- ЗАГЛАВИЕ ----------
st.markdown("""
<div class="hero">
    <div class="eyebrow">CLASSIFIED MISSION · 2027</div>
    <h1>THE LAST COMMIT</h1>
    <p>12А · Последният проект</p>
    <p class="small">Някои проекти приключват. Други остават завинаги.</p>
</div>
""", unsafe_allow_html=True)

st.progress(min(st.session_state.unlocked / len(levels), 1.0))
st.caption(f"Отключени нива: {st.session_state.unlocked} от {len(levels)}")

# ---------- НАЧАЛЕН ЕКРАН ----------
if not st.session_state.mission_started:
    st.markdown("""
    <div class="panel">
        <div class="level">ВХОДЯЩО СЪОБЩЕНИЕ</div>
        <h2>Добре дошли в мисията, госпожо!</h2>
        <p>Вашата система е избрана за специален проект на 12А.</p>
        <p>Пред Вас има поредица от заключени нива. Всяко правилно решение ще отключи следващата следа.</p>
        <p><b>Правило:</b> следващото ниво се показва само след правилен отговор.</p>
        <p class="small">SYSTEM STATUS: WAITING FOR INPUT...</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("СТАРТИРАЙ МИСИЯТА"):
        st.session_state.mission_started = True
        st.rerun()

# ---------- АКТИВНО НИВО ----------
if st.session_state.mission_started and st.session_state.unlocked < len(levels):
    i = st.session_state.unlocked
    level = levels[i]

    st.markdown(f"""
    <div class="panel">
        <div class="level">{level['type'].upper()}</div>
        <h2>{level['title']}</h2>
        <p class="location">📍 {level['place']}</p>
        <p>{level['story']}</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("### 🔐 Вашата задача")
        st.markdown(level["question"])

        answer = st.text_input(
            "Въведете отговора:",
            key=f"answer_{i}",
            placeholder="Напишете отговора тук..."
        )

        if st.button("ПРОВЕРИ ОТГОВОРА", key=f"check_{i}"):
            accepted = [normalize(a) for a in level["answers"]]
            if normalize(answer) in accepted:
                st.session_state.unlocked += 1
                st.session_state.hints.discard(i)
                st.session_state[f"success_{i}"] = True
                st.rerun()
            else:
                st.error("Достъпът е отказан. Отговорът не е правилен. Опитайте отново!")

        if i not in st.session_state.hints:
            if st.button("ПОКАЖИ ПОДСКАЗКА", key=f"hint_{i}"):
                st.session_state.hints.add(i)
                st.rerun()
        else:
            st.info("Подсказка: " + level["hint"])

# ---------- ПОСЛЕДНО ОТКЛЮЧЕНО НИВО ----------
# Показва потвърждение за предишното ниво, без да разкрива бъдещите задачи.
completed = st.session_state.unlocked - 1
if st.session_state.mission_started and completed >= 0 and completed < len(levels):
    if st.session_state.get(f"success_{completed}", False):
        st.markdown(f"""
        <div class="success">
            <b>✓ {levels[completed]['success']}</b><br><br>
            {levels[completed]['next']}
        </div>
        """, unsafe_allow_html=True)
        st.session_state[f"success_{completed}"] = False

# ---------- ФИНАЛ ----------
if st.session_state.mission_started and st.session_state.unlocked == len(levels):
    st.balloons()
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">ALL LEVELS COMPLETED</div>
        <h1>SYSTEM SUCCESS</h1>
        <p>Достигнахте финалната локация.</p>
    </div>
    <div class="panel">
        <h2>Скъпа госпожо,</h2>
        <p>Успешно преминахте всички нива.</p>
        <p>Открихте кодовете, разгадавахте загадките и стигнахте до финала.</p>
        <p>Но има нещо, което нито един програмист не може да създаде с няколко реда код – спомените.</p>
        <p>През годините заедно написахме една история, в която имаше много грешки, смях, трудни моменти, нови версии и безброй незабравими мигове.</p>
        <p>Вие бяхте човекът, който ни водеше през всички тях.</p>
        <h3 style="color:#e2c4ff; text-align:center;">
            Госпожо, ще бъдете ли наш специален гост на абитуриентския ни бал?
        </h3>
        <p style="text-align:center;">С обич, Вашият 12А клас ❤️</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### FINAL PROJECT · CLASS 12А")
    st.caption("Error 404: По-добра класна не е намерена.")

st.divider()
st.caption("THE LAST COMMIT · A special mission created by 12А")
