"""Run every stage notebook end-to-end. Usage:  python run_all.py

Executes Step1..Step6 in order, stopping at the first failure. This is the
headless equivalent of notebooks/Step0_Run_All.ipynb and is what is run on RunPod:
    jupyter nbconvert --to notebook --execute Step0_Run_All.ipynb --output Step0_executed.ipynb
"""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

PROJECT = Path(__file__).resolve().parent
NB_DIR = PROJECT / "notebooks"

STEPS = [
    "Step1_Data_Preparation.ipynb",
    "Step2_EDA.ipynb",
    "Step3_Modeling.ipynb",
    "Step4_Forecasting.ipynb",
    "Step5_Monitoring.ipynb",
    "Step6_Deployment.ipynb",
]


def main() -> int:
    print(f"Project: {PROJECT}")
    print(f"Python : {sys.executable}")
    timings: dict[str, float] = {}
    for name in STEPS:
        nb = NB_DIR / name
        if not nb.exists():
            print(f"MISSING: {nb}")
            return 1
        print(f"\n>>> {name} ...", flush=True)
        t0 = time.time()
        proc = subprocess.run(
            [sys.executable, "-m", "nbconvert", "--to", "notebook", "--execute",
             "--inplace", "--ExecutePreprocessor.timeout=3600", str(nb)],
            capture_output=True, text=True, cwd=str(PROJECT))
        dt = time.time() - t0
        timings[name] = round(dt, 1)
        status = "OK  " if proc.returncode == 0 else "FAIL"
        print(f"    {status} {dt:6.1f} s")
        if proc.returncode != 0:
            print(proc.stderr[-2000:])
            return proc.returncode

    out = PROJECT / "outputs" / "runs" / "run_all_timings.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        "{\n" + ",\n".join(f'  "{k}": {v}' for k, v in timings.items()) + "\n}\n",
        encoding="utf-8")
    print("\nAll stages completed.")
    for k, v in timings.items():
        print(f"  {k:34s} {v:7.1f} s")
    print(f"\nWrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
