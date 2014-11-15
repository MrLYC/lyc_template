#!/usr/bin/env python
# encoding: utf-8

from unittest import TestCase

from lyc_template.template import Template


class TestTemplate(TestCase):
    TestModel = {
        "host": {
            "ip": "127.0.0.1",
            "user": {
                "name": "Bill"
            }
        },
        "id": "9527",
        "items": [1, 2, 3]
    }

    def test_useage(self):
        template = "{{ host.user.name}} is using host[{{ HosT.IP }}] which id is {{ID }}"
        template_render = Template(template)
        assert template_render.render(self.TestModel) == \
            "Bill is using host[127.0.0.1] which id is 9527"

        template = "{'model_items': {{ items }}}"
        template_render = Template(template)
        assert template_render.render(self.TestModel) == \
            "{'model_items': [1, 2, 3]}"

    def test_var_not_found(self):
        template = "{{None}} is None"
        template_render = Template(template)
        assert template_render.render(self.TestModel) == \
            "None is None"

        template = "host.{{host.None}} also is None"
        template_render = Template(template)
        assert template_render.render(self.TestModel) == \
            "host.None also is None"

        template = "var id is {{id}}, and ID is {{ID}}"
        template_render = Template(template, ignorecase=False)
        assert template_render.render(self.TestModel) == \
            "var id is 9527, and ID is None"

    def test_option(self):
        template = "the law of host.ip is {{ host.ip }}"
        template_render = Template(template, tostr=repr)
        assert template_render.render(self.TestModel) == \
            "the law of host.ip is '127.0.0.1'"

        template = "the coustomed default val of var None is {{ None }}"
        template_render = Template(template, default="<Null>")
        assert template_render.render(self.TestModel) == \
            "the coustomed default val of var None is <Null>"
