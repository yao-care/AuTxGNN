---
layout: default
title: Heparin
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Heparin
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

# Heparin: From Anticoagulation to Thrombophilia Due to Protein C Deficiency (Autosomal Recessive)

## One-Sentence Summary

Heparin is a well-established anticoagulant widely used for thromboprophylaxis and treatment of thromboembolic conditions including deep vein thrombosis, pulmonary embolism, and acute coronary syndromes.
The TxGNN model predicts it may be effective for **Thrombophilia Due to Protein C Deficiency (Autosomal Recessive)**, with a prediction score of **99.29%**;
however, **no matching clinical trials or published literature** were retrieved in this search cycle — almost certainly reflecting the extreme rarity of this condition rather than an absence of clinical experience with heparin in this context.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anticoagulation / thromboprophylaxis (no ARTG licence record available) |
| Predicted New Indication | Thrombophilia Due to Protein C Deficiency (Autosomal Recessive) |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L4 (Mechanistic rationale only) |
| Australia Market Status | Not marketed (0 ARTG entries found — see note below) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Data pipeline note:** Heparin is a critical-care medicine in routine use in Australian hospitals. The 0 ARTG entries likely reflects a query-matching issue (e.g. products registered as "Heparin Sodium" or under specific brand names). ARTG registration should be confirmed directly via the TGA ARTG public portal before drawing clinical conclusions from this field.

---

## Why is This Prediction Reasonable?

Protein C is one of the body's primary anticoagulant regulators. When activated by the thrombomodulin–thrombin complex on vascular endothelium, it cleaves and inactivates clotting factors Va and VIIIa, thereby suppressing further thrombin generation. In autosomal recessive Protein C deficiency — the most severe form of the condition — both alleles are affected, leaving this pathway severely impaired or entirely absent. The result is uncontrolled procoagulant activity: a state of constitutive thrombophilia. Homozygous or compound heterozygous neonates characteristically present with purpura fulminans or disseminated intravascular coagulation (DIC) in the first days of life.

Heparin acts through a complementary but pathway-independent mechanism. By binding and conformationally activating Antithrombin III (ATIII), it dramatically accelerates ATIII-mediated inhibition of thrombin and factor Xa. Because this anticoagulant axis bypasses the Protein C pathway entirely, Heparin can directly compensate for the coagulation excess that accumulates when Protein C–mediated feedback is lost. The mechanistic rationale is not merely plausible — it is the basis for established acute management of thrombotic crises in Protein C-deficient patients in current clinical practice.

Detailed MOA data was not returned by the DrugBank query in this review cycle. Nevertheless, Heparin's mechanism is well-characterised in the published literature, and the mechanistic link to Protein C deficiency thrombophilia is direct and strong. The absence of retrieved trials or publications for this specific drug–disease pairing is consistent with the rarity of autosomal recessive Protein C deficiency (estimated incidence of the severe homozygous form: approximately 1 in 500,000 live births), which makes randomised controlled trials impractical and means clinical experience is concentrated in case series and expert guidelines not captured by the current query parameters.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Practical note for clinicians:** No formal safety data was retrieved in this review cycle. Heparin carries a well-recognised risk profile that includes Heparin-Induced Thrombocytopenia (HIT), major and minor haemorrhage, heparin resistance (particularly in ATIII-depleted states), and hyperkalaemia with prolonged use. In the context of Protein C deficiency — where patients may already be receiving anticoagulation or Protein C concentrate — a full PI review and clinical pharmacist input are essential prior to any new prescribing decision.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Heparin and autosomal recessive Protein C deficiency thrombophilia is strong, direct, and clinically well-understood — Heparin compensates for the absent Protein C anticoagulant pathway by activating a parallel ATIII-dependent axis. The complete absence of retrieved evidence reflects the rarity of this condition and limitations in the current evidence collection pipeline, not a lack of clinical plausibility or precedent.

**To proceed, the following is needed:**

- **ARTG registration verification:** Confirm Heparin's current TGA registration status directly via the ARTG public portal; the 0-entry result is inconsistent with Heparin's established clinical use in Australia and is likely a data query artefact
- **Full PI / safety review:** Obtain and review the TGA-approved Product Information for complete warnings, contraindications, dosing guidance, and monitoring requirements
- **Specialist haematology consultation:** Management of acute thrombotic events in Protein C-deficient patients requires specialist input, particularly for neonatal presentations (purpura fulminans)
- **Long-term management planning:** Heparin is appropriate for acute thrombotic crises; maintenance strategies (warfarin, direct oral anticoagulants, or Protein C concentrate) should be considered with haematology for ongoing thromboprophylaxis
- **DDI assessment:** Formal drug interaction review is required, especially where concurrent anticoagulants or antiplatelet agents are used
- **MOA data retrieval:** Supplement the DrugBank query to obtain complete mechanism-of-action data to support the mechanistic rationale assessment in the final dossier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

