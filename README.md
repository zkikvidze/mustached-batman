# mustached-batman
სხვადასხვა სკრიპტების საწყობი (რეპოს სახელი გითჰაბმა მირჩია).


#GEO: 

# fb-phisher-finder.py - სკრიპტი განკუთვნილია facebook.com-ის ჯგუფებში ფიშერების ლინკების მოსაძებნად. სკრიპტი იყენებს facebook graph API-ს, რომ ავტომატურად წამოიღოს ინფორმაცია ფეისბუკის იმ ჯგუფებიდან, რომლის წევრიც არის იუსერი. ჯგუფებში განთავსებულ ბოლო რამდენიმე პოსტში ის ეძებს ბმულებს სხვა საიტებზე, რის შემდეგადაც გადადის ყოველ ბმულზე და ცდილობს დაადგინოს არის თუ არა ის ფეისბუკის ფიშერი. თუმცა შესაძლებელია, რომ მოხდეს regex მოდიფიკაცია და მოძებნოთ სხვა ტიპის კონტენტი.

# სკრიპტის ასამუშავებლად საჭიროა ACCESS_TOKEN ფეისბუკიდან, რომელიც შეგიძლიათ აიღოთ ამ გვერდიდან: 
https://developers.facebook.com/tools/explorer/

# ასევე საჭიროა რამდენიმე ბიბლიოთეკა, რომლებიც შეგიძლიათ  დააყენოთ შემდეგი ბრძანებით:
pip install facebook-sdk re urllib2 urlparse

# სკრიპტი მუშაობს უპრობლემოდ, უბრალოდ facebook-ის წესების თანახმად, ავტომატური ხელსაწყოების გამოყენება მათი საიტიდან
# ინფორმაციის მისაღებად, აკრძალულია. ანუ ამ სკრიპტის გამოყენებაც აკრძალულია :)



#ENG:

# fb-phisher-finder.py - this python script uses Facebook Graph API to crawl all facebook groups member of which is user. It searches resent posts in this group and tries to find URLs to external domains. After this it searches some patterns which may be sign of facebook login page phisher. Currently, regex in this script detects Georgian version of phisher pages but you can modify it to detect other pages.

# You need ACCESS_TOKEN from facebook.com which can be obtained from here:
https://developers.facebook.com/tools/explorer/

# Also it depent on several packages, which can be installed with this command:
pip install facebook-sdk re urllib2 urlparse

NOTICE: According to facebook rules, using of automating tools for scraping facebook pages, it not allowed! So using of this script is not allowed by facebook!





