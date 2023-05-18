# The last part of the example requires a QF_LIA solver to be installed.
#
#
# This example shows how to interact with files in the SMT-LIB
# format. In particular:
#
# 1. How to read a file in SMT-LIB format
# 2. How to write a file in SMT-LIB format
# 3. Formulas and SMT-LIB script
# 4. How to access annotations from SMT-LIB files
# 5. How to extend the parser with custom commands
#
from io import StringIO

from pysmt.smtlib.parser import SmtLibParser


# To make the example self contained, we store the example SMT-LIB
# script in a string.
DEMO_SMTLIB=\
"""
(set-info :smt-lib-version 2.6)
(set-logic QF_UF)
(set-info :source |
Generating minimum transitivity constraints in P-time for deciding Equality Logic,
Ofer Strichman and Mirron Rozanov,
SMT Workshop 2005.

Translator: Leonardo de Moura. |)
(set-info :category "crafted")
(set-info :status unsat)
(declare-sort U 0)
(declare-fun x0 () U)
(declare-fun y0 () U)
(declare-fun z0 () U)
(declare-fun x1 () U)
(declare-fun y1 () U)
(declare-fun z1 () U)
(declare-fun x2 () U)
(declare-fun y2 () U)
(declare-fun z2 () U)
(declare-fun x3 () U)
(declare-fun y3 () U)
(declare-fun z3 () U)
(declare-fun x4 () U)
(declare-fun y4 () U)
(declare-fun z4 () U)
(declare-fun x5 () U)
(declare-fun y5 () U)
(declare-fun z5 () U)
(declare-fun x6 () U)
(declare-fun y6 () U)
(declare-fun z6 () U)
(declare-fun x7 () U)
(declare-fun y7 () U)
(declare-fun z7 () U)
(declare-fun x8 () U)
(declare-fun y8 () U)
(declare-fun z8 () U)
(declare-fun x9 () U)
(declare-fun y9 () U)
(declare-fun z9 () U)
(declare-fun x10 () U)
(declare-fun y10 () U)
(declare-fun z10 () U)
(declare-fun x11 () U)
(declare-fun y11 () U)
(declare-fun z11 () U)
(declare-fun x12 () U)
(declare-fun y12 () U)
(declare-fun z12 () U)
(declare-fun x13 () U)
(declare-fun y13 () U)
(declare-fun z13 () U)
(declare-fun x14 () U)
(declare-fun y14 () U)
(declare-fun z14 () U)
(declare-fun x15 () U)
(declare-fun y15 () U)
(declare-fun z15 () U)
(declare-fun x16 () U)
(declare-fun y16 () U)
(declare-fun z16 () U)
(declare-fun x17 () U)
(declare-fun y17 () U)
(declare-fun z17 () U)
(declare-fun x18 () U)
(declare-fun y18 () U)
(declare-fun z18 () U)
(declare-fun x19 () U)
(declare-fun y19 () U)
(declare-fun z19 () U)
(assert (and (or (and (= x0 y0) (= y0 x1)) (and (= x0 z0) (= z0 x1))) (or (and (= x1 y1) (= y1 x2)) (and (= x1 z1) (= z1 x2))) (or (and (= x2 y2) (= y2 x3)) (and (= x2 z2) (= z2 x3))) (or (and (= x3 y3) (= y3 x4)) (and (= x3 z3) (= z3 x4))) (or (and (= x4 y4) (= y4 x5)) (and (= x4 z4) (= z4 x5))) (or (and (= x5 y5) (= y5 x6)) (and (= x5 z5) (= z5 x6))) (or (and (= x6 y6) (= y6 x7)) (and (= x6 z6) (= z6 x7))) (or (and (= x7 y7) (= y7 x8)) (and (= x7 z7) (= z7 x8))) (or (and (= x8 y8) (= y8 x9)) (and (= x8 z8) (= z8 x9))) (or (and (= x9 y9) (= y9 x10)) (and (= x9 z9) (= z9 x10))) (or (and (= x10 y10) (= y10 x11)) (and (= x10 z10) (= z10 x11))) (or (and (= x11 y11) (= y11 x12)) (and (= x11 z11) (= z11 x12))) (or (and (= x12 y12) (= y12 x13)) (and (= x12 z12) (= z12 x13))) (or (and (= x13 y13) (= y13 x14)) (and (= x13 z13) (= z13 x14))) (or (and (= x14 y14) (= y14 x15)) (and (= x14 z14) (= z14 x15))) (or (and (= x15 y15) (= y15 x16)) (and (= x15 z15) (= z15 x16))) (or (and (= x16 y16) (= y16 x17)) (and (= x16 z16) (= z16 x17))) (or (and (= x17 y17) (= y17 x18)) (and (= x17 z17) (= z17 x18))) (or (and (= x18 y18) (= y18 x19)) (and (= x18 z18) (= z18 x19))) (not (= x0 x19))))
(check-sat)
(exit)

"""
# """
# (set-logic QF_LIA)
# (declare-fun p () Int)
# (declare-fun q () Int)
# (declare-fun x () Bool)
# (declare-fun y () Bool)
# (define-fun .def_1 () Bool (! (and x y) :cost 1))
# (assert (=> x (> p q)))
# (check-sat)
# (push)
# (assert (=> y (> q p)))
# (check-sat)
# (assert .def_1)
# (check-sat)
# (pop)
# (check-sat)
# """

# We read the SMT-LIB Script by creating a Parser.
# From here we can get the SMT-LIB script.
parser = SmtLibParser()

# The method SmtLibParser.get_script takes a buffer in input. We use
# StringIO to simulate an open file.
# See SmtLibParser.get_script_fname() if to pass the path of a file.
script = parser.get_script(StringIO(DEMO_SMTLIB))

# The SmtLibScript provides an iterable representation of the commands
# that are present in the SMT-LIB file.
#
# Printing a summary of the issued commands
print("First script:")
for cmd in script:
    print(cmd.name)
print("*"*50)

# SmtLibScript provides some utilities to perform common operations: e.g,
# - Checking if a command is present
assert script.contains_command("check-sat")
# - Counting the occurrences of a command
assert script.count_command_occurrences("assert") == 1
# - Obtain all commands of a particular type
decls = script.filter_by_command_name("declare-fun")
for d in decls:
    print(d)
print("*"*50)

# Most SMT-LIB scripts define a single SAT call. In these cases, the
# result can be obtained by conjoining multiple assertions.  The
# method to do that is SmtLibScript.get_strict_formula() that, raises
# an exception if there are push/pop calls.  To obtain the formula at
# the end of the execution of the Script (accounting for push/pop) we
# use get_last_formula

f = script.get_last_formula()
print(f"Last formula: {f}")
print()
# Finally, we serialize the script back into SMT-Lib format.  This can
# be dumped into a file (see SmtLibScript.to_file).  The flag daggify,
# specifies whether the printing is done as a DAG or as a tree.

buf_out = StringIO()
script.serialize(buf_out, daggify=True)
# print(buf_out.getvalue())
print("*"*50)
# Expressions can be annotated in order to provide additional
# information. The semantic of annotations is solver/problem
# dependent. For example, VMT uses annotations to identify two
# expressions as 1) the Transition Relation and 2) Initial Condition
#
# Here we pretend that we make up a ficticious Weighted SMT format
# and label .def1 with cost 1
#
# The class pysmt.smtlib.annotations.Annotations deals with the
# handling of annotations.
#
# ann = script.annotations
# print(ann.all_annotated_formulae("cost"))

# print("*"*50)

# # Annotations are part of the SMT-LIB standard, and are the
# # recommended way to perform inter-operable operations. However, in
# # many cases, we are interested in prototyping some algorithm/idea and
# # need to write the input files by hand. In those cases, using an
# # extended version of SMT-LIB usually provides a more readable input.
# # We provide now an example on how to define a symbolic transition
# # system as an extension of SMT-LIB.
# # (A more complete version of this example can be found in :
# #    pysmt.tests.smtlib.test_parser_extensibility.py)
# #
# EXT_SMTLIB="""\
# (declare-fun A () Bool)
# (declare-fun B () Bool)
# (init (and A B))
# (trans (=> A (next A)))
# (exit)
# """

# # We define two new commands (init, trans) and a new
# # operator (next). In order to parse this file, we need to create a
# # sub-class of the SmtLibParser, and add handlers for he new commands
# # and operators.
# from pysmt.smtlib.script import SmtLibCommand

# class TSSmtLibParser(SmtLibParser):
#     def __init__(self, env=None, interactive=False):
#         SmtLibParser.__init__(self, env, interactive)

#         # Add new commands
#         #
#         # The mapping function takes care of consuming the command
#         # name from the input stream, e.g., '(init' . Therefore,
#         # _cmd_init will receive the rest of the stream, in our
#         # example, '(and A B)) ...'
#         self.commands["init"] = self._cmd_init
#         self.commands["trans"] = self._cmd_trans

#         # Remove unused commands
#         #
#         # If some commands are not compatible with the extension, they
#         # can be removed from the parser. If found, they will cause
#         # the raising of the exception UnknownSmtLibCommandError
#         del self.commands["check-sat"]
#         del self.commands["get-value"]
#         # ...

#         # Add 'next' function
#         #
#         # New operators can be added similarly as done for commands.
#         # e.g., 'next'. The helper function _operator_adapter,
#         # simplifies the writing of such extensions.  In this example,
#         # we will rewrite the content of the next without the need of
#         # introducing a new pySMT operator. If you are interested in a
#         # simple way of handling new operators in pySMT see
#         # pysmt.test.test_dwf.
#         self.interpreted["next"] = self._operator_adapter(self._next_var)

#     def _cmd_init(self, current, tokens):
#         # This cmd performs the parsing of:
#         #   <expr> )
#         # and returns a new SmtLibCommand
#         expr = self.get_expression(tokens)
#         self.consume_closing(tokens, current)
#         return SmtLibCommand(name="init", args=(expr,))

#     def _cmd_trans(self, current, tokens):
#         # This performs the same parsing as _cmd_init, but returns a
#         # different object. The parser is not restricted to return
#         # SmtLibCommand, but using them makes handling them
#         # afterwards easier.
#         expr = self.get_expression(tokens)
#         self.consume_closing(tokens, current)
#         return SmtLibCommand(name="trans", args=(expr,))

#     def _next_var(self, symbol):
#         # The function is called with the arguments obtained from
#         # parsing the rest of the SMT-LIB file. In this case, 'next'
#         # is a unary function, thus we have only 1 argument. 'symbol'
#         # is an FNode. We require that 'symbol' is _really_ a symbol:
#         if symbol.is_symbol():
#             name = symbol.symbol_name()
#             ty = symbol.symbol_type()
#             # The return type MUST be an FNode, because this is part
#             # of an expression.
#             return self.env.formula_manager.Symbol("next_" + name, ty)
#         else:
#             raise ValueError("'next' operator can be applied only to symbols")

#     def get_ts(self, script):
#         # New Top-Level command that takes a script stream in input.
#         # We return a pair (Init, Trans) that defines the symbolic
#         # transition system.
#         init = self.env.formula_manager.TRUE()
#         trans = self.env.formula_manager.TRUE()

#         for cmd in self.get_command_generator(script):
#             if cmd.name=="init":
#                 init = cmd.args[0]
#             elif cmd.name=="trans":
#                 trans = cmd.args[0]
#             else:
#                 # Ignore other commands
#                 pass

#         return (init, trans)

# # Time to try out the parser !!!
# #
# # First we check that the standard SMT-Lib parser cannot handle the new format.
# from pysmt.exceptions import UnknownSmtLibCommandError

# try:
#     parser.get_script(StringIO(EXT_SMTLIB))
# except UnknownSmtLibCommandError as ex:
#     print("Unsupported command: %s" % ex)

# # The new parser can parse our example, and returns the (init, trans) pair
# ts_parser = TSSmtLibParser()
# init, trans = ts_parser.get_ts(StringIO(EXT_SMTLIB))
# print("INIT: %s" % init.serialize())
# print("TRANS: %s" % trans.serialize())
