# 🇹🇼 ROC-flag (Multi-resolution Suite)

> [🇹🇼正體中文](#正體中文) ・ [🇺🇸/🇬🇧English](#english)

---

<a name="正體中文"></a>

## 🇹🇼 正體中文

### 專案簡介
本專案旨在透過 Python 內建的 `turtle` 函式庫，嚴格遵循**中華民國內政部頒布之國旗畫法**，以嚴謹的數學公式重現中華民國國旗的幾何美感。專案支援多種解析度版本，確保在不同顯示環境下均能維持完美的比例與精確度。

### 技術特點與繪製規範
本專案之繪製流程完全符合法定標準：
*   **設定比例**：繪製橫比縱為 3:2 的紅色長方形旗面。
*   **繪製青天**：於左上角繪製佔全旗 $1/4$ 的青色長方形（縱橫分別為旗面之 $1/2$）。
*   **精準定位**：以青天長方形之中心為白日圓心。
*   **白日體比例**：白日體（中心圓）半徑為青天高度之 $1/8$。
*   **十二道光芒**：
    *   光芒頂點（外圓）半徑為白日體半徑之 $17/15$ 倍。
    *   每道光芒間隔 $30^\circ$，光芒頂點位於外圓周上，基部與白日體相連。
    *   白日體與十二道尖角光芒均採用純白色填充。

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
This project reproduces the geometric beauty of the Republic of China flag using Python's built-in `turtle` library, strictly following the **official flag specifications mandated by the Ministry of the Interior**. It ensures geometric precision across various resolutions through rigorous mathematical formulas.

### Technical Highlights & Drawing Standards
The rendering process strictly adheres to statutory standards:
*   **Aspect Ratio**: A red rectangular field with a 3:2 width-to-height ratio.
*   **Blue Canton**: A blue rectangle in the upper-left corner occupying 1/4 of the total flag area.
*   **Sun Placement**: The center of the blue canton serves as the center of the white sun.
*   **Sun Emblem (Sun Body)**: The radius of the central white sun is 1/8 of the height of the blue canton.
*   **Twelve Rays**:
    *   The outer radius (tips of the rays) is 17/15 times the radius of the sun body.
    *   Twelve rays are spaced at 30° intervals, with vertices positioned on the outer circle and bases connected to the sun body.
    *   Both the sun body and the 12 pointed rays are filled in solid white.

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
