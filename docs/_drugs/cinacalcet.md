---
layout: default
title: Cinacalcet
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
---

# Cinacalcet
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

# Cinacalcet: From Hyperparathyroidism to Multiple Endocrine Neoplasia Type 1 (MEN1)-Associated Hyperparathyroidism

*(TxGNN also flagged 9 other candidate indications for this drug — see "Ranked Overview" below. Most have no corroborating evidence and are not recommended for further action.)*

---

## One-Sentence Summary

Cinacalcet (DrugBank DB01012) is a calcimimetic that acts on the calcium-sensing receptor (CaSR) to suppress parathyroid hormone (PTH) secretion; it is internationally established for secondary hyperparathyroidism and hypercalcaemia related to parathyroid disease, although this evidence pack found **no Australian regulatory (ARTG) records** confirming that indication locally. Of ten TxGNN-predicted new indications, the only one with meaningful clinical support is **Multiple Endocrine Neoplasia Type 1 (MEN1)-associated hyperparathyroidism**, backed by **3 clinical trials** (including one completed Phase 3 RCT) and **19 publications**. The remaining nine predictions — including the highest TxGNN-scoring one (nephrogenic syndrome of inappropriate antidiuresis) — currently have **no supporting trials or literature** and should be treated as unverified model signals only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in this evidence pack (0 regulatory license records returned). Cinacalcet is internationally known for secondary hyperparathyroidism in dialysis-dependent CKD and hypercalcaemia of parathyroid carcinoma, but this is background pharmacological knowledge, not data sourced from this pack. |
| Highest-Scoring TxGNN Prediction | Nephrogenic syndrome of inappropriate antidiuresis (98.48%) — **no supporting trials or literature** |
| Best-Evidenced Predicted Indication | Multiple Endocrine Neoplasia Type 1 (MEN1)-associated hyperparathyroidism (93.73%) |
| Evidence Level (best candidate) | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails (MEN1 candidate only) / Hold (all other 9 candidates) |

### Ranked Overview of All 10 TxGNN-Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Clinical Trials | Literature | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------|-----------------|-----------------|
| 1 | Nephrogenic syndrome of inappropriate antidiuresis | 98.48% | 0 | 0 | L5 | Hold |
| 2 | Common cold | 95.39% | 0 | 0 | L5 | Hold |
| 3 | Female breast carcinoma | 94.23% | 0 | 5 | L4 | Hold |
| 4 | Multiple endocrine neoplasia (MEN1/2A) | 93.73% | 3 | 19 | L2 | Proceed with Guardrails |
| 5 | Headache disorder | 93.08% | 0 | 0 | L5 | Hold |
| 6 | Trigeminal autonomic cephalalgia | 92.16% | 0 | 0 | L5 | Hold |
| 7 | Hypertrichosis | 91.66% | 0 | 0 | L5 | Hold |
| 8 | Subarachnoid haemorrhage | 91.39% | 0 | 0 | L5 | Hold |
| 9 | Pulmonary hypertension | 91.21% | 0 | 4 | L4 | Hold |
| 10 | Familial combined hyperlipidaemia (obsolete term) | 90.80% | 0 | 0 | L5 | Hold |

**Note:** TxGNN score reflects embedding similarity, not evidence strength. Score and evidence level do not correlate in this candidate — the top-ranked prediction has the weakest evidence, while the fourth-ranked prediction has the strongest.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for cinacalcet was not available in this evidence pack (data gap). Based on known pharmacology, cinacalcet is a positive allosteric modulator of the calcium-sensing receptor (CaSR) on parathyroid chief cells, increasing CaSR sensitivity to extracellular calcium and thereby suppressing PTH secretion and lowering serum calcium.

**MEN1-associated hyperparathyroidism (best-evidenced candidate):** Primary hyperparathyroidism is the most common and earliest manifestation of MEN1, arising from multi-gland parathyroid hyperplasia rather than a single adenoma. The underlying driver of hypercalcaemia — excess PTH from dysregulated parathyroid tissue — is pharmacologically identical to sporadic primary hyperparathyroidism, the setting in which cinacalcet's PTH-suppressing effect is already well characterised. Because MEN1 patients often have multifocal or recurrent disease and higher surgical failure/recurrence rates, cinacalcet is used in practice as a medical option for patients unsuitable for or with recurrence after parathyroidectomy. This is a mechanistically direct, low-novelty repurposing case rather than a speculative one.

**Female breast carcinoma and pulmonary hypertension (exploratory candidates):** CaSR is expressed in some breast cancer tissue and in vascular smooth muscle/endothelium, offering a plausible biological rationale for tumour microenvironment calcium signalling or vascular tone modulation. However, the available literature for both indications consists of case reports, database/bioinformatics analyses, or CKD-related vascular calcification studies — none evaluate cinacalcet as a treatment for these conditions directly. These should be regarded as hypothesis-generating only.

**The remaining seven candidates** (NSIAD, common cold, headache, trigeminal autonomic cephalalgia, hypertrichosis, subarachnoid haemorrhage, obsolete familial combined hyperlipidaemia) have no supporting trials or literature at all, and in several cases (e.g. subarachnoid haemorrhage, where standard therapy nimodipine works by calcium **channel blockade** rather than CaSR activation) the proposed mechanistic direction may even be biologically contradictory. These are best interpreted as knowledge-graph embedding noise rather than credible repurposing leads.

---

## Clinical Trial Evidence

### MEN1-Associated Hyperparathyroidism

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00325104](https://clinicaltrials.gov/study/NCT00325104) | Phase 3 | Completed | 25 | Evaluated benefits/side effects of cinacalcet specifically in primary hyperparathyroidism associated with MEN1 or MEN2A — the most directly relevant trial identified, though a small sample. |
| [NCT03123406](https://clinicaltrials.gov/study/NCT03123406) | Phase 4 | Completed | 750 | Large multicentre study of cinacalcet for calcium/phosphorus/iPTH control in Chinese CKD haemodialysis patients with secondary hyperparathyroidism (supportive, not MEN1-specific). |
| [NCT04637360](https://clinicaltrials.gov/study/NCT04637360) | N/A (observational) | Completed | 40 | Bone turnover markers and bone density changes in dialysis patients with hyperparathyroidism on cinacalcet (indirect, non-randomised). |

No ANZCTR-registered trials were identified for this candidate.

### Other Predicted Indications

Currently no related clinical trials registered for nephrogenic syndrome of inappropriate antidiuresis, common cold, female breast carcinoma, headache disorder, trigeminal autonomic cephalalgia, hypertrichosis, subarachnoid haemorrhage, pulmonary hypertension, or familial combined hyperlipidaemia.

---

## Literature Evidence

### MEN1-Associated Hyperparathyroidism (top entries of 19 identified)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35407574](https://pubmed.ncbi.nlm.nih.gov/35407574/) | 2022 | Cohort | J Clin Med | Long-term follow-up of hyperparathyroidism management in MEN1 at a single centre. |
| [26224587](https://pubmed.ncbi.nlm.nih.gov/26224587/) | 2016 | Cohort/case series | Endocrine | Cinacalcet therapy specifically in MEN1-associated primary hyperparathyroidism. |
| [24285106](https://pubmed.ncbi.nlm.nih.gov/24285106/) | 2013 | Cohort | Minerva Endocrinol | Impact of cinacalcet in clinical management of MEN1-related primary hyperparathyroidism. |
| [22577108](https://pubmed.ncbi.nlm.nih.gov/22577108/) | 2012 | Cohort | Eur J Endocrinol | Response to cinacalcet in MEN1-related hyperparathyroidism, including CaSR gene variant effects. |
| [36090548](https://pubmed.ncbi.nlm.nih.gov/36090548/) | 2022 | Multicentre case series | Front Pediatr | French multicentre experience of off-label cinacalcet in paediatric primary hyperparathyroidism. |
| [22104762](https://pubmed.ncbi.nlm.nih.gov/22104762/) | 2012 | Review | J Endocrinol Invest | Review of cinacalcet use in primary hyperparathyroidism, including MEN1 subgroup. |
| [30736110](https://pubmed.ncbi.nlm.nih.gov/30736110/) | 2012 | Review | Expert Rev Endocrinol Metab | Review of cinacalcet's role where parathyroidectomy is not curative or feasible. |
| [20585352](https://pubmed.ncbi.nlm.nih.gov/20585352/) | 2010 | Prospective audit | Int J Endocrinol | Prospective audit of cinacalcet in 8 patients with MEN1-associated hyperparathyroidism. |
| [37893182](https://pubmed.ncbi.nlm.nih.gov/37893182/) | 2023 | Review | Biomedicines | Narrative review of paediatric parathyroid neuroendocrine neoplasia/primary hyperparathyroidism. |
| [21971564](https://pubmed.ncbi.nlm.nih.gov/21971564/) | 2012 | Study | J Endocrinol Invest | Cinacalcet efficacy in moderately severe primary hyperparathyroidism per EMA labelling. |

### Female Breast Carcinoma

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38780484](https://pubmed.ncbi.nlm.nih.gov/38780484/) | 2024 | Review/bioinformatics | Technol Cancer Res Treat | CaSR proposed as a biomarker in metastatic breast cancer via database analysis; no cinacalcet treatment data. |
| [27873072](https://pubmed.ncbi.nlm.nih.gov/27873072/) | 2017 | Case series | J Bone Miner Metab | Cinacalcet for hypercalcaemia in parathyroid carcinoma/refractory PHPT (not breast cancer). |
| [18541104](https://pubmed.ncbi.nlm.nih.gov/18541104/) | 2008 | Case report | Acta Dermatovenerol Croat | Breast calciphylaxis mimicking breast cancer on differential diagnosis. |
| [19627726](https://pubmed.ncbi.nlm.nih.gov/19627726/) | 2009 | Review | Endocrinol Nutr | Review of medical alternatives to surgery for primary hyperparathyroidism. |
| [32312250](https://pubmed.ncbi.nlm.nih.gov/32312250/) | 2020 | Case report | BMC Endocr Disord | Cystic parathyroid adenoma with rapid growth induced by cinacalcet. |

### Pulmonary Hypertension

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25498383](https://pubmed.ncbi.nlm.nih.gov/25498383/) | 2014 | Review | Semin Nephrol | CaSR activation effects beyond PTH control in CKD; mechanistic background only. |
| [39677159](https://pubmed.ncbi.nlm.nih.gov/39677159/) | 2024 | Case series | Cureus | Calcific uraemic arteriolopathy in Malaysian dialysis patients; vascular calcification context. |
| [37404402](https://pubmed.ncbi.nlm.nih.gov/37404402/) | 2023 | Case report/review | Cureus | Managing primary hyperparathyroidism with concurrent congestive heart failure. |
| [27230839](https://pubmed.ncbi.nlm.nih.gov/27230839/) | 2016 | Review | Clin Calcium | Pharmacological properties of cinacalcet as a CaSR allosteric modulator. |

### Other Predicted Indications

Currently no related literature available for nephrogenic syndrome of inappropriate antidiuresis, common cold, headache disorder, trigeminal autonomic cephalalgia, hypertrichosis, subarachnoid haemorrhage, or familial combined hyperlipidaemia.

---

## Australia Market Information

Cinacalcet is not currently registered on the ARTG (Australian Register of Therapeutic Goods) according to this evidence pack — 0 licence entries were returned.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack returned no key warnings, contraindications, or drug interaction data for cinacalcet, and a targeted TFDA/TGA label lookup is flagged as a **blocking data gap (DG001)** — meaning a formal safety (S1) assessment cannot proceed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (MEN1-associated hyperparathyroidism only) — **Hold** on all other 9 predicted indications.

**Rationale:**
- The MEN1 candidate has a directly relevant completed Phase 3 RCT (n=25), supportive Phase 4 and observational data in the broader hyperparathyroidism population, and 19 publications including multiple cohort studies — evidence level L2, decision stage S2. The mechanistic link (shared parathyroid PTH-dysregulation pathology) is direct, not speculative.
- The other 9 candidates, including the single highest TxGNN-scoring prediction (nephrogenic syndrome of inappropriate antidiuresis, 98.48%), have zero corroborating clinical trials or literature and should not advance beyond model-signal status (L5/S0).

**To proceed, the following is needed:**
- TGA-approved Product Information covering warnings, contraindications, and drug interactions for cinacalcet (currently a blocking data gap)
- Confirmed mechanism-of-action documentation from DrugBank (currently a high-severity data gap)
- Clarification of Australian market/registration pathway, since 0 ARTG entries were found despite cinacalcet being marketed in comparable jurisdictions
- A larger confirmatory trial or updated meta-analysis for the MEN1 indication, given the pivotal RCT enrolled only 25 patients
- A formal drug-drug interaction review, given the polypharmacy typical of CKD and MEN1 patient populations

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

