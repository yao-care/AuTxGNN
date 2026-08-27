---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Naproxen：從關節炎/疼痛治療到 Brachydactyly-Syndactyly Syndrome（低信心度預測）

## 一句話摘要

Naproxen 是傳統非類固醇消炎止痛藥（NSAID），臨床上廣泛用於關節炎、疼痛與發炎症狀。
TxGNN 模型將其評分最高的新適應症為 **Brachydactyly-Syndactyly Syndrome**（短指-併指症候群），
但目前**沒有任何臨床試驗或文獻支持**此連結，機轉理由亦明確指出該疾病屬先天骨骼發育異常，與 NSAID 消炎機轉無直接病理關聯。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 本證據包未提供 TFDA/ARTG 核准適應症文字（Naproxen 目前未在澳洲上市）；就公開藥理學常識，Naproxen 為傳統 NSAID，普遍用於疼痛、發炎與關節炎治療 |
| 預測新適應症 | Brachydactyly-Syndactyly Syndrome（短指-併指症候群） |
| TxGNN 預測分數 | 99.35% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 澳洲市場狀態 | 未上市 |
| ARTG 登錄數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前尚無詳細作用機轉資料。根據已知資訊，Naproxen 為傳統非選擇性 COX-1/COX-2 抑制劑類 NSAID 之一員，其於疼痛與發炎相關適應症之療效已獲廣泛臨床證實，機轉上主要透過抑制前列腺素合成產生消炎、鎮痛與解熱作用。

然而，Brachydactyly-Syndactyly Syndrome 屬先天性肢端骨骼發育異常（骨骼形成基因缺陷所致），病理核心為胚胎發育期的骨骼形成機制異常，而非發炎介質驅動的病理過程。根據本證據包提供的 `repurposing_rationale`，此預測「與 NSAID 之 COX 抑制/消炎機轉無直接病理連結」，推測高分主要源自知識圖譜中骨骼相關節點的間接鄰近性（graph-proximity 假陽性），而非真實的機轉關聯。

換言之，此預測目前**沒有機轉層面的合理支持**，屬於需要人工審查排除的低信心度候選。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 澳洲市場資訊

Naproxen 目前**未在澳洲上市**（ARTG 登錄數：0），本證據包未提供任何 ARTG 條目資料。

---

## 安全性考量

請參閱 TGA 核准的產品說明書（PI）以取得安全性資訊（本證據包之關鍵警語、禁忌症與藥物交互作用資料均缺失）。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
此候選僅達 L5 證據等級（純模型預測，無任何臨床試驗或文獻佐證），且機轉理由本身已明確指出與原適應症之藥理機轉無直接病理連結，高分可能為知識圖譜結構性假陽性。不建議投入後續資源。

**若要繼續推進，需要補充：**
- 至少 1 項體外/體內機轉研究，證實 COX 抑制路徑與短指-併指症候群病理的關聯性
- TFDA/TGA 產品說明書（仿單警語、禁忌症）以完成 S1 安全性初評
- DrugBank 完整 MOA 資料
- 若機轉支持薄弱，建議直接排除此候選

---

**附註：** 本證據包（TW-DB00788-multi）內含 10 個 TxGNN 預測適應症，其中排名第 8（inflammatory spondylopathy）與第 10（polyarticular juvenile rheumatoid arthritis）之證據等級達 L2、決策階段 S2、建議「Proceed with Guardrails」，但兩者的 `repurposing_rationale` 均註明屬既有臨床實務用途之再確認，而非新穎機轉假說。若目的是尋找具實證支持的候選，建議改以這兩項適應症為主體另行產出報告，而非本文所評估之 rank 1 候選。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

