# jsonl-doctor
Check for anomalies in LLM training data and provide simple repair tools.

# use
## check
``` shell
(mlx-lora) ~/code/temp-important/mlx-examples/lora git:[main]
python ./jsonl_valide.py ./data/train.jsonl
[❌] 行 2557, 列 226: 包含无效的控制字符（如换行符、制表符等）
  → 原始错误信息: Invalid control character at: line 1 column 226 (char 225)
```

## fix
``` shell
(mlx-lora) ~/code/temp-important/mlx-examples/lora git:[main]
python ./jsonl_fix.py ./data/train.jsonl
[✅] 修复完成，结果已保存至: ./data/train_fixed.jsonl
```