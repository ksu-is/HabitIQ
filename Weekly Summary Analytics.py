def weekly_summary(df):
    df["week"] = df["timestamp"].dt.isocalendar().week
    summary = df.groupby(["habit", "week"]).size().reset_index(name="count")
    return summary
