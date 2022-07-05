from unittest.mock import patch
import pytest 

import funclg.managers.modifier_manager as mod_man


@patch("funclg.utils.input_validation.yes_no_validation")
@patch("funclg.utils.input_validation.number_range_validation")
@patch("funclg.utils.input_validation.string_validation")
@patch("funclg.utils.input_validation.list_choice_selection")
def test_modifier_manager_build_modifier(m_list_select, m_str_val, m_num_range, m_yn_val):
    # TODO: Test new build method (no name, no from method)
    mod_man.build_modifier()