def generate_insights(report):

    insights = []


    # Пропуски

    for column, value in report["missing_values"].items():

        if value > 0:

            insights.append(
                f"⚠ В колонке '{column}' обнаружено пропусков: {value}. "
                f"Рекомендация: проверить источник данных или заполнить значения."
            )


    # Дубликаты

    if report["duplicates"] > 0:

        insights.append(
            f"⚠ Найдено полных дубликатов: {report['duplicates']}. "
            f"Рекомендация: удалить повторяющиеся записи."
        )


    if report["duplicates_without_id"] > 0:

        insights.append(
            "⚠ Найдены повторяющиеся записи без учета ID. "
            "Рекомендация: проверить уникальность данных."
        )


    # Выбросы

    for column, values in report["outliers"].items():

        insights.append(
            f"⚠ В колонке '{column}' найдены аномальные значения: {values}. "
            f"Рекомендация: проверить корректность этих записей."
        )


    if not insights:

        insights.append(
            "✅ Качество данных хорошее. Существенных проблем не обнаружено."
        )


    return insights
