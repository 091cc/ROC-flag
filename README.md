# 🚩 ROC-flag (Multi-resolution Suite)

> [🇹🇼正體中文](#%E6%AD%A3%E9%AB%94%E4%B8%AD%E6%96%87) ・ [🇺🇸/🇬🇧English](#english)

---

## 🇹🇼 正體中文

### 專案簡介

本專案旨在透過 Python 內建的 `turtle` 函式庫，以嚴謹的數學公式重現兩面與中華民國密切相關的旗幟：

1. **中華民國國旗**（青天白日滿地紅）——嚴格遵循**[中華民國內政部](https://www.moi.gov.tw)頒布之國旗畫法**繪製。
2. **鐵血十八星旗**——辛亥革命武昌起義旗幟，依據**[武昌首義同志會](https://www.19111010.com.tw)**之歷史考證繪製。

專案支援多種解析度版本，確保在不同顯示環境下均能維持完美的比例與精確度。

---

### 一、中華民國國旗

#### 技術特點與繪製規範

本專案之繪製流程完全符合法定標準：

- **設定比例**：繪製橫比縱為 3:2 的紅色長方形旗面。
- **繪製青天**：於左上角繪製佔全旗 $1/4$ 的青色長方形（縱橫分別為旗面之 $1/2$）。
- **精準定位**：以青天長方形之中心為白日圓心。
- **白日體比例**：白日體（中心圓）半徑為青天高度之 $1/8$。
- **十二道光芒**：
  - 光芒頂點（外圓）半徑為白日體半徑之 $17/15$ 倍。
  - 每道光芒間隔 $30^\circ$，光芒頂點位於外圓周上，基部與白日體相連。
  - 白日體與十二道尖角光芒均採用純白色填充。

#### 版本清單

| 檔案名稱 | 解析度 | 比例 | 狀態 |
| --- | --- | --- | --- |
| `ROC_flag(240x160).py` | 240 × 160 | 1.0x (基準) | [已上架](https://github.com/091cc/ROC-flag/blob/main/ROC_flag(240x160).py) |
| `ROC_flag(240x160).ipynb` | 240 × 160 | 1.0x | [已上架 Google Colab 支援](https://github.com/091cc/ROC-flag/blob/main/ROC_flag(240x160).ipynb) |
| `ROC_flag(600x400).py` | 600 × 400 | 2.5x | 製作中 |

---

### 二、鐵血十八星旗

#### 技術特點與繪製規範

依據**武昌首義同志會**考證，以旗橫長 $L=20$ 單位為基準：

- **設定比例**：繪製橫比縱為 **8:5** 的正紅色長方形旗面。
- **黑色九角星**：施萊夫利符號 **{9/4}**，每個內角 20°，置中於旗面。
- **外九星**：位於大圓（半徑 $R = \frac{11}{2}$ 單位）上，對應各尖頂。
- **內九星**：位於小圓（半徑 $r = \frac{3}{2}$ 單位）上，與外星同處一內角平分線方向。
- **十八顆黃星大小一致**。
- **標準配色**：正紅 `#FF0000`・正黑 `#000000`・正黃 `#FFFF00`

#### 幾何公式

九角星突出三角形的精確邊長（$L=240$，縮放因子 $= 12$）：

**斜邊**（尖頂 → 內凹點）：

$$12 \times \sqrt{\frac{65 - 33\cos\dfrac{\pi}{9}}{2}} \approx 49.47$$

**底邊**（兩內凹點連線）：

$$36\sin\frac{\pi}{9} \approx 12.31$$

Python 表示：

```python
import math

hypotenuse = 12 * math.sqrt((65 - 33 * math.cos(math.pi / 9)) / 2)
base = 36 * math.sin(math.pi / 9)
```

#### 版本清單

| 檔案名稱 | 解析度 | 比例 | 狀態 |
| --- | --- | --- | --- |
| `iron_blood_flag(240x150).py` | 240 × 150 | 1.0x (基準) | 已上架 |

---

### 執行方式

#### 1. Python 腳本版本 (.py)

直接於終端機執行對應尺寸的檔案：

```bash
python3 "ROC_flag(240x160).py"
```

#### 2. Jupyter Notebook 版本 (.ipynb)

本專案提供 `.ipynb` 版本以支援 Google Colab 開發環境：

- 匯入方式：將檔案上傳至 [Google Colab](https://colab.research.google.com)，或直接從本 GitHub 倉庫連結開啟。

---

### 開發背景與致謝

**中華民國國旗**之核心幾何計算法由 **[sugardaddy16](https://github.com/sugardaddy16)** 與**本人**共同研發完成。

開發過程中，我們投入了整整一天的時間進行數學推導與座標校正。儘管當時正處於重要考試前九天的關鍵衝刺期，我們仍憑藉對程式開發、幾何美學及愛國的熱忱，堅持完成了這項兼具精確度與美觀的專案。特別感謝 Seven 在複雜三角形計算上的校正與貢獻。

**鐵血十八星旗**之規格考證參考自[武昌首義同志會](https://www.19111010.com.tw)。

---

## 🇺🇸/🇬🇧English

### Overview

This project reproduces two flags closely associated with the Republic of China using Python's built-in `turtle` library and rigorous mathematical formulas:

1. **ROC National Flag** (Blue Sky, White Sun, and a Wholly Red Earth) — drawn strictly following the **[Ministry of the Interior, ROC](https://www.moi.gov.tw)** flag specifications.
2. **Iron Blood 18-Star Flag** (鐵血十八星旗) — the flag of the Hubei Military Government during the 1911 Wuchang Uprising, drawn according to historical research by the **[Wuchang Uprising Comrades Association](https://www.19111010.com.tw)**.

---

### I. ROC National Flag

#### Technical Highlights & Drawing Standards

The rendering process strictly adheres to statutory standards:

- **Aspect Ratio**: A red rectangular field with a 3:2 width-to-height ratio.
- **Blue Canton**: A blue rectangle in the upper-left corner occupying 1/4 of the total flag area.
- **Sun Placement**: The center of the blue canton serves as the center of the white sun.
- **Sun Emblem (Sun Body)**: The radius of the central white sun is 1/8 of the height of the blue canton.
- **Twelve Rays**:
  - The outer radius (tips of the rays) is 17/15 times the radius of the sun body.
  - Twelve rays are spaced at 30° intervals, with vertices positioned on the outer circle and bases connected to the sun body.
  - Both the sun body and the 12 pointed rays are filled in solid white.

#### Available Versions

| Filename | Resolution | Scale | Status |
| --- | --- | --- | --- |
| `ROC_flag(240x160).py` | 240 × 160 | 1.0x (Base) | [Available](https://github.com/091cc/ROC-flag/blob/main/ROC_flag(240x160).py) |
| `ROC_flag(240x160).ipynb` | 240 × 160 | 1.0x | [Google Colab Support](https://github.com/091cc/ROC-flag/blob/main/ROC_flag(240x160).ipynb) |
| `ROC_flag(600x400).py` | 600 × 400 | 2.5x | In Progress |

---

### II. Iron Blood 18-Star Flag

#### Technical Highlights & Drawing Standards

Based on historical research by the Wuchang Uprising Comrades Association, using flag width $L = 20$ units as reference:

- **Aspect Ratio**: Red rectangular field, width-to-height = **8:5**.
- **Black 9-Pointed Star**: Schläfli symbol **{9/4}**, interior angle 20°, centered on the flag.
- **Outer 9 Stars**: On the large circle ($R = \frac{11}{2}$ units), at each spike tip.
- **Inner 9 Stars**: On the small circle ($r = \frac{3}{2}$ units), along each interior angle bisector.
- **All 18 yellow circles are equal in size**.
- **Standard colors**: Red `#FF0000` · Black `#000000` · Yellow `#FFFF00`

#### Geometry

Exact side lengths of each spike triangle ($L = 240$, scale factor $= 12$):

**Hypotenuse** (spike tip → concave point):

$$12 \times \sqrt{\frac{65 - 33\cos\dfrac{\pi}{9}}{2}} \approx 49.47$$

**Base** (between two adjacent concave points):

$$36\sin\frac{\pi}{9} \approx 12.31$$

#### Available Versions

| Filename | Resolution | Scale | Status |
| --- | --- | --- | --- |
| `iron_blood_flag(240x150).py` | 240 × 150 | 1.0x (Base) | Available |

---

### Usage

#### 1. Python Script (.py)

Execute the script via terminal:

```bash
python3 "ROC_flag(240x160).py"
```

#### 2. Jupyter Notebook (.ipynb)

This project provides `.ipynb` files optimized for **Google Colab**:

- **Import**: Visit [Google Colab](https://colab.research.google.com), then upload the file or open it directly via the GitHub integration.

---

### Acknowledgments & Background

The core geometric algorithms for the **ROC National Flag** were co-developed by **[sugardaddy16](https://github.com/sugardaddy16)** and **myself**.

During the development process, we spent a whole day on mathematical derivation and coordinate correction. Although we were in the critical sprint period nine days before the important exam, we still insisted on completing this project with both accuracy and beauty with our enthusiasm for program development, geometric aesthetics and patriotism. Special thanks to Seven for its correction and contribution to the complex trigonometric calculations.

The **Iron Blood 18-Star Flag** specifications are referenced from the [Wuchang Uprising Comrades Association](https://www.19111010.com.tw).
