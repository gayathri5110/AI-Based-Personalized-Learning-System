import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(
    page_title="AI-Based Personalized Learning System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Based Personalized Learning System")
st.write("Learn smarter with personalized recommendations based on your performance.")

# ---------------- SIDEBAR ----------------

st.sidebar.header("👨‍🎓 Student Details")

name = st.sidebar.text_input("Student Name", "Student")

level = st.sidebar.selectbox(
    "Learning Level",
    ["Beginner", "Intermediate", "Advanced"]
)

subject = st.sidebar.selectbox(
    "Select Subject",
    ["Python", "Java", "DBMS", "Data Structures", "Machine Learning"]
)

hours = st.sidebar.slider(
    "Daily Study Hours",
    1,
    8,
    2
)

# ---------------- TOPICS ----------------

topics = {
    "Python": [
        "Variables",
        "Loops",
        "Functions",
        "Lists",
        "Dictionaries"
    ],
    "Java": [
        "Variables",
        "Classes & Objects",
        "Inheritance",
        "Arrays",
        "Exception Handling"
    ],
    "DBMS": [
        "SQL",
        "Keys",
        "Normalization",
        "Joins",
        "Transactions"
    ],
    "Data Structures": [
        "Arrays",
        "Linked Lists",
        "Stacks",
        "Queues",
        "Trees"
    ],
    "Machine Learning": [
        "Regression",
        "Classification",
        "Clustering",
        "Feature Engineering",
        "Model Evaluation"
    ]
}

selected_topics = topics[subject]

# ---------------- QUIZ ----------------

st.header("📝 Learning Assessment")

st.write(
    f"Enter your scores for each topic in **{subject}**."
)

scores = {}

for topic in selected_topics:
    scores[topic] = st.slider(
        topic,
        min_value=0,
        max_value=100,
        value=50
    )

if st.button("🚀 Analyze My Performance"):

    # ---------------- ANALYSIS ----------------

    average_score = np.mean(list(scores.values()))

    weak_topics = [
        topic for topic, score in scores.items()
        if score < 50
    ]

    medium_topics = [
        topic for topic, score in scores.items()
        if 50 <= score < 75
    ]

    strong_topics = [
        topic for topic, score in scores.items()
        if score >= 75
    ]

    # ---------------- PERFORMANCE ----------------

    st.subheader("📊 Performance Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Score", f"{average_score:.1f}%")

    with col2:
        st.metric("Strong Topics", len(strong_topics))

    with col3:
        st.metric("Weak Topics", len(weak_topics))

    # ---------------- PERFORMANCE LEVEL ----------------

    if average_score >= 80:
        performance = "Excellent 🌟"
    elif average_score >= 60:
        performance = "Good 👍"
    elif average_score >= 40:
        performance = "Needs Improvement 📚"
    else:
        performance = "Beginner Level 🌱"

    st.success(f"Overall Performance: **{performance}**")

    # ---------------- TOPIC ANALYSIS ----------------

    st.subheader("🔍 Topic-wise Analysis")

    result_df = pd.DataFrame({
        "Topic": list(scores.keys()),
        "Score": list(scores.values())
    })

    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True
    )

    # ---------------- CHART ----------------

    st.subheader("📈 Performance Chart")

    fig, ax = plt.subplots()

    ax.bar(
        result_df["Topic"],
        result_df["Score"]
    )

    ax.set_xlabel("Topics")
    ax.set_ylabel("Score (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Student Topic Performance")

    plt.xticks(rotation=30)

    st.pyplot(fig)

    # ---------------- WEAK AREAS ----------------

    st.subheader("⚠️ Topics That Need Improvement")

    if weak_topics:
        for topic in weak_topics:
            st.warning(
                f"📌 {topic} - Practice this topic more."
            )
    else:
        st.success("🎉 No major weak topics found!")

    # ---------------- RECOMMENDATIONS ----------------

    st.subheader("🤖 Personalized Recommendations")

    if weak_topics:

        for topic in weak_topics:

            st.write(
                f"### 📖 {topic}"
            )

            st.write(
                f"Spend around 30–45 minutes learning **{topic}** "
                f"and solve at least 5 practice questions."
            )

    if medium_topics:

        st.write("### 📚 Topics to Revise")

        for topic in medium_topics:
            st.write(
                f"🔹 Revise **{topic}** and practice additional questions."
            )

    if strong_topics:

        st.write("### ⭐ Strong Topics")

        for topic in strong_topics:
            st.write(
                f"✅ **{topic}** - Try advanced-level problems."
            )

    # ---------------- ML MODEL ----------------

    st.subheader("🧠 AI Performance Prediction")

    # Sample training data
    X_train = np.array([
        [30, 1],
        [40, 1],
        [50, 2],
        [60, 2],
        [70, 3],
        [80, 4],
        [90, 5],
        [95, 6]
    ])

    y_train = np.array([
        35,
        42,
        50,
        62,
        70,
        78,
        88,
        94
    ])

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predicted_score = model.predict(
        [[average_score, hours]]
    )[0]

    predicted_score = max(
        0,
        min(100, predicted_score)
    )

    st.info(
        f"🎯 Predicted future performance: "
        f"**{predicted_score:.1f}%**"
    )

    # ---------------- STUDY PLAN ----------------

    st.subheader("📅 Personalized Study Plan")

    if weak_topics:
        study_topic = weak_topics[0]
    elif medium_topics:
        study_topic = medium_topics[0]
    else:
        study_topic = strong_topics[0]

    study_minutes = hours * 60

    st.write(
        f"""
        **Student:** {name}

        **Subject:** {subject}

        **Level:** {level}

        **Daily Study Time:** {hours} hours

        **Priority Topic:** {study_topic}

        **Recommended Plan:**
        - 📖 40% – Learn concepts
        - ✍️ 30% – Practice questions
        - 🧪 20% – Take quizzes
        - 🔄 10% – Revise previous topics
        """
    )

    st.success(
        "Your personalized learning plan has been generated! 🎓"
    )