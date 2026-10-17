# Polytechnix Server Guidelines & Specifications

## Connection
*   Remote access requires connecting to the TUC VPN.

## Storage Management
*   The `boulimix` NAS server is mounted on `polytechnix` to handle large files (datasets, results) due to limited local disk space.
*   **NAS Directory:** `/mnt/nas_drive/akaralis`
*   **Quick Navigation:** `cd /mnt/nas_drive/akaralis`
*   **Maintenance:** Periodically delete temporary files and unused data.

---

## Hardware Specifications: Dell PowerEdge R750 Server

### Compute
*   **CPU:** 2x Intel Xeon Silver 4310 (2.1GHz, 12 Cores / 24 Threads per CPU, 18MB Cache, 120W)
*   **GPU:** 2x NVIDIA Ampere A10 (PCIe, 150W, 24GB Passive, Single Wide, Full Height)

### Memory & Storage
*   **RAM:** 256GB (4x 64GB RDIMM, 3200MT/s, Dual Rank)
*   **Storage:** 960GB SSD vSAS Read Intensive 12Gbps 512e 2.5-inch Hot-Plug AG Drive SED
*   **RAID Controller:** PERC H755 SAS Front with 8GB DDR4 Cache

### Infrastructure & Chassis
*   **Chassis:** 2.5" Chassis with up to 16 SAS/SATA Drives
*   **Power Supply:** Dual, Hot-Plug, Redundant (1+1), 1400W Mixed Mode
*   **Networking:** Broadcom 5720 Dual Port 1Gb On-Board LOM
*   **Management:** iDRAC9, Express 15G
*   **Rails:** ReadyRails Sliding Rails with Cable Management Arm (2U)