# CSky v2(CK802) Instruction Set Toy Decoder

This is a simple Python-based toy decoder for the CSky v2 instruction set. The decoder parses 16-bit and 32-bit hexadecimal instructions and provides a human-readable representation of the decoded instruction along with its fields and description.

## Features
- Decodes both 16-bit and 32-bit CK802 instructions.
- Supports both direct and little-endian formats for input.
- Automatically identifies unknown instructions.
- Flexible JSON-based instruction set definitions for easy extension.

## Prerequisites
- Python 3.6 or above

## Files
- `toy_decoder.py`: Main script for decoding instructions.
- `ck802_instruction_set.json`: JSON file defining the instruction set, including opcodes, formats, and field descriptions.
- `manual_decode_instruction.py`: Helper script file to prepare instruction json file.

## Usage

### 1. Prepare the Instruction Set File
Ensure that the `ck802_instruction_set.json` file is in the same directory as `toy_decoder.py`. This file should include the definitions for all CK802 instructions, formatted as follows:

```json
{
    "ADDI16": {
        "format": "16-bit",
        "opcode": "00100XXXXXXXXXXX",
        "fields": {
            "RZ": [8, 10],
            "IMM8": [0, 7]
        },
        "description": "RZ = RZ + zero_extend(OIMM8)"
    },
    "ADDI32": {
        "format": "32-bit",
        "opcode": "111001XXXXXXXXXX0000XXXXXXXXXXXX",
        "fields": {
            "RZ": [21, 25],
            "RX": [16, 20],
            "IMM12": [0, 11]
        },
        "description": "RZ = RX + zero_extend(OIMM12)"
    }
}
```

### 2. Run the Decoder
Execute the script:

```bash
python toy_decoder.py
```

### 3. Input Instruction Code
Provide the hexadecimal instruction code when prompted. The decoder accepts:

- **16-bit direct format**: Example: `1234`
- **16-bit little-endian format**: Example: `34 12`
- **32-bit direct format**: Example: `12345678`
- **32-bit little-endian format**: Example: `78 56 34 12`

### 4. View Decoded Result
The decoder outputs the decoded instruction, including its name, description, and fields. For example:

**Input:**
```
输入指令编码（十六进制）: 0011
```

**Output:**
```
解析结果: [{
    "instruction": "ADDI16",
    "description": "RZ = RZ + zero_extend(OIMM8)",
    "RZ": 2,
    "IMM8": 3
}]
```

### 5. Handle Unknown Instructions
If the instruction is not recognized, the decoder will return an "Unknown instruction" message.

## Extending the Instruction Set
You can add or modify instruction definitions in the `ck802_instruction_set.json` file. Each instruction must include:
- `format`: Either `16-bit` or `32-bit`.
- `opcode`: The binary representation of the instruction, with `X` indicating variable fields.
- `fields`: Field names and their corresponding bit ranges (start and end positions).
- `description`: A brief explanation of the instruction.

You can use the `manual_decode_instruction.py` for easy preparing instructions, for example, if you want to add the following `SUBI16` instruction, you can use the simple `add_instruction` call with following param:

```python
add_instruction(
    "SUBI",
    "16-bit",
    "00110XXXXXXXXXXX",
    {"RZ": [8, 10], "IMM8": [0, 7]},
    "RZ = RZ - zero_extend(OIMM8)"
)
```

## Example
To add a new instruction `SUBI16`:

```json
"SUBI16": {
    "format": "16-bit",
    "opcode": "00110XXXXXXXXXXX",
    "fields": {
        "RZ": [8, 10],
        "IMM8": [0, 7]
    },
    "description": "RZ = RZ - zero_extend(OIMM8)"
}
```

## Notes
- The script assumes the JSON file is properly formatted and includes valid instruction definitions.
- Ensure that the input hex format matches the expected instruction format.

## License
This project is open-source and distributed under the MIT License. Feel free to modify and use it as needed.
