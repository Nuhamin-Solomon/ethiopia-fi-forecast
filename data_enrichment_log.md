# Data Enrichment Log

This log documents all new observations, events, and impact_links added to the dataset.

---

## **1. Observations**

| source_url | original_text | confidence | collected_by | collection_date | notes | record_type | pillar | parent_id |
|------------|---------------|-----------|--------------|----------------|-------|-------------|--------|-----------|
| https://example.com/ethiopia-mobile-money | "9.45% of adults have mobile money accounts" | High | Kifiya | 2026-02-02 | Useful for forecasting digital access | observation | Access | - |
| https://example.com/atm-data | "ATM density increased from 5 to 7 per 100k adults in 2023" | Medium | Kifiya | 2026-02-02 | Infrastructure indicator | observation | Infrastructure | - |

---

## **2. Events**

| source_url | original_text | confidence | collected_by | collection_date | notes | record_type | pillar | parent_id |
|------------|---------------|-----------|--------------|----------------|-------|-------------|--------|-----------|
| https://example.com/telebirr-launch | "Telebirr launched May 2021" | High | Kifiya | 2026-02-02 | Impacts mobile money usage | event | - | - |
| https://example.com/regulation | "New digital payment regulation, 2023" | Medium | Kifiya | 2026-02-02 | Expected effect on adoption | event | - | - |

---

## **3. Impact Links**

| parent_id | source_url | original_text | confidence | collected_by | collection_date | notes | pillar | related_indicator | impact_direction | impact_magnitude | lag_months | evidence_basis |
|-----------|------------|---------------|-----------|--------------|----------------|-------|--------|-----------------|-----------------|-----------------|------------|----------------|
| 1001 | https://example.com/telebirr-launch | "Telebirr adoption increased MM accounts" | High | Kifiya | 2026-02-02 | Based on pre/post data | Usage | ACC_MM_ACCOUNT | Positive | 0.05 | 0 | Observed change |
| 1002 | https://example.com/regulation | "New regulation expected to increase account ownership" | Medium | Kifiya | 2026-02-02 | Based on comparable country evidence | Access | ACC_OWNERSHIP | Positive | 0.03 | 6 | Expert opinion |

---

### **Notes on Schema**
- **record_type**: observation, event, or target  
- **pillar**: Access, Usage, Infrastructure (leave blank for events initially)  
- **parent_id**: connects an event to its impact in `impact_links`  

