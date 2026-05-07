# 🇹🇼 ROC-flag (Multi-resolution Suite)

> [🇹🇼正體中文](#正體中文) ・ [🇺🇸/🇬🇧English](#english)

---

<a name="正體中文"></a>

## 🇹🇼 正體中文

### 專案簡介
本專案旨在透過 Python 內建的 `turtle` 函式庫，以嚴謹的數學公式重現中華民國國旗的幾何美感。專案現已擴充支援多種解析度版本，確保在不同顯示環境下均能維持完美的比例與精確度。

### 技術特點
*   **多解析度支援**：提供從 240x160 至 600x400 的多種預設尺寸。
*   **幾何精確度**：使用三角函數與無理數公式精確定義十二道光芒的頂點，確保在縮放時不產生幾何偏差。
*   **參數化邏輯**：基於國徽法標準比例，計算白日與藍色分隔環的相對位置。

### 版本清單
| 檔案名稱 | 解析度 | 比例 | 狀態 |
| :--- | :--- | :--- | :--- |
| `ROC_flag(240x160).py` | 240 × 160 | 1.0x (基準) | [已上架](https://github.com/091cc/ROCflag/blob/main/ROC_flag(240x160).py) |
| `ROC_flag(240x160).ipynb` | 240 × 160 | 1.0x | [已上架 Google Colab 支援](https://github.com/091cc/ROCflag/blob/main/ROC_flag(240x160).ipynb) |
| `ROC_flag(600x400).py` | 480 × 320 | 2.5x | 製作中 |

### 執行方式
#### 1. Python 腳本版本 (.py)
直接於終端機執行對應尺寸的檔案：
```bash
python3 "ROC_flag(240x160).py"
```
#### 2. Jupyter Notebook 版本 (.ipynb)
本專案提供 .ipynb 版本以支援Google Colab開發環境：
匯入[Google Colab](https://colab.research.google.com)
* 匯入方式：將檔案上傳至 Google Colab 或直接從本 GitHub 倉庫連結開啟。

### 開發背景與致謝
本專案之核心幾何計算法由 **Seven** 與 **本人** 共同研發完成。

開發過程中，我們投入了整整一天的時間進行數學推導與座標校正。儘管當時正處於重要考試前九天的關鍵衝刺期，我們仍憑藉對程式開發、幾何美學及愛國的熱忱，堅持完成了這項兼具精確度與美觀的專案。特別感謝 Seven 在複雜三角型計算上的校正與貢獻。

---

<a name="english"></a>

## 🇺🇸/🇬🇧English
### Overview
This project reproduces the geometric beauty of the Republic of China flag using Python's built-in `turtle` library. By applying rigorous mathematical formulas, it ensures geometric precision across various resolutions, maintaining official proportions in any display environment.

### Technical Highlights
*   **Multi-resolution Support**: Preset sizes ranging from 240x160 to 600x400.
*   **Geometric Precision**: Utilizes trigonometric and irrational formulas to define the 12 rays' vertices, preventing distortion during scaling.
*   **Parametric Logic**: Precisely calculates the positions of the sun emblem and blue spacing ring according to national standards.

### Available Versions
| Filename | Resolution | Scale | Status |
| :--- | :--- | :--- | :--- |
| `ROC_flag(240x160).py` | 240 × 160 | 1.0x (Base) | [Available](https://github.com/091cc/ROCflag/blob/main/ROC_flag(240x160).py) |
| `ROC_flag(240x160).ipynb` | 240 × 160 | 1.0x | [Google Colab Support](https://github.com/091cc/ROCflag/blob/main/ROC_flag(240x160).ipynb) |
| `ROC_flag(600x400).py` | 600 × 400 | 2.5x | In Progress |

### Usage
#### 1. Python Script (.py)
Execute the script via terminal:
```bash
python3 "ROC_flag(240x160).py"
```

#### 2. Jupyter Notebook (.ipynb)
This project provides `.ipynb` files optimized for **Google Colab**:
*   **Import**: Visit [Google Colab](https://colab.research.google.com), then upload the file or open it directly via the GitHub integration.

### Acknowledgments & Background
The core geometric algorithms and logic were co-developed by **Seven** and **myself**.

During the development process, we spent a whole day on mathematical derivation and coordinate correction. Although we were in the critical sprint period nine days before the important exam, we still insisted on completing this project with both accuracy and beauty with our enthusiasm for program development, geometric aesthetics and patriotism. Special thanks to Seven for its correction and contribution to the complex triangular calculation.
