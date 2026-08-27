---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic Protozoal/Bacterial Infections to Pneumocystosis

## One-Sentence Summary

> Metronidazole is a nitroimidazole antimicrobial historically used for anaerobic bacterial and protozoal infections (e.g. trichomoniasis, amoebiasis, giardiasis).
> The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis pneumonia)** with a very high prediction score, but currently **no clinical trials or literature directly support this use**, and the drug's own mechanism argues against biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaerobic bacterial and protozoal infections (e.g. trichomoniasis, amoebiasis, giardiasis) — based on general pharmacology; no Australian ARTG-approved indication text is available, as this product is not currently marketed |
| Predicted New Indication | Pneumocystosis (Pneumocystis pneumonia) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for metronidazole is not available in this evidence pack. Based on general pharmacological knowledge, metronidazole is a nitroimidazole antimicrobial/antiprotozoal agent. It requires reductive activation by anaerobic or microaerophilic organisms to generate cytotoxic intermediates that damage microbial DNA — this underlies its established efficacy against anaerobic bacteria and protozoa such as *Trichomonas vaginalis*, *Entamoeba histolytica* and *Giardia lamblia*.

*Pneumocystis jirovecii*, the causative organism of pneumocystosis, is neither an anaerobic bacterium nor a protozoan — it is a fungus-like organism that does not undergo the reductive activation metronidazole depends on. Standard treatment for pneumocystosis is trimethoprim-sulfamethoxazole, not nitroimidazoles.

The literature identified for this candidate consists largely of reviews on antiparasitic therapy and HIV-related opportunistic infections, plus case reports in which patients were treated with metronidazole for an unrelated condition (e.g. amoebic dysentery) and *separately* developed pneumocystosis. None of these sources demonstrate metronidazole activity against *P. jirovecii*. On balance, this appears to be a high-scoring TxGNN prediction without a supporting mechanistic or clinical rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. A keyword search returned 23 clinical trials, but all trials reviewed to date (10 of 23) were assessed as **Grade C — not relevant** (e.g. mindfulness interventions, primary-care delivery models, opioid risk reduction, dementia care programs). None evaluate metronidazole for pneumocystosis. The remaining unreviewed trials are similarly unrelated primary-care/health-services studies based on their titles.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | General antiparasitic drug review; lists metronidazole for amebic colitis, extraintestinal amebiasis and trichomoniasis — separately notes trimethoprim-sulfamethoxazole (not metronidazole) as the drug of choice for pneumocystis pneumonia |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clinical Pharmacokinetics | Pharmacokinetic rationale for antiprotozoal therapy in general; no specific metronidazole/PCP data |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clinic Proceedings | Broad review of antiparasitic agents; no direct PCP treatment data |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | Review of HIV-related opportunistic infections generally; does not evaluate metronidazole for PCP |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Reviews treatment of AIDS-related infections including PCP; metronidazole not described as PCP therapy |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case Report | American Review of Respiratory Disease | Patient with PCP and CMV pneumonia had previously received metronidazole for unrelated diarrhoeal illness — incidental exposure, not treatment of PCP |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case Report | Kansenshogaku Zasshi | AIDS patient treated with metronidazole for amoebic dysentery, later separately developed PCP — again incidental, not causal treatment |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case Report | Journal of the Formosan Medical Association | AIDS patient with CMV/amoebic colitis; PCP not the focus and metronidazole not used for it |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Reviews of Infectious Diseases | General critique of antimicrobial prophylaxis trials; not specific to metronidazole or PCP |

None of the above literature demonstrates metronidazole efficacy against *Pneumocystis jirovecii*; mentions of metronidazole and PCP are coincidental (same patient, different indications).

---

## Australia Market Information

Metronidazole currently has **no ARTG entries** on file, and market status is recorded as **Not marketed** in Australia. No product-specific dosage form or approved-indication data is available for this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications and a drug-drug interaction (DDI) check for metronidazole are all outstanding data gaps (DG001, Blocking) that must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.99%), there is no direct clinical trial or literature evidence that metronidazole is effective against pneumocystosis, and the drug's known mechanism (anaerobic/protozoal reductive activation) is not applicable to *Pneumocystis jirovecii*. This is a model-only prediction (Evidence Level L5) that is not currently biologically or clinically supported.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information — warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action data from DrugBank (DG002, High)
- Purpose-designed pharmacological or in vitro studies testing nitroimidazole activity against *Pneumocystis jirovecii*, since no such studies currently exist
- Note: other candidates for this drug in the same evidence pack — cap polyposis (Evidence Level L3, Research Question) and ulceration of vulva (Evidence Level L3, Research Question) — have materially stronger mechanistic and case-based support and may warrant separate evaluation ahead of pneumocystosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

