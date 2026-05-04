---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Enzalutamide
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

# Enzalutamide: From Prostate Cancer to Male Reproductive Organ Cancer

## One-Sentence Summary

Enzalutamide (Xtandi®) is a second-generation androgen receptor (AR) signalling inhibitor with established global efficacy across the prostate cancer disease spectrum, from metastatic hormone-sensitive to castration-resistant disease.
The TxGNN model's highest-evidenced prediction supports its use in **Male Reproductive Organ Cancer** (prostate cancer broadly), with **50 clinical trials** and **20 publications** directly supporting this direction.
Enzalutamide does not appear on the Australian ARTG in the current dataset — this likely represents a data retrieval gap requiring urgent verification, given the drug's well-established global approval status.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not found on Australian ARTG (globally approved for prostate cancer — mCRPC, nmCRPC, mHSPC) |
| Predicted New Indication | Male Reproductive Organ Cancer |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (0 ARTG entries found — potential data gap) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN ranking**: The highest TxGNN-scored prediction (rank 1: *prostate cancer/brain cancer susceptibility*, 99.71%) represents a composite disease node with no supporting clinical evidence (L5, Hold). This report focuses on the most clinically evidenced prediction — **male reproductive organ cancer** (rank 6, 99.51%), which carries an L1 evidence level and a "Proceed with Guardrails" recommendation.

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not available in this Evidence Pack. Based on publicly available pharmacological information, Enzalutamide is a potent second-generation non-steroidal androgen receptor signalling inhibitor that simultaneously disrupts three sequential steps: androgen-induced AR nuclear translocation, AR DNA binding, and coactivator recruitment. Unlike first-generation antiandrogens (e.g., bicalutamide), Enzalutamide functions as a full antagonist even in AR-overexpressing conditions and does not exhibit agonist switching — a critical pharmacological advantage in the castration-resistant setting.

Prostate cancers are highly dependent on AR signalling throughout their disease course. Even after surgical or medical castration, tumours frequently adapt through AR gene amplification, ligand-binding domain mutations, or constitutively active AR splice variants — particularly AR-V7 — which bypass the need for androgen ligand and confer resistance to earlier antiandrogens. Enzalutamide's multi-step blockade directly targets these adaptation mechanisms, explaining its consistent efficacy across the full prostate cancer spectrum: from metastatic hormone-sensitive prostate cancer (mHSPC) through to non-metastatic CRPC (nmCRPC) and metastatic CRPC (mCRPC).

The TxGNN knowledge graph prediction of 99.51% for male reproductive organ cancer directly reflects Enzalutamide's established clinical profile. Multiple Phase 3 landmark trials — AFFIRM (mCRPC, post-docetaxel), PROSPER (nmCRPC), ARCHES (mHSPC), and ENZAMET (mHSPC) — have each demonstrated clinically significant improvements in key survival endpoints, cementing Enzalutamide as a standard-of-care agent in this disease class. The absence from the current Australian ARTG dataset is inconsistent with this evidence base and warrants immediate verification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00974311](https://clinicaltrials.gov/study/NCT00974311) | Phase 3 | Completed | 1,199 | **AFFIRM**: Enzalutamide vs placebo in mCRPC post-docetaxel; significant overall survival benefit, establishing Enzalutamide as a standard of care |
| [NCT02003924](https://clinicaltrials.gov/study/NCT02003924) | Phase 3 | Completed | 1,401 | **PROSPER**: Enzalutamide vs placebo in nmCRPC with rapidly rising PSA; metastasis-free survival 36.6 vs 14.7 months |
| [NCT00510718](https://clinicaltrials.gov/study/NCT00510718) | Phase 1 | Completed | 140 | First-in-human dose-escalation study of MDV3100 (Enzalutamide) in CRPC; established safety, pharmacokinetics, and 160 mg/day as the recommended dose |
| [NCT03809000](https://clinicaltrials.gov/study/NCT03809000) | Phase 2 | Active, not recruiting | 188 | **STEEL**: Enzalutamide-enhanced ADT vs standard ADT with salvage radiotherapy in post-prostatectomy PSA recurrence with aggressive disease features; assessing progression-free survival |
| [NCT02228265](https://clinicaltrials.gov/study/NCT02228265) | N/A | Completed | 41 | Mechanistic characterisation of Enzalutamide resistance in mCRPC; identified AR-V7 and AR ligand-binding domain mutations as clinically actionable resistance biomarkers |
| [NCT01927627](https://clinicaltrials.gov/study/NCT01927627) | Phase 2 | Completed | 42 | Enzalutamide monotherapy in high-risk non-metastatic prostate cancer post-radical prostatectomy; assessed time to PSA progression |
| [NCT05873192](https://clinicaltrials.gov/study/NCT05873192) | Phase 2 | Recruiting | 30 | Talazoparib (PARP inhibitor) + Enzalutamide + ADT as presurgical therapy in de novo lymph node–metastatic prostate cancer |
| [NCT07028853](https://clinicaltrials.gov/study/NCT07028853) | Phase 3 | Recruiting | 1,000 | **MEVPRO-3**: Mevrometostat (EZH2 inhibitor) + Enzalutamide vs Enzalutamide alone in ARPI-naïve metastatic castration-sensitive prostate cancer |
| [NCT06136650](https://clinicaltrials.gov/study/NCT06136650) | Phase 3 | Recruiting | 1,314 | **OMAHA-004**: Opevesostat + hormone replacement therapy vs abiraterone or Enzalutamide in mCRPC progressed on one prior next-generation hormonal agent |
| [NCT04104893](https://clinicaltrials.gov/study/NCT04104893) | Phase 2 | Active, not recruiting | 40 | Pembrolizumab in veterans with mCRPC characterised by MMR deficiency or biallelic CDK12 inactivation; evaluates checkpoint immunotherapy in an enzalutamide-context population |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31329516](https://pubmed.ncbi.nlm.nih.gov/31329516/) | 2019 | Phase 3 RCT | Journal of Clinical Oncology | **ARCHES**: Enzalutamide + ADT significantly reduced risk of radiographic progression or death vs placebo + ADT in mHSPC |
| [29949494](https://pubmed.ncbi.nlm.nih.gov/29949494/) | 2018 | Phase 3 RCT | New England Journal of Medicine | **PROSPER**: Enzalutamide in nmCRPC with rapidly rising PSA; significantly prolonged metastasis-free survival — pivotal approval publication |
| [40439959](https://pubmed.ncbi.nlm.nih.gov/40439959/) | 2025 | Comparative Effectiveness | Advances in Therapy | Real-world comparison of apalutamide vs enzalutamide in mCSPC; overall survival at 24 months in ARPI-naïve patients |
| [39275993](https://pubmed.ncbi.nlm.nih.gov/39275993/) | 2024 | Review | Expert Review of Anticancer Therapy | Current uses of enzalutamide across biochemically recurrent, mHSPC, nmCRPC, and mCRPC settings; resistance mechanisms including AR-V7 and splice variants |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Review | Trends in Cancer | Treatment landscape of advanced prostate cancer; enzalutamide as a key approved agent across multiple disease stages |
| [28655021](https://pubmed.ncbi.nlm.nih.gov/28655021/) | 2017 | Review | JAMA | Clinical overview of prostate cancer diagnosis and treatment; contextualises the role of AR pathway inhibitors |
| [36842160](https://pubmed.ncbi.nlm.nih.gov/36842160/) | 2023 | Review | The Prostate | 3βHSD1 steroidogenic enzyme in prostate cancer precision medicine; implications for androgen biosynthesis and enzalutamide sensitivity |
| [37844613](https://pubmed.ncbi.nlm.nih.gov/37844613/) | 2023 | Preclinical | Nature | Myeloid chemotaxis inhibition reverses prostate cancer therapy resistance; mechanism with direct relevance to overcoming enzalutamide resistance in a subset of patients |
| [34752846](https://pubmed.ncbi.nlm.nih.gov/34752846/) | 2022 | Basic Science | Cancer Letters | Enzalutamide-induced PTH1R-mediated TGFBR2 degradation in osteoblasts drives bone microenvironment–dependent resistance in prostate cancer bone metastases |
| [29460922](https://pubmed.ncbi.nlm.nih.gov/29460922/) | 2018 | Review | Nature Reviews Urology | Neuroendocrine phenotype and cellular plasticity as AR-independent resistance mechanisms to enzalutamide and abiraterone; treatment implications for CRPC |

---

## Australia Market Information

No ARTG entries were identified for Enzalutamide in the current data query. This is almost certainly a **data retrieval gap**: Enzalutamide (Xtandi®) is known to hold TGA approval and is listed on the Pharmaceutical Benefits Scheme (PBS) for eligible prostate cancer patients in Australia. Australian clinicians and pharmacists should verify the current ARTG status and PBS reimbursement criteria directly via official sources before any prescribing or formulary decisions.

> **Action required**: Confirm ARTG registration via the [TGA ARTG Public Search](https://www.tga.gov.au/resources/artg) and PBS listing via [Services Australia](https://www.pbs.gov.au) before clinical use.

---

## Cytotoxicity

Enzalutamide is used to treat prostate cancer (a malignancy) and qualifies for inclusion of this section. It is an androgen receptor signalling inhibitor — a targeted oncology agent, not a conventional cytotoxic chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Androgen Receptor Signalling Inhibitor (ARSI); non-cytotoxic mechanism of action |
| Myelosuppression Risk | Low (ARSIs do not cause clinically significant myelosuppression; routine haematological monitoring is not required beyond standard care) |
| Emetogenicity Classification | Minimal (oral targeted agent; classified as minimal emetogenic risk per MASCC/ESMO guidelines — routine antiemetic prophylaxis not indicated) |
| Monitoring Items | Liver function tests (LFTs), blood pressure, baseline seizure risk assessment, falls and fracture risk in elderly patients, cognitive function screening |
| Handling Protection | Classified as a hazardous drug due to reproductive toxicity (teratogenicity); standard oral hazardous drug safe-handling procedures apply — use gloves when handling tablets, do not crush or split |

---

## Safety Considerations

**Key Warnings:**
- **Seizure risk**: Enzalutamide lowers the seizure threshold — use with caution or avoid in patients with a history of seizure disorder, brain injury, brain metastases, stroke, or other predisposing neurological conditions
- **Posterior Reversible Encephalopathy Syndrome (PRES)**: Rare but serious neurological adverse event reported in post-marketing surveillance — discontinue immediately if clinically suspected
- **Falls and fatigue**: Fatigue, dizziness, and cognitive impairment are common adverse effects; significantly elevated falls and fracture risk in elderly patients — proactive falls prevention strategies are recommended
- **Cardiovascular events**: Ischaemic heart disease reported in clinical trials — baseline cardiac assessment recommended, particularly in patients with pre-existing cardiovascular risk factors

**Drug Interactions:**
- Enzalutamide is a **strong inducer of CYP3A4, CYP2C9, and CYP2C19**, and a P-glycoprotein (P-gp) inducer
- May significantly reduce plasma concentrations of co-administered medications including: **warfarin** (clinically critical — INR monitoring essential), statins (e.g., rosuvastatin is a P-gp/BCRP substrate), certain antiepileptics, immunosuppressants, hormonal contraceptives, and many other commonly prescribed agents
- A comprehensive drug interaction review against the patient's full medication list is mandatory before initiating or dispensing Enzalutamide

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Enzalutamide has an exceptionally strong evidence base in male reproductive organ cancer (prostate cancer), anchored by multiple Phase 3 RCTs across disease stages — AFFIRM (mCRPC), PROSPER (nmCRPC), ARCHES (mHSPC), and ENZAMET (mHSPC) — all demonstrating statistically and clinically significant improvements in primary survival endpoints. The TxGNN prediction score of 99.51% is fully consistent with this established clinical profile. The primary Australian-specific concern is the current absence from the ARTG dataset, which almost certainly reflects a data retrieval gap rather than an actual registration gap and must be urgently clarified.

**To proceed, the following is needed:**
- **Verify ARTG registration**: Confirm Xtandi® ARTG entry via the TGA public database — a data retrieval error is the most likely explanation for the current gap
- **Obtain Australian PI**: Review the TGA-approved Australian Product Information for approved indications, contraindications, dosing guidance, and local safety requirements
- **PBS status**: Confirm current PBS listing and Special Authority criteria applicable to each eligible prostate cancer subtype (mCRPC, nmCRPC, mHSPC) and patient-specific clinical parameters
- **Drug interaction assessment**: Conduct a full CYP3A4/CYP2C9/P-gp interaction review against the patient's complete medication list before initiation
- **Seizure risk screening**: Implement a baseline neurological risk assessment protocol and ensure patients and carers are counselled on seizure recognition
- **Falls prevention strategy**: Establish a falls and fracture risk protocol, particularly for elderly or frail patients, in collaboration with the multidisciplinary team
- **Specialist referral**: Urological oncology or medical oncology review is strongly recommended for treatment initiation, ongoing monitoring, and resistance management (including AR-V7 testing where appropriate)

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing predictions require clinical validation before therapeutic application. Refer to TGA-approved Product Information and current clinical guidelines for prescribing decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

