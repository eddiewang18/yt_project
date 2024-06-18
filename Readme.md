這是一個youtube轉mp3與mp4的小專案，使用Django (DRF) + Vue 來開發:
首頁:
  功能說明:功能畫面上有輸入框供使用者輸入youtube連結，然後使用者可依選擇要將影片轉mp3或mp4，並在下方會呈現各個國家地區當日最受歡迎的youtube音樂影片
  技術使用:
    a.前端:使用Vue配置Router來呈現各個Component，並搭配Bootstrap的modal來呈現訊息，並用axios來向後端的API發送請求，並依得到的response做資料的幾解析與畫面上的渲染
    b.後端:
        b.1:當前端載入手頁畫面時，後端會收到get請求，此時去串接google youtube api的相關資料，並將資料整理後進行json序列化返回給前端(呈現各個國家地區當日最受歡迎的youtube音樂影片)
        b.2:當收到前端轉檔的post請求時，使用pytube第三方的package下載youtube影片，並依前端的需求做後續的轉檔，轉完檔後，刪除server中占存的檔案，並將轉完檔後的檔案返回給前端(browser)，前端收到後會對後端轉的檔案進行(瀏覽器)下載