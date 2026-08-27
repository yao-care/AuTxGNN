---
layout: default
title: Ganciclovir
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Ganciclovir
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

# Ganciclovir: From Cytomegalovirus Infection to Cytomegalovirus Pneumonia

## One-Sentence Summary

> Ganciclovir is an established antiviral used to treat cytomegalovirus (CMV) disease in immunocompromised patients. The TxGNN model predicts it may be effective for **Cytomegalovirus Pneumonia**, with **9 clinical trials** and **20 publications** currently supporting this direction — noting this is less a novel "repurposing" than an extension within ganciclovir's core CMV-disease indication spectrum.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cytomegalovirus (CMV) disease/infection (established antiviral use; no ARTG-registered indication text is available in this evidence pack — see Australia Market Information) |
| Predicted New Indication | Cytomegalovirus Pneumonia |
| TxGNN Prediction Score | 97.56% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action record was not returned in this evidence pack (flagged as data gap DG002). Based on the pharmacology referenced in the prediction rationale, ganciclovir is a synthetic 2′-deoxyguanosine analogue. After intracellular phosphorylation to its triphosphate form, it competitively inhibits viral DNA polymerase and causes premature termination of viral DNA chain elongation. Cytomegalovirus is one of ganciclovir's original and core pharmacological targets.

CMV pneumonia is a clinical manifestation of CMV disease — the same disease category ganciclovir was developed for and is already used to treat (e.g., CMV retinitis, disseminated CMV disease in transplant recipients). This means the predicted indication does not represent a cross-disease repurposing in the usual sense, but rather an extension within ganciclovir's existing core indication spectrum.

Because CMV pneumonia is caused by the exact pathogen ganciclovir's antiviral activity is directed against, the mechanistic plausibility here is about as strong as a TxGNN prediction can be. This is reflected in the L1 evidence level and the substantial body of completed trials in transplant and immunocompromised populations (bone marrow/stem cell transplant, ICU, paediatric HIV) supporting the drug-disease pairing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02152358](https://clinicaltrials.gov/study/NCT02152358) | Phase 4 | Completed | 317 | Randomised, double-blind trial of preemptive ganciclovir (CMV) vs aciclovir (HSV) in ICU patients on prolonged mechanical ventilation with viral replication; endpoint was ventilator-free days at Day 60. |
| [NCT04690933](https://clinicaltrials.gov/study/NCT04690933) | N/A | Completed | 400 | Real-world observational study of efficacy and resistance to anti-CMV agents in haematopoietic stem cell transplant recipients; CMV interstitial pneumonia noted as the most severe manifestation. |
| [NCT03915366](https://clinicaltrials.gov/study/NCT03915366) | Phase 2/3 | Completed | 563 | Multicentre RCT of empirical anti-CMV/anti-tuberculosis treatment in HIV-infected infants with severe pneumonia; survival endpoint. |
| [NCT01199562](https://clinicaltrials.gov/study/NCT01199562) | N/A | Active, not recruiting | 153 | Modified preemptive CMV management strategy after allogeneic HCT, correlated with innate immune function — validates the ganciclovir-based preemptive treatment pathway. |
| [NCT05708755](https://clinicaltrials.gov/study/NCT05708755) | Phase 2 | Recruiting | 50 | CMV-specific T-cell immunity assay to guide duration/minimisation of valganciclovir prophylaxis in lung transplant recipients. |
| [NCT00078533](https://clinicaltrials.gov/study/NCT00078533) | Phase 1 | Completed | 26 | Dose-finding trial of virus-specific cytotoxic T-lymphocytes as an adjunct/alternative for CMV after allogeneic stem cell transplant. |
| [NCT02109887](https://clinicaltrials.gov/study/NCT02109887) | N/A | Completed | 76 | CMV-specific ELISPOT assay to predict CMV co-infection in Pneumocystis pneumonia patients — diagnostic rather than treatment trial. |
| [NCT00000726](https://clinicaltrials.gov/study/NCT00000726) | Phase 1 | Completed | 53 | Foscarnet (not ganciclovir) for CMV retinitis in AIDS patients — different drug/site; low direct relevance. |
| [NCT00141037](https://clinicaltrials.gov/study/NCT00141037) | Phase 1/2 | Completed | 130 | Tacrolimus/steroid vs daclizumab induction in paediatric renal transplant — immunosuppression trial, not a ganciclovir efficacy study. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8380243](https://pubmed.ncbi.nlm.nih.gov/8380243/) | 1993 | RCT (placebo-controlled, double-blind) | Annals of Internal Medicine | Ganciclovir prophylaxis for prevention of CMV infection/disease in allogeneic bone marrow transplant recipients. |
| [39774866](https://pubmed.ncbi.nlm.nih.gov/39774866/) | 2025 | Review | Intensive Care Medicine | What intensivists need to know about CMV infection/disease, including pneumonia, in immunocompromised ICU patients. |
| [8274605](https://pubmed.ncbi.nlm.nih.gov/8274605/) | 1993 | Review | Clinical Infectious Diseases | Prevention and treatment of CMV pneumonia in transplant recipients; positions ganciclovir as increasingly central to early prevention. |
| [2161731](https://pubmed.ncbi.nlm.nih.gov/2161731/) | 1990 | Review | Drugs | Review of ganciclovir's antiviral activity, pharmacokinetics and therapeutic efficacy in CMV infections; recommends it as first-line therapy for life/sight-threatening CMV disease. |
| [8668848](https://pubmed.ncbi.nlm.nih.gov/8668848/) | 1995 | Review | Seminars in Respiratory Infections | CMV pneumonia presentation, diagnosis and treatment, particularly in allogeneic bone marrow transplant recipients. |
| [8786764](https://pubmed.ncbi.nlm.nih.gov/8786764/) | 1996 | Review | New England Journal of Medicine | Classic NEJM review of ganciclovir pharmacology and clinical use. |
| [37225488](https://pubmed.ncbi.nlm.nih.gov/37225488/) | 2024 | Case Report | Internal Medicine (Tokyo) | Primary CMV pneumonia in an immunocompetent patient successfully treated with corticosteroid therapy and valganciclovir. |
| [2847609](https://pubmed.ncbi.nlm.nih.gov/2847609/) | 1988 | Case Series | Annals of Internal Medicine | CMV interstitial pneumonia after allogeneic BMT successfully treated with ganciclovir plus high-dose IV immune globulin. |
| [2847610](https://pubmed.ncbi.nlm.nih.gov/2847610/) | 1988 | Case Series | Annals of Internal Medicine | Treatment of CMV pneumonia with ganciclovir and IV CMV immunoglobulin in bone marrow transplant patients. |
| [2161510](https://pubmed.ncbi.nlm.nih.gov/2161510/) | 1990 | Case Series (pilot study) | Nouvelle Revue Française d'Hématologie | Ganciclovir plus high-dose IV immunoglobulin for severe CMV infection in allogeneic BMT recipients. |

---

## Australia Market Information

No ARTG entries are currently registered for Ganciclovir in this evidence pack (0 of 0 licenses; market status: **Not marketed**). Local product availability, dosage forms, and TGA-approved indication wording could not be confirmed and would need direct verification against the TGA/ARTG database.

---

## Safety Considerations

No warnings, contraindications, or drug-interaction data were returned in this evidence pack — this is flagged as a **blocking data gap (DG001)**: TFDA/TGA-equivalent Product Information has not yet been obtained. A DDI query also returned "not found." Because Ganciclovir is not currently marketed in Australia (0 ARTG entries), no local PI exists to reference; prescribers should consult overseas-approved Product Information (e.g. FDA/EMA labelling) and institutional protocols until Australian regulatory safety data is confirmed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed trials (including a Phase 4 RCT, n=317, and a Phase 2/3 RCT, n=563) plus a substantial literature base, and the mechanistic link is exceptionally strong since CMV pneumonia sits within ganciclovir's core, already-established CMV disease indication. However, safety data is a blocking gap and the drug has no current Australian market presence.

**To proceed, the following is needed:**
- TGA-equivalent Product Information covering warnings, contraindications and monitoring (DG001, blocking)
- Formal DrugBank/pharmacology confirmation of mechanism of action (DG002)
- Confirmation of Australian registration pathway, dosage forms and market entry (currently 0 ARTG entries)
- Completion of the drug interaction (DDI) dataset query, currently returning "not found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

