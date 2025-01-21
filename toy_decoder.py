import json

def match_instruction(instruction_bin, instruction_fmt):
    if len(instruction_bin) != len(instruction_fmt):
        return False
    for i in range(len(instruction_fmt)):
        if instruction_fmt[i] != "X" and instruction_bin[i] != instruction_fmt[i]:
            return False
    return True

def decode_instruction(instruction, instruction_set, is_32_bit):
    instruction_bin = f"{instruction:032b}" if is_32_bit else f"{instruction:016b}"
    instruction_str = f"{instruction:08x}" if is_32_bit else f"{instruction:04x}"
    results = []
    for name, details in instruction_set.items():
        if is_32_bit and details["format"] == "16-bit":
            continue
        if match_instruction(instruction_bin, details["opcode"]):
            fields = details["fields"]
            result = {"instruction": name, 'description': details["description"]}
            for field, (start, end) in fields.items():
                result[field] = int(instruction_bin[start:end], 2)
            results.append(result)
    if len(results) == 0:
        results.append(f"Unknown {'32' if is_32_bit else '16'}-bit instruction: {instruction_str}")
    return results

# 加载指令集 JSON 文件
with open("ck802_instruction_set.json", "r", encoding="utf-8") as json_file:
    instruction_set = json.load(json_file)

# 示例：解析输入的指令编码
# 处理用户输入，将hex格式解析为16-bit或32-bit指令
def process_user_input(hex_input):
    # 如果输入是16位（4个字符），直接解析
    if len(hex_input) == 4:
        return int(hex_input, 16), False

    # 如果输入是用空格分隔的16位Little Endian
    if len(hex_input.split()) == 2:
        parts = hex_input.split()
        return int(parts[1] + parts[0], 16), False

    # 如果输入是32位（8个字符），直接解析
    if len(hex_input) == 8:
        return int(hex_input, 16), True

    # 如果输入是用空格分隔的32位Little Endian
    if len(hex_input.split()) == 4:
        parts = hex_input.split()
        high = int(parts[1] + parts[0], 16)
        low = int(parts[3] + parts[2], 16)
        return (high << 16) | low, True

    raise ValueError("Invalid input format")

while True:
    instruction_code_with_type = process_user_input(input("输入指令编码（十六进制）: "))
    decoded = decode_instruction(instruction_code_with_type[0], instruction_set, instruction_code_with_type[1])
    print("解析结果:", decoded)
