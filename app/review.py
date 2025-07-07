from app.utils import handle_error
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from app.config import Config

def review_code(code):
    try:
        api_key = Config.AZURE_API_KEY
        if not api_key:
            raise Exception("A key should be provided to invoke the endpoint")

        client = ChatCompletionsClient(
            endpoint=Config.AZURE_ENDPOINT,
            credential=AzureKeyCredential(api_key),
            api_version=Config.API_VERSION
        )

        # payload = {
        #     "messages": [
        #         {
        #             "role": "user",
        #             "content": code
        #         },
        #         {
        #             "role": "assistant",
        #             "content": (
        #                 "You are a code reviewer expert who can review the code and generate the report..."
        #             )
        #         }
        #     ],
        #     "max_tokens": 512
        # }

        payload = {
        "messages": [
            {
            "role": "user",
            "content": code
            },
            {
            "role": "assistant",
            "content": (
                "You are a code reviewer expert who can review the code and generate the report. Report should not contain the introduction or paragraphs. \
                Also give the answers in markdown format. Do not give the thought process or step by step process. Structure the answer like below. Do not give final grade and summary. \
                Also do not elaborate below points in the beginning.\
                Code Analysis Report\
                Performance Optimizations: list\
                Security Vulnerabilities: list\
                Best Practices & Standards Violations: list\
                Potential Bugs: list\
                Architecture & Design Patterns Issues: list\
                \
                example:\
                Review the following code\
                response:\
                **Code Analysis Report**\
                **Performance Optimizations:** list\
                **Security Vulnerabilities:** list\
                **Best Practices & Standards Violations:** list\
                **Potential Bugs:** list\
                **Architecture & Design Patterns Issues:** list\ "
                )
            }
        ],
        "max_tokens": 512
        }

        response = client.complete(payload)
        return response.choices[0].message.content

    except Exception as e:
        return handle_error(e)
