from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from edge_tts import Communicate
import uuid, os
from django.views.decorators.csrf import csrf_exempt
# 從learn的models
from learn.models import EnglishWord
from asgiref.sync import sync_to_async

# Create your views here.

@sync_to_async
def get_eng_word_row(comm_text):
    # 先檢查資料表示是否有該詞彙
    try:
        eng_word_row = EnglishWord.objects.get(word=comm_text)
        return eng_word_row
    except EnglishWord.DoesNotExist:
        return None


"""將詞彙與檔案路徑存入資料庫

Returns:
    _type_: _description_
"""
@sync_to_async
def set_eng_word_row(comm_text, audio_path):
    EnglishWord.objects.create(word=comm_text, audio_path=audio_path)

"""
將文字透過edge_tts轉成聲音檔案，使用異步(async)方式

comm_text: 要轉換的文字

"""
@csrf_exempt
async def edge_tts(request):

    if request.method == "POST":

        # 要轉換的文字
        comm_text = request.POST.get('comm_text')

        # 回傳的資料
        data = {}

        # 先檢查資料表示是否有該詞彙
        eng_word_row = await get_eng_word_row(comm_text)

        if eng_word_row:
            data['audio_file'] = eng_word_row.audio_path
        else:
            # 匯出聲音檔案目錄
            output_dir = f"static/media/"
            # 音檔檔名
            fname = f"{str(uuid.uuid4())}.mp3"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # 匯出檔案的路徑
            output_path = output_dir + fname
            data['audio_file'] = f"/{output_path}"

            # 將文字轉成聲音
            tts = Communicate(text=comm_text)
            # 因為save() 是 coroutine，所以需要await
            await tts.save(output_path)

            # 將該詞彙存入資料庫
            await set_eng_word_row(comm_text, data['audio_file'])
        return JsonResponse(data)
    else:
        return HttpResponse(status=403)