---
layout: default
title: Bicalutamide
parent: Model Prediction Only (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bicalutamide: predicted new indication Hypertrichosis (evidence level L5). Approved use: Not stated in the data compiled (bicalutamide is generally used as an…"
monitor_inn: "Bicalutamide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "leprosy", "multiple endocrine neoplasia", "pulmonary hypertension", "female breast carcinoma", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Bicalutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Bicalutamide: From Prostate Cancer to Hypertrichosis (Top Prediction), with Female Breast Carcinoma as the Best-Evidenced Candidate

## One-Sentence Summary

Bicalutamide is a nonsteroidal androgen receptor antagonist. The data compiled for this report do not list an approved indication text for the Australian product, although the drug is widely known as an anti-androgen used in prostate cancer.
The TxGNN model's top-ranked prediction is **hypertrichosis**, but it is supported by only **1 comment/letter**. The best-evidenced prediction is **female breast carcinoma**, with **1 Phase 2 trial** and **20 publications**, mostly preclinical or review articles.

> **Note:** The approved indication text was not available in the data compiled for this report. The "original indication" below is drawn from the drug's known pharmacology and should be confirmed against the TGA Product Information.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled (bicalutamide is generally used as an anti-androgen in prostate cancer; confirm against the PI) |
| Predicted New Indication | Hypertrichosis (rank 1); female breast carcinoma has the most evidence (rank 9) |
| TxGNN Prediction Score | 99.69% (hypertrichosis); 99.11% (female breast carcinoma) |
| Evidence Level | L4 (hypertrichosis); L2 (female breast carcinoma, as assigned in the data compiled) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (hypertrichosis); Proceed with Guardrails as a research question (female breast carcinoma) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data were not available in the data compiled. Bicalutamide is, however, a nonsteroidal androgen receptor (AR) antagonist. By blocking AR signalling, it can reduce androgen-driven cell growth.

**Hypertrichosis:** Androgen signalling drives hair growth in androgen-sensitive follicles, so AR blockade could plausibly reduce androgen-dependent hair growth. The only supporting record is a 2022 comment on a retrospective review of bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss. This is indirect, secondary evidence, and the source study was not among the records provided.

**Female breast carcinoma:** AR is expressed in a substantial subset of triple-negative breast cancers (TNBC), including the luminal androgen receptor (LAR) subtype and apocrine carcinoma. In these tumours AR may act as a growth driver. Preclinical work shows bicalutamide effects on proliferation and invasion in TNBC cell lines, combination effects with curcumin, and AR/ERK co-targeting that induces ferroptosis. Reviews support AR as a therapeutic target in TNBC. Clinical evidence is still early, however. A Phase 2 study of bicalutamide plus an aromatase inhibitor in ER-positive/AR-positive advanced breast cancer did not show synergistic activity (clinical benefit rate 16.7%, objective response rate 0% at 6 months) and was terminated.

**Other predictions (ranks 2–8 and 10):** These have no plausible mechanistic link to AR antagonism and no meaningful evidence. They are model predictions only (see the table below).

| Rank | Predicted Indication | Score | Evidence Level |
|---|---|---|---|
| 2 | Malformation syndrome with odontal/periodontal component | 99.59% | L5 |
| 3 | Ambras type hypertrichosis universalis congenita | 99.57% | L5 |
| 4 | Syndrome with Dandy-Walker malformation as major feature | 99.57% | L5 |
| 5 | Isolated genetic hair shaft abnormality | 99.53% | L5 |
| 6 | Leprosy | 99.41% | L5 |
| 7 | Multiple endocrine neoplasia | 99.22% | L5 |
| 8 | Pulmonary hypertension | 99.18% | L5 |
| 10 | Nephrogenic syndrome of inappropriate antidiuresis | 99.03% | L5 |

---

## Clinical Trial Evidence

**Female breast carcinoma**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) | Phase 2 | Active, not recruiting | 30 | Nivolumab + bicalutamide + ipilimumab in metastatic HER2-negative breast cancer. Tests AR blockade combined with immune checkpoint therapy, omitting or delaying chemotherapy. No results provided; the combination design confounds bicalutamide's individual effect. |

**Hypertrichosis:** Currently no related clinical trials registered.

**Multiple endocrine neoplasia (low relevance):** Two trials were linked, but neither is specific to this condition and neither provides usable evidence.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME precision-oncology platform trial; no interpretable efficacy or safety signal. |
| [NCT02615223](https://clinicaltrials.gov/study/NCT02615223) | N/A | Unknown | 120 | Endocrine therapy with or without cryoablation in stage IV prostate cancer (quality of life and tumour control). Not specific to this indication. |

---

## Literature Evidence

**Female breast carcinoma** (10 most relevant of 20 records; no RCTs identified)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31434793](https://pubmed.ncbi.nlm.nih.gov/31434793/) | 2020 | Phase 2 single-arm study | The Oncologist | Bicalutamide plus aromatase inhibitor in ER+/AR+ advanced breast cancer showed no synergy; clinical benefit rate 16.7%, objective response rate 0%; study terminated. |
| [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 | Review | Current Medical Science | Anti-androgen therapy (including bicalutamide) for TNBC; combinations with chemotherapy and immunotherapy being explored. |
| [29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) | 2018 | Review | Cancer Treatment Reviews | AR as a potential target in the LAR subtype of TNBC. |
| [32145961](https://pubmed.ncbi.nlm.nih.gov/32145961/) | 2020 | Review | Bulletin du Cancer | AR-positive TNBC is about 30% of TNBC; biology and therapy. |
| [35027319](https://pubmed.ncbi.nlm.nih.gov/35027319/) | 2022 | Review | Clinical Breast Cancer | Apocrine carcinoma is ER-negative and AR-positive; molecular and clinical update. |
| [24740738](https://pubmed.ncbi.nlm.nih.gov/24740738/) | 2014 | Review | J Mol Endocrinol | Revisits the role of AR in breast cancer. |
| [32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | 2020 | Preclinical | Medicine | Bicalutamide inhibited proliferation and invasion of MDA-MB-231 TNBC cells. |
| [31917699](https://pubmed.ncbi.nlm.nih.gov/31917699/) | 2020 | Preclinical | Anti-Cancer Drugs | Bicalutamide plus curcumin showed a strong effect in AR-positive TNBC models. |
| [40974527](https://pubmed.ncbi.nlm.nih.gov/40974527/) | 2026 | Preclinical | Sci China Life Sci | AR/ERK co-targeting (bicalutamide plus GDC-0994) triggers ferroptosis in TNBC. |
| [39063165](https://pubmed.ncbi.nlm.nih.gov/39063165/) | 2024 | Preclinical | Int J Mol Sci | Bicalutamide enhanced chemotherapy in human and canine inflammatory mammary cancer cell lines. |

**Hypertrichosis**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Comment/Letter | J Am Acad Dermatol | Comment on a retrospective review of bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss. Indirect, secondary evidence. |

**Pulmonary hypertension:** The single record (PMID 27149136, a 2016 paraneoplastic scleroderma case series) does not show a bicalutamide effect and is not meaningful evidence.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 8094B | Cosudex | Tablet 50 mg (oral) | Not stated in the data compiled; refer to the PI |

The data compiled list this entry as a single-ingredient, valid licence. The listed licence number may reflect a source other than an ARTG number, so verify it against the TGA register.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (nonsteroidal anti-androgen), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Liver function and haematological parameters (anaemia appears in the knowledge-graph signals below) |
| Handling Protection | Please refer to the Product Information (PI) |

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled. Please refer to the TGA-approved Product Information (PI) for these.

**Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): liver disease, gallbladder disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, anaemia (including macrocytic anaemia), interstitial lung disease and drug-induced liver injury.

**Drug interactions:** The query returned 100 interactions, and 20 are shown here. Of those, 2 are **Major** and 1 is Minor; the rest are Moderate.
- **Major:** cisapride, dolasetron
- **Moderate (examples):** clarithromycin, levofloxacin, aprepitant, granisetron, budesonide, eliglustat, famotidine, loperamide, and several laxatives (bisacodyl, lactulose, lactitol, magnesium citrate, magnesium hydroxide, castor oil, glycerin, mineral oil)
- **Minor:** metronidazole

---

## Conclusion and Next Steps

**Decision: Hold for hypertrichosis; Proceed with Guardrails (research question) for female breast carcinoma**

**Rationale:**
- Hypertrichosis has the highest TxGNN score, but its only support is a single comment letter, so it remains a prediction with indirect evidence.
- Female breast carcinoma has a plausible AR-based mechanism, one active Phase 2 combination trial and substantial preclinical literature. However, the one clinical study of bicalutamide plus an aromatase inhibitor was negative, and the Phase 2 combination trial cannot isolate bicalutamide's effect. This supports further research, not clinical adoption. The remaining predictions have no actionable evidence.

**To proceed, the following is needed:**
- The approved indication text and the label warnings and contraindications from the TGA PI (the data compiled flagged the missing safety data as a blocking gap)
- Detailed mechanism of action data
- Results from NCT03650894, and ideally randomised data on bicalutamide alone in AR-positive TNBC
- Identification and review of the underlying retrospective study of bicalutamide for minoxidil-induced hypertrichosis
- A biomarker strategy (AR/LAR status) for patient selection in breast cancer
- A safety monitoring plan covering liver function and the Major and Moderate interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

