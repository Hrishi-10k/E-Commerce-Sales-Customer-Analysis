from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak,
)
from src.config import PDF_FILE, GRAPH_DIR, INSIGHTS_FILE


def generate_pdf_report(df, summaries):
    PDF_FILE.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(PDF_FILE),
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )
    styles = getSampleStyleSheet()
    story = []
    story.append(Paragraph("E-Commerce Sales & Customer Analysis", styles["Title"]))
    story.append(Paragraph("Exploratory Data Analysis Report", styles["Heading2"]))
    story.append(Spacer(1, 12))
    kpis = summaries["kpis"]
    table_data = [
        ["KPI", "Value"],
        ["Total Revenue", f"{kpis['total_revenue']:,.2f}"],
        ["Unique Orders", f"{kpis['unique_orders']:,}"],
        ["Average Order Value", f"{kpis['aov']:,.2f}"],
        ["Cancelled order rows", f"{kpis['cancelled']:,}"],
        ["Returned order rows", f"{kpis['returned']:,}"],
        ["Clean rows analyzed", f"{len(df):,}"],
    ]
    table = Table(table_data, colWidths=[3.0 * inch, 2.5 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#163A5F")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [colors.white, colors.HexColor("#F1F5F8")],
                ),
                ("PADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 14))
    story.append(Paragraph("Key Findings", styles["Heading1"]))
    if INSIGHTS_FILE.exists():
        with open(INSIGHTS_FILE, "r", encoding="utf-8") as f:
            insight_lines = f.read().splitlines()
        for line in insight_lines:
            if line.strip() and not line.startswith("="):
                story.append(Paragraph(line.replace("&", "&amp;"), styles["BodyText"]))
                story.append(Spacer(1, 3))
    chart_files = [
        "revenue_by_region.png",
        "revenue_by_category.png",
        "profit_by_category.png",
        "monthly_revenue_trend.png",
        "top_customers.png",
        "discount_vs_profit.png",
        "revenue_distribution.png",
        "profit_margin_boxplot.png",
        "correlation_heatmap.png",
        "payment_method_usage.png",
    ]
    story.append(PageBreak())
    story.append(Paragraph("Visual Analysis", styles["Heading1"]))
    for chart_name in chart_files:
        chart_path = GRAPH_DIR / chart_name
        if chart_path.exists():
            story.append(
                Paragraph(
                    chart_name.replace("_", " ").replace(".png", "").title(),
                    styles["Heading2"],
                )
            )
            img = Image(str(chart_path), width=6.5 * inch, height=3.6 * inch)
            img.hAlign = "CENTER"
            story.append(img)
            story.append(Spacer(1, 10))
    doc.build(story)
    print(f"PDF report created: {PDF_FILE}")
