---
layout: default
title: Flutamide
parent: Model Prediction Only (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Flutamide: predicted new indication Top-ranked: prostate cancer/brain cancer susceptibility (Hold… (evidence level L5). Approved use: Prostate cancer"
---

# Flutamide
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

# Flutamide: From Prostate Cancer to Male Reproductive Organ Cancer

## One-Sentence Summary

Flutamide is a nonsteroidal androgen receptor antagonist, originally used to treat prostate cancer.
The TxGNN model's top-ranked prediction is "prostate cancer/brain cancer susceptibility", a genetic susceptibility label with no supporting evidence. The best-supported prediction in this dataset is **male reproductive organ cancer**, which includes prostate cancer and so is effectively the drug's existing use. It has **40 registered clinical trials** and **20 publications**, but the retrieved titles often do not confirm flutamide as a studied arm.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (the ARTG entry has no indication text; this comes from the knowledge graph) |
| Predicted New Indication | Top-ranked: prostate cancer/brain cancer susceptibility (Hold, L5). Best-supported: male reproductive organ cancer |
| TxGNN Prediction Score | 99.98% (top-ranked prediction); 99.98% (male reproductive organ cancer) |
| Evidence Level | L1 (male reproductive organ cancer); L5 for the top-ranked prediction |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (male reproductive organ cancer only); Hold for the top-ranked prediction |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the literature, flutamide is a pure nonsteroidal antiandrogen that blocks androgen receptors and is usually combined with an LHRH agonist for combined androgen blockade in prostate cancer (PMID 8252497, PMID 3071951).

The top-ranked prediction, "prostate cancer/brain cancer susceptibility", is a genetic susceptibility label rather than a treatable disease. Its high score most likely reflects graph proximity to prostate cancer. The same applies to the other highly ranked rare prostate or reproductive tumours (fibroma of prostate, prostate leiomyoma, benign prostate phyllodes tumour). Brenner tumour has no known androgen-dependent biology. None of these has trials or literature.

"Male reproductive organ cancer" is a broad category that contains prostate cancer, so this is confirmation of an existing use rather than true repurposing. The HIV, simian immunodeficiency virus and feline immunodeficiency predictions have no plausible antiviral mechanism and are likely graph artefacts.

## Clinical Trial Evidence

Trials linked to male reproductive organ cancer (up to 10 shown, prioritising those with a direct flutamide link or relevance grade A/B). Many retrieved titles do not confirm flutamide as a studied arm.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006214](https://clinicaltrials.gov/study/NCT00006214) | Phase 2 | Completed | 63 | Flutamide as an androgen deprivation agent for chemoprevention in men with prostatic intraepithelial neoplasia |
| [NCT06601205](https://clinicaltrials.gov/study/NCT06601205) | Phase 2/3 | Completed | 125 | Pre-surgical window-of-opportunity trial: finasteride vs low-dose flutamide vs placebo in prostate cancer |
| [NCT02918968](https://clinicaltrials.gov/study/NCT02918968) | Phase 4 | Completed | 206 | Enzalutamide vs flutamide (each with ADT) in castration-resistant prostate cancer after failure of bicalutamide-based combined androgen blockade |
| [NCT00450463](https://clinicaltrials.gov/study/NCT00450463) | Phase 2 | Completed | 64 | PROSTVAC vaccine plus flutamide vs flutamide alone in non-metastatic androgen-insensitive prostate cancer |
| [NCT00002881](https://clinicaltrials.gov/study/NCT00002881) | Phase 3 | Completed | Not stated | Orchiectomy/LHRH analogue plus flutamide with or without suramin and hydrocortisone in metastatic prostate cancer |
| [NCT00003645](https://clinicaltrials.gov/study/NCT00003645) | Phase 3 | Terminated | 64 | Adjuvant leuprolide plus flutamide vs no further therapy in high-risk surgically treated prostate cancer; underpowered after early termination |
| [NCT00002597](https://clinicaltrials.gov/study/NCT00002597) | Phase 3 | Completed | 2,028 | Radiation therapy with or without antiandrogen therapy (flutamide, goserelin, leuprolide) in locally confined prostate cancer |
| [NCT00104741](https://clinicaltrials.gov/study/NCT00104741) | Phase 3 | Completed | 378 | Triptorelin and flutamide with radiotherapy in intermediate-risk localised prostate cancer |
| [NCT00003734](https://clinicaltrials.gov/study/NCT00003734) | Phase 3 | Unknown | 276 | 4 vs 8 months of neoadjuvant triptorelin plus flutamide before radiotherapy in high-risk localised prostate cancer |
| [NCT00003323](https://clinicaltrials.gov/study/NCT00003323) | Phase 2 | Completed | 101 | Flutamide plus finasteride (potency-sparing) for rising PSA after radiotherapy or prostatectomy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8252497](https://pubmed.ncbi.nlm.nih.gov/8252497/) | 1993 | Review | Cancer | Mechanism and pure antiandrogenic properties of flutamide; maximal prostate inhibition when combined with an LHRH agonist |
| [3071951](https://pubmed.ncbi.nlm.nih.gov/3071951/) | 1988 | Review | Am J Clin Oncol | Rationale for combining nonsteroidal antiandrogens with LH-RH agonists in prostate cancer |
| [3285484](https://pubmed.ncbi.nlm.nih.gov/3285484/) | 1988 | Review | Semin Oncol | Advantages of total androgen blockade over castration alone in advanced prostate cancer |
| [2934257](https://pubmed.ncbi.nlm.nih.gov/2934257/) | 1985 | Clinical study | Eur J Cancer Clin Oncol | Adrenal androgen blockade in relapsed prostate cancer |
| [20541672](https://pubmed.ncbi.nlm.nih.gov/20541672/) | 2010 | Review | Prog Brain Res | Optimal androgen blockade in hormonal therapy of prostate cancer |
| [24950779](https://pubmed.ncbi.nlm.nih.gov/24950779/) | 2014 | Phase 2 and preclinical | Cancer Prev Res | Preoperative flutamide (125 mg/day for 6 weeks) in women at high risk of ovarian cancer; tissue biomarker study |
| [8087144](https://pubmed.ncbi.nlm.nih.gov/8087144/) | 1994 | Review | World J Urol | Androgen signal transduction and the shift to androgen independence in prostatic carcinoma |
| [29958919](https://pubmed.ncbi.nlm.nih.gov/29958919/) | 2018 | Preclinical review | Reprod Toxicol | Effects of flutamide on cell-cell junctions in the testis, epididymis and prostate |
| [7576816](https://pubmed.ncbi.nlm.nih.gov/7576816/) | 1995 | Toxicology review | Hum Exp Toxicol | Drug-induced Leydig cell hyperplasia and neoplasia in rats, including flutamide |
| [37919464](https://pubmed.ncbi.nlm.nih.gov/37919464/) | 2023 | In vitro | Sci Rep | Ganoderma lucidum polysaccharide sensitises prostate cancer cells to flutamide and docetaxel |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1417N | Flutamin | Tablet 250 mg | Indication text not recorded in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (nonsteroidal androgen receptor antagonist); not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Liver function tests (hepatotoxicity is a boxed warning concern), per the PI |
| Handling Protection | Please refer to the Product Information (PI) warnings and precautions |

## Safety Considerations

- **Key Warnings**: Hepatotoxicity (boxed warning), noted in the repurposing analysis. Label text was not available, so confirm against the TGA-approved PI.
- **Contraindications (from the knowledge graph, not label text)**: liver failure, liver disease, gallbladder disease, methemoglobinemia, sulfhemoglobinemia, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, and pyruvate dehydrogenase E3 deficiency.
- **Drug Interactions**: 100 interactions were identified. Major: dolasetron and cisapride. Moderate examples: clarithromycin, levofloxacin, ondansetron, palonosetron, naltrexone, famotidine, loperamide and obeticholic acid, plus several laxatives and bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol, lactulose, lactitol, castor oil, glycerin, sodium sulfate). Minor example: metronidazole.

Please refer to the TGA-approved Product Information (PI) for complete safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (male reproductive organ cancer only); Hold for all other predictions**

**Rationale:**
- Male reproductive organ cancer includes prostate cancer, flutamide's established use, and many Phase 3 trials exist in this setting. This is confirmation of an existing indication rather than new repurposing, and newer antiandrogens have largely replaced flutamide.
- The top-ranked "prostate cancer/brain cancer susceptibility" label and the other rare tumour, HIV and animal-disease predictions have no trials or literature, so they remain on Hold. Benign reproductive system neoplasm has only indirect, small-scale evidence (L4) and is a research question rather than a candidate.

**To proceed, the following is needed:**
- Verify from full trial records whether flutamide was a studied arm in each retrieved Phase 3 trial.
- Obtain the TGA Product Information to confirm approved indications, warnings and contraindications for ARTG 1417N.
- Obtain detailed mechanism of action data from DrugBank.
- Put in place a liver function monitoring plan and a review of the interaction burden (especially QT-prolonging drugs).
- Compare flutamide against current antiandrogen standards of care before any new use is considered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

