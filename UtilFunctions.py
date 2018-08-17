import re
import Lookups as l
from collections import defaultdict


def __remove_comments(file_contents):
  file_contents = re.sub(l.single_line_comment, "", file_contents, flags=re.MULTILINE)
  file_contents = re.sub(l.multy_line_comment, "", file_contents)
  return file_contents


def __remove_empty_lines(file_contents):
  file_contents = re.sub(l.empty_line, "\n", file_contents)
  return file_contents


def __split_file_contents(file_contents):
  result = re.split(l.split_separator, file_contents)
  result = [line.strip() for line in result]
  result = list(filter(None, result))
  return result


def __parse_simple_operators(line_of_code):
  result_operators = defaultdict(lambda: 0)

  line_of_code = re.sub(l.string_char_literals, "", line_of_code)

  if l.comp_cs_operators.search(line_of_code):
    matches = l.comp_cs_operators.findall(line_of_code)

    for match in matches:
      result_operators[match] += 1
  else:
    matches = l.comp_cs_keyword_operators_patt.findall(line_of_code)

    for match in matches:
      result_operators[match[1]] += 1


  return dict(result_operators)


def __parse_operands(input_string):
  result_operands = defaultdict(lambda: 0)
  matches = l.compiled_cs_identifier_or_keyword_or_operand.findall(input_string)

  for match in matches:
    current_operand = match[0] + match[1] + match[0]

    if current_operand not in l.all_cs_keywords or\
       current_operand in l.cs_keyword_operands:
      result_operands[current_operand] += 1

  return dict(result_operands)


def __merge_dictionaries(dict1, dict2):
  result_dict = dict1

  for dict_key, dict_value in dict2.items():
    if dict_key in result_dict:
      result_dict[dict_key] += dict_value
    else:
      result_dict[dict_key] = dict_value

  return result_dict


def __parse_nested(line_of_code):
  operators = defaultdict(lambda: 0)

  matches = re.findall(l.nest_operators, line_of_code)

  for match in matches:
    operators[match] += 1

  return dict(operators)


def getMetrics(file_contents):
  operators = dict()
  operands = dict()

  file_contents = __remove_comments(file_contents)
  file_contents = __remove_empty_lines(file_contents)

  lines_of_code = __split_file_contents(file_contents)

  for line in lines_of_code:
    __merge_dictionaries(operators, __parse_simple_operators(line))
    __merge_dictionaries(operators, __parse_nested(line))
    __merge_dictionaries(operands, __parse_operands(line))

  return operands, operators
