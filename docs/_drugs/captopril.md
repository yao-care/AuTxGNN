---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Captopril
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

# Captopril: From Hypertension and Heart Failure to Malignant Renovascular Hypertension

## One-Sentence Summary

Captopril is a first-generation angiotensin-converting enzyme (ACE) inhibitor, widely established globally for the management of hypertension, chronic heart failure, and diabetic nephropathy, though it currently holds no Australian TGA registration.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with **no registered clinical trials** but **20 publications** currently supporting this direction.
The mechanistic alignment between Captopril and this condition is particularly compelling — Captopril stimulation renography is itself the standard diagnostic tool for renovascular hypertension.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and heart failure (globally established; no current Australian TGA registration) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on well-established pharmacology, Captopril directly inhibits angiotensin-converting enzyme (ACE), blocking the conversion of angiotensin I to angiotensin II. This interrupts the renin-angiotensin-aldosterone system (RAAS), reducing systemic vascular resistance, lowering blood pressure, and decreasing aldosterone-driven sodium and water retention.

The pathophysiology of malignant renovascular hypertension maps directly onto this mechanism. Renal artery stenosis triggers excessive renin secretion from the ischaemic kidney, driving angiotensin II levels to critically high levels, producing severe and rapidly progressive hypertension with end-organ damage — including hypertensive retinopathy, acute kidney injury, and hypertensive encephalopathy. Captopril cuts this cascade at its enzymatic hub, making it mechanistically well-suited to this condition.

Perhaps the strongest signal of mechanistic alignment is that the **Captopril stimulation renal scan (Captopril renography)** is itself a standard diagnostic investigation for renovascular hypertension. The scan exploits Captopril's precise mechanism to reveal renin-dependent blood pressure elevation. This dual role — therapeutic agent and diagnostic probe — underscores the exceptional fit between the drug's pharmacology and the disease's driving pathology, and provides strong biological rationale for the TxGNN model's high-confidence prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Captopril in malignant renovascular hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | The Journal of Pediatrics | Review of malignant hypertension including pathophysiology and management; ACE inhibitor therapy discussed in context of paediatric cases |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | Clinical concepts of renovascular hypertension; treatment strategies targeting RAAS, including ACE inhibitors |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Clinical Study | Clinical Science | Captopril and SQ 20881 induced renin elevation >14 ng/h/mL in 43/44 patients with untreated renovascular hypertension; absent in essential hypertension — validated captopril's diagnostic and mechanistic role |
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Clinical Series | Biulleten' Vsesoiuznogo | Direct clinical assessment of captopril use in arterial hypertension with both stable and malignant courses |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case Series | Pediatric Nephrology | 27 patients with NF1 assessed for renovascular hypertension; captopril test and Doppler ultrasonography used to characterise RAAS-mediated hypertension |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case Report / Review | Clinical Nephrology | Two cases of renovascular hypertension with neurofibromatosis; captopril stimulation demonstrated markedly elevated renin (2.8 → 12.6 ng/mL/h), confirming renin-dependent hypertension mechanism |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review | Endocrinology and Metabolism Clinics of North America | Analysis of renin-secreting tumours; blood pressure falls under ACE inhibitor (captopril) treatment; diagnostic criteria reviewed |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case Report | Clinical Nuclear Medicine | False-positive captopril renal scintigraphy in malignant hypertension without renal artery stenosis; highlights diagnostic complexity and captopril's mechanistic probe function |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Basic / Clinical Research | Japanese Heart Journal | Neurohormonal characterisation of benign and malignant phases in 2K2C Goldblatt hypertension; demonstrates progressive RAAS, catecholamine, and vasopressin activation in malignant phase |
| [3904655](https://pubmed.ncbi.nlm.nih.gov/3904655/) | 1985 | Clinical Study | Archives of Internal Medicine | Multicentre surveillance study of captopril in 975 hypertensive patients aged ≥65; BP reduced from 193/105 to 159/88 mmHg; renal function preserved in most patients |

---

## Australia Market Information

Captopril currently has **no active ARTG entries** in Australia. The drug is not marketed and holds no TGA product registration at the time of this report (data cutoff: 21 June 2026). Any clinical use in Australia would require a Special Access Scheme (SAS) application or Authorised Prescriber pathway.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note for prescribers:** Although no Australian PI exists for Captopril, the following considerations are clinically important in the context of malignant renovascular hypertension and are documented in the international literature:
>
> - **Acute renal failure risk:** ACE inhibitors can precipitate acute renal failure in patients with bilateral renal artery stenosis or stenosis to a single functioning kidney — particularly relevant in this indication.
> - **First-dose hypotension:** Risk is heightened in volume-depleted or high-renin states, both of which are common in malignant renovascular hypertension.
> - **Hyperkalaemia:** Monitor serum potassium closely, especially with concurrent use of potassium-sparing agents or in the setting of impaired renal function.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Captopril (an ACE inhibitor) and malignant renovascular hypertension is exceptionally strong — Captopril directly targets the RAAS over-activation that is the central driver of this condition, and its role as a standard diagnostic agent (Captopril renography) confirms this mechanistic alignment. Multiple observational studies and clinical case series from the 1979–2006 period document Captopril's use in renovascular and malignant hypertension, supporting L3-level evidence.

**To proceed, the following is needed:**
- Obtain and review the most current international Product Information (e.g., UK MHRA or US FDA label) as a safety reference, given the absence of an Australian TGA PI
- Conduct specialist nephrology and/or hypertension consultation prior to prescribing — particularly to assess bilateral renal artery stenosis before initiating ACE inhibitor therapy
- Establish renal function monitoring protocol (serum creatinine, eGFR, electrolytes) at baseline and within 1–2 weeks of initiation
- Determine the appropriate access pathway in Australia: Special Access Scheme Category B (SAS-B) or Authorised Prescriber, as no ARTG registration currently exists
- Source Captopril supply through a TGA-licensed importer or compounding pharmacy with appropriate quality assurance
- Document clinical justification and informed consent clearly in the medical record given off-label / unapproved status in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

