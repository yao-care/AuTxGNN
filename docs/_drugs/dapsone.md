---
layout: default
title: Dapsone
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Dapsone
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

# Dapsone: From Leprosy to Pneumocystosis (PCP)

## One-Sentence Summary

Dapsone is a sulfone antibacterial classically used to treat leprosy (Hansen's disease), as referenced within this evidence pack's own literature (PMID 11155588, 19824739).
The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis jirovecii pneumonia, PCP)**,
with **14 clinical trials** and **19 publications** currently supporting this direction — notably, dapsone is already an established second-line PCP prophylaxis/treatment agent in clinical practice for patients intolerant of trimethoprim-sulfamethoxazole (TMP-SMX).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leprosy (per literature evidence, PMID 11155588/19824739/20966036); not present in the ARTG licence data in this pack |
| Predicted New Indication | Pneumocystosis (PCP) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data (DrugBank MOA field) is currently a data gap. Based on the repurposing rationale captured in this evidence pack, dapsone is a sulfone-class antibacterial that inhibits dihydropteroate synthase (DHPS), blocking folic acid synthesis in *Pneumocystis jirovecii* — the same mechanistic pathway targeted by sulfonamide antimicrobials.

This mechanistic link is not merely theoretical: dapsone (alone or combined with trimethoprim/pyrimethamine) is already recognised clinical practice as a standard second-line option for PCP prophylaxis and treatment in patients who cannot tolerate TMP-SMX. Multiple completed Phase 3 RCTs (e.g. NCT00000802, NCT00000640, NCT00000991) directly compared dapsone-based regimens against TMP-SMX, aerosolized pentamidine, and atovaquone in this setting, which strongly reinforces the plausibility of the TxGNN prediction.

The principal safety concern carried over from dapsone's known pharmacology is haemolysis and methemoglobinemia in patients with G6PD deficiency, which is why pre-treatment G6PD screening is clinically important whenever dapsone is used for PCP prophylaxis or treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Dapsone vs atovaquone for PCP prophylaxis in HIV patients intolerant of TMP/sulfonamides |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/trimethoprim vs clindamycin/primaquine vs TMP-SMX for mild-to-moderate PCP treatment in AIDS |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Comparison of three anti-*Pneumocystis* regimens plus zidovudine for primary prevention of serious infection in advanced HIV |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | N/A | Completed | N/A | Dapsone plus trimethoprim vs TMP-SMX for first-episode PCP in AIDS patients |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Aerosolized pentamidine vs thrice-weekly dapsone for PCP prophylaxis in TMP/sulfonamide-intolerant patients |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Two oral dapsone dosing regimens for PCP prophylaxis in paediatric HIV infection |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Unknown | 3130 | HLA-B*1301 prospective genetic screening for dapsone hypersensitivity syndrome risk, including PCP patients |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Trimetrexate + dapsone + leucovorin vs TMP-SMX for moderately severe PCP |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | Completed | 30 | Clindamycin-TMP/SMX for PCP after solid organ transplant; notes dapsone as a second-line alternative when TMP-SMX fails |
| [NCT05077150](https://clinicaltrials.gov/study/NCT05077150) | N/A | Completed | 168 | Case-control study of PCP risk factors after allogeneic HSCT; notes elevated PCP incidence (up to 7.2%) on low-dose dapsone prophylaxis |

No Australian/New Zealand Clinical Trials Registry (ANZCTR) entries were identified for this evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guideline | J Antimicrob Chemother | ECIL-5 guidelines for PCP prophylaxis in haematological malignancy/HSCT recipients |
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Systematic Review / Network Meta-analysis | Clin Microbiol Infect | Comparative efficacy/safety of PCP prophylaxis regimens in people living with HIV, including dapsone-based regimens |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic Review / Network Meta-analysis | Clin Microbiol Infect | Comparative efficacy/safety of PCP treatment regimens in people living with HIV |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opin Pharmacother | *Pneumocystis jirovecii* review focused on prevention and treatment options |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Review | Clin Infect Dis | Use of dapsone in prevention and treatment of PCP; covers DHPS mechanism and pharmacokinetics |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Review | J Formos Med Assoc | General review of Pneumocystis pneumonia |
| [7979291](https://pubmed.ncbi.nlm.nih.gov/7979291/) | 1994 | PK/Safety Study | Antimicrob Agents Chemother | Pharmacokinetics and safety of weekly dapsone (± pyrimethamine) for PCP prevention |
| [8605054](https://pubmed.ncbi.nlm.nih.gov/8605054/) | 1995 | Clinical Study | AIDS | Aerosolized pentamidine, cotrimoxazole, and dapsone-pyrimethamine for primary PCP/toxoplasmic encephalitis prophylaxis |
| [10073326](https://pubmed.ncbi.nlm.nih.gov/10073326/) | 1999 | PK Study | J Clin Pharmacol | Pharmacokinetics of trimetrexate and dapsone in AIDS patients with PCP |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case Report | Ann Pharmacother | Dapsone-induced methemoglobinemia during PCP prophylaxis |

---

## Australia Market Information

No ARTG entries were found for dapsone in this evidence pack (`total_licenses: 0`, `market_status: 未上市` / Not Marketed). Dapsone does not currently appear to hold an Australian Register of Therapeutic Goods listing under the data reviewed.

---

## Safety Considerations

Formal TGA-sourced key warnings, contraindications, and drug–drug interaction data are marked as data gaps in this evidence pack (blocking gap DG001).

Evidence-derived signals worth noting from the literature and repurposing rationale (not formal PI data):
- **Haemolysis / methemoglobinemia**: Case-level and mechanistic evidence (PMID 9606476) associates dapsone with methemoglobinemia; the repurposing rationale specifically flags G6PD deficiency as a key risk factor requiring pre-treatment screening.
- **Dapsone hypersensitivity syndrome**: A dedicated Phase 4 trial (NCT02550080) is evaluating HLA-B*1301 screening to reduce this risk across dapsone indications, including PCP.

Please refer to the TGA-approved Product Information (PI) for authoritative safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence Level L1 is supported by four or more completed Phase 3 RCTs directly evaluating dapsone-based regimens against standard-of-care comparators for PCP prophylaxis and treatment, and this use is already established second-line clinical practice — well beyond a purely model-driven prediction. However, dapsone has no current ARTG listing in Australia and formal TGA safety/labelling data are absent, so guardrails are required before clinical application.

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) — warnings, contraindications, and DDI data (blocking gap DG001)
- Formal DrugBank/regulatory mechanism-of-action documentation (gap DG002)
- Confirmation of Australian market/import pathway, since dapsone currently has 0 ARTG entries
- A G6PD deficiency screening protocol prior to dapsone initiation for PCP indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

