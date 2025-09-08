from translate import Translator
from pykakasi import kakasi
from replace import japanese_to_kouranki


# 转换汉字到平假名
kakasi_instance = kakasi()
kakasi_instance.setMode('J', 'H')  
conv_kana = kakasi_instance.getConverter()

# 罗马音转换
kakasi_romaji = kakasi()
kakasi_romaji.setMode('H', 'a')
kakasi_romaji.setMode('K', 'a')
conv_romaji = kakasi_romaji.getConverter()

def translate_chinese_to_japanese(text):
    """将中文翻译为日文，并生成古朗基语罗马音"""
    # 创建翻译器实例，从中文翻译为日文
    translator = Translator(from_lang="zh", to_lang="ja")
    
    # 翻译文本
    japanese_text = translator.translate(text)

    kana_text = conv_kana.do(japanese_text)
    
    # 将日文转换为古朗基语
    kouranki_text = japanese_to_kouranki(kana_text)
    
    # 将古朗基语转换为罗马音
    romaji = conv_romaji.do(kouranki_text)
    
    return japanese_text, kouranki_text, romaji
