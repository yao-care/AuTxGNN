---
layout: default
title: Warfarin
parent: 僅模型預測 (L5)
nav_order: 729
evidence_level: L5
indication_count: 10
---

# Warfarin
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

Using no additional skill — this is a direct content-generation task fully specified by the prompt template; proceeding with report generation from the supplied Evidence Pack.

---

# Warfarin: From Anticoagulation Therapy to Heparin Cofactor II Deficiency

## One-Sentence Summary

> Warfarin is a long-established oral anticoagulant, though this evidence pack does not contain a confirmed original indication text or mechanism-of-action record (flagged as data gaps).
> The TxGNN model predicts potential utility in **Heparin Cofactor II Deficiency**, a rare inherited thrombophilia,
> currently supported only by **5 case reports/reviews** and **no registered clinical trials** — an early, hypothesis-generating stage of evidence.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not confirmed in this evidence pack (no ARTG licences on file; MOA also flagged as a data gap — see Conclusion) |
| Predicted New Indication | Heparin Cofactor II Deficiency |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for warfarin is not available in this evidence pack (data gap DG002). Based on well-documented pharmacology reflected elsewhere in this evidence pack's own repurposing rationale (see the thrombophilia candidate, rank 4), warfarin's core action is inhibition of vitamin K–dependent clotting factor synthesis (Factors II, VII, IX, X), the basis of its decades-long use as the standard oral anticoagulant for thromboembolic disease.

Heparin cofactor II (HC2) deficiency is a rare inherited thrombophilia in which a natural anticoagulant protein is deficient, predisposing patients to venous thrombosis. Mechanistically, warfarin's antithrombotic effect is plausible in this setting by the same logic already validated for other inherited thrombophilias — indeed, this evidence pack's rank 4 candidate ("thrombophilia" broadly) carries the strongest evidence tier here (L1), reflecting that warfarin is already standard-of-care anticoagulation across this disease family. This lends indirect biological plausibility to the HC2-deficiency-specific prediction, even though direct clinical evidence for this narrow, rare phenotype remains limited to case-level literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11177584](https://pubmed.ncbi.nlm.nih.gov/11177584/) | 2001 | Review | AIDS Patient Care and STDs | Reviews prothrombotic states in HIV/AIDS, including deficiencies of natural anticoagulant proteins predisposing to hypercoagulability; general thrombophilia context, not HC2-specific warfarin data |
| [3778142](https://pubmed.ncbi.nlm.nih.gov/3778142/) | 1986 | Review | Archives of Pathology & Laboratory Medicine | Describes laboratory assay for HC II activity; low levels linked to liver disease, consumptive coagulopathy, and preeclampsia — diagnostic reference, no treatment outcome data |
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case Report | Kyobu Geka (Japanese Journal of Thoracic Surgery) | 14-year-old female with familial HC II deficiency and right ventricular outflow thrombus, managed surgically; illustrates thrombotic risk but no warfarin outcome reported |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case Report | Journal of UOEH | Family with recurrent thrombosis including infantile onset; one member started on warfarin still developed further DVT, suggesting anticoagulation alone may be insufficient in some thrombophilia phenotypes |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case Report | Nihon Kyobu Shikkan Gakkai Zasshi | 48-year-old woman with congenital antithrombin (a related natural-anticoagulant deficiency) and recurrent pulmonary infarction, treated with warfarin for 7 years before switching to heparin — demonstrates long-term warfarin use in inherited thrombophilia, though for a distinct (antithrombin) deficiency |

## Australia Market Information

Warfarin has **0 ARTG entries** on file in this evidence pack, with market status recorded as **Not marketed**. No product licence records are available to summarise.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack contains no confirmed key warnings, contraindications, or drug interaction data for warfarin (formal safety/PI extraction is an outstanding, blocking data gap — see Conclusion).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for warfarin in heparin cofactor II deficiency consists only of case reports and narrative reviews (Evidence Level L4), with no registered clinical trials and no HC2-deficiency-specific treatment outcome data. Critical drug-level data (formal safety/PI warnings, confirmed mechanism of action) are also unresolved, and warfarin has no current Australian market presence in this dataset.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism-of-action data via DrugBank — currently a high-impact data gap (DG002)
- Original registered indication confirmation (no ARTG licence data available)
- Targeted case-series or registry data specifically in HC2-deficiency patients, rather than the related-but-distinct antithrombin/protein C/S deficiency literature currently cited
- Given ARTG status of "Not marketed," a route-to-market/ARTG registration assessment before any clinical evaluation in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

