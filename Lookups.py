import os
from re import compile

# misc
single_line_comment = r"\s*//.*$"
multy_line_comment = r"/\*(\s*.*\s*)*?\*/"
empty_line = r"\s*\n{2,}"
split_separator = r"[" + os.linesep + "{};]"
string_char_literals = r"([\"']).*\1"
nest_operators = r"[\(<]|\??\["


# keywords and keyword operators
cs_identifier_or_keyword = r"[\w@][\d_\w]*"

cs_identifier_or_keyword_or_operand = r"([@$]?[\"']?)(" +\
                                      cs_identifier_or_keyword +\
                                      r"|\d+)\1?"

compiled_cs_identifier_or_keyword_or_operand = compile(cs_identifier_or_keyword_or_operand)

cs_keyword_operators = {"new",     "typeof",   "checked", "unchekeced",
                        "default", "delegate", "sizeof",  "await",
                        "is",      "as",       "if",      "for",
                        "do",      "while",    "else",    "continue",
                        "goto",    "try",      "in",      "foreach",
                        "catch",   "throw",    "return",  "finally"}

cs_keyword_operands = {"false", "null", "true", "base",
                       "this"}

cs_keywords = {"abstract",  "event",      "struct",     "lock",
               "explicit",  "switch",     "double",
               "extern",    "object",
               "bool",      "operator",
               "break",     "out",
               "byte",      "fixed",      "override",
               "case",      "float",      "params",     "string",
               "private",   "uint",
               "char",      "protected",  "ulong",
               "public",    "namespace",  "enum",
               "class",     "readonly",   "unsafe",
               "const",     "implicit",   "ref",        "ushort",
               "using",
               "decimal",   "int",        "sbyte",      "virtual",
               "interface", "sealed",     "volatile",   "long",
               "internal",  "short",      "void",
               "static",    "stackalloc"}

all_cs_keywords = cs_keywords.union(cs_keyword_operators).union(cs_keyword_operands)

# operators
__member_access = r"\.\??"  # . and .?
__null_checker = r"\?\?"
__plus_minus = r"[+-]{1,2}"  # (inc/dec)rement, +- both unary and binary
__arithmetic_logical_ops = r"[!~&*\/%=><\^|]=?"  # unary/binary arithmetic and logical operators
__lshift_lcomp = r"<?<"  # <<, <
__rshift_gcomp = r">?>"  # >>, >
__lshift_eq = r">>="
__rshift_eq = r"<<="
__lambda_operator = r"=>"
__cond_or = r"\|\|"
__cond_and = r"&&"
__access_by_ptr_op = r"->"
__coma = r","

cs_operators = __member_access + "|" +\
               __null_checker + "|" +\
               __plus_minus + "|" +\
               __arithmetic_logical_ops + "|" +\
               __lshift_lcomp + "|" +\
               __rshift_gcomp + "|" +\
               __lshift_eq + "|" +\
               __rshift_eq + "|" +\
               __lambda_operator + "|" +\
               __cond_or + "|" +\
               __cond_and + "|" +\
               __access_by_ptr_op + "|" +\
               __coma

cs_keyword_operators_patt = r"(\W|^)(" + "|".join(cs_keyword_operators) + ")(\W|$)"

comp_cs_operators = compile(cs_operators)
comp_cs_keyword_operators_patt = compile(cs_keyword_operators_patt)
