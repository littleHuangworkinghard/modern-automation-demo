# @Version : 1.0
# @Author : Jie
# @File    : run_tests.py
import subprocess
import sys
import webbrowser
from pathlib import Path


def run_tests():
    print("🚀 开始运行自动化测试...")

    # 创建报告目录
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    # 运行 pytest 并生成 HTML 报告
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",  # 详细输出
        "--html=reports/report.html",
        "--self-contained-html"
    ]

    print(f"执行命令: {' '.join(cmd)}")
    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("✅ 所有测试通过！")
    else:
        print("❌ 有测试失败")

    # 尝试打开报告
    report_path = reports_dir / "report.html"
    if report_path.exists():
        print(f"📊 报告已生成: {report_path.absolute()}")
        try:
            webbrowser.open(f"file://{report_path.absolute()}")
        except:
            print("请手动打开 reports/report.html 查看报告")

    return result.returncode


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)
