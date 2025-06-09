from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from io import BytesIO
from pypdf import PdfWriter, PdfReader, Transformation

DEFAULT_FONT_SIZE = 24  # Set the default font size

def split_string_by_max_length(input_text, max_length, canvas_obj, font_name, font_size):
    words = input_text.split(" ")
    result = []
    current_part = ""

    for word in words:
        if canvas_obj.stringWidth(current_part + " " + word, font_name, font_size) > max_length:
            result.append(current_part.strip())
            current_part = word
        else:
            current_part += " " + word

    if current_part.strip() != "":
        result.append(current_part.strip())

    return result

def get_text_placement(text, initial_y, page_width, font_name, font_size):
    # Create a temporary canvas to calculate text dimensions
    packet = BytesIO()
    temp_canvas = canvas.Canvas(packet, pagesize=letter)
    temp_canvas.setFont(font_name, font_size)

    # Calculate max width for text
    max_width = (page_width * 5) / 6
    min_width = page_width / 6
    center_x = page_width / 2

    total_text_width = temp_canvas.stringWidth(text, font_name, font_size)
    line_height = temp_canvas._leading

    if total_text_width > (max_width - min_width):
        divided_text = split_string_by_max_length(text, max_width - min_width, temp_canvas, font_name, font_size)
        font_size -= max(1 * (len(divided_text) / 2), 2)
        temp_canvas.setFont(font_name, font_size)
        line_height = temp_canvas._leading
        initial_y += line_height / 2 if len(divided_text) > 2 else 0
        if len(divided_text) > 3:
            divided_text = divided_text[:3] + ["..."]

        positions = []
        for line in divided_text:
            text_width = temp_canvas.stringWidth(line, font_name, font_size)
            x = max(center_x - (text_width / 2), min_width)
            positions.append({
                "text": line,
                "x": x,
                "y": initial_y,
                "size": font_size,
                "line_height": line_height,
            })
            initial_y -= line_height

        temp_canvas.save()
        return positions
    else:
        text_width = temp_canvas.stringWidth(text, font_name, font_size)
        return [{
            "text": text,
            "x": max(center_x - (text_width / 2), min_width),
            "y": initial_y,
            "size": font_size,
            "line_height": line_height,
        }]

def add_store_name_to_pdf(pdf_path, store_name, output_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    page = reader.pages[0]

    # Set page dimensions and font details
    page_width = page.mediabox.width
    initial_y = 710  # Example Y position, adjust as needed
    font_name = "Helvetica-Bold"
    font_size = DEFAULT_FONT_SIZE

    # Get text placement
    text_positions = get_text_placement(store_name, initial_y, page_width, font_name, font_size)

    # Create a new canvas to draw the text
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    for pos in text_positions:
        can.setFont(font_name, pos["size"])
        can.drawString(pos["x"], pos["y"], pos["text"])
    can.save()

    # Merge the text canvas with the existing PDF
    packet.seek(0)
    new_pdf = PdfReader(packet)
    page.merge_page(new_pdf.pages[0])
    writer.add_page(page)

    # Save the modified PDF
    with open(output_path, "wb") as outputStream:
        writer.write(outputStream)

# Example usage
# add_store_name_to_pdf("assets/Poster.pdf", "Store Name", "output_with_name.pdf")