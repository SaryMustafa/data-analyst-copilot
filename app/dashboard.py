import streamlit as st
import tempfile
import os
import matplotlib.pyplot as plt
import seaborn as sns

from report_history import save_report_history
from recommendations import generate_recommendations
from data_loader import load_csv
from analyzer import analyze_data
from insights import generate_insights
from ai_analyzer import generate_ai_analysis
from quality_score import calculate_quality_score
from html_report import generate_html_report


st.set_page_config(
    page_title="Data Analyst Copilot",
    layout="wide"
)


st.title("🤖 Data Analyst Copilot")

st.write(
    "AI-инструмент для автоматического анализа данных"
)


uploaded_file = st.file_uploader(
    "Загрузите CSV файл",
    type=["csv"]
)


if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv"
    ) as tmp:

        tmp.write(uploaded_file.getvalue())

        file_path = tmp.name


    df = load_csv(file_path)

    st.success(
    	f"Файл загружен: {uploaded_file.name}"
    )
    st.info(
    	f"Размер данных: {df.shape[0]} строк × {df.shape[1]} колонок"
    )	


    report = analyze_data(df)



    insights = generate_insights(report)

    report["insights"] = insights

    recommendations = generate_recommendations(report)


    report["quality_score"] = calculate_quality_score(report)


    try:
        ai_text = generate_ai_analysis(report)

    except Exception:
        ai_text = (
            "AI анализ недоступен. "
            "Проверьте запуск Ollama."
        )


    report["ai_analysis"] = ai_text


    generate_html_report(report)

    save_report_history(report)

    st.subheader("📊 Качество данных")

    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "📄 Строки",
            report["rows"]
        )


    with col2:
        st.metric(
            "📌 Колонки",
            report["columns"]
        )


    with col3:

        missing_count = sum(
            report["missing_values"].values()
        )

        st.metric(
            "⚠️ Пропуски",
            missing_count
        )


    with col4:

    	score = report["quality_score"]

    	st.metric(
        	"⭐ Quality Score",
        	f"{score}%"
    	)

    	if score >= 80:
        	st.success("🟢 Хорошее качество данных")

    	elif score >= 50:
        	st.warning("🟡 Требуется проверка")

    	else:
        	st.error("🔴 Плохое качество данных")
    
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📊 Обзор",
            "🔍 Качество данных",
            "🤖 AI Анализ",
            "📈 Графики",
            "📚 История"
        ]
    )

    with tab1:

        st.header(
            "Общая информация"
        )


        st.subheader(
            "Первые строки данных"
        )


        st.dataframe(
            df.head(20),
            use_container_width=True
        )


        st.subheader(
            "Статистика данных"
        )


        st.dataframe(
            df.describe(),
            use_container_width=True
        )

        st.subheader(
    		"📋 Профиль колонок"
	)

        st.dataframe(
    		report["column_profile"],
    		use_container_width=True
	)


    with tab2:

        st.header(
            "Проверка качества"
        )


        st.write(
            "Пропуски:",
            report["missing_values"]
        )


        st.write(
            "Дубликаты:",
            report["duplicates"]
        )

        st.subheader(
            "💡 Рекомендации"
    	)

        for rec in recommendations:
            st.info(rec)


        st.subheader(
            "Инсайты"
        )


        for insight in insights:
            st.warning(insight)



    with tab3:

        st.header(
            "AI вывод"
        )


        st.markdown(
            report["ai_analysis"]
        )



    with tab4:

        st.header(
            "📈 Автоматические графики"
        )


        numeric_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()


        if numeric_columns:


            selected_column = st.selectbox(
                "Выберите показатель",
                numeric_columns
            )


            fig, ax = plt.subplots(
                figsize=(8,4)
            )


            ax.hist(
                df[selected_column].dropna(),
                bins=20
            )


            ax.set_title(
                f"Распределение {selected_column}"
            )


            st.pyplot(fig)



            if len(numeric_columns) > 1:

                st.subheader(
                    "🔥 Корреляция признаков"
                )


                fig, ax = plt.subplots(
                    figsize=(8,6)
                )


                sns.heatmap(
                    df[numeric_columns].corr(),
                    annot=True,
                    cmap="coolwarm",
                    ax=ax
                )


                st.pyplot(fig)


        else:

            st.info(
                "Нет числовых колонок для анализа"
            )


    with tab5:
        st.header("📚 История анализов")
        st.write("История анализов будет здесь")
