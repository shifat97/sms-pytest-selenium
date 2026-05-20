from pages.base_page import BasePage

class TableFilterHandler(BasePage):
    def table_filter(self, TABLE_ROW, TABLE_COLUMN):
        rows = self.find_elements(TABLE_ROW)
        table_dict = []

        for row in rows:
            column = row.find_elements(*TABLE_COLUMN) 
            row_data = {
                "name": column[0].text,
                "email": column[1].text,
                "department": column[2].text,
                "registration_id": column[3].text,
                "age": column[4].text
            }
            table_dict.append(row_data)

        return table_dict