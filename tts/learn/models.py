from django.db import models

class EnglishWord(models.Model):
    word = models.CharField(primary_key=True, max_length=255)
    # 聲音檔路徑
    audio_path = models.CharField(max_length=255)

    def __str__(self):
        return self.word
