from src.v1.filter import extract_information
from fpdf import FPDF
import qrcode
import time
# import cups
import os

user_current_directory = os.getcwd()
path_qr = os.path.join(user_current_directory, "path_of_qr")
directory_save_path_logo = os.path.join(user_current_directory, "src/v1/LOGO_SIEMAV.jpg")
directory_save_path_document = os.path.join(user_current_directory, "path_of_document")


class Document:

    def new_page_pdf(self):
        self.pdf.add_page()

    def save_pdf(self, name_document):
        name_pdf = os.path.join(directory_save_path_document, name_document)
        self.pdf.output(name=name_pdf)

    def border(self, offset_x=0):
        self.pdf.rect(x=10 + offset_x, y=10, w=85, h=190)
        self.pdf.rect(x=12 + offset_x, y=60, w=81, h=12)
        self.pdf.rect(x=12 + offset_x, y=75, w=81, h=80)
        self.pdf.rect(x=12 + offset_x, y=158, w=81, h=22)

    def sign(self, offset_x=0):
        self.pdf.set_font("Arial", style="", size=10)
        self.pdf.set_xy(x=12 + offset_x, y=204)
        self.pdf.cell(w=100, h=-15, txt="   Transportado Por                      Entregado A", align='L')

    def line_sign(self, offset_x=0):
        self.pdf.line(x1=15 + offset_x, y1=192, x2=45 + offset_x, y2=192)
        self.pdf.line(x1=60 + offset_x, y1=192, x2=90 + offset_x, y2=192)

    def siemav(self, offset_x=0):
        self.pdf.set_font("Arial", style="", size=10)
        self.pdf.image(directory_save_path_logo, x=35 + offset_x, y=12, w=32, h=42)
        self.pdf.set_xy(x=10 + offset_x, y=34)
        self.pdf.multi_cell(w=60, h=6,
                            txt="Sistemas Embebidos Avanzados\nVía Daule Km 5.5\nCel: +593 99 645 7383\nRUC: 0993230928001",
                            align='C')

    def number_guide(self, offset_x=0, value=1):
        self.pdf.set_font("Arial", style="B", size=20)
        self.pdf.set_xy(x=71 + offset_x, y=12, )
        self.pdf.cell(w=20, h=5, txt="GUIA", align='C')
        self.pdf.ln(7)
        self.pdf.set_x(x=71 + offset_x)
        self.pdf.cell(w=20, h=5, txt=str(value).zfill(5), align='C')
        self.pdf.ln(8)
        self.pdf.set_x(x=68 + offset_x)
        self.pdf.set_font("Arial", style="", size=12)
        today = time.strftime("%d/%m/%y")
        self.pdf.cell(w=25, h=5, txt=str(today), align='C')

    def generate_qr(self, offset_x=0, message="Save Message", value=1):
        image_qr = qrcode.make(message)
        name_qr = "GUIA" + str(value)
        save_file_image = os.path.join(path_qr, name_qr + ".png")
        image_qr.save(save_file_image)
        self.pdf.image(save_file_image, x=67 + offset_x, y=32, w=27, h=27)

    def name_guide(self, offset_x=0):
        self.pdf.set_font("Arial", style="", size=12)
        self.pdf.set_xy(x=12 + offset_x, y=60)
        self.pdf.cell(w=90, h=5, txt="Siemav        Ing. Geovanny Arguello", align='L')
        self.pdf.ln(6)
        self.pdf.set_x(x=12 + offset_x)
        self.pdf.cell(w=90, h=5, txt="Ipsp             Ing. Guillermo Moncayo", align='L')

    def place_of_delivery(self, offset_x=0, place="Guayaquil"):
        self.pdf.set_font("Arial", style="", size=12)
        self.pdf.set_xy(x=12 + offset_x, y=159)
        self.pdf.cell(w=20, h=5, txt="Lugar de Entrega", align='L')
        self.pdf.ln(9)
        self.pdf.set_x(x=10 + offset_x)
        self.pdf.set_font("Arial", style="B", size=19)
        self.pdf.cell(w=90, h=5, txt=place, align='C')

    def header_item_detail_quantity(self, offset_x=0):
        self.pdf.set_font("Arial", style="", size=12)
        self.pdf.set_xy(x=12 + offset_x, y=76)
        self.pdf.cell(w=150, h=5, txt="  Art.                   Detalle                   Cant.  ", align='L')

    def position_initial_y(self):
        self.pdf.set_y(y=85)

    def line_feed_vertical(self):
        self.pdf.ln(5)

    def add_message(self, item, detail, quantity, offset_x=0):
        self.pdf.set_font("Arial", style="", size=10)
        self.pdf.set_x(x=12 + offset_x)
        self.pdf.cell(w=10, h=5, txt=str(item), align='C')
        self.pdf.set_x(x=80 + offset_x)
        self.pdf.cell(w=10, h=5, txt=str(quantity), align='C')
        self.pdf.set_x(x=25 + offset_x)
        self.pdf.multi_cell(w=50, h=5, txt=str(detail))

    def create_document(self, value_guide, value_place, save_message_received_qr, list_item, save_name):
        self.pdf = FPDF(orientation="L", format="A4", unit="mm")
        self.new_page_pdf()

        self.border(offset_x=0)
        self.border(offset_x=95)
        self.border(offset_x=190)

        self.sign(offset_x=0)
        self.sign(offset_x=95)
        self.sign(offset_x=190)

        self.line_sign(offset_x=0)
        self.line_sign(offset_x=95)
        self.line_sign(offset_x=190)

        self.siemav(offset_x=0)
        self.siemav(offset_x=95)
        self.siemav(offset_x=190)

        self.number_guide(offset_x=0, value=value_guide)
        self.number_guide(offset_x=95, value=value_guide)
        self.number_guide(offset_x=190, value=value_guide)

        self.generate_qr(offset_x=0, value=value_guide, message=save_message_received_qr)
        self.generate_qr(offset_x=95, value=value_guide, message=save_message_received_qr)
        self.generate_qr(offset_x=190, value=value_guide, message=save_message_received_qr)

        self.name_guide(offset_x=0)
        self.name_guide(offset_x=95)
        self.name_guide(offset_x=190)

        self.place_of_delivery(offset_x=0, place=value_place)
        self.place_of_delivery(offset_x=95, place=value_place)
        self.place_of_delivery(offset_x=190, place=value_place)

        self.header_item_detail_quantity(offset_x=0)
        self.header_item_detail_quantity(offset_x=95)
        self.header_item_detail_quantity(offset_x=190)

        self.position_initial_y()
        for item, detail, quantity in list_item:
            self.add_message(item, detail, quantity, offset_x=0)
            self.line_feed_vertical()

        self.position_initial_y()
        for item, detail, quantity in list_item:
            self.add_message(item, detail, quantity, offset_x=95)
            self.line_feed_vertical()

        self.position_initial_y()
        for item, detail, quantity in list_item:
            self.add_message(item, detail, quantity, offset_x=190)
            self.line_feed_vertical()

        self.save_pdf(name_document=save_name)

    def print_epson(self, path: str, name_document: str):
        try:
            file_to_print = os.listdir(path)
            if name_document in file_to_print:
                # time.sleep(1)
                # conn = cups.Connection()
                # conn.printFile(printer=PRINTER_NAME, filename=path + name_document, title=name_document, options={})
                message = "DOCUMENTO IMPRESO"
            else:
                message = "Pdf no encontrado"
        except:
            message = "Problem with function print epson"

        return message

    def write_pdf(self, sentence: str):
        response = extract_information(sentence)
        if isinstance(response, tuple):
            data_information_list, multiples_item = response
            number_guide_str = data_information_list[2]
            place = data_information_list[4]

            list_item_detail_quantity = []
            for index, line in enumerate(multiples_item, start=1):
                message = line.split(" ")
                description = message[1]
                cant = message[2]
                list_item_detail_quantity.append([index, description, cant])

            guide_more_number = "GUIA_" + number_guide_str + ".pdf"
            self.create_document(value_guide=number_guide_str,
                                 value_place=place,
                                 save_message_received_qr=sentence,
                                 list_item=list_item_detail_quantity,
                                 save_name=guide_more_number)

            return [True, guide_more_number]
        else:
            return [False, response]

    def message_to_print(self, sentence: str):
        validating_information, response = self.write_pdf(sentence)
        if validating_information:
            result = self.print_epson(path=directory_save_path_document, name_document=response)
        else:
            result = response
        return result

DOCUMENT = Document()
