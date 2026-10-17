---
layout: default
title: Levonorgestrel
parent: Moderate Evidence (L3-L4)
nav_order: 424
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Levonorgestrel: predicted new indication Acne (disease) (evidence level L4). Approved use: Postmenopausal osteoporosis / osteoporosis"
monitor_inn: "Levonorgestrel"
predicted_indications: ["acne (disease)", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "apocrine adenosis of breast", "blunt duct adenosis of breast", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "fat necrosis of breast", "breast abscess", "lactation disease"]
---

# Levonorgestrel
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Levonorgestrel: From Postmenopausal Osteoporosis to Acne

## One-Sentence Summary

Levonorgestrel is a progestin. The knowledge graph lists its original indications as postmenopausal osteoporosis and osteoporosis, although it is widely used in contraception. The TxGNN model predicts it may be effective for **acne**, but **no clinical trials** are registered for this indication. The 20 publications compiled are mostly general contraception reviews, and only one randomised trial concerns an oral contraceptive that combines levonorgestrel with ethinyl estradiol.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis / osteoporosis (knowledge graph; no approved indication text in the ARTG data compiled) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Levonorgestrel is a progestin, and its original indications come from knowledge graph links rather than approved label text.

The mechanistic case for acne is weak. Levonorgestrel has residual androgenic activity (PMID 7825629), which is a theoretical concern for acne rather than a benefit. Dermatological benefit is documented for combined oral contraceptives containing anti-androgenic progestins, such as chlormadinone acetate (PMID 21895044), not for levonorgestrel itself. The high TxGNN score likely reflects network proximity to hormonal contraceptives as a class.

Any acne effect of levonorgestrel is indirect. It could be neutral or adverse depending on formulation, and levonorgestrel-releasing intrauterine systems and implants have been associated with acne as an adverse effect. The one randomised trial in the data tested a combination product (ethinyl estradiol 20 µg plus levonorgestrel 100 µg), so benefit there is likely driven by the estrogen component and cannot be attributed to levonorgestrel alone.

## Clinical Trial Evidence

Currently no related clinical trials registered for acne.

## Literature Evidence

The 20 publications compiled are mostly narrative reviews. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | RCT (placebo-controlled) | J Am Acad Dermatol | Low-dose oral contraceptive (ethinyl estradiol 20 µg + levonorgestrel 100 µg) tested for moderate acne. Combination product, so the effect cannot be attributed to levonorgestrel alone |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Review | Drugs | Ethinylestradiol/chlormadinone acetate was significantly more effective than ethinylestradiol/levonorgestrel in mild-to-moderate papulopustular acne |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Review | Am J Clin Dermatol | Dermatological benefits of an anti-androgenic progestin combination in acne, seborrhoea, hirsutism and hair loss |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Med | Describes the androgenicity of progestins, including 19-carbon progestins used in contraceptives |
| [30088446](https://pubmed.ncbi.nlm.nih.gov/30088446/) | 2018 | Review | Curr Drug Targets | Molecular interactions of steroids in sebum production and acne |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Review | Semin Reprod Med | Levonorgestrel-releasing intrauterine system as contraception, with an antiproliferative endometrial action. Not acne-specific |
| [32909630](https://pubmed.ncbi.nlm.nih.gov/32909630/) | 2020 | Systematic review | Cochrane Database Syst Rev | Levonorgestrel-releasing intrauterine system for endometrial hyperplasia. Not acne-specific |
| [14688179](https://pubmed.ncbi.nlm.nih.gov/14688179/) | 2004 | Clinical study | Hum Reprod | Levonorgestrel-releasing intrauterine system for symptomatic treatment of endometriosis. Not acne-specific |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11909T | Kyleena | Intrauterine drug delivery system 19.5 mg | Not available in the data compiled |

## Safety Considerations

Product Information safety text was not available in the data compiled, so please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

- **Contraindications suggested by the knowledge graph** (not label text): hypertension, epilepsy, anxiety and neurotic disorders, porphyria, kidney disease, liver disease, gallbladder disease, hyperglycaemia and diabetes mellitus (including diabetic ketoacidosis), hypothyroidism, systemic lupus erythematosus, asthma, blood coagulation disease, hypertriglyceridaemia, and hypercalcaemia or other calcium and phosphorus metabolism disorders.
- **Drug interactions:** 100 interactions were identified, and the 20 shown were all of Moderate severity. Most involve glucose-lowering agents, which fits the hyperglycaemia signal above: acarbose, canagliflozin, dapagliflozin, ertugliflozin, exenatide, liraglutide, linagliptin, nateglinide and several insulins. Others include aprepitant, clotrimazole, glycerol phenylbutyrate and linaclotide.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a network score with no registered trials for acne. The only randomised trial involved a combination product, and levonorgestrel's androgenic activity and its reported acne adverse effects with intrauterine systems and implants argue against benefit. Other predicted indications in the data (ranks 2 to 9) have no supporting evidence at all.

**To proceed, the following is needed:**
- Mechanism of action data for levonorgestrel
- Approved indication text and safety sections from the TGA Product Information, which are currently missing
- Controlled studies of levonorgestrel alone in acne, with a comparison against anti-androgenic progestin regimens
- Clarification of the original indication, since the knowledge graph lists osteoporosis while the registered Australian product is an intrauterine system
- A risk assessment of the knowledge graph contraindications against any intended acne population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

