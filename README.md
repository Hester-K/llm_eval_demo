## 简介

本项目以标准化大语言模型的测评流程和Benchmark文件格式为切入点，设计一个支持多种Benchmark类型、兼容人工评估与自动评估、能够自动化运行的大语言模型测评系统。

## 项目亮点

#### Benchmark测试流程标准化

- 模型输出：针对单个测试用例，将prompt输入模型获得原始回答（raw response），经过formatter程序处理得到用于评估的formatted response。

- 参考答案：充分兼容不同任务场景的评测需求，支持三种参考答案类型：Given（给定参考答案）；Generated（由其他指定模型生成）；None（不给定参考答案）。

- 评测方式：基于模型输出的formatted response与该测试用例的参考答案进行评测。兼容自动化与人工评测的方式，内置常用评测函数如完全匹配精度（accuracy）、rouge-L、Bleu等，也支持以likert量表的形式选择人工打分评测。

以C-EVAL Benchmark为例，选择Given参考答案类型，以精度作为评估指标，测试流程图如下所示，黑色实线箭头既对于选择测试路径。

![](readme_assets\sample-flowchart.jpg)

#### Benchmark文件组织格式

将Benchmark内容按照基本信息、测试用例、测试程序、测试配置四个部分组织为单个JSON文件，如[SafetyBench dev集文件](datautil\output\SafetyBench_dev.json)

#### 支撑运行系统

基于flask框架开发上支持Benchmark解析、模型测试等功能的web应用作为大语言模型测评的支撑平台

## 下载运行方式

1. 获取仓库代码，安装依赖包

```
$ git clone https://github.com/Hester-K/llm_eval_demo.git
$ cd llm_eval_demo
$ pip install -r requirements.txt
```

2. 在根目录下创建model_config.ini文件配置模型API

```
[GPT]
API_KEY=
BASE_URL=

[Gemini]
API_KEY=

[Qwen]
API_KEY=
```

3. 运行代码，开始使用系统

```
$ python main.py
```

## 已支持Benchmark

- C-EVAL：百科知识
- AlignBench：模型对齐成都
- SafetyBench：模型安全性
- TruthfulQA：模型回答真实性

## 后续工作计划

- 开发完善系统，优化前端UI和操作逻辑，撰写项目文档
- 继续迁移主流常用的Benchmark文件
- 提出全面的软件系统测试和验证方案并完成测试验证