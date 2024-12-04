# 亚马逊爬虫

[![推广](https://github.com/bright-cn/Amazon-scraper/blob/main/images/Proxies%20and%20scrapers%20GitHub%20bonus%20banner.png)](https://bright.cn/products/web-scraper/amazon?promo=github15)

## 目录

- [免费亚马逊爬虫](#免费亚马逊爬虫)
   - [前提条件](#前提条件)
   - [快速设置](#快速设置)
   - [如何爬取亚马逊数据](#如何爬取亚马逊数据)
   - [输出](#输出)
- [爬取亚马逊数据的挑战](#爬取亚马逊数据的挑战)
- [解决方案：Bright CN 亚马逊爬虫 API](#解决方案bright-cn-亚马逊爬虫-api)
- [亚马逊爬虫 API 实践](#亚马逊爬虫-api-实践)
   - [使用 API 参数自定义数据收集](#使用-api-参数自定义数据收集)
   - [亚马逊产品数据](#亚马逊产品数据)
   - [亚马逊评论数据](#亚马逊评论数据)
   - [亚马逊产品搜索](#亚马逊产品搜索)
   - [亚马逊卖家信息](#亚马逊卖家信息)
   - [按畅销商品分类的亚马逊产品](#亚马逊畅销商品)
   - [按类别 URL 分类的亚马逊产品](#按类别-url-的亚马逊产品)
   - [按关键词分类的亚马逊产品](#按关键词的亚马逊产品)
   - [全球亚马逊产品数据集](#全球亚马逊产品数据集)
   - [全球亚马逊产品数据集 - 按类别 URL 发现](#全球亚马逊产品数据集---按类别-url-发现)
   - [全球亚马逊产品数据集 - 按关键词发现](#全球亚马逊产品数据集---按关键词发现)

## 免费亚马逊爬虫

使用此免费工具直接从搜索结果页面提取亚马逊产品数据。只需几个简单步骤即可轻松获取产品标题、价格、评分、评论等信息。

### 前提条件

- Python 3.11 或更高版本。
- 安装必要的依赖项（见下方步骤）。

### 快速设置

1. 打开终端并导航到此项目的目录。
2. 运行以下命令以安装依赖项：

  ```bash
    pip install -r requirements.txt
```

### 如何爬取亚马逊数据

要开始爬取亚马逊数据，只需提供一个搜索查询。您还可以指定亚马逊的域名以及要爬取的页面数量。

#### 命令：
```bash
python main.py "coffee maker" --domain="com" --pages=3
```

### 输出

爬取完成后，提取的数据将保存为 `amazon_data.csv` 文件，位于项目目录中。CSV 文件将包含以下详细信息：
- **名称：** 产品标题。
- **当前价格：** 产品价格（如果缺货则为空）。
- **评分：** 平均客户评分。
- **评论：** 客户评论总数。
- **ASIN：** 亚马逊标准识别号。
- **链接：** 产品页面的直接 URL。

以下是数据的示例格式：

<img width="700" alt="bright-cn-amazon_csv_data" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-amazon_csv_data.png">

## 爬取亚马逊数据的挑战

爬取亚马逊数据并非总是轻而易举。以下是一些常见的挑战：

1. **高级反爬措施：** 亚马逊使用 CAPTCHA、隐形机器人检测技术以及行为分析（例如跟踪鼠标移动）来阻止爬虫。
2. **频繁的页面结构更新：** 亚马逊经常更改其 HTML 结构、ID 和类名，需要定期更新爬虫以适应新的页面布局。
3. **高资源消耗：** 使用 Playwright 或 Selenium 等工具爬取 JavaScript 密集型页面会消耗大量系统资源。处理动态内容并运行多个浏览器实例可能会降低性能，尤其是在爬取大量数据时。

以下是亚马逊检测到自动爬取尝试时的示例：

<img src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/Amazon%20Blocked.png" alt="Amazon Blocked" width="700"/>

如上所示，亚马逊阻止了该请求以防止进一步的数据爬取——这是许多爬虫常遇到的问题。

## 解决方案：Bright CN 亚马逊爬虫 API

[Bright CN 亚马逊爬虫 API](https://bright.cn/products/web-scraper/amazon) 是大规模爬取亚马逊产品数据的终极解决方案。以下是它的优势：

- **无需基础设施管理：** 无需处理代理或解除封锁系统。
- **地理位置爬取：** 可从任何地理区域爬取数据。
- **全球 IP 覆盖：** 通过 [超过 7200 万真实用户 IP](https://bright.cn/proxy-types/residential-proxies) 和 [覆盖 195 个国家](https://bright.cn/locations)，提供 99.99% 的正常运行时间。
- **灵活的数据交付：** 可通过 Amazon S3、Google Cloud、Azure、Snowflake 或 SFTP 以 JSON、NDJSON、CSV 和 `.gz` 格式获取数据。
- **隐私合规：** 完全符合 GDPR、CCPA 和其他数据保护法律。
- **全天候支持：** 专业支持团队 24/7 提供帮助，解决所有与 API 相关的问题。

此外，您可获得 **20 次免费 API 调用** 以测试产品并验证其是否适合您的需求。

## 亚马逊爬虫 API 实践

> 有关设置亚马逊爬虫 API 的详细指南，请查阅我们的 [分步设置指南](https://github.com/bright-cn/Amazon-scraper/blob/main/scraper_api_setup.md#amazon-reviews)。

### 使用 API 参数自定义数据收集

通过以下 API 参数自定义数据收集方式：

| **参数**           | **类型**   | **描述**                                                                                         | **示例**                                               |
|---------------------|------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `limit`             | `integer`  | 限制每个输入返回的结果数量。                                                                     | `limit=10`                                            |
| `include_errors`    | `boolean`  | 在输出中包含错误报告以便排查问题。                                                               | `include_errors=true`                                 |
| `notify`            | `url`      | 数据收集完成后发送通知的 URL。                                                                   | `notify=https://notify-me.com/`                       |
| `format`            | `enum`     | 数据交付的格式。支持的格式：JSON、NDJSON、JSONL、CSV。                                           | `format=json`                                         |

💡 **额外交付方式：** 数据可以通过 [Webhook](https://docs.bright.cn/scraping-automation/web-data-apis/web-scraper-api/overview#via-webhook) 或 [API](https://docs.bright.cn/scraping-automation/web-data-apis/web-scraper-api/overview#via-api) 提供。

### 亚马逊产品数据

通过提供产品 URL，收集亚马逊的详细产品数据。

<img width="700" alt="bright-cn-web-scraper-api-amazon-product-data" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-amazon-product-data.png">

#### 关键输入参数：
| 参数       | 类型     | 描述                         | 是否必需 |
|------------|----------|------------------------------|----------|
| `url`      | `string` | 亚马逊产品 URL，用于爬取数据 | 是       |

#### 性能：
- 每个输入的平均响应时间：13 秒

#### 示例输出数据：
以下是爬取亚马逊产品数据后生成的输出示例：
```json
{
    "url": "https://www.amazon.com/KitchenAid-Protective-Dishwasher-Stainless-8-72-Inch/dp/B07PZF3QS3",
    "title": "KitchenAid All Purpose Kitchen Shears with Protective Sheath...",
    "seller_name": "Amazon.com",
    "brand": "KitchenAid",
    "description": "These all-purpose shears from KitchenAid are a valuable addition...",
    "initial_price": 11.99,
    "final_price": 8.99,
    "currency": "USD",
    "availability": "In Stock",
    "reviews_count": 77557,
    "rating": 4.8,
    "categories": [
        "Home & Kitchen",
        "Kitchen & Dining",
        "Kitchen Utensils & Gadgets",
        "Shears"
    ],
    "asin": "B07PZF3QS3",
    "images": [
        "https://m.media-amazon.com/images/I/41E7ALk+uXL._AC_SL1200_.jpg",
        "https://m.media-amazon.com/images/I/710B9HpzMPL._AC_SL1500_.jpg"
    ],
    "delivery": [
        "FREE delivery Friday, October 25 on orders shipped by Amazon over $35",
        "Or fastest Same-Day delivery Today 10 AM - 3 PM. Order within 4 hrs 46 mins"
    ]
}
```
#### 代码示例：

以下是一个 Python 脚本，用于触发亚马逊产品数据收集并将结果存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(api_token, dataset_id, datasets):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = (
        f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}"
    )

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = (
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
    )

    # Polling until the snapshot data is ready
    while True:
        time.sleep(10)
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None


def store_data(data, filename="amazon_products_data.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "YOUR_API_TOKEN"
    DATASET_ID = "gd_l7q7dkf244hwjntr0"

    datasets = [
        {
            "url": "https://www.amazon.com/Quencher-FlowState-Stainless-Insulated-Smoothie/dp/B0CRMZHDG8"
        },
        {
            "url": "https://www.amazon.com/KitchenAid-Protective-Dishwasher-Stainless-8-72-Inch/dp/B07PZF3QS3"
        },
        {
            "url": "https://www.amazon.com/TruSkin-Naturals-Vitamin-Topical-Hyaluronic/dp/B01M4MCUAF"
        },
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_products_data.json) 查看完整的输出。

### 亚马逊评论数据

通过提供产品 URL 和特定参数（如时间范围、关键词以及要爬取的评论数量），收集亚马逊的产品评论。

<img width="700" alt="bright-cn-web-scraper-api-amazon-product-reviews" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-amazon-product-reviews.png">

#### 关键输入参数：
| **参数**            | **类型**   | **描述**                                                                          | **是否必需** |
|---------------------|------------|-----------------------------------------------------------------------------------|--------------|
| `url`               | `string`   | 亚马逊产品 URL，用于爬取评论。                                                     | 是           |
| `days_range`        | `number`   | 爬取评论时考虑的过去天数（留空表示无时间限制）。                                   | 否           |
| `keyword`           | `string`   | 根据特定关键词过滤评论。                                                           | 否           |
| `num_of_reviews`    | `number`   | 要爬取的评论数量（如果未提供，将爬取所有可用评论）。                                | 否           |

#### 性能：
- 每个输入的平均响应时间：1 分 1 秒

#### 示例输出数据：
以下是爬取亚马逊评论后生成的输出示例：
```json
{
    "url": "https://www.amazon.com/RORSOU-R10-Headphones-Microphone-Lightweight/dp/B094NC89P9/",
    "product_name": "RORSOU R10 On-Ear Headphones with Microphone...",
    "product_rating": 4.5,
    "product_rating_object": {
        "one_star": 386,
        "two_star": 237,
        "three_star": 584,
        "four_star": 1493,
        "five_star": 7630
    },
    "rating": 5,
    "author_name": "Amazon Customer",
    "review_header": "Great Sound For the Price!",
    "review_text": "I bought these headphones twice...",
    "badge": "Verified Purchase",
    "review_posted_date": "September 7, 2024",
    "helpful_count": 3
}
```
#### 代码示例：
以下是一段 Python 脚本，用于触发亚马逊评论数据的收集，并将结果存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(api_token, dataset_id, datasets):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = (
        f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}"
    )

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = (
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
    )

    # Polling until the snapshot data is ready
    while True:
        time.sleep(10)
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None


def store_data(data, filename="amazon_reviews_data.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "YOUR_API_TOKEN"
    DATASET_ID = "gd_le8e811kzy4ggddlq"

    datasets = [
        {
            "url": "https://www.amazon.com/RORSOU-R10-Headphones-Microphone-Lightweight/dp/B094NC89P9/",
            "days_range": 0,
            "num_of_reviews": 4,
            "keyword": "great",
        },
        {
            "url": "https://www.amazon.com/Solar-Eclipse-Glasses-Certified-Viewing/dp/B08GB3QC1H",
            "days_range": 0,
            "num_of_reviews": 4,
            "keyword": "",
        },
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_reviews_data.json) 查看完整的输出。

### 亚马逊产品搜索

通过提供关键词进行亚马逊产品的搜索。

<img width="700" alt="bright-cn-web-scraper-api-keyword-search" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-keyword-search.png">

#### 关键输入参数：
| **参数**           | **类型**   | **描述**                                      | **是否必需** |
|-------------------|-----------|----------------------------------------------|--------------|
| `keyword`         | `string`  | 用于搜索产品的关键词。                         | 是           |
| `url`             | `string`  | 要搜索的域名 URL。                             | 是           |
| `pages_to_search` | `number`  | 要搜索的页面数量。                             | 否           |

#### 性能：
- 每个输入的平均响应时间：1 秒

#### 示例输出数据：
以下是通过关键词在亚马逊上搜索产品后生成的输出示例：
```json
{
    "asin": "B08H75RTZ8",
    "url": "https://www.amazon.com/Microsoft-Xbox-Gaming-Console-video-game/dp/B08H75RTZ8/ref=sr_1_1",
    "name": "Xbox Series X 1TB SSD Console - Includes Xbox Wireless Controller...",
    "sponsored": "false",
    "initial_price": 479,
    "final_price": 479,
    "currency": "USD",
    "sold": 2000,
    "rating": 4.8,
    "num_ratings": 28675,
    "variations": null,
    "badge": null,
    "brand": null,
    "delivery": ["FREE delivery"],
    "keyword": "X-box",
    "image": "https://m.media-amazon.com/images/I/616klipzdtL._AC_UY218_.jpg",
    "domain": "https://www.amazon.com/",
    "bought_past_month": 2000,
    "page_number": 1,
    "rank_on_page": 1,
    "timestamp": "2024-10-20T10:39:37.679Z",
    "input": {
        "keyword": "X-box",
        "url": "https://www.amazon.com",
        "pages_to_search": 1
    }
}
```
#### 代码示例：  
以下是一段 Python 脚本，用于基于关键词触发亚马逊产品搜索，并将结果存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(api_token, dataset_id, datasets):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = (
        f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}"
    )

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = (
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
    )

    # Polling until the snapshot data is ready
    while True:
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        time.sleep(10)


def store_data(data, filename="amazon_keywords_data.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "YOUR_API_TOKEN"
    DATASET_ID = "gd_lwdb4vjm1ehb499uxs"

    datasets = [
        {"keyword": "X-box", "url": "https://www.amazon.com", "pages_to_search": 1},
        {"keyword": "PS5", "url": "https://www.amazon.de"},
        {
            "keyword": "car cleaning kit",
            "url": "https://www.amazon.es",
            "pages_to_search": 4,
        },
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_keywords_data.json) 查看完整的输出。

### 亚马逊卖家信息

通过提供特定的卖家 URL，获取亚马逊卖家的详细信息。

<img width="700" alt="bright-cn-web-scraper-api-seller-info" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-seller-info.png">

#### 关键输入参数：
| **参数**       | **类型**   | **描述**                          | **是否必需** |
|---------------|-----------|------------------------------------|--------------|
| `url`         | `string`  | 亚马逊卖家 URL                    | 是           |

#### 性能：
- 每个输入的平均响应时间：1 秒

#### 示例输出数据：
以下是爬取亚马逊卖家信息后生成的输出示例：
```json
{
    "input": {
        "url": "https://www.amazon.com/sp?seller=A33W53J5GVPZ8K"
    },
    "seller_id": "A33W53J5GVPZ8K",
    "seller_name": "Peckomatic",
    "description": "Peckomatic is committed to providing each customer with the highest standard of customer service.",
    "detailed_info": [
        {"title": "Business Name"},
        {"title": "Business Address"}
    ],
    "stars": "4.5 out of 5 stars",
    "feedbacks": [
        {
            "date": "By Kao y. on November 16, 2021.",
            "stars": "5 out of 5 stars",
            "text": "It say not to exceed 10lbs total but I did anyway. My bird was 8lbs + the 3lb box = 11lbs. Bird arrived in great condition."
        },
        {
            "date": "By JL on June 9, 2021.",
            "stars": "1 out of 5 stars",
            "text": "How this seller packages its items is not acceptable..."
        }
    ],
    "rating_positive": "89%",
    "feedbacks_percentages": {
        "star_5": "80%",
        "star_4": "9%",
        "star_3": "7%",
        "star_2": "0%",
        "star_1": "5%"
    },
    "products_link": "https://www.amazon.com/s?me=A33W53J5GVPZ8K",
    "buisness_name": "Francis Kunnumpurath",
    "buisness_address": "2612 State Route 80, Lafayette, NY, 13084, US",
    "rating_count_lifetime": 44,
    "country": "US"
}
```
#### 代码示例：  
以下是一段 Python 脚本，用于触发亚马逊卖家数据的收集，并将结果存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(api_token, dataset_id, datasets):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = (
        f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}"
    )

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = (
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
    )

    # Polling until the snapshot data is ready
    while True:
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        time.sleep(10)


def store_data(data, filename="amazon_seller_data.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "API_TOKEN"
    DATASET_ID = "gd_lhotzucw1etoe5iw1k"

    # Define the dataset with seller URLs
    datasets = [
        {"url": "https://www.amazon.com/sp?seller=A33W53J5GVPZ8K"},
        {"url": "https://www.amazon.com/sp?seller=A33YXLPENB0JBD"},
        {"url": "https://www.amazon.com/sp?seller=A33ZG27WW2U3E6"},
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_seller_data.json) 查看完整的输出。

### 亚马逊畅销商品

通过提供畅销商品类别的 URL，发现亚马逊上的热销产品。

<img width="700" alt="bright-cn-web-scraper-api-amazon-best-sellers" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-amazon-best-sellers.png">

#### 关键输入参数：

| **参数**         | **类型**  | **描述**                                     | **是否必需** |
|-----------------|----------|---------------------------------------------|--------------|
| `category_url`  | `string` | 要爬取的畅销商品类别 URL                     | 是           |

#### 性能：
- 每个输入的平均响应时间：6 分 49 秒

#### 示例输出数据：
以下是爬取亚马逊畅销商品数据后生成的输出示例：
```json
{
    "title": "Amazon Basics Multipurpose Copy Printer Paper, 8.5\" x 11\", 1 Ream, 500 Sheets, White",
    "seller_name": "Amazon.com",
    "brand": "Amazon Basics",
    "initial_price": 9.99,
    "final_price": 7.41,
    "currency": "USD",
    "availability": "In Stock",
    "reviews_count": 178695,
    "rating": 4.8,
    "categories": [
        "Office Products",
        "Paper",
        "Copy & Multipurpose Paper"
    ],
    "asin": "B01FV0F8H8",
    "buybox_seller": "Amazon.com",
    "discount": "-26%",
    "root_bs_rank": 1,
    "url": "https://www.amazon.com/AmazonBasics-Multipurpose-Copy-Printer-Paper/dp/B01FV0F8H8?th=1&psc=1",
    "image_url": "https://m.media-amazon.com/images/I/81x0cTHWQJL._AC_SL1500_.jpg",
    "delivery": [
        "FREE delivery Friday, October 25",
        "Same-Day delivery Today 10 AM - 3 PM"
    ],
    "features": [
        "1 ream (500 sheets) of 8.5 x 11 white copier and printer paper",
        "Works with laser/inkjet printers, copiers, and fax machines",
        "Smooth 20lb weight paper for consistent ink and toner distribution"
    ],
    "bought_past_month": 100000,
    "root_bs_category": "Office Products",
    "bs_category": "Copy & Multipurpose Paper",
    "bs_rank": 1,
    "amazon_choice": true,
    "badge": "Amazon's Choice",
    "seller_url": "https://www.amazon.com/sp?ie=UTF8&seller=ATVPDKIKX0DER&asin=B01FV0F8H8",
    "timestamp": "2024-10-20T13:30:56.666Z"
}
```
#### 代码示例：  
以下是一段 Python 脚本，用于触发亚马逊畅销商品数据的收集，并将结果存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(api_token, dataset_id, datasets):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}&type=discover_new&discover_by=best_sellers_url&limit_per_input=3"

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = (
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
    )

    # Polling until the snapshot data is ready
    while True:
        time.sleep(10)
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None


def store_data(data, filename="amazon_bestsellers_data.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "YOUR_API_TOKEN"
    DATASET_ID = "gd_l7q7dkf244hwjntr0"

    datasets = [
        {
            "category_url": "https://www.amazon.com/gp/bestsellers/office-products/ref=pd_zg_ts_office-products"
        },
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_bestsellers.json) 查看完整的输出。

### 按类别 URL 的亚马逊产品

通过提供特定类别的 URL，发现并收集亚马逊产品数据。可通过排序选项和基于位置的过滤器自定义搜索。

<img width="700" alt="bright-cn-web-scraper-api-discover-by-category-url" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-discover-by-category-url.png">

#### 关键输入参数：
| **参数**       | **类型**   | **描述**                                      | **是否必需** |
|---------------|-----------|----------------------------------------------|--------------|
| `url`         | `string`  | 要爬取产品的类别 URL                          | 是           |
| `sort_by`     | `string`  | 产品结果的排序标准                            | 否           |
| `zipcode`     | `string`  | 基于位置的产品结果邮政编码                     | 否           |

#### 性能：
- 每个输入的平均响应时间：16 分 16 秒

#### 示例输出数据：
以下是爬取特定类别中的产品后生成的数据示例：
```json
{
    "title": "Quilted Makeup Bag Floral Makeup Bag Cotton Makeup Bag",
    "brand": "WYJ",
    "price": 9.99,
    "currency": "USD",
    "availability": "In Stock",
    "rating": 5,
    "reviews_count": 1,
    "categories": [
        "Beauty & Personal Care",
        "Cosmetic Bags"
    ],
    "asin": "B0DC3WX7RM",
    "seller_name": "yisenshangmaoyouxiangongsi",
    "number_of_sellers": 1,
    "url": "https://www.amazon.com/WYJ-Quilted-Coquette-Aesthetic-Blue/dp/B0DC3WX7RM",
    "image_url": "https://m.media-amazon.com/images/I/71SI04tB6QL._AC_SL1500_.jpg",
    "product_dimensions": "8.7\"L x 2.8\"W x 5.1\"H",
    "item_weight": "2.5 Ounces",
    "variations": [
        {
            "name": "Pink",
            "asin": "B0DC3RKYPF",
            "price": 9.99
        },
        {
            "name": "Blue",
            "asin": "B0DC3WX7RM",
            "price": 9.99
        },
        {
            "name": "Purple",
            "asin": "B0DC47CDDT",
            "price": 9.99
        }
    ],
    "badge": "#1 New Release",
    "top_review": "I love everything about this bag! It's made well and a good size. Super cute!"
}
```
#### 代码示例：  
以下是一段 Python 脚本，用于触发从指定类别 URL 收集产品数据，并将其存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(api_token, dataset_id, datasets):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}&type=discover_new&discover_by=category_url&limit_per_input=4"

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = (
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
    )

    # Polling until the snapshot data is ready
    while True:
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        time.sleep(10)


def store_data(data, filename="amazon_bestsellers_data.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "YOUR_API_TOKEN"
    DATASET_ID = "gd_l7q7dkf244hwjntr0"

    datasets = [
        {
            "url": "https://www.amazon.com/s?i=luggage-intl-ship",
            "sort_by": "Best Sellers",
            "zipcode": "10001",
        },
        {
            "url": "https://www.amazon.com/s?i=baby-products-intl-ship",
            "sort_by": "Avg. Customer Review",
            "zipcode": "",
        },
        {
            "url": "https://www.amazon.com/s?rh=n%3A16225012011&fs=true&ref=lp_16225012011_sar",
            "sort_by": "Price: Low to High",
            "zipcode": "",
        },
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_discover_by_category_url.json) 查看完整的输出。

### 按关键词的亚马逊产品

通过使用特定关键词发现产品。

<img width="700" alt="bright-cn-web-scraper-api-discover-by-keyword" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-discover-by-keyword.png">

#### 关键输入参数：
| **参数**       | **类型**   | **描述**                          | **是否必需** |
|---------------|-----------|-----------------------------------|--------------|
| `keyword`     | `string`  | 用于搜索产品的关键词               | 是           |

#### 性能：
- 每个输入的平均响应时间：2 分 46 秒

#### 示例输出数据：
以下是使用关键词搜索产品后生成的输出示例：
```json
{
    "title": "SYLVANIA ECO LED Light Bulb, A19 60W Equivalent, 750 Lumens, 2700K, Non-Dimmable, Frosted, Soft White - 8 Count (Pack of 1)",
    "brand": "LEDVANCE",
    "seller_name": "Amazon.com",
    "initial_price": 13.99,
    "final_price": 12.12,
    "currency": "USD",
    "discount": "-13%",
    "rating": 4.7,
    "reviews_count": 48418,
    "availability": "In Stock",
    "url": "https://www.amazon.com/Sylvania-40821-Equivalent-Efficient-Temperature/dp/B08FRSS4BF",
    "image_url": "https://m.media-amazon.com/images/I/81wKhRO66oL._AC_SL1500_.jpg",
    "delivery": [
        "FREE delivery Friday, October 25 on orders shipped by Amazon over $35",
        "Or Prime members get FREE delivery Tomorrow, October 21. Order within 8 hrs 8 mins. Join Prime"
    ],
    "features": [
        "60W Incandescent Replacement Bulb - 750 Lumens",
        "Long-lasting – 7 years lifespan",
        "Energy-saving – Estimated energy cost of $1.08 per year"
    ],
    "discovery_input": {
        "keyword": "light bulb"
    },
    "input": {
        "url": "https://www.amazon.com/Sylvania-40821-Equivalent-Efficient-Temperature/dp/B08FRSS4BF"
    }
}
```
#### 代码示例：  
以下是一段 Python 脚本，用于基于关键词触发亚马逊产品数据的收集，并将结果存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(
    api_token, dataset_id, datasets, dataset_type="discover_new", discover_by="keyword"
):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}&type={dataset_type}&discover_by={discover_by}"

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = (
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
    )

    # Polling until the snapshot data is ready
    while True:
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        time.sleep(10)


def store_data(data, filename="amazon_keyword_data.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "API_TOKEN"
    DATASET_ID = "gd_l7q7dkf244hwjntr0"

    # Define the dataset with keywords
    datasets = [{"keyword": "light bulb"}, {"keyword": "dog toys"}]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_keyword_data.json) 查看完整的输出。

### 全球亚马逊产品数据集

通过提供 URL，从所有主要亚马逊域名中收集产品数据。

<img width="700" alt="bright-cn-web-scraper-api-amazon-product-global-dataset" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-amazon-product-global-dataset.png">

#### 关键输入参数：
| **参数**       | **类型**   | **描述**                | **是否必需** |
|---------------|-----------|------------------------|--------------|
| `url`         | `string`  | 亚马逊产品 URL          | 是           |

#### 性能：
- **每个输入的平均响应时间：** 少于 1 秒

#### 示例输出数据：
以下是收集产品数据后生成的输出示例：
```json
{
    "title": "Toys of Wood Oxford Wooden Stacking Rings – Learning to Count – Counting Game with 45 Rings – Wooden Toy for Ages 3 and Above",
    "brand": "Toys of Wood Oxford",
    "seller_name": "Toys of Wood Oxford",
    "initial_price": 23.99,
    "currency": "EUR",
    "final_price": 23.99,
    "availability": "Only 20 left in stock.",
    "rating": 4.5,
    "reviews_count": 1677,
    "asin": "B078TNNZK3",
    "url": "https://www.amazon.de/dp/B078TNNZK3?th=1&psc=1",
    "image_url": "https://m.media-amazon.com/images/I/815t1-d+7BL._AC_SL1500_.jpg",
    "product_dimensions": "43.31 x 11.61 x 11.51 cm; 830 g",
    "categories": [
        "Toys",
        "Baby & Toddler Toys",
        "Early Development & Activity Toys",
        "Sorting, Stacking & Plugging Toys"
    ],
    "delivery": [
        "FREE delivery Friday, 25 October on eligible first order",
        "Or fastest delivery Thursday, 24 October. Order within 4 hrs 40 mins"
    ],
    "features": [
        "Sturdy and stable base plate with 9 pins and 45 beautiful large wooden rings and 10 removable square number plates in rainbow colours.",
        "Great for learning counting, sorting, and matching colors and numbers, as well as practicing simple mathematics.",
        "Made from sustainable wood with eco-friendly and non-toxic paints. Complies with EN71 / CPSA standards."
    ],
    "top_review": "Sehr lehrreich",
    "variations": [
        {
            "name": "Caterpillar Threading Toy",
            "price": 13.99,
            "currency": "EUR"
        },
        {
            "name": "Pack of 15",
            "price": 16.99,
            "currency": "EUR"
        },
        {
            "name": "Pack of 45",
            "price": 23.99,
            "currency": "EUR"
        }
    ],
    "product_rating_object": {
        "one_star": 35,
        "two_star": 0,
        "three_star": 82,
        "four_star": 227,
        "five_star": 1308
    }
}
```
#### 代码示例：  
以下是一段 Python 脚本，用于触发从所有主要亚马逊域名收集产品数据，并将结果存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(
    api_token, dataset_id, datasets, dataset_type="trigger", discover_by="url"
):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={
        dataset_id}&type={dataset_type}&discover_by={discover_by}"

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = f"https://api.brightdata.com/datasets/v3/snapshot/{
        snapshot_id}?format=json"

    # Polling until the snapshot data is ready
    while True:
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        time.sleep(10)


def store_data(data, filename="amazon_products_global_dataset.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "API_TOKEN"
    DATASET_ID = "gd_lwhideng15g8jg63s7"

    # Define the dataset with URLs
    datasets = [
        {"url": "https://www.amazon.com/dp/B0CHHSFMRL/"},
        {
            "url": "https://www.amazon.de/-/en/dp/B078TNNZK3/ref=sspa_dk_browse_2/?_encoding=UTF8&ie=UTF8&sp_csd=d2lkZ2V0TmFtZT1zcF9icm93c2VfdGhlbWF0aWM%3D&pd_rd_w=fHlOu&content-id=amzn1.sym.642a11a6-0e1e-47fa-93c2-5dc9d607a7a1&pf_rd_p=642a11a6-0e1e-47fa-93c2-5dc9d607a7a1&pf_rd_r=4JX920KFM8Q7PR83HJ7V&pd_rd_wg=K1OVN&pd_rd_r=be656f87-1a09-4144-b7cf-4e932d6a73c4&ref_=sspa_dk_browse&th=1"
        },
        {
            "url": "https://www.amazon.co.jp/X-TRAK-Folding-Bicycle-Carbon-Adjustable/dp/B0CWV9YTLV/ref=sr_1_1_sspa?crid=3MKZ2ALHSLFOM&dib=eyJ2IjoiMSJ9.YnBVPwJ7nLxlNGHktwDTFM5v2evnsXlnZTJHJKuG8dLeeRCILpy0Knr3ofiKpUGQYi6xR6y4tgdtal85DJ8u6DD_n9r1oVCXdVo0NFmNAfStU6E-MhBig5p_gZGjluAYv5HgUIoEPl0v3iMiRxZNRfivqB-utxOkPOOfXIBHLemry17XcltUDTQqtJv-kP-ZqdP29mjD2cRlbkALtHPKU44MvBC9WUrNcUHAMrlAxtTAByuriywMqz-w2P0HCeehcZTJ1EiLf2VR8cxCiwuaUbIOU3tr1kDN6D7yYPrgRn4.6AOdSmJsksZkqLg8kNM6EvWxIFOijCsP2zo5NLHn1P4&dib_tag=se&keywords=Bicycles&qid=1716973495&sprefix=%2Caps%2C851&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
        },
        {
            "url": "https://www.amazon.in/Watches-Women%EF%BC%8CLadies-Stainless-Waterproof-Luminous/dp/B0D31HBWG1/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.1zFa2vTCZdD-bv6Knt_pWqvcRZPSSTPDwgMClRJNsWqdyGdCmryjEAfWpd-ZhwhC3vvNx9A0G2Gt1R952e7huzlukge2bmJETNf-kHBoWS5kV6g0pUVapEyDOEAGcw5ZvWlkeuLQ9oIwuhckRC6ARCt2yglYV-1HpP7lVGXotK6K6tjrdKxUSAOZJSXeOGP3dGuYPTjo9sllOrwA7FC2GG00aDcsSTzURENFj1c2rS-vNHkYmxOL1JYuwDWK2PJdMpsmkJw3jeMdgaiw7jG5ppMfAjwiETVldQzhHGVUFV8.manfNZwtTUhvDuSGdh32APM1_SmnNiKgOGabyA7rXBo&dib_tag=se&qid=1716973272&rnid=2563505031&s=watch&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&psc=1"
        },
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_products_global_dataset.json) 查看完整的输出。

### 全球亚马逊产品数据集 - 按类别 URL 发现

通过提供特定的类别 URL，发现产品数据。

<img width="700" alt="bright-cn-web-scraper-api-amazon-product-global-category-url" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-amazon-product-global-category-url.png">

#### 关键输入参数：
| **参数**       | **类型**   | **描述**                                       | **是否必需** |
|---------------|-----------|-----------------------------------------------|--------------|
| `url`         | `string`  | 要爬取产品的类别 URL                            | 是           |
| `sort_by`     | `string`  | 结果的排序标准                                  | 否           |
| `zipcode`     | `string`  | 基于位置的结果的邮政编码                         | 否           |

#### 性能：
- 每个输入的平均响应时间：3 分 57 秒

#### 示例输出数据：
以下是收集产品数据后生成的输出示例：
```json
{
    "title": "De'Longhi Stilosa EC230.BK, Traditional Barista Pump Espresso Machine, Espresso and Cappuccino, 2 cups, Black",
    "brand": "De'Longhi",
    "seller_name": "Hughes Electrical",
    "initial_price": 104.99,
    "final_price": 94,
    "currency": "GBP",
    "availability": "Only 1 left in stock.",
    "rating": 3.9,
    "reviews_count": 395,
    "asin": "B085J8LV4F",
    "url": "https://www.amazon.co.uk/dp/B085J8LV4F?th=1&psc=1",
    "image_url": "https://m.media-amazon.com/images/I/715gqhkOEiL._AC_SL1500_.jpg",
    "categories": [
        "Cooking & Dining",
        "Coffee, Tea & Espresso",
        "Coffee Machines",
        "Espresso & Cappuccino Machines"
    ],
    "delivery": [
        "FREE delivery 25 - 28 October",
        "Or fastest delivery Tomorrow, 22 October. Order within 3 hrs 59 mins"
    ],
    "features": [
        "Unleash your inner barista and create all your coffee shop favourites at home",
        "15-bar pump espresso maker with a stainless steel boiler for perfect coffee extraction",
        "Steam arm to create frothy cappuccinos and smooth lattes",
        "Combination of matt and glossy black finish with an anti-drip system"
    ],
    "input": {
        "url": "https://www.amazon.co.uk/DeLonghi-EC230-BK-Traditional-Espresso-Cappuccino/dp/B085J8LV4F/ref=sr_1_4"
    },
    "discovery_input": {
        "url": "https://www.amazon.co.uk/b/?_encoding=UTF8&node=10706951&ref_=Oct_d_odnav_d_13528598031_1",
        "sort_by": "Best Sellers",
        "zipcode": ""
    }
}
```
#### 代码示例：  
以下是一段 Python 脚本，用于触发按类别 URL 收集产品数据，并将结果存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(api_token, dataset_id, datasets, dataset_type="discover_new", discover_by="category_url", limit_per_input=4):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}&type={
        dataset_type}&discover_by={discover_by}&limit_per_input={limit_per_input}"

    # Sending API request to trigger dataset collection
    response = requests.post(
        trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = f"https://api.brightdata.com/datasets/v3/snapshot/{
        snapshot_id}?format=json"

    # Polling until the snapshot data is ready
    while True:
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        time.sleep(10)


def store_data(data, filename="amazon_category_url_data.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "API_TOKEN"
    DATASET_ID = "gd_lwhideng15g8jg63s7"

    # Define the dataset with category URLs, sort_by, and zipcodes
    datasets = [
        {"url": "https://www.amazon.com/s?i=luggage-intl-ship",
            "sort_by": "Featured", "zipcode": "10001"},
        {"url": "https://www.amazon.de/-/en/b/?node=1981001031&ref_=Oct_d_odnav_d_355007011_2&pd_rd_w=OjE3S&content-id=amzn1.sym.0069bc39-a323-47d6-a8fb-7558e4a563e4&pf_rd_p=0069bc39-a323-47d6-a8fb-7558e4a563e4&pf_rd_r=6YXZ7HGFNNEAF0GSDPDH&pd_rd_wg=0yR1G&pd_rd_r=a95cb46c-78ef-4b7b-845d-49fe04556440", "sort_by": "Price: Low to High", "zipcode": ""},
        {"url": "https://www.amazon.co.uk/b/?_encoding=UTF8&node=10706951&bbn=11052681&ref_=Oct_d_odnav_d_13528598031_1&pd_rd_w=LghVp&content-id=amzn1.sym.7414f21e-2c95-4394-9a75-8c1b3641bcea&pf_rd_p=7414f21e-2c95-4394-9a75-8c1b3641bcea&pf_rd_r=EE0PQWMSY2J0G8M032EB&pd_rd_wg=7snrU&pd_rd_r=349e1e79-8bf8-4e00-947d-17eab2942b8d", "sort_by": "Best Sellers", "zipcode": ""},
        {"url": "https://www.amazon.co.jp/-/en/b/?node=377403011&ref_=Oct_d_odnav_d_15314601_0&pd_rd_w=ajUV4&content-id=amzn1.sym.0d505cca-fde9-497c-b5f8-e827c26fad17&pf_rd_p=0d505cca-fde9-497c-b5f8-e827c26fad17&pf_rd_r=92HSETNKKN3RTA615BV7&pd_rd_wg=AwOOk&pd_rd_r=629211d8-6768-478c-94a2-829a0a0ca2a6", "sort_by": "", "zipcode": ""}
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_product_global_category_url.json) 查看完整的输出。

### 全球亚马逊产品数据集 - 按关键词发现

通过使用特定关键词，在亚马逊各个域名中发现产品数据。

<img width="700" alt="bright-cn-web-scraper-api-amazon_global_dataset_by_keyword" src="https://github.com/bright-cn/Amazon-scraper/blob/main/images/bright-data-web-scraper-api-amazon_global_dataset_by_keyword.png">

#### 关键输入参数：
| **参数**           | **类型**   | **描述**                                   | **是否必需** |
|--------------------|-----------|-------------------------------------------|--------------|
| `keywords`         | `string`  | 用于搜索产品的关键词                        | 是           |
| `domain`           | `string`  | 要搜索的亚马逊域名                          | 是           |
| `pages_to_search`  | `number`  | 要搜索的页面数量                            | 否           |

#### 性能：
- 每个输入的平均响应时间：56 秒

#### 示例输出数据：
以下是通过关键词搜索产品后生成的输出示例：
```json
{
    "title": "Mitutoyo 500-197-30 Electronic Digital Caliper AOS Absolute Scale Digital Caliper, 0 to 8\"/0 to 200mm Measuring Range, 0.0005\"/0.01mm Resolution",
    "brand": "Mitutoyo",
    "seller_name": "Everly Home & Gift",
    "initial_price": 157.97,
    "final_price": 137.77,
    "currency": "USD",
    "availability": "In Stock",
    "rating": 4.8,
    "reviews_count": 88,
    "asin": "B01N6C3EGR",
    "url": "https://www.amazon.com/dp/B01N6C3EGR?th=1&psc=1",
    "image_url": "https://m.media-amazon.com/images/I/61Gigoh3LbL._SL1500_.jpg",
    "categories": [
        "Industrial & Scientific",
        "Test, Measure & Inspect",
        "Dimensional Measurement",
        "Calipers",
        "Digital Calipers"
    ],
    "delivery": [
        "FREE delivery Saturday, October 26",
        "Or Prime members get FREE delivery Tomorrow, October 22"
    ],
    "features": [
        "Hardened stainless steel construction for protection of caliper components",
        "Digital, single-value readout LCD display in metric units for readability",
        "Measuring Range 0 to 8\"/0 to 200mm",
        "Measurement Accuracy +/-0.001",
        "Resolution 0.0005\"/0.01mm"
    ],
    "input": {
        "url": "https://www.amazon.com/Mitutoyo-500-197-30-Electronic-Measuring-Resolution/dp/B01N6C3EGR"
    },
    "discovery_input": {
        "keywords": "Mitutoyo",
        "domain": "https://www.amazon.com",
        "pages_to_search": 1
    }
}
```
#### 代码示例：  
以下是一段 Python 脚本，用于触发按关键词搜索产品数据的收集，并将结果存储为 JSON 文件：
```python
import json
import requests
import time


def trigger_datasets(
    api_token, dataset_id, datasets, dataset_type="discover_new", discover_by="keywords"
):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={
        dataset_id}&type={dataset_type}&discover_by={discover_by}"

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = f"https://api.brightdata.com/datasets/v3/snapshot/{
        snapshot_id}?format=json"

    # Polling until the snapshot data is ready
    while True:
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        time.sleep(10)


def store_data(data, filename="amazon_global_dataset_by_keyword.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "YOUR_API_TOKEN"
    DATASET_ID = "gd_lwhideng15g8jg63s7"

    # Define the dataset with keywords, domain, and pages_to_search
    datasets = [
        {
            "keywords": "Mitutoyo",
            "domain": "https://www.amazon.com",
            "pages_to_search": 1,
        },
        {
            "keywords": "smart watch",
            "domain": "https://www.amazon.co.uk",
            "pages_to_search": 2,
        },
        {
            "keywords": "football",
            "domain": "https://www.amazon.in",
            "pages_to_search": 4,
        },
        {
            "keywords": "baby cloth",
            "domain": "https://www.amazon.de",
            "pages_to_search": 3,
        },
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)
```
您可以通过下载 [此示例 JSON 文件](https://github.com/bright-cn/Amazon-scraper/blob/main/output_data/amazon_global_dataset_by_keyword.json) 查看完整的输出。
