from scheme_eval_apply import *
from scheme_utils import *
from scheme_classes import *
from scheme_builtins import *

#################
# Special Forms #
#################

"""
How you implement special forms is up to you. We recommend you encapsulate the
logic for each special form separately somehow, which you can do here.
"""

# BEGIN PROBLEM 1/2/3
"*** YOUR CODE HERE ***"


def define_macro(args, env):
    if len(args) < 2:
        raise SchemeError("define expression is not well-formed")
    else:
        first = args.first
        if not scheme_listp(first):
            raise SchemeError(f"{first} is not a symbol")

        symbol = first.first
        if not scheme_symbolp(symbol):
            raise SchemeError(f"{first} is not a symbol")
        validate_formals(first.rest)
        env.define(symbol, MacroProcedure(first.rest, args.rest, env))
        return symbol


def do_and_define(args, env):
    if len(args) < 2:
        raise SchemeError("define expression is not well-formed")
    else:
        first = args.first
        if scheme_listp(first):
            symbol = first.first
            if not scheme_symbolp(symbol):
                raise SchemeError(f"{first} is not a symbol")
            validate_formals(first.rest)
            env.define(symbol, LambdaProcedure(first.rest, args.rest, env))
            return symbol
        elif scheme_symbolp(first):
            value = scheme_eval(args.rest.first, env)
            env.define(first, value)
            return first
        else:
            raise SchemeError(f"{first} is not a symbol")


def do_and_if(args, env):
    if len(args) != 3:
        raise SchemeError("wrong number of arguments")
    else:
        predecate = args.first
        value1 = args.rest.first
        value2 = args.rest.rest.first
        if is_scheme_true(scheme_eval(predecate, env)):
            return scheme_eval(value1, env, True)
        else:
            return scheme_eval(value2, env, True)


def do_and_quote(args, env):
    if len(args) != 1:
        raise SchemeError("wrong number of arguments")
    else:
        return args.first


def do_and_lambda(args, env):
    if len(args) < 2:
        raise SchemeError("wrong number of arguments")
    validate_formals(args.first)
    return LambdaProcedure(args.first, args.rest, env)


def do_and_mu(args, env):
    if len(args) < 2:
        raise SchemeError("wrong number of arguments")
    validate_formals(args.first)
    return MuProcedure(args.first, args.rest)


def do_and_begin(args, env):
    return eval_all(args, env)


def do_and(args, env):
    length = len(args)
    if length == 0:
        return True
    for i in range(length - 1):
        value = scheme_eval(args.first, env)
        if is_scheme_false(value):
            return value
        args = args.rest
    return scheme_eval(args.first, env, True)


def do_or(args, env):
    length = len(args)
    if length == 0:
        return False
    for i in range(length - 1):
        value = scheme_eval(args.first, env)
        if is_scheme_true(value):
            return value
        args = args.rest
    return scheme_eval(args.first, env, True)


def do_cond(args, env):
    length = len(args)
    if length == 0:
        return None
    clauses = args
    for _ in range(length):
        ptr = clauses.first

        if not scheme_listp(ptr):
            raise SchemeError("bad formed list")

        if ptr.first == "else":
            if scheme_nullp(ptr.rest):
                return True
            else:
                return eval_all(ptr.rest, env)

        pred = scheme_eval(ptr.first, env)
        if is_scheme_true(pred):
            if scheme_nullp(ptr.rest):
                return pred
            else:
                return eval_all(ptr.rest, env)

        clauses = clauses.rest
    return None


def do_and_let(args, env):
    if len(args) < 2:
        raise SchemeError("wrong number of arguments")
    else:
        newenv = Frame(env)
        bindings = args.first
        length = len(bindings)
        for _ in range(length):
            ptr = bindings.first

            if len(ptr) != 2:
                raise SchemeError("bad formed bindings")

            if not scheme_symbolp(ptr.first):
                raise SchemeError(f"{ptr.first} is not a symbol")

            newenv.define(ptr.first, scheme_eval(ptr.rest.first, env))
            bindings = bindings.rest
        return eval_all(args.rest, newenv)


SPECIAL_FORMS = {
    "define": do_and_define,
    "if": do_and_if,
    "quote": do_and_quote,
    "lambda": do_and_lambda,
    "begin": do_and_begin,
    "and": do_and,
    "or": do_or,
    "cond": do_cond,
    "mu": do_and_mu,
    "let": do_and_let,
    "define-macro": define_macro,
}
# END PROBLEM 1/2/3
