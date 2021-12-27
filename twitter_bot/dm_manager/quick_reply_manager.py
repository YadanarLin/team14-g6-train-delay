from twitter_bot.worker import ALL_TRAIN_OPERATORS, ALL_TRAIN_LINES

class QuickrepOptionManager:
    def __init__(self):
        pass

    def default_options(self):
        """Return list of default options like 'Home', 'Help' button"""
        default_option = [
                {
                    "label": "🏠 Home",
                    "description": "Return to top",
                    "metadata": "home"
                },
                {
                    "label": "❓ Help",
                    "description": "Do you need help?",
                    "metadata": "help"
                }
        ]
        return default_option

    def CHECK_DELAY_all_operator_options(self):
        """Return list of all operator for checking current delay state. For choosing operator to follow train line, use follow_delay_all_operator_options()"""
        quickrep_options = []
        for number, operator in enumerate(ALL_TRAIN_OPERATORS, start=1):
            quickrep_option = {
                'label': f'{number}. {operator}',
                'description': f'Click to check trainline of {operator}',
                'metadata': f'check_delay#{operator}'
            }
            quickrep_options.append(quickrep_option)
        # add default options
        quickrep_options.extend(self.default_options())
        return quickrep_options 

    def CHECK_DELAY_all_trainline_of_specific_operator_one_page_options(self, operator_name):
        quickrep_options = []
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name]

        # if operator has <= 17 trainlines
        for number, trainline in enumerate(all_train_lines_in_operator, start=1):
            quickrep_option = {
                'label': f'{number}. {trainline}',
                'description': f'Click to check the delay status of {trainline} trainline',
                'metadata': f'check_delay#get_status#{operator_name}#{trainline}#0'
                # the last number 0 is the page number, because one page -> 0
            }
            quickrep_options.append(quickrep_option)

        # add return button
        return_option = {
            'label': '⬅ Back',
            'description': 'Return to previous page',
            'metadata': 'return_to#check_delay_info'
        }
        quickrep_options.append(return_option)
        quickrep_options.extend(self.default_options())
        return quickrep_options
        
    def CHECK_DELAY_all_trainline_of_specific_operator_first_page_options(self, operator_name):
        """Quick reply when number of item > 20 and is the first page, have 'Next' option"""
        quickrep_options = []
        # because have 'Next', 'Back', 2 default buttons -> 16 options remaining
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][:16]
        for number, trainline in enumerate(all_train_lines_in_operator, start=1):
            quickrep_option = {
                'label': f'{number}. {trainline}',
                'description': f'Click to check the delay status of {trainline} trainline',
                'metadata': f'check_delay#get_status#{operator_name}#{trainline}#0'
            }
            quickrep_options.append(quickrep_option)
        # add return button
        return_option = {
            'label': '⬅ Back',
            'description': 'Return to previous page',
            'metadata': 'return_to#check_delay_info'
        }
        # add continue button
        continue_option = {
            'label': '➡ Continue',
            'description': 'Next trainlines',
            'metadata': f'continue#check_delay#{operator_name}#1'
        }
        quickrep_options.extend([return_option, continue_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def CHECK_DELAY_all_trainline_of_specific_operator_middle_page_options(self, operator_name, page:int):
        quickrep_options = []
        # because have 'Next', 'Back', 2 default buttons -> 16 options remaining
        start_index = page*16
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][start_index:start_index+16]
        for number, trainline in enumerate(all_train_lines_in_operator, start=start_index+1):
            quickrep_option = {
                'label': f'{number}. {trainline}',
                'description': f'Click to check the delay status of {trainline} trainline',
                'metadata': f'check_delay#get_status#{operator_name}#{trainline}#{page}'
            }
            quickrep_options.append(quickrep_option)
        # add return button
        return_option = {
            'label': '⬅ Back',
            'description': 'Return to previous page',
            'metadata': f'return_to#check_delay#{operator_name}#{page-1}'
        }
        # add continue button
        continue_option = {
            'label': '➡ Continue',
            'description': 'Next trainlines',
            'metadata': f'continue#check_delay#{operator_name}#{page+1}'
        }
        quickrep_options.extend([return_option, continue_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def CHECK_DELAY_all_trainline_of_specific_operator_last_page_options(self, operator_name, page:int):
        quickrep_options = []
        # because have 'Next', 'Back', 2 default buttons -> 16 options remaining
        start_index = page*16
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][start_index:]
        for number, trainline in enumerate(all_train_lines_in_operator, start=start_index+1):
            quickrep_option = {
                'label': f'{number}. {trainline}',
                'description': f'Click to check the delay status of {trainline} trainline',
                'metadata': f'check_delay#get_status#{operator_name}#{trainline}#{page}'
            }
            quickrep_options.append(quickrep_option)
        # add return button
        return_option = {
            'label': '⬅ Back',
            'description': 'Return to previous page',
            'metadata': f'return_to#check_delay#{operator_name}#{page-1}'
        }
        quickrep_options.extend([return_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def CHECK_DELAY_all_trainline_of_specific_operator_options(self, operator_name, page=0):
        """Return list of all railway in a specific operator_name
        
        @page: Twitter only allow quick reply max 20 entries. If have more, must separate different pages -> eg JREast has 37 trainlines -> need parameter page"""
        start_index = page*17
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][start_index:]

        if (page == 0) and (len(all_train_lines_in_operator) <= 17):
            return self.CHECK_DELAY_all_trainline_of_specific_operator_one_page_options(operator_name)
        elif (page == 0) and (len(all_train_lines_in_operator) > 17):
            return self.CHECK_DELAY_all_trainline_of_specific_operator_first_page_options(operator_name)
        elif (page != 0) and (len(all_train_lines_in_operator) > 17):
            return self.CHECK_DELAY_all_trainline_of_specific_operator_middle_page_options(operator_name, page)
        else:
            return self.CHECK_DELAY_all_trainline_of_specific_operator_last_page_options(operator_name, page)

    def CHECK_DELAY_show_trainline_delay_status_options(self, operator_name, trainline_name, page):
        """After get the delay status, give the options of all current trainlines"""
        return self.CHECK_DELAY_all_trainline_of_specific_operator_options(operator_name, page)


    def home_options(self):
        quickrep_options = [
            {
                'label': '💻 Visit website',
                'description': 'Visit train delay website for more details...',
                'metadata': 'visit_website'
            },
            {
                'label': '🔎 Check train delay status',
                'description': 'Get current delay info of 86 train lines in Tokyo',
                'metadata': 'check_delay_info'
            },
            {
                'label': '🔔 Follow train line status',
                'description': 'Get notified when delay in a train line occur',
                'metadata': 'follow_delay_info'
            }
        ]
        return quickrep_options