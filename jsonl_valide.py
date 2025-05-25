import json
import sys

def translate_error(error_msg):
    """
    将 JSON 解析错误信息翻译为中文
    """
    if "Expecting value" in error_msg:
        return "期望一个值（如字符串、数字、对象、数组、true、false 或 null）"
    elif "Expecting ',' delimiter" in error_msg:
        return "期望逗号分隔符（用于分隔键值对或数组元素）"
    elif "Expecting ':' delimiter" in error_msg:
        return "期望冒号分隔符（用于分隔键与值）"
    elif "Expecting property name" in error_msg:
        return "期望属性名（需用双引号包裹）"
    elif "Invalid control character" in error_msg:
        return "包含无效的控制字符（如换行符、制表符等）"
    elif "Extra data" in error_msg:
        return "包含多余的数据（可能多个 JSON 对象挤在同一行）"
    else:
        return "未知的 JSON 格式错误"

def check_jsonl(file_path):
    """
    检查 .jsonl 文件格式是否正确
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            line_number = i + 1
            try:
                json.loads(line.strip())  # 移除前后空格
                # print(f"[✅] 行 {line_number}: 格式正确")
            except json.JSONDecodeError as e:
                error_type = translate_error(e.msg)
                print(f"[❌] 行 {line_number}, 列 {e.colno}: {error_type}")
                print(f"  → 原始错误信息: {e}")

    except FileNotFoundError:
        print(f"[⚠️] 文件未找到: {file_path}")
    except Exception as e:
        print(f"[⚠️] 发生意外错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python check_jsonl.py <文件路径>")
    else:
        check_jsonl(sys.argv[1])