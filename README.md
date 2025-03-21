# OpenAI Responses API


## Important things to know

1. **Backward Compatibility**: The Responses API is a superset of Chat Completions - everything you can do with Chat Completions can be done with Responses API, plus additional features.

2. **Migration Timeline**: The Chat Completions API is not being deprecated and will continue to be supported indefinitely as an industry standard for building AI applications, while the Assistants API (not Chat Completions) is the one planned for eventual deprecation in 2026.


3. **Key New Features**:
   - Simplified interface for different interaction types
   - Native support for web search capabilities
   - A new `developer` role you can use
   - Improved support for reasoning models
   - Built-in file/vector search functionality
   - Simplified conversation state management

4. **Continous chating feature**:
   - **Response_id**: will there that will contain the information about previous chat so continous chating is easy.

5. **Available Tools**:
   - **Web search**: Include data from the Internet in model response generation
   - **File search**: Search the contents of uploaded files for context when generating a response
   - **Computer use**: Create agentic workflows that enable a model to control a computer interface
   - **Function calling**: Enable the model to call custom code that you define, giving it access to additional data and capabilities

6. **Implementation Considerations**:
   - API structure changes but core AI engineering principles remain the same
   - Features that previously required multiple API calls can now be done in single calls
   - The fundamental patterns of retrieval, tools, and memory management still apply

7. **Implementation Considerations**:
   -API structure changes but core AI engineering principles remain the same
   -Features that previously required multiple API calls can now be done in single calls

8. **Documentation Resources**:
   - Official OpenAI documentation: https://platform.openai.com/docs/api-reference/responses
