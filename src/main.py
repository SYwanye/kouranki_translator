from translator import translate_chinese_to_japanese

def main():
    print("中文翻译为古朗基语程序")
    print("=" * 30)
    
    while True:
        # 获取用户输入
        chinese_text = input("请输入要翻译的中文（输入'q'退出）: ")
        
        if chinese_text.lower() == 'q':
            print("程序结束")
            break
        
        if chinese_text.strip() == '':
            continue
        
        try:
            # 翻译文本
            japanese, kouranki, romaji = translate_chinese_to_japanese(chinese_text)
            
            # 显示结果
            print(f"\n原文: {chinese_text}")
            print(f"日文: {japanese}")
            print(f"古朗基语: {kouranki}")
            print(f"古朗基语罗马音: {romaji}")
            print("-" * 30)
        except Exception as e:
            print(f"翻译出错: {e}")


if __name__ == "__main__":
    main()