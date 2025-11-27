import sqlite3
import os

# ----------------------------------------
# 設定 DB 路徑
# ----------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "waiver.db")


WAIVER_DATA = [
    # --- CTS Waivers ---
    {"suite": "CTS", "waiver_id": "b/437127898", "module": "CtsWindowManagerDeviceTestCases",
     "test_case": "android.server.wm.PinnedStackTests testDismissPipWhenLaunchNewOne", "note": ""},
    {"suite": "CTS", "waiver_id": "b/443835370", "module": "CtsScopedStorageDeviceOnlyTest",
     "test_case": "android.scopedstorage.cts.device.ScopedStorageDeviceTest#testSystemGalleryCanRenameImageAndVideoDirs[volume=external]",
     "note": ""},
    {"suite": "CTS", "waiver_id": "b/443835370", "module": "CtsScopedStorageDeviceOnlyTest",
     "test_case": "android.scopedstorage.cts.device.ScopedStorageDeviceTest#testSystemGalleryCanRenameImageAndVideoDirs[volume=volume_public]",
     "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.DataAccessFragmentTest dataAccess_deleteCategoryData_showsDeleteDataRanges",
     "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.DataAccessFragmentTest dataAccess_navigateToDataAccess", "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.HomeFragmentTest homeFragment_openDataManagement", "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.PermissionTypesFragmentTest permissionTypes_showsDeleteCategoryData",
     "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.PermissionTypesFragmentTest permissionTypes_filterByApp", "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.DataEntriesFragmentTest dataEntries_showsInsertedEntry", "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.DataEntriesFragmentTest dataEntries_deletesData_showsNoData",
     "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.DataEntriesFragmentTest dataEntries_changeDate_updatesSelectedDate",
     "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.DataEntriesFragmentTest dataEntries_navigateToYesterday", "note": ""},
    {"suite": "CTS", "waiver_id": "b/428801091", "module": "CtsHealthConnectControllerTestCases",
     "test_case": "android.healthconnect.cts.ui.DataEntriesFragmentTest dataEntries_changeUnit_showsUpdatedUnit",
     "note": ""},
    {"suite": "CTS", "waiver_id": "b/419744307", "module": "CtsHealthFitnessDeviceTestCases",
     "test_case": "android.healthconnect.cts.RateLimiterTest testTryAcquireApiCallQuota_writeLimitExceeded_flagDisabled",
     "note": ""},
    {"suite": "CTS", "waiver_id": "b/419744307", "module": "CtsHealthFitnessDeviceTestCases",
     "test_case": "android.healthconnect.cts.RateLimiterTest testTryAcquireApiCallQuota_readLimitExceeded_flagDisabled",
     "note": ""},
    {"suite": "CTS", "waiver_id": "b/427899490", "module": "CtsJvmtiRunTest906HostTestCases",
     "test_case": "android.jvmti.cts.JvmtiHostTest906 testJvmti", "note": ""},
    {"suite": "CTS", "waiver_id": "b/427899491", "module": "CtsJvmtiRunTest913HostTestCases",
     "test_case": "android.jvmti.cts.JvmtiHostTest913 testJvmti", "note": ""},
    {"suite": "CTS", "waiver_id": "b/421800984", "module": "CtsNetTestCases",
     "test_case": "android.net.cts.EthernetManagerTest testCallbacks_withRunningInterface", "note": ""},
    {"suite": "CTS", "waiver_id": "b/407682957", "module": "CtsNetTestCases",
     "test_case": "android.net.cts.NetworkAgentTest#testAgentStartsInConnecting", "note": "Android 13"},
    {"suite": "CTS", "waiver_id": "b/407682957", "module": "CtsNetTestCases",
     "test_case": "android.net.cts.NetworkAgentTest#testSetAcceptUnvalidatedPreventAutomaticReconnect",
     "note": "Android 13"},
    {"suite": "CTS", "waiver_id": "b/407682957", "module": "CtsNetTestCases",
     "test_case": "android.net.cts.NetworkAgentTest#testPreventAutomaticReconnect", "note": "Android 13"},
    {"suite": "CTS", "waiver_id": "b/407682957", "module": "CtsNetTestCases",
     "test_case": "android.net.cts.NetworkAgentTest#testValidationStatus", "note": "Android 13"},
    {"suite": "CTS", "waiver_id": "b/407682957", "module": "CtsNetTestCases",
     "test_case": "android.net.cts.NetworkAgentTest#testSocketKeepalive", "note": "Android 13"},
    {"suite": "CTS", "waiver_id": "b/407682957", "module": "CtsNetTestCases",
     "test_case": "android.net.cts.NetworkAgentTest#testSetAcceptUnvalidated", "note": "Android 13"},

    # --- GTS Waivers ---
    {"suite": "GTS", "waiver_id": "b/141733998", "module": "GtsOsTestCases",
     "test_case": "com.google.android.os.gts.SecurityPatchTest#testSecurityPatchDate", "note": ""},

    # --- STS Waivers ---
    {"suite": "STS", "waiver_id": "", "module": "StsHostTestCases",
     "test_case": "android.security.sts.KernelLtsTest testRequiredKernelLts_WARN", "note": "只有 Warning，無 bug id"},

    # --- GSI Waivers ---
    {"suite": "GSI", "waiver_id": "b/453870468", "module": "CtsBiometricsTestCases",
     "test_case": "android.server.biometrics.BiometricPromptContentViewTest  testMoreOptionsButton_clickButton",
     "note": ""},
]


def import_waiver_data():
    """
    連接資料庫並批量匯入 Waiver 資料。
    """
    if not os.path.exists(DB_PATH):
        print(f"❌ 錯誤：找不到資料庫檔案 {DB_PATH}。")
        print("請先執行 app.py (步驟二) 建立新的資料庫。")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # 準備 SQL 語句 (只有 5 個欄位)
        sql = """
        INSERT INTO waivers (suite, waiver_id, module, test_case, note)
        VALUES (?, ?, ?, ?, ?)
        """

        # 準備要匯入的資料 (將字典轉為元組)
        data_to_insert = [
            (
                d["suite"].upper(),  # 統一轉大寫
                d["waiver_id"],
                d["module"],
                d["test_case"],
                d["note"]
            )
            for d in WAIVER_DATA
        ]

        # 批量執行插入操作
        cursor.executemany(sql, data_to_insert)
        conn.commit()

        print(f"✅ 成功匯入 {cursor.rowcount} 筆 Waiver 紀錄到 {DB_PATH} (新結構)。")

    except sqlite3.Error as e:
        print(f"❌ 資料庫操作失敗: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    import_waiver_data()