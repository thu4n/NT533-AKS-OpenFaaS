from faas import Function

class HelloWorld(Function):
  def __init__(self):
    self.languages = {
      "C++": "#include <iostream>\nint main() { std::cout << \"Hello World!\" << std::endl; return 0; }",
      "Javascript": "console.log(\"Hello World!\");",
      "Java": "// This requires a Java runtime environment\npublic class HelloWorld {  public static void main(String[] args) {  System.out.println(\"Hello World!\");  }}",
      "Golang": "package main\nimport \"fmt\"\nfunc main() {\n  fmt.Println(\"Hello World!\")\n}",
    }

  def handle(self, event, context):
    lang = event.body.get("lang", event.query.get("lang"))  # Get language from body or query
    code = self.languages.get(lang)
    return {"statusCode": 200 if code else 400, "body": code or "Language not supported!"}

function = HelloWorld()
