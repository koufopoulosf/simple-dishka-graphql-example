# Simple Dishka and FastAPI GraphQL Example

This simplified example demonstrates how to set up the Dishka container, pass it to the GraphQL context, and use it in a mutation with a simple `HelloWorld` use case.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/koufopoulosf/simple-dishka-graphql-example.git
    cd simple-dishka-graphql-example
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python main.py
    ```

5. Test the GraphQL Mutation

    After starting the server, you can test the GraphQL mutation using the built-in GraphQL Playground available at [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql).

    Use the following mutation for testing purposes:

    ```graphql
    mutation {
      sayHello(name: "Alice") {
        message
      }
    }
    ```

    This should be the expected output:

    ```json
    {
      "data": {
        "sayHello": {
          "message": "Hello, Alice!"
        }
      }
    }
    ```
