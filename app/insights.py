def generate_insights(report):

    insights = []


    # Пропуски

    for column, value in report["missing_values"].items():

        if value > 0:
            insights.append(
                f"В колонке '{column}' обнаружено пропусков: {value}."
            )


    # Дубликаты

    if report["duplicates"] > 0:

        insights.append(
            f"Найдено полных дубликатов строк: {report['duplicates']}."
        )


    if report["duplicates_without_id"] > 0:

        insights.append(
            "Обнаружены повторяющиеся записи без учета ID."
        )


    # Выбросы

    for column, values in report["outliers"].items():

        insights.append(
            f"В колонке '{column}' найдены аномальные значения: {values}."
        )


    # Если проблем нет

    if not insights:

        insights.append(
            "Качество данных хорошее. Существенных проблем не обнаружено."
        )


    return insights
