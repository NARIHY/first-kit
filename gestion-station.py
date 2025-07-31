from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle

def generate_pdf():
    total_stations = 220
    stations_per_sup = 14
    total_sup = (total_stations + stations_per_sup - 1) // stations_per_sup

    # Création du document PDF
    pdf_path = "gestion_pc_agents.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=40)

    # Styles
    title_style = ParagraphStyle(
        name="Title",
        fontName="Helvetica-Bold",
        fontSize=18,
        alignment=1,              # Centré
        textColor=colors.white,
        backColor=colors.HexColor("#2b2b2b"),
        spaceAfter=20
    )
    header_style = ParagraphStyle(
        name="Header",
        fontName="Helvetica-Bold",
        fontSize=12,
        textColor=colors.white,
        backColor=colors.grey
    )

    story = []
    # Titre
    story.append(Paragraph("GESTION DES PC AGENT", title_style))
    story.append(Spacer(1, 12))

    station_num = 1
    for sup_num in range(1, total_sup + 1):
        # Table des stations
        data = [["NOM STATION", "STATUS", "ETAT"]]
        while len(data) - 1 < stations_per_sup and station_num <= total_stations:
            data.append([f"STATION-{station_num:03d}", "", ""])
            station_num += 1

        tbl = Table(data, colWidths=[150, 100, 100], repeatRows=1)
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.white),
            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#2b2b2b")),
        ]))
        story.append(tbl)
        story.append(Spacer(1, 12))

        # Table du SUP correspondant
        sup_data = [["NOM STATION", "STATUS", "ETAT"], [f"SUP-{sup_num:02d}", "", ""]]
        sup_tbl = Table(sup_data, colWidths=[150, 100, 100], repeatRows=1)
        sup_tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.white),
            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#2b2b2b")),
        ]))
        story.append(sup_tbl)
        story.append(Spacer(1, 24))

    # Génération du PDF
    doc.build(story)
    print(f"✅ Fichier '{pdf_path}' généré avec succès.")

if __name__ == "__main__":
    generate_pdf()
