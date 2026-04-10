# SYSAI — Total System AI Assistant
## Expansion Roadmap: From Display Tool to Full System Intelligence Platform
### Built on Screen Resolution AI Assistant v1.0.0 — UniversalStandards

---

## THE PIVOT

The display tool proved a concept: an AI that reads raw system state, reasons about it, and executes
targeted fixes with surgical precision. That pattern is not display-specific. It applies to every
single layer of a Windows system.

This document defines the architecture and phased roadmap for expanding into SYSAI —
a Total System AI Assistant that monitors, diagnoses, and autonomously optimizes every hardware
and software layer of a PC.

There is nothing on the market that does this. Existing tools (CCleaner, MSI Afterburner, HWiNFO,
Task Manager, Process Monitor, Malwarebytes) are all single-domain, manual, and reactive.
SYSAI is multi-domain, conversational, and proactive.

---

## ARCHITECTURE — The Spine That Makes It Work

### Domain Plugin System

```
sysai/
  core/
    engine.py          # AI orchestration, tool routing, history
    executor.py        # Action execution engine
    snapshot.py        # System snapshot aggregator
    rollback.py        # Rollback stack manager
    monitor.py         # Background monitoring service
    db.py              # SQLite telemetry store
  domains/
    display/           # v1.0 — already exists
    cpu/
    memory/
    storage/
    network/
    processes/
    services/
    registry/
    startup/
    power/
    audio/
    peripherals/
    security/
    thermal/
    drivers/
    updates/
  ui/
    main_window.py
    domain_tabs.py
    chat_panel.py
    action_cards.py
    telemetry_graphs.py
    system_map.py
  agent/
    react_loop.py      # Extended ReAct agentic loop
    memory_store.py    # Local vector memory (chromadb)
    planner.py         # Multi-step planning across domains
```

### Cross-Domain Intelligence
Problems rarely exist in a single layer:
- "App is slow" = CPU throttling + disk I/O saturation + memory pressure + GPU bottleneck
- "Network is laggy" = DNS misconfiguration + Wi-Fi driver bug + background bandwidth hog
- "PC crashes at night" = thermal runaway during Windows Update + driver conflict + bad RAM slot

The AI receives the FULL system snapshot across ALL domains simultaneously and reasons across
all of them in a single inference call. This is what no existing tool can do.

---

## DOMAIN 01 — CPU & PROCESSOR MANAGEMENT

**Data Collected**
- Per-core utilization (WMI Win32_Processor + PDH counters)
- Clock speed per core (MSR via OpenLibSys or WMI)
- CPU temperature per core (WMI MSAcpi_ThermalZoneTemperature)
- Power consumption (RAPL via MSR 0x611 on Intel, SMU on AMD)
- Turbo Boost / SpeedStep state (registry + MSR)
- NUMA topology, hyperthreading state
- L1/L2/L3 cache hit rates (PDH performance counters)

**AI Actions**
- `set_power_plan(name)` — High Performance, Balanced, Ultimate Performance
- `set_core_affinity(pid, cores)` — Pin process to specific cores
- `set_process_priority(pid, level)` — Realtime/High/Normal/Low
- `toggle_hyperthreading(enable)` — Registry + reboot flag
- `toggle_turbo_boost(enable)` — Power plan or MSR write
- `set_cpu_governor(min_pct, max_pct)` — Min/max processor state
- `run_cpu_stress_test(duration_sec)` — Expose thermal issues

---

## DOMAIN 02 — MEMORY (RAM) MANAGEMENT

**Data Collected**
- Total/available/committed/cached/paged pool (WMI Win32_OperatingSystem)
- Per-process working set and private bytes
- Memory pressure score (commit charge vs commit limit)
- Page file size, location, current usage
- RAM speed, latency, timings (WMI Win32_PhysicalMemory)
- RAM slot population (physical topology)
- Memory errors (WHEA event log)

**AI Actions**
- `set_pagefile(size_mb, drive)`
- `optimize_pagefile_location()` — Move to fastest drive
- `clear_standby_memory()` — EmptyWorkingSet
- `set_process_working_set(pid, max_mb)` — RAM footprint limit
- `toggle_superfetch(enable)` — SysMain service
- `run_memory_diagnostic()` — mdsched.exe on next boot

---

## DOMAIN 03 — STORAGE & DISK MANAGEMENT

**Data Collected**
- Drive inventory: model, serial, interface (NVMe/SATA/USB), capacity, type
- SMART attributes: reallocated sectors, pending sectors, wear level, temperature
- Partition layout: volumes, mount points, free space
- Disk I/O: read/write MB/s, IOPS, queue depth, latency (PDH counters)
- Folder size distribution (top 20 space consumers)
- Recycle bin, temp folder, Windows Update cache sizes

**AI Actions**
- `run_trim(drive)` — FSUtil TRIM
- `run_chkdsk(drive, fix)` — Schedule on next boot
- `run_defrag(drive)` — HDD only
- `clean_temp_files()` — %TEMP%, Windows\Temp, WU cache
- `analyze_large_files(threshold_gb)`
- `enable_bitlocker(drive)`
- `run_smart_test(drive, type)` — Short or extended

---

## DOMAIN 04 — NETWORK & CONNECTIVITY

**Data Collected**
- Network adapter inventory: name, type, link speed, MAC
- IP config: IP, subnet, gateway, DNS, DHCP vs static
- Current throughput per adapter (PDH)
- TCP connection table with PID and remote address
- DNS resolution times (measured in real-time)
- Wi-Fi signal, SSID, channel, band, noise floor (netsh wlan)
- Routing table, Windows Firewall rules, proxy config
- MTU size, hosts file contents

**AI Actions**
- `set_dns(primary, secondary)`
- `flush_dns()` — ipconfig /flushdns
- `reset_tcp_stack()` — netsh int ip reset
- `reset_winsock()` — netsh winsock reset
- `set_mtu(adapter, size)`
- `toggle_ipv6(enable)`
- `add_firewall_rule(name, port, action)`
- `run_speed_test()`
- `scan_open_ports()`
- `edit_hosts_file(action, entry)`

---

## DOMAIN 05 — PROCESS & APPLICATION MANAGEMENT

**Data Collected**
- Full process list: PID, name, CPU%, memory, disk I/O, network I/O, path
- Process tree topology (parent-child)
- Process signature verification (Authenticode)
- DLL list per process, open handles
- Process crash history (WER logs)

**AI Actions**
- `kill_process(pid)`
- `suspend_process(pid)` — NtSuspendProcess
- `set_priority(pid, level)` — SetPriorityClass
- `analyze_process(pid)` — Deep dive: DLLs, handles, network
- `quarantine_process(pid)` — Suspend + move binary
- `set_process_memory_limit(pid, mb)` — Job Object

---

## DOMAIN 06 — WINDOWS SERVICES MANAGEMENT

**Data Collected**
- All services: name, status, start type, binary path, account
- Service dependencies
- Service failure actions

**AI Actions**
- `start/stop/restart_service(name)`
- `set_service_startup(name, type)`
- `apply_service_profile(profile)` — Gaming/Privacy/Battery/Server

**Service Profiles**
- **Gaming**: disables WU Delivery Optimization, Xbox services, Search indexer, Superfetch
- **Privacy**: disables DiagTrack, dmwappushsvc, Connected User Experiences
- **Battery**: disables Search, Bluetooth, Print Spooler, SSDP Discovery
- **Server**: ensures IIS/SQL/critical services running; disables consumer services

---

## DOMAIN 07 — STARTUP & BOOT MANAGEMENT

**Data Collected**
- Startup programs: registry Run keys, Startup folders, Task Scheduler
- Boot configuration (BCD via bcdedit)
- Boot duration from Event Log (Event ID 100)
- Service startup sequence and timing

**AI Actions**
- `toggle_startup_item(name, enable)`
- `set_boot_timeout(seconds)` — bcdedit /timeout
- `toggle_fast_startup(enable)`
- `analyze_boot_time()` — Parse Diagnostics-Performance log
- `schedule_task(name, trigger, action)` — schtasks /create

---

## DOMAIN 08 — REGISTRY INTELLIGENCE

**Data Collected**
- Performance, security, appearance registry keys
- Orphaned registry entries (references to deleted files)

**AI Actions**
- `read/write/delete_registry(key, value)`
- `backup_registry_key(key)` — Export .reg before editing
- `restore_registry_backup(path)`
- `scan_orphaned_entries()`
- `apply_tweak_pack(name)` — Performance/Gaming/Privacy/Developer

---

## DOMAIN 09 — POWER & THERMAL MANAGEMENT

**Data Collected**
- Active power plan and all settings
- Battery: charge%, wear level, design vs actual capacity, charge rate
- CPU/GPU/NVMe/board temperatures
- Fan speeds (LibreHardwareMonitor COM or WMI)
- Thermal throttling events (Event Log + MSR TJ_MAX proximity)

**AI Actions**
- `set_power_plan(guid_or_name)`
- `create_custom_power_plan(settings)`
- `toggle_hibernate(enable)`
- `run_battery_report()` — powercfg /batteryreport
- `run_energy_report()` — powercfg /energy
- `set_charge_limit(percent)` — ASUS/Dell/Lenovo battery health APIs

---

## DOMAIN 10 — AUDIO SYSTEM MANAGEMENT

**Data Collected**
- Audio devices, default device, exclusive mode status
- Audio driver version and date
- Audio sessions per application (WASAPI)
- Volume levels per app (IAudioSessionManager2)
- Sample rate and bit depth per device

**AI Actions**
- `set_default_audio_device(name, role)`
- `set_sample_rate(device, hz, bit_depth)`
- `toggle_audio_enhancements(device, enable)`
- `set_app_volume(pid, level)`
- `restart_audio_service()` — AudioSrv + AudioEndpointBuilder
- `configure_spatial_sound(format)` — Windows Sonic / Atmos / DTS

---

## DOMAIN 11 — PERIPHERAL & USB MANAGEMENT

**Data Collected**
- All connected USB devices (WMI Win32_USBHub)
- HID devices: report rate, driver version
- Device error state (Device Manager yellow bangs)
- USB host controller type and power delivery

**AI Actions**
- `reset_usb_device(device_id)` — Disable + re-enable
- `reset_usb_controller()` — Restart host controller
- `set_usb_power_management(device, enable)` — Selective suspend
- `reinstall_device_driver(device_id)` — PnP reinstall
- `scan_device_errors()` — All devices with error codes

---

## DOMAIN 12 — WINDOWS UPDATE & PATCH MANAGEMENT

**Data Collected**
- Installed updates (WMI + Windows Update API)
- Pending updates (WUA API)
- Update history: failures, rollbacks
- Delivery Optimization settings and usage

**AI Actions**
- `check_for_updates()` — WUA API scan
- `install_update(kb_number)` — Selective install
- `uninstall_update(kb_number)` — wusa /uninstall
- `pause_updates(days)`
- `clean_update_cache()` — SoftwareDistribution flush
- `disable_delivery_optimization()`

---

## DOMAIN 13 — SECURITY & THREAT DETECTION

**Data Collected**
- Windows Defender status, last scan, threat history, exclusion list
- Firewall state per profile (Domain/Private/Public)
- UAC level, BitLocker status per drive
- Unsigned processes with network connections
- Autorun locations, open shares, RDP/SSH/SMBv1 status

**AI Actions**
- `run_defender_scan(type)` — Quick/Full/Custom
- `add_defender_exclusion(path)`
- `set_uac_level(level)` — 0-3
- `enable_bitlocker(drive, method)`
- `toggle_smb1(enable)` — DISM + registry
- `toggle_rdp(enable)` — Registry + firewall rule
- `scan_autoruns()` — Full autorun analysis
- `quarantine_file(path)` — Move to quarantine
- `block_process_from_network(pid)` — Firewall rule by process path

---

## DOMAIN 14 — SYSTEM HEALTH DASHBOARD

**Real-Time Telemetry**
- Live graphs: CPU%, Memory%, Disk I/O, Network throughput, GPU%, Temperatures
- 60fps double-buffered Canvas rendering
- Color-coded thresholds: green → yellow → red
- Configurable time windows: 30s / 5min / 1hr

**Health Score**
- Overall score (0-100) from weighted domain scores
- Per-domain scores with trend direction
- Score history in SQLite — view trends over weeks

**AI Daily Narrative**
Example output:
> "Your SSD is showing early SMART warning indicators in the reallocated sector count.
> Your CPU is running 8°C hotter than baseline — likely thermal compound aging after 3 years.
> RAM is healthy. Network performance degraded 12% this week due to Delivery Optimization —
> I've disabled it. Overall health score: 71/100 (down from 84 last week)."

**Predictive Alerts** (local sklearn models)
- SSD failure probability (SMART attribute trajectories)
- RAM error probability (WHEA event frequency trends)
- Thermal event probability (temperature trend during load)
- Boot time degradation trend

---

## THE AGENTIC LOOP

```
User: "My PC feels slow and laggy"

SYSAI Process:
  1. Snapshot all 14 domains simultaneously
  2. Send to Claude with cross-domain reasoning prompt
  3. Claude returns multi-domain plan:
     - [LOW]    CPU power plan set to Balanced on AC power (wrong plan)
     - [LOW]    47 startup items, 31 unnecessary
     - [MEDIUM] NVMe temperature at 73°C causing thermal throttling
     - [LOW]    SysMain (Superfetch) running on NVMe — counterproductive
     - [LOW]    Chrome has 12 active connections consuming 40% bandwidth
     - [LOW]    Windows Defender full scan running in background — defer
  4. User approves plan
  5. SYSAI executes all 6 in sequence with rollback after each
  6. Re-snapshot all affected domains
  7. Claude narrates: "Fixed. CPU performance +34%. Boot time -22 seconds.
     NVMe throttling eliminated. Effective immediately."
```

---

## IMPLEMENTATION PHASES

| Phase | Domains Added | Duration | Deliverable |
|---|---|---|---|
| 1 | CPU, Memory, Storage (+ refactor) | 8 weeks | 4-domain SYSAI |
| 2 | Network, Processes, Services, Startup | 8 weeks | 8-domain + service profiles |
| 3 | Registry, Power, Audio, Peripherals, Updates, Security | 8 weeks | Full 14-domain + health score |
| 4 | Agentic loop, local ML, trust levels | 6 weeks | Autonomous mode |
| 5 | Cloud sync, fleet management, macOS port | 10 weeks | Enterprise + multi-platform |

---

## DEPLOYMENT ARCHITECTURE

```
ScreenResAI (v1.0) Display-only
     │
     ▼
SYSAI Desktop ─────────────────── SYSAI Agent Service (Windows Service)
     │                                     │
     │                             Background monitoring
     │                             Anomaly detection
     │                             Predictive models
     ├── Local SQLite Telemetry DB
     ├── Local Vector Memory (chromadb)
     ├── Domain Plugin Engine (14 domains)
     ├── Rollback Stack (complete undo)
     │
     ▼
SYSAI Cloud (optional)
     ├── Fleet dashboard (web)
     ├── Encrypted profile sync
     ├── Multi-machine AI coordination
     └── Anomaly aggregation across fleet
```

---

## THE END STATE

An operating system co-pilot. It knows your machine better than you do.
It catches problems before you feel them. It fixes things you didn't know were broken.
It speaks plain English and requires zero technical knowledge to operate.

Nothing like it exists. The Windows Troubleshooter is embarrassingly limited compared to what this
becomes. SYSAI is to Windows what a Formula 1 pit crew is to a race car — constant expert
attention, real-time optimization, and immediate response to every anomaly.
