# lyc_template
一个简单的模版渲染类。

## Features

示例：

```
model = {
    "name": "lyc",
    "foo": {
      "bar": "hello"
    }
  }
template = "{{foo.bar}} {{ name }}"
template_render = Template(template)

print template_render.render(model)
```

输出：
 > hello lyc
