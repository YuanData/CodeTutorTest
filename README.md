# Web 測試專案

這是一個使用 **Page Object Model (POM)** 方法的 web 測試專案。專案目錄結構如下：

```
webtest/
│
├── conftest.py
├── config_manager.py
├── README.md
│
├── drivers/
│   └── chromedriver
├── setting/
│   └── config.ini
├── data/
│   └── daten.py
│
├── locators/
│   └── contact_loc.py
├── pages/
│   └── contact_page.py
│
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

## 初始設定

在執行測試前，請確保進行以下初始設定：

### 下載 chromedriver

1. 根據您的作業系統和安裝的Chrome版本，前往 [ChromeDriver官方網站](https://sites.google.com/a/chromium.org/chromedriver/) 下載相對應版本的ChromeDriver。
2. 下載完成後，請將 `chromedriver` 放入 `drivers` 目錄下。確保其路徑為：`drivers/chromedriver`。

### 設定config

1. 將 `setting/config.ini.example` 重新命名為 `setting/config.ini`。
2. 打開 `setting/config.ini`，找到網址示例的部分，替換成您想要測試的真實網址。

## 執行測試

如果您想要執行測試，可以使用以下的指令：

```bash
pytest test/test_register.py
```
