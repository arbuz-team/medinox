
class Pages_Manager:

    def Get_Elements_From_Current_Page(self):

        page = self.selected_page
        start = (page-1) * self.number_elements_on_page
        end = page * self.number_elements_on_page

        return self.elements[start:end]

    @staticmethod
    def Get_List_Pages(number_of_pages):
        return list(range(1, number_of_pages + 1))

    def Get_Split_Pages(self, number_of_pages):
        page = self.selected_page

        if number_of_pages < 8:  # 1 2 3 4 5 6 7
            return [list(range(1, number_of_pages + 1))]

        if page < 5:  # 1 2 3 4 5 … 9
            return [list(range(1, 6)), [number_of_pages]]

        if page > number_of_pages - 4:  # 1 … 5 6 7 8 9
            return [[1], list(range(number_of_pages - 4, number_of_pages + 1))]

        # 1 … 3 4 5 6 7 … 9
        return [[1], list(range(page - 2, page + 3)), [number_of_pages]]

    def Create_Pages(self):

        # count number of pages
        number_of_pages = int(len(self.elements) / self.number_elements_on_page)

        # products more than can be located in pages
        # additional not full page
        if len(self.elements) % self.number_elements_on_page:
            number_of_pages += 1

        # create content
        self.content['elements'] = self.Get_Elements_From_Current_Page()
        self.content['list_pages'] = self.Get_List_Pages(number_of_pages)
        self.content['split_pages'] = self.Get_Split_Pages(number_of_pages)
        self.content['number_of_pages'] = number_of_pages
        self.content['next_page'] = self.selected_page + 1
        self.content['prev_page'] = self.selected_page - 1

        return self.content

    def __init__(self, elements, number_elements_on_page, selected_page):

        self.elements = elements
        self.number_elements_on_page = number_elements_on_page
        self.selected_page = selected_page
        self.content = {}

