---
layout: default
title: Capecitabine
parent: Model Prediction Only (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Capecitabine: predicted new indication Top-ranked: gastric adenocarcinoma and proximal polyposis of the stom… (evidence level L5). Approved use: Gastric cancer"
---

# Capecitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Capecitabine: From Gastric Cancer to Gastric Tubular Adenocarcinoma

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine chemotherapy, originally used for gastric cancer and metastatic colon cancer.
The TxGNN model predicts it may be effective for **gastric adenocarcinoma and proximal polyposis of the stomach** (top-ranked), but the best-supported prediction in the data compiled for this report is **gastric tubular adenocarcinoma**, which is backed by **20 publications** (including several Phase 3 RCTs) and no registered trials.
Note that this prediction is largely an on-label use rather than true repurposing, and the top-ranked prediction itself has no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer; metastatic colon cancer (from the knowledge graph; the ARTG entry lists no indication text) |
| Predicted New Indication | Top-ranked: gastric adenocarcinoma and proximal polyposis of the stomach (no evidence). Best-supported: gastric tubular adenocarcinoma, presented below |
| TxGNN Prediction Score | 99.94% (both) |
| Evidence Level | L1 for gastric tubular adenocarcinoma (L5 for the top-ranked prediction) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (gastric tubular adenocarcinoma); Hold (top-ranked prediction) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, capecitabine is an oral prodrug converted to 5-fluorouracil (5-FU), which inhibits thymidylate synthase and disrupts DNA synthesis. Its efficacy in gastric cancer is established, and mechanistically it is applicable to histological subtypes of gastric adenocarcinoma.

Tubular adenocarcinoma is a common histological subtype of gastric adenocarcinoma, so it is essentially the same disease as the original gastric cancer indication. Phase 3 literature includes CLASSIC (adjuvant capecitabine plus oxaliplatin after D2 gastrectomy) and several first-line trials in which a capecitabine/oxaliplatin backbone was combined with immunotherapy or targeted agents. The supplied titles are not subtype-specific, so subtype applicability should be confirmed.

**Other predictions in the list**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Gastric adenocarcinoma and proximal polyposis of the stomach | 99.94% | L5 | Prediction only; rare hereditary syndrome with no direct evidence |
| Microinvasive gastric cancer | 99.94% | L5 | Usually managed by endoscopic or surgical resection; weak rationale for systemic therapy |
| Signet ring cell gastric adenocarcinoma | 99.94% | L3 | One not-yet-recruiting Phase 2 trial; mostly case reports; histology often less chemosensitive |
| Gastric cardia adenocarcinoma | 99.91% | L2 | Two completed Phase 2 trials of oxaliplatin plus capecitabine in oesophagogastric cancer |
| Gastric body carcinoma | 99.90% | L1 | A completed Phase 3 trial, but not site-specific and capecitabine's role needs verification |
| Epstein-Barr virus-associated gastric carcinoma | 99.90% | L3 | A small neoadjuvant toripalimab plus CapeOX study; capecitabine's contribution is not separable |
| Gastric pylorus carcinoma | 99.91% | L4 | A single case report |
| Carcinoma of stomach, salivary gland type | 99.91% | L3 | Only general Phase 1/2 solid-tumour trials |
| Malignant gastric granular cell tumour | 99.89% | L5 | Non-epithelial tumour; rationale weak and unsupported |

---

## Clinical Trial Evidence

No clinical trials are registered for gastric tubular adenocarcinoma. The most relevant trials from the other gastric predictions are shown below.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | Completed | 48 | Oxaliplatin plus capecitabine in metastatic oesophageal, GEJ and gastric cardia adenocarcinoma |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | Completed | 73 | Extended neoadjuvant therapy in locally advanced oesophageal, GEJ and gastric cardia adenocarcinoma; capecitabine is likely part of the regimen (to be verified) |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | NA | Completed | 27 | Dose-finding of docetaxel, oxaliplatin and capecitabine with trastuzumab in HER2-positive advanced oesophagogastric cancer |
| [NCT02494583](https://clinicaltrials.gov/study/NCT02494583) | Phase 3 | Completed | 763 | Pembrolizumab with or without cisplatin plus 5-FU or capecitabine in advanced gastric/GEJ adenocarcinoma (KEYNOTE-859 type design); not site-specific |
| [NCT07091227](https://clinicaltrials.gov/study/NCT07091227) | Phase 2 | Not yet recruiting | 66 | AK112 plus chemotherapy as neoadjuvant treatment for signet ring cell-containing gastric/GEJ cancer; capecitabine's role is unconfirmed |
| [NCT00021047](https://clinicaltrials.gov/study/NCT00021047) | Phase 1/2 | Completed | Not reported | Epirubicin, carboplatin and capecitabine in adult patients with solid tumours |
| [NCT00010023](https://clinicaltrials.gov/study/NCT00010023) | Phase 1 | Completed | Not reported | Capecitabine plus cisplatin in advanced digestive system cancer (dose and safety) |

No ANZCTR trial identifiers were available in the data compiled for this report.

---

## Literature Evidence

Gastric tubular adenocarcinoma (up to 10 shown, prioritising RCTs involving capecitabine):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | RCT (Phase 3) | Lancet | CLASSIC: adjuvant capecitabine plus oxaliplatin after D2 gastrectomy versus surgery alone in stage II-IIIB gastric cancer |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | RCT (Phase 3) | Lancet Oncol | RESOLVE: perioperative S-1 plus oxaliplatin versus postoperative capecitabine plus oxaliplatin |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | RCT (Phase 3) | Lancet Oncol | RESOLVE final report with updated survival data |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | RCT (Phase 3) | Nat Med | GLOW: zolbetuximab plus CAPOX in CLDN18.2-positive gastric/GEJ adenocarcinoma |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | RCT (Phase 3) | Lancet Oncol | KEYNOTE-859: pembrolizumab plus chemotherapy in HER2-negative advanced gastric cancer |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | RCT (Phase 3) | Lancet | CheckMate 649: first-line nivolumab plus chemotherapy |
| [38906161](https://pubmed.ncbi.nlm.nih.gov/38906161/) | 2024 | RCT (Phase 3) | Lancet Gastroenterol Hepatol | ATTRACTION-5: adjuvant nivolumab plus chemotherapy in stage III gastric/GEJ cancer |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | RCT (Phase 2/3) | Lancet | FLOT4: perioperative FLOT versus ECF/ECX; not capecitabine-based, though capecitabine was in the comparator arm |
| [20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/) | 2010 | RCT (Phase 3) | Lancet | ToGA: trastuzumab plus chemotherapy in HER2-positive advanced gastric cancer |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | RCT (Phase 3) | JAMA | ORIENT-16: sintilimab plus chemotherapy in unresectable gastric/GEJ cancer |

Most of these trials test capecitabine as part of a chemotherapy backbone. The benefit of capecitabine alone cannot be separated from the added agents, and none of the titles are specific to the tubular subtype.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8362D | Capecitabine Sandoz | Tablet 500 mg (oral) | Not listed in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class; oral prodrug of 5-FU) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions. The knowledge graph flags neutropenia, thrombocytopenia, agranulocytosis and anaemia as contraindicated conditions |
| Emetogenicity Classification | Low to moderate for oral fluoropyrimidines (general class knowledge; confirm in the PI) |
| Monitoring Items | FBC with differential, liver function (bilirubin), renal function; consider DPD deficiency status |
| Handling Protection | Follow local cytotoxic drug handling procedures |

---

## Safety Considerations

TGA-approved Product Information warnings and contraindications were not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for authoritative safety information.

**Conditions flagged as contraindicated in the knowledge graph** (not label text, so verify against the PI):
- Dihydropyrimidine dehydrogenase deficiency
- Haematological: neutropenia, agranulocytosis, thrombocytopenia, anaemia (including macrocytic)
- Hepatic and biliary: liver disease, gallbladder disease, hyperbilirubinaemia (including hereditary), Gilbert syndrome
- Impaired renal function
- Cardiac: coronary artery disease, sudden cardiac arrest, heart conduction disease
- Stomatitis, necrotising enterocolitis, infectious disease

**Drug interactions** (100 recorded; examples from the interaction screen):
- Moderate: metronidazole, tinidazole
- Minor: aluminium hydroxide, magaldrate, magnesium carbonate/hydroxide/oxide, levofloxacin
- Severity unknown: pantoprazole, omeprazole, lansoprazole, glimepiride, metformin, doxycycline, morphine, atropine, prednisone, simvastatin, hydrocortisone, dolasetron

A full interaction review against the PI is needed. Warfarin interactions, well known for capecitabine, were not captured in the supplied list and should be checked.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (gastric tubular adenocarcinoma and gastric cardia adenocarcinoma). **Hold** for the top-ranked prediction (gastric adenocarcinoma with proximal polyposis of the stomach) and for microinvasive, pyloric, salivary gland type and granular cell predictions.

**Rationale:**
- Tubular adenocarcinoma is a subtype of the already established gastric cancer indication. Several Phase 3 RCTs support capecitabine-based regimens in gastric cancer, but the evidence is not subtype-specific and this is largely on-label use rather than true repurposing.
- The highest-scored predictions are rare or poorly matched conditions with no trials or literature, so the score alone does not justify action.

**To proceed, the following is needed:**
- Mechanism of action data and the TGA Product Information (warnings, contraindications, approved indications) for Capecitabine Sandoz
- Confirmation of subtype-specific applicability and the regimen-specific evidence (capecitabine's contribution within combination trials)
- Verification of capecitabine's role in NCT02494583 and NCT00938470
- DPD deficiency testing and a monitoring plan for haematological, hepatic and renal toxicity
- A full interaction review, including warfarin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

