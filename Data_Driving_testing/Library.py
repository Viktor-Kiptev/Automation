import json, jsonpath, requests, openpyxl


class Common:

    def __init__(self, FilePathName, SheetName):
        global my_exel_file
        global sheet_name
        my_exel_file = openpyxl.load_workbook(FilePathName)
        sheet_name = my_exel_file[SheetName]

    def fetch_rov_count(self):
        global num_of_rov
        num_of_row = sheet_name.max_row
        return num_of_row

    def fetch_column_count(self):
        global column_num
        column_num = sheet_name.max_column
        return column_num

    def fetch_key_names(self):
        column_list = []
        for i in range(1, column_num + 1):
            column_list.insert(i-1, (sheet_name.cell(1, i)))
        return column_list

    def update_json_with_data(self, num_of_rov, jsonRequest, key_list):
        for i in range(1, column_num + 1):
            cell = sheet_name.cell(num_of_rov, i)
            jsonRequest[key_list[i-1]]=cell.value
        return jsonRequest