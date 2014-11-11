#!/usr/bin/env python
# encoding: utf-8

from unittest import TestCase

from lyc_template.template import Template


class TestTemplate(TestCase):
    def test_useage(self):
        model = {
            "host": {
                "ip": "127.0.0.1",
                "user": {
                    "name": "Bill"
                }
            },
            "id": "9527",
            "items": [1, 2, 3]
        }

        template = "{{ host.user.name}} is using host[{{ HosT.IP }}] which id is {{ID }}"
        template_render = Template(template)
        assert template_render.render(model) == \
            "Bill is using host[127.0.0.1] which id is 9527"

        template = "{'model_items': {{ items }}}"
        template_render = Template(template)
        assert template_render.render(model) == \
            "{'model_items': [1, 2, 3]}"
