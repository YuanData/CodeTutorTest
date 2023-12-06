# Web 測試專案

這是一個使用 **Page Object Model (POM)** 方法的 web 測試專案。專案目錄結構如下：

```
webtest/
├── conftest.py
├── README.md
├── data/
│   └── daten.py
├── locators/
│   └── contact_loc.py
├── pages/
│   └── contact_page.py
└── test/
    └── test_contact.py
```

## Page Object Model (POM)

在這個專案中，我們選擇使用 **Page Object Model** 作為我們的測試設計模式。POM 的主要目的是為了抽象化測試和業務邏輯之間的界面，將 web 頁面的每個頁面視為一個物件，並在該物件中封裝該頁面的行為。

### Locators

我們將所有的定位器（例如：Xpath、CSS selectors、element IDs 等）獨立放置在 `locators` 資料夾中。這樣的組織方式有以下好處：

1. **維護容易**：當 web 頁面的某些元素更改時，我們只需修改 `locators` 資料夾下的相應檔案，而不必修改測試邏輯。
2. **提高可讀性**：把測試邏輯與定位器分開可以使測試腳本更簡潔、有組織，提高整體的可讀性。
3. **重用性**：如果有多個測試需要相同的定位器，我們只需定義一次即可。

## 執行測試

如果您想要執行測試，可以使用以下的指令：

```bash
pytest test/test_contact.py
```

### `TestContactForm` 測試用例說明

`TestContactForm` 類別包含針對聯絡表單的自動化測試。這個測試類別旨在驗證表單提交功能以及電子郵件欄位的驗證機制。

#### 表單提交測試

- **描述**：驗證使用有效的測試數據可以成功提交聯絡表單。
- **預期結果**：提交後應該看到提示訊息，表示表單已成功提交。

#### 電子郵件有效性測試

- **描述**：通過一系列不同情況來驗證電子郵件欄位的輸入效驗。
- **測試數據**：
  - 空的電子郵件 (`""`) — 預期無效
  - 缺少 "@" 的電子郵件 (`"no-at-sign"`) — 預期無效
  - 只有 "@" 沒有域名的電子郵件 (`"no-domain@"`) — 預期無效
  - 正確格式的電子郵件 (`"valid@test.com"`) — 預期有效
- **預期結果**：每個測試用例應該符合預期的有效性結果。

### 實現細節

- **`test_form_submission` 方法**：這個方法測試表單使用自動生成的測試數據是否能成功提交。
- **`test_email_validity` 方法**：這個方法使用 `pytest.mark.parametrize` 裝飾器進行多個測試用例的參數化測試，以驗證電子郵件欄位的輸入效驗。
