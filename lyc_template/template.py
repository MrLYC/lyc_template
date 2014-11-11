#!/usr/bin/env python
# encoding: utf-8

import re


class Template(object):
    VarsPattern = r"[\.\w]+?"
    QuotePattern = r"{{\s*(%s)\s*}}" % VarsPattern
    VarSeparator = "."

    _VarsRex = re.compile(VarsPattern)
    _QuoteRex = re.compile(QuotePattern)

    def __init__(self, template, default=None, ignorecase=True, tostr=str):
        self._template = self._QuoteRex.split(template)
        self._defalut = default
        self._ignorecase = ignorecase
        self._tostr = tostr

    def get_var(self, var_name, model):
        """Get the var from model, if the var not found,
        use self._defalut.

        Args:
            var_name: var quote name.
            model: model from self.render.

        Return:
            var value as a string.
        """
        target = model
        var_name = var_name.lower() if self._ignorecase else var_name

        for name in var_name.split(self.VarSeparator):
            # var not found
            if target is None:
                target = self._defalut
                break

            target = target.get(name)

        return self._tostr(target)

    def render(self, model):
        """Render the template with model.

        Args:
            model: a dict object which the template vars quoted for.

        Return:
            string.
        """
        parts = []
        isvar = True

        for part in self._template:
            isvar = not isvar
            parts.append(self.get_var(part, model) if isvar else part)

        return "".join(parts)