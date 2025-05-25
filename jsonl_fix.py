import json
import re
import sys

def sanitize_string(s):
    """转义 JSON 中的非法控制字符"""
    return s.replace('\t', '\\t') \
            .replace('\n', '\\n') \
            .replace('\r', '\\r') \
            .replace('\b', '\\b') \
            .replace('\f', '\\f')

def fix_jsonl_file(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()

        fixed_lines = []
        for line in lines:
            try:
                # 尝试解析 JSON，若成功则无需修改
                json.loads(line.strip())
                fixed_lines.append(line)
            except json.JSONDecodeError:
                # 若解析失败，转义非法控制字符
                obj = json.loads(sanitize_string(line.strip()))
                fixed_lines.append(json.dumps(obj, ensure_ascii=False) + '\n')

        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.writelines(fixed_lines)

        print(f"[✅] 修复完成，结果已保存至: {output_path}")

    except FileNotFoundError:
        print(f"[⚠️] 错误：文件未找到: {input_path}")
    except Exception as e:
        print(f"[⚠️] 发生意外错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python fix_jsonl.py <输入文件路径>")
    else:
        input_path = sys.argv[1]
        output_path = input_path.replace('.jsonl', '_fixed.jsonl')
        fix_jsonl_file(input_path, output_path)