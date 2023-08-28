import openai


openai.api_key = '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'


def completion(prompt, **kwargs):
    return openai.ChatCompletion.create(
        **kwargs,
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': prompt},
        ]
    )

def completion_image(prompt, n, **kwargs):
    response = openai.Image.create(
        prompt=prompt,
        n=n,
        **kwargs,
    )
    image_url = []
    for i in range(0, n):
        image_url.append(response['data'][i]['url'])
    
    return image_url

# if __name__ == '__main__':
#     prompt = 'a white siamese cat'
#     print('正在加载，请稍后...')
#     print(completion_image(prompt, n=1, size='1024x1024'))