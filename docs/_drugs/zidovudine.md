---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 731
evidence_level: L5
indication_count: 10
---

# Zidovudine
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

Using no additional skill — this is a direct content-generation task governed by the report-writing instructions already provided in the system prompt. Proceeding straight to the report.

Note on methodology before the report: TxGNN's top-ranked predictions for this drug (rank 1–2: feline/simian immunodeficiency models — species mismatch, not human-applicable; rank 3–4: obsolete/unlinked disease terms with zero evidence; rank 5–6: AIDS-related complex and congenital HIV — these are zidovudine's **existing approved indications**, not new repurposing candidates) are not informative for a repurposing evaluation. The most credible genuine repurposing signal in this evidence pack is **rank 9, female breast carcinoma** — a human, non-obsolete, non-already-approved candidate with actual (preclinical) supporting literature and a "Research Question" scoring stage. This report is built around that candidate.

---

# Zidovudine: From HIV/AIDS Antiretroviral Therapy to Female Breast Carcinoma

## One-Sentence Summary

> Zidovudine (AZT) was the first antiretroviral agent approved for HIV infection, acting as a nucleoside reverse transcriptase inhibitor (NRTI). Screening out veterinary, obsolete, and already-approved TxGNN candidates, the most credible novel signal is **Female Breast Carcinoma**, currently supported only by **preclinical laboratory studies** (no registered clinical trials) exploring its antiproliferative and telomerase-inhibiting effects on breast cancer cells.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection (Human Immunodeficiency Virus) / AIDS — antiretroviral therapy |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 96.20% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed (no active ARTG entries in this evidence pack) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a detailed structured mechanism-of-action record is not available for zidovudine in this evidence pack. Based on the literature contained within the evidence itself, zidovudine (AZT, azidothymidine) is a synthetic thymidine (nucleoside) analogue — the first drug in the nucleoside reverse transcriptase inhibitor (NRTI) class. It is phosphorylated intracellularly to its active triphosphate form, which competitively inhibits HIV reverse transcriptase and causes premature viral DNA chain termination, blocking retroviral replication.

Beyond its antiviral action, zidovudine's underlying chemistry — a modified thymidine analogue capable of being incorporated into replicating DNA — gives it a plausible, if distinct, secondary mechanism relevant to rapidly dividing tumour cells. Multiple in vitro and animal studies in this evidence pack (e.g. PMID 9192804, 9533539, 27633795) report that AZT inhibits growth of human breast cancer cell lines and rat/mouse mammary tumours, with proposed mechanisms including **telomerase inhibition**, **incorporation into telomeric DNA causing senescence/apoptosis**, and reduced tumorigenicity and metastatic potential in xenograft models.

This is mechanistically distinct from — but not incompatible with — zidovudine's original antiviral use: both actions stem from its identity as a nucleoside analogue capable of interfering with nucleic acid synthesis. However, all supporting evidence to date is preclinical (cell lines and animal models); no clinical trial has evaluated zidovudine as a breast cancer therapy in humans. This corresponds to Evidence Level L4 and decision stage S1 ("Research Question") — appropriate for further translational research, not clinical deployment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35584347](https://pubmed.ncbi.nlm.nih.gov/35584347/) | 2022 | Cohort | JCO Global Oncology | Assessed pathologic response and chemotherapy dose intensity in breast cancer patients with/without HIV (antiretroviral-treated); relevant clinical context but not a direct zidovudine-as-oncology-agent trial |
| [9192804](https://pubmed.ncbi.nlm.nih.gov/9192804/) | 1997 | Preclinical (in vitro/animal) | Cancer Research | AZT shows potent growth-inhibitory activity on cultured human breast cancer cells and rat mammary tumours |
| [9533539](https://pubmed.ncbi.nlm.nih.gov/9533539/) | 1998 | Preclinical (in vitro) | Clinical Cancer Research | AZT inhibits cell growth and telomerase activity across four breast cancer cell lines |
| [11261835](https://pubmed.ncbi.nlm.nih.gov/11261835/) | 2001 | Preclinical (in vitro) | Breast Cancer Research and Treatment | Chronic AZT exposure induces senescence/apoptosis and reduces tumorigenicity of metastatic mouse mammary tumour cells |
| [27633795](https://pubmed.ncbi.nlm.nih.gov/27633795/) | 2016 | Preclinical (animal model) | Oncology Reports | AZT exerts antitumoral effects via both telomeric and non-telomeric mechanisms in a mammary adenocarcinoma model |
| [10841805](https://pubmed.ncbi.nlm.nih.gov/10841805/) | 2000 | Preclinical (synthesis/in vitro) | Journal of Medicinal Chemistry | AZT phosphoramidate monoester derivatives show anti-breast cancer activity in MCF-7 cells |
| [21945463](https://pubmed.ncbi.nlm.nih.gov/21945463/) | 2011 | Preclinical (in vitro) | Bioorganic & Medicinal Chemistry | Novel AZT chloromethylphosphonate derivatives show cytotoxic activity in MCF-7 breast cancer cells |
| [32199136](https://pubmed.ncbi.nlm.nih.gov/32199136/) | 2020 | Preclinical (in vitro) | European Journal of Medicinal Chemistry | AZT-based cationic derivatives regulate metastasis of breast cancer cells |
| [32738968](https://pubmed.ncbi.nlm.nih.gov/32738968/) | 2020 | Preclinical (in vitro) | Bioorganic & Medicinal Chemistry Letters | Tellurium-containing AZT derivatives inhibit proliferation and induce apoptosis in MDA-MB-231 breast cancer cells |
| [16797627](https://pubmed.ncbi.nlm.nih.gov/16797627/) | 2006 | Preclinical (in vitro, off-target) | Toxicology and Applied Pharmacology | AZT combined with cisplatin increases p14ARF tumour-suppressor expression in an ovarian cancer cell line; supportive of a broader antitumour signalling effect |

---

## Australia Market Information

No ARTG entries are recorded in this evidence pack for zidovudine, and market status is listed as **Not marketed**. Given zidovudine is a long-established, internationally marketed antiretroviral, this likely reflects a gap in the underlying regulatory dataset rather than confirmed absence from the Australian market — **TGA/ARTG should be checked directly** before relying on this status for decision-making.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The breast carcinoma signal is supported only by preclinical in vitro and animal studies (Evidence Level L4, decision stage S1 "Research Question") — no human clinical trials have evaluated zidovudine as a breast cancer therapy. Combined with a blocking data gap on TGA warnings/contraindications and an unresolved market-status discrepancy, the evidence is insufficient to progress beyond a research hold.

**To proceed, the following is needed:**
- Retrieve TGA-approved Product Information (PI) — warnings and contraindications (blocking gap)
- Confirm structured mechanism-of-action documentation via DrugBank
- Early-phase (Phase I/II) clinical or translational studies specifically evaluating zidovudine (or its AZT-phosphonate/tellurium derivatives) in breast cancer patients
- Verify current ARTG registration and market-availability status directly with TGA
- Independently confirm that TxGNN's top-ranked candidates (feline/simian immunodeficiency models, obsolete disease terms, already-approved HIV indications) are correctly excluded from future repurposing pipelines for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

