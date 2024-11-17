class PrinterQueue:

    def __init__(self, printer_queue: list = None):
        if printer_queue is None:
            self.__printer_queue = []
        else:
            self.__printer_queue = printer_queue

    def add_document(self, document_name):
        self.__printer_queue.append(document_name)
        return f"{document_name} помещён в очередь печати"

    def print_documents(self):
        while self.__printer_queue:
            document = self.__printer_queue.pop(0)
            print(f"Печать {document}...")
        return "очередь печати пуста"


hp_printer = PrinterQueue()
kyocera_printer = PrinterQueue(["Документ kyocera 1", "Документ kyocera 2"])

hp_printer.add_document("Отчет hp_1")
hp_printer.add_document("Отчет hp_2")
print(hp_printer.print_documents())
print()

kyocera_printer.add_document("Документ kyocera 3")
kyocera_printer.add_document("Документ kyocera 4")
kyocera_printer.print_documents()