# 🇹🇼 ROC-flag (Multi-resolution Suite)

> [🇹🇼正體中文](#%E6%AD%A3%E9%AB%94%E4%B8%AD%E6%96%87) ・ [🇺🇸/🇬🇧English](#english)

---

## 🇹🇼 正體中文

### 專案簡介

本專案旨在透過 Python 內建的 `turtle` 函式庫，以嚴謹的數學公式重現三面與中華民國密切相關的旗幟：

1. **中華民國國旗**（青天白日滿地紅）——嚴格遵循[**中華民國內政部**](https://www.moi.gov.tw)**頒布之國旗畫法**繪製。
2. **鐵血十八星旗**——辛亥革命武昌起義旗幟，依據[**武昌首義同志會**](https://www.19111010.com.tw)**之歷史考證**繪製。
3. **五色旗**（五族共和旗）——中華民國建國初期（1912–1928）國旗，依據旗面比例 **5:8** 繪製五色橫條。

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
| `ROC_flag(240x160).ipynb` | 240 × 160 | 1.0x | [已上架 Google Colab 支援](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/ROC_flag(240x160).ipynb) |
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

九角星突出三角形的精確邊長（L=240，縮放因子 $= 12$）：

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
| `iron_blood_flag(240x150).py` | 240 × 150 | 1.0x (基準) | [已上架](https://github.com/091cc/ROC-flag/blob/main/Iron-Blooded_18_stars_flag.py) |
| `iron_blood_flag(240x150).ipynb` | 240 × 150 | 1.0x | [已上架 Google Colab 支援](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/Iron-Blooded_18_stars_flag.ipynb) |

---

### 三、五色旗（五族共和旗）

#### 歷史背景

五色旗為中華民國第一代國旗，由南京臨時政府與北洋政府採用，正式使用期間為 **1912 至 1928 年**。旗面由上而下依序排列紅、黃、藍、白、黑五色橫條，分別象徵漢、滿、蒙、回、藏五族共和。此五色同時呼應中國傳統五行學說（火、土、木、金、水），兼具五德（仁、義、禮、智、信）之意涵。1928 年北伐完成後，五色旗正式由青天白日滿地紅旗取代。

#### 技術特點與繪製規範

- **設定比例**：繪製縱比橫為 **5:8** 的長方形旗面。
- **五色橫條**：由上而下均等劃分為五條，每條高度為旗面高度之 $1/5$。
- **色彩順序**（由上而下）：

| 橫條 | 顏色 | 色碼 | 象徵民族 |
| --- | --- | --- | --- |
| 第一條 | 紅 | `#FE0000` | 漢族 |
| 第二條 | 黃 | `#FFC000` | 滿族 |
| 第三條 | 藍 | `#0070C0` | 蒙古族 |
| 第四條 | 白 | `#FFFFFF` | 回族 |
| 第五條 | 黑 | `#000000` | 藏族 |

#### 版本清單

| 檔案名稱 | 解析度 | 比例 | 狀態 |
| --- | --- | --- | --- |
| `five_color_flag(400x250).py` | 400 × 250 | 1.0x (基準) | [已上架](https://github.com/091cc/ROC-flag/blob/main/five_color_flag(400x250).py) |
| `five_color_flag(400x250).ipynb` | 400 × 250 | 1.0x | [已上架 Google Colab 支援](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/five_color_flag(400x250).ipynb) |

---

### 執行方式

#### 1. Python 腳本版本 (.py)

直接於終端機執行對應尺寸的檔案：

```bash
python3 "ROC_flag(240x160).py"
```

#### 2. Jupyter Notebook 版本 (.ipynb)

本專案提供 `.ipynb` 版本以支援 Google Colab 開發環境：

- 匯入方式：將檔案上傳至 [Google Colab](https://colab.research.google.com)，或直接從本 GitHub 倉庫點擊連結開啟。
- 連結
  1. [ROC_flag(240x160)](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/ROC_flag(240x160).ipynb)
  2. [iron_blood_flag(240x150)](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/Iron-Blooded_18_stars_flag.ipynb)
  3. [five_color_flag(400x250)](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/five_color_flag(400x250).ipynb)

---

### 開發背景與致謝

**中華民國國旗**之核心幾何計算法由 **[sugardaddy16](https://github.com/sugardaddy16)** 與**本人**共同研發完成。

開發過程中，我們投入了整整一天的時間進行數學推導與座標校正。儘管當時正處於重要考試前九天的關鍵衝刺期，我們仍憑藉對程式開發、幾何美學及愛國的熱忱，堅持完成了這項兼具精確度與美觀的專案。特別感謝 Seven 在複雜三角形計算上的校正與貢獻。

**鐵血十八星旗**之規格考證參考自[武昌首義同志會](https://www.19111010.com.tw)。

---

## 🇺🇸/🇬🇧English

### Overview

This project reproduces three flags closely associated with the Republic of China using Python's built-in `turtle` library and rigorous mathematical formulas:

1. **ROC National Flag** (Blue Sky, White Sun, and a Wholly Red Earth) — drawn strictly following the **[Ministry of the Interior, ROC](https://www.moi.gov.tw)** flag specifications.
2. **Iron Blood 18-Star Flag** (鐵血十八星旗) — the flag of the Hubei Military Government during the 1911 Wuchang Uprising, drawn according to historical research by the **[Wuchang Uprising Comrades Association](https://www.19111010.com.tw)**.
3. **Five-Color Flag** (五色旗, Five Races Under One Union Flag) — the first national flag of the Republic of China (1912–1928), rendered with five equal horizontal stripes in a **5:8** aspect ratio.

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
| `ROC_flag(240x160).ipynb` | 240 × 160 | 1.0x | [Google Colab Support](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/ROC_flag(240x160).ipynb) |
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
| `iron_blood_flag(240x150).py` | 240 × 150 | 1.0x (Base) | [Available](https://github.com/091cc/ROC-flag/blob/main/Iron-Blooded_18_stars_flag.py) |
| `iron_blood_flag(240x150).ipynb` | 240 × 150 | 1.0x | [Google Colab Support](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/Iron-Blooded_18_stars_flag.ipynb) |

---

### III. Five-Color Flag (Five Races Under One Union)

#### Historical Background

The Five-Color Flag served as the first national flag of the Republic of China, adopted by both the Nanjing Provisional Government and the Beiyang Government from **1912 to 1928**. Its five horizontal stripes — red, yellow, blue, white, and black from top to bottom — represent the Han, Manchu, Mongol, Hui, and Tibetan peoples respectively, embodying the concept of the Five Races Under One Union (五族共和). The five colors also reflect the traditional Five Elements theory (fire, earth, wood, metal, water) and the Five Virtues (benevolence, righteousness, propriety, wisdom, faithfulness). The flag was formally replaced by the Blue Sky, White Sun, and a Wholly Red Earth flag following the completion of the Northern Expedition in 1928.

#### Technical Highlights & Drawing Standards

- **Aspect Ratio**: A rectangular field with a **5:8** height-to-width ratio.
- **Five Equal Stripes**: The field is divided into five equal horizontal bands, each 1/5 of the total flag height.
- **Color Order** (top to bottom):

| Stripe | Color | Hex Code | Represented People |
| --- | --- | --- | --- |
| 1st | Red | `#FE0000` | Han |
| 2nd | Yellow | `#FFC000` | Manchu |
| 3rd | Blue | `#0070C0` | Mongol |
| 4th | White | `#FFFFFF` | Hui |
| 5th | Black | `#000000` | Tibetan |

#### Available Versions

| Filename | Resolution | Scale | Status |
| --- | --- | --- | --- |
| `five_color_flag(400x250).py` | 400 × 250 | 1.0x (Base) | [Available](https://github.com/091cc/ROC-flag/blob/main/five_color_flag(400x250).py) |
| `five_color_flag(400x250).ipynb` | 400 × 250 | 1.0x | [Google Colab Support](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/five_color_flag(400x250).ipynb) |

---

### Usage

#### 1. Python Script (.py)

Execute the script via terminal:

```bash
python3 "ROC_flag(240x160).py"
```

#### 2. Jupyter Notebook (.ipynb)

This project provides `.ipynb` files optimized for **Google Colab**:

- **Import**: Upload the file to [Google Colab](https://colab.research.google.com), or open it directly from this GitHub repository by clicking the link.

- **Links**
  1. [ROC_flag(240x160)](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/ROC_flag(240x160).ipynb)
  2. [iron_blood_flag(240x150)](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/Iron-Blooded_18_stars_flag.ipynb)
  3. [five_color_flag(400x250)](https://colab.research.google.com/github/091cc/ROC-flag/blob/main/five_color_flag(400x250).ipynb)

---

### Acknowledgments & Background

The core geometric algorithms for the **ROC National Flag** were co-developed by **[sugardaddy16](https://github.com/sugardaddy16)** and **myself**.

During the development process, we spent a whole day on mathematical derivation and coordinate correction. Although we were in the critical sprint period nine days before the important exam, we still insisted on completing this project with both accuracy and beauty with our enthusiasm for program development, geometric aesthetics and patriotism. Special thanks to Seven for its correction and contribution to the complex trigonometric calculations.

The **Iron Blood 18-Star Flag** specifications are referenced from the [Wuchang Uprising Comrades Association](https://www.19111010.com.tw).
