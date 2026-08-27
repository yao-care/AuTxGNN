---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: From Antifungal Therapy to Vulvovaginitis (Candida Vulvovaginitis)

## One-Sentence Summary

Nystatin is a polyene antifungal agent whose established clinical role is treating *Candida* infections of the skin and mucous membranes; the specific original indication is not recorded in this evidence pack. The TxGNN model predicts it may be effective for **Vulvovaginitis**, and this direction is currently supported by **20 publications**, though **no dedicated clinical trials** are registered for this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in source data (no ARTG listing on file); Nystatin's mechanism is that of a general topical/mucosal antifungal — see below |
| Predicted New Indication | Vulvovaginitis (Candida vulvovaginitis) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed (not currently on the ARTG) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data was not available for this record (`original_moa` was not provided). However, the evidence pack's own mechanistic analysis notes that Nystatin is a polyene antifungal that binds ergosterol in the fungal cell membrane, forming pores that cause leakage of cellular contents and lead to fungal cell death.

*Candida albicans* — the organism responsible for roughly 85–90% of vulvovaginal candidiasis cases per the literature below — is an ergosterol-dependent organism, i.e. exactly the molecular target Nystatin acts on. Vaginal nystatin (e.g. as vaginal tablets/pessaries) has in fact been used clinically for decades for this indication, so this prediction largely reflects a well-established, class-appropriate use rather than a novel repurposing signal.

Because the drug's mechanism maps directly onto the pathogen driving vulvovaginitis, and because a substantial and long-running body of published literature already documents this use, the TxGNN prediction is biologically plausible and well corroborated — even though it may represent recovery of a known application rather than a genuinely new one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | Vulvovaginal candidiasis is the second most common cause of vaginitis after bacterial vaginosis; *C. albicans* accounts for 85–90% of cases |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | Discusses recurrent VVC management and rising azole resistance among non-albicans species, supporting alternative antifungals |
| [4919155](https://pubmed.ncbi.nlm.nih.gov/4919155/) | 1970 | Review | Med Clin North Am | Classic clinical review of nystatin |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Cohort | Ceska Gynekologie | Evaluation of mixed/miscellaneous vulvovaginal infections treated with combined vaginal nifuratel + nystatin |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | Overview of vulvovaginal candidiasis diagnosis and management |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Review | BMJ Clinical Evidence | VVC epidemiology; *C. albicans* accounts for 85–90% of cases |
| [11363911](https://pubmed.ncbi.nlm.nih.gov/11363911/) | 1996 | Review | J Int Assoc Physicians AIDS Care | Review of candidiasis |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Update on management of fluconazole-resistant VVC; covers alternative antifungals including boric acid, nystatin, oteseconazole and ibrexafungerp |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | In vitro | Infect Drug Resist | ZnO nanoparticles and nystatin downregulate SAP1-3 gene expression in fluconazole-resistant *C. albicans* isolates from VVC |
| [19454049](https://pubmed.ncbi.nlm.nih.gov/19454049/) | 2007 | Review | BMJ Clinical Evidence | VVC epidemiology; *C. albicans* accounts for 85–90% of cases |

## Australia Market Information

Nystatin is not currently registered on the Australian Register of Therapeutic Goods (ARTG) — no product listings were found in the source data.

## Safety Considerations

No TGA-approved Product Information exists for Nystatin in Australia, as it is not currently registered on the ARTG. Key warnings, contraindications and drug-interaction data were also not available from the sources queried for this evidence pack (DDI query returned no results). Safety information should be sourced from the manufacturer's PI in a jurisdiction where the product is licensed before any clinical use is considered.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Nystatin's antifungal activity and the *Candida*-driven pathology of vulvovaginitis is strong and corroborated by a substantial literature base (L3, decision stage S2), but the prediction largely reflects an already-established use rather than a novel indication, and the drug currently has no Australian market presence or safety documentation on file.

**To proceed, the following is needed:**
- Formal TGA-equivalent Product Information / safety labelling, since Nystatin is not currently on the ARTG (blocking gap per evidence pack)
- Confirmed DrugBank-sourced mechanism-of-action documentation (currently marked as a data gap)
- A complete drug-interaction (DDI) profile, as the current query returned no results
- Clarification of whether this candidate represents a genuinely new indication or recovery of Nystatin's known vaginal-antifungal label, to set appropriate expectations for any regulatory or clinical pathway
- If market entry is pursued, an ARTG registration assessment given the current "not marketed" status in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

