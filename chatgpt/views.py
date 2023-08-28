from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse, StreamingHttpResponse
from django.http import HttpRequest
from .service.chatgpt import completion, completion_image

    
def generate(request):
    return JsonResponse(data=completion('hello'), safe=False)

def get_streaming_content(completion_stream):
    result = ''
    for chunk in completion_stream:
        if chunk['choices'][0]['finish_reason'] is not None:
            result = '[DONE]'
        else:
            result = chunk['choices'][0]['delta'].get('content', '')
        print(result)
        # 处理换行
        result = result.replace('\n', '<br/>')
        yield f"data: {result}\n\n"

def generate_stream(request: HttpRequest):
    question = request.GET['question']
    # 增加流式传输
    completion_stream = completion(question, stream=True)
    return StreamingHttpResponse(
        streaming_content=get_streaming_content(completion_stream),
        # 不加 charset=utf-8 会乱码
        content_type='text/event-stream; charset=utf-8',
    )

def generate_image(request: HttpRequest):
    prompt = request.GET['question']
    size = request.GET['generate_image_size']
    num = int(request.GET['generate_image_num'])
    image_url = completion_image(prompt, n=num, size=size)
    print(image_url)
    
    # return HttpResponse(image_url, content_type='text/html')
    # 传递了一个列表（非字典对象），但是默认情况下JsonResponse只能序列化字典对象。
    # 为了解决这个问题，你需要将safe参数设置为False，以允许JsonResponse序列化非字典对象。
    return JsonResponse(data=image_url, safe=False)
    
def chatgpt(request):
    return render(request, 'chatgpt.html')