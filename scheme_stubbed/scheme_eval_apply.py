import sys
import os

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, tail=False):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # BEGIN Problem 1/2
    "*** YOUR CODE HERE ***"
    # atomic
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr
    # non-atomic
    elif scheme_listp(expr):
        if scheme_symbolp(expr.first) and expr.first in scheme_forms.SPECIAL_FORMS:
            return scheme_forms.SPECIAL_FORMS[expr.first](expr.rest, env)
        else:
            return scheme_apply(scheme_eval(expr.first, env), expr.rest, env)

    # error
    else:
        raise SchemeError("input is not well-formed")
    # END Problem 1/2


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    # BEGIN Problem 1/2
    "*** YOUR CODE HERE ***"
    # if procedure in BUILTINS:
    validate_procedure(procedure)
    if not isinstance(procedure, Procedure):
        raise SchemeError(f"{procedure} is not a procedure")

    if isinstance(procedure, BuiltinProcedure):
        argslist = ()
        for i in range(len(args)):
            argslist += (scheme_eval(args.first, env),)
            args = args.rest
        try:
            if procedure.need_env == False:
                return procedure.py_func(*argslist)
            else:
                return procedure.py_func(*argslist, env)
        except TypeError as err:
            raise SchemeError(f"incorrect number of arguments{len(args)}")

    elif isinstance(procedure, LambdaProcedure):
        if len(args) != len(procedure.formals):
            raise SchemeError(f"incorrect number of arguments")
        formals = procedure.formals
        newenv = Frame(procedure.env)
        for i in range(len(procedure.formals)):
            newenv.define(formals.first, scheme_eval(args.first, env))
            formals = formals.rest
            args = args.rest
        expr = procedure.body
        # for i in range(len(procedure.body)):
        #     if i == len(procedure.body) - 1:
        #         # print("DEBUG:", expr.first.first)
        #         # print("DEBUG:", procedure.name)
        #         # try:
        #         #     tmp = scheme_eval(expr.first.first, env)
        #         # except SchemeError as err:
        #         #     tmp = nil
        #         # if scheme_listp(expr.first) and tmp == procedure:
        #         #     return scheme_eval(expr.first, newenv, True)
        #         return scheme_eval(expr.first, newenv)
        #     scheme_eval(expr.first, newenv)
        #     expr = expr.rest
        return eval_all(expr, newenv)

    elif isinstance(procedure, MuProcedure):

        if len(args) != len(procedure.formals):
            raise SchemeError(f"incorrect number of arguments")

        formals = procedure.formals

        newenv = Frame(env)
        for i in range(len(procedure.formals)):
            newenv.define(formals.first, scheme_eval(args.first, env))
            formals = formals.rest
            args = args.rest

        expr = procedure.body
        # for i in range(len(procedure.body)):
        #     if i == len(procedure.body) - 1:
        #         if scheme_listp(expr.first) and expr.first.first == procedure:
        #             return scheme_eval(expr.first, newenv, True)
        #         return scheme_eval(expr.first, newenv)
        #     scheme_eval(expr.first, newenv)
        #     expr = expr.rest
        return eval_all(expr, newenv)

    else:
        raise SchemeError(f"TODO")

    # END Problem 1/2


def eval_all(expr, env):
    if len(expr) < 1:
        raise SchemeError("wrong number of arguments")
    length = len(expr)
    for i in range(length):
        if i == length - 1:
            return scheme_eval(expr.first, env)
        scheme_eval(expr.first, env)
        expr = expr.rest


##################
# Tail Recursion #
##################

# Make classes/functions for creating tail recursive programs here!
# BEGIN Problem EC
"*** YOUR CODE HERE ***"


def optimize_tail_call(unoptimized_eval):
    def optimized_eval(expr, env, tail=False):

        if tail == True and scheme_listp(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        while isinstance(result, Unevaluated):
            result = unoptimized_eval(expr, env)
        return result

    return optimized_eval


scheme_eval = optimize_tail_call(scheme_eval)


class Unevaluated:
    def __init__(self, expr, env):
        self.expr = expr
        self.env = env


# END Problem EC


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not Unevaluated.
    Right now it just calls scheme_apply, but you will need to change this
    if you attempt the extra credit."""
    validate_procedure(procedure)
    # BEGIN
    return val
    # END